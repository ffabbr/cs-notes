#!/usr/bin/env python3
"""
Recursively scans a folder for PDF files and removes their white background.

Usage:
    python3 remove_pdf_bg.py [folder]          # overwrite in place
    python3 remove_pdf_bg.py [folder] --suffix # save as "<name> (no bg).pdf"
    python3 remove_pdf_bg.py [folder] --debug  # print first-page stream for diagnosis

If no folder is given, the current directory is used.
Files already ending with " (no bg).pdf" are skipped.
"""

import fitz  # pip install pymupdf
import re
import sys
import tempfile
from pathlib import Path

# Each entry is (pattern, max_start) where max_start is the furthest byte offset
# at which a match is accepted (None = anywhere).  Patterns that include a clip
# setup (re W n …) are inherently specific, so max_start=None is fine.
# Pattern 5 has no clip anchor, so we restrict it to the very start of the stream
# to avoid accidentally removing a small white element inside page content.

# Near-white: matches "1" or values like ".999", ".9999966", etc.
_NW = r'(?:1|0?\.9{2,}\d*)'

# Optional empty save/restore pairs before clip setup (e.g. "q Q q …")
_QQ = r'(?:q\s+Q\s+)*'

_BG_PATTERNS: list[tuple[re.Pattern, int | None]] = [
    # 1. Custom colorspace, rect fill — cs + sc/scn (PowerPoint/Keynote standard)
    (re.compile(rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+)1\s+scn?\s+[\d.\s-]+re\s+f\*?'), None),
    # 2. DeviceGray with clip — handles W* and optional /GSx gs between n and fill (DDCA-style)
    (re.compile(rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s*(?:/\w+\s+gs\s+)?)1\s+g\s+[\d.\s-]+re\s+f\*?'), None),
    # 3. DeviceRGB white with clip — 1 1 1 rg <rect> f
    (re.compile(rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+)1\s+1\s+1\s+rg\s+[\d.\s-]+re\s+f\*?'), None),
    # 4. DeviceGray, no clip — "q 1 g <rect> re f" (PowerPoint+iPad mixed exports).
    #    max_start=50: only fires if the fill is the very first thing in the stream,
    #    preventing accidental removal of small white elements deeper in page content.
    (re.compile(r'(q\s+)1\s+g\s+[\d.\s-]+re\s+f\*?'), 50),
    # 5. Custom colorspace, path fill — "cs 1 1 1 sc/scn <m l l h f>" (some DDCA exports)
    (re.compile(
        rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+)'
        r'1\s+1\s+1\s+scn?\s+[\d.\s-]+m(?:\s+[\d.\s-]+l)+\s+h\s+f\*?'
    ), None),
    # 6. Custom colorspace, near-white 3-component sc/scn, path fill (Keynote/beamer/AuW exports)
    #    e.g. "q Q q 0 60 842 473 re W n /Cs1 cs .9999966 1 1 sc 0 534 m 842 534 l … h f"
    (re.compile(
        rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+)'
        rf'{_NW}\s+{_NW}\s+{_NW}\s+scn?\s+[\d.\s-]+m(?:\s+[\d.\s-]+l)+\s+h\s+f\*?'
    ), None),
    # 7. Custom colorspace, near-white 3-component sc/scn, rect fill
    (re.compile(
        rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+)'
        rf'{_NW}\s+{_NW}\s+{_NW}\s+scn?\s+[\d.\s-]+re\s+f\*?'
    ), None),
    # 8. Custom colorspace, near-white single-component sc/scn, path fill
    (re.compile(
        rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+)'
        rf'{_NW}\s+scn?\s+[\d.\s-]+m(?:\s+[\d.\s-]+l)+\s+h\s+f\*?'
    ), None),
    # 9. Split clip/fill: clip group closes (Q) then new group (q) re-establishes
    #    colorspace before white path fill — e.g. "q Q q <rect> re W n /Cs1 cs Q q /Cs1 cs 1 1 1 sc <path> h f"
    (re.compile(
        rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+Q\s+q\s+/\w+\s+cs\s+)'
        rf'{_NW}\s+{_NW}\s+{_NW}\s+scn?\s+[\d.\s-]+m(?:\s+[\d.\s-]+l)+\s+h\s+f\*?'
    ), None),
    # 10. Same split clip/fill but with single-component sc/scn
    (re.compile(
        rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+Q\s+q\s+/\w+\s+cs\s+)'
        rf'{_NW}\s+scn?\s+[\d.\s-]+m(?:\s+[\d.\s-]+l)+\s+h\s+f\*?'
    ), None),
    # 11. Same split clip/fill but with rect fill instead of path fill
    (re.compile(
        rf'({_QQ}q\s+[\d.\s]+re\s+W\*?\s+n\s+/\w+\s+cs\s+Q\s+q\s+/\w+\s+cs\s+)'
        rf'{_NW}\s+{_NW}\s+{_NW}\s+scn?\s+[\d.\s-]+re\s+f\*?'
    ), None),
]

