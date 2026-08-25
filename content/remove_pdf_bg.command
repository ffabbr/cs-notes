#!/bin/bash
# Double-click this file in Finder to run remove_pdf_bg.py

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$SCRIPT_DIR/remove_pdf_bg.py" "$@"

echo
read -rp "Press Enter to close..."
