import path from "path"
import { visit, SKIP } from "unist-util-visit"
import type { Root } from "mdast"
import type { QuartzTransformerPlugin } from "../types"
import { slugifyFilePath, type FilePath } from "../../util/path"

// Obsidian addresses a page inside a PDF with `#page=N`, which is also what
// every PDF viewer expects. `@quartz-community/obsidian-flavored-markdown`
// drops it: embeds are rendered as `<iframe src="{file}">` with no fragment at
// all, and plain links run the fragment through the heading slugifier, which
// eats the `=` and turns `#page=43` into `#page43`. Both land the reader on
// page 1.
//
// This plugin claims PDF wikilinks before that happens. It has to run ahead of
// the Obsidian plugin's own transform, so quartz.ts splices it in above rather
// than appending it — see the note there.

const pdfViewerParams = "toolbar=0&navpanes=0&scrollbar=0&statusbar=0&messages=0"

interface WikilinkNode {
  type: "wikilink"
  embedded?: boolean
  path?: string
  heading?: string
  alias?: string
}

const buildPdfEmbedSrc = (url: string, anchor: string) => {
  const hash = anchor.startsWith("#") ? anchor.slice(1) : anchor
  return `${url}#${hash.length > 0 ? `${hash}&${pdfViewerParams}` : pdfViewerParams}`
}

export const PdfEmbeds: QuartzTransformerPlugin = () => ({
  name: "PdfEmbeds",
  markdownPlugins() {
    return [
      () => (tree: Root) => {
        visit(
          tree,
          (node) => (node as unknown as WikilinkNode).type === "wikilink",
          (node, index, parent) => {
            if (parent == null || index == null) return
            const wikilink = node as unknown as WikilinkNode
            const fp = wikilink.path?.trim() ?? ""
            if (path.extname(fp).toLowerCase() !== ".pdf") return

            const anchor = wikilink.heading?.trim() ?? ""
            const aliasRaw = wikilink.alias?.trim() ?? ""
            const alias = aliasRaw.length > 0 ? aliasRaw : undefined

            if (wikilink.embedded) {
              const src = buildPdfEmbedSrc(slugifyFilePath(fp as FilePath), anchor)
              parent.children[index] = {
                type: "html",
                value: `<iframe src="${src}" class="pdf" scrolling="no" tabindex="-1"></iframe>`,
              }
            } else {
              // The path stays raw here, the way the Obsidian plugin leaves it:
              // CrawlLinks resolves it later, and its splitAnchor already keeps
              // PDF fragments verbatim.
              parent.children[index] = {
                type: "link",
                url: anchor.length > 0 ? `${fp}#${anchor}` : fp,
                children: [{ type: "text", value: alias ?? fp }],
              }
            }

            return SKIP
          },
        )
      },
    ]
  },
})