def _remove_bg(raw: str) -> tuple[str, int]:
    for pat, max_start in _BG_PATTERNS:
        m = pat.search(raw)
        if m and (max_start is None or m.start() <= max_start):
            new = raw[:m.start()] + m.group(1) + raw[m.end():]
            return new, 1
    return raw, 0


def process_pdf(src: Path, dst: Path, debug: bool = False) -> tuple[int, int]:
    """Remove white background from src and save to dst. Returns (modified_pages, total_pages)."""
    doc = fitz.open(src)
    modified = 0

    for page in doc:
        # Do NOT call page.clean_contents() — it triggers MuPDF xref errors on
        # PDFs with broken cross-reference tables and may reformat streams so
        # the patterns no longer match.
        xrefs = page.get_contents()
        if not xrefs:
            continue

        page_modified = False
        for xref in xrefs:
            try:
                raw = doc.xref_stream(xref).decode('latin-1')
            except Exception:
                continue

            if debug and page.number == 0 and xref == xrefs[0]:
                print(f"\n--- DEBUG {src.name}: page 0 stream (first 600 chars) ---")
                print(raw[:600])
                print("---\n")

            new_raw, n = _remove_bg(raw)
            if n and not page_modified:
                doc.update_stream(xref, new_raw.encode('latin-1'))
                page_modified = True

        if page_modified:
            modified += 1

    page_count = doc.page_count
    if src == dst:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf", dir=src.parent) as tmp:
            tmp_path = Path(tmp.name)
        doc.save(tmp_path, garbage=4, deflate=True)
        doc.close()
        tmp_path.replace(dst)
    else:
        doc.save(dst, garbage=4, deflate=True)
        doc.close()
    return modified, page_count


def main():
    args = sys.argv[1:]
    use_suffix = "--suffix" in args
    debug = "--debug" in args
    args = [a for a in args if not a.startswith("--")]

    DEFAULT_DIR = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/Computer Science/2nd Semester"
    root = Path(args[0]).resolve() if args else DEFAULT_DIR
    if not root.is_dir():
        print(f"Error: '{root}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    pdfs = sorted(p for p in root.rglob("*.pdf") if " (no bg)" not in p.stem)

    if not pdfs:
        print(f"No PDF files found under: {root}")
        return

    print(f"Found {len(pdfs)} PDF(s) under: {root}\n")

    total_files = 0
    total_pages = 0

    for pdf in pdfs:
        if use_suffix:
            dst = pdf.with_name(pdf.stem + " (no bg)" + pdf.suffix)
        else:
            dst = pdf  # overwrite in place

        relative = pdf.relative_to(root)
        try:
            modified, pages = process_pdf(pdf, dst, debug=debug)
            label = f"-> {dst.name}" if use_suffix else "(in place)"
            print(f"  {relative}  {label}  [{modified}/{pages} pages]")
            total_files += 1
            total_pages += modified
        except Exception as e:
            print(f"  SKIP {relative}: {e}")

    print(f"\nDone. Processed {total_files} file(s), removed background from {total_pages} page(s).")


if __name__ == "__main__":
    main()
