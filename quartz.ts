import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import * as ExternalPlugin from "./.quartz/plugins"
import { SocialImage } from "./quartz/components/SocialImage"
import { SiteTweaks } from "./quartz/plugins/transformers/siteTweaks"
import { PdfEmbeds } from "./quartz/plugins/transformers/pdfEmbeds"

ExternalPlugin.CustomOgImages({
  colorScheme: "darkMode",
  imageStructure: SocialImage,
})

// The root index belongs to the trie root, which Explorer does not render.
// Add just that page as a visible child; folder index pages stay as folders.
ExternalPlugin.Explorer({
  mapFn: (node) => {
    if (node.slugSegments?.length === 0 && node.data?.slug === "index") {
      const home = Object.assign(Object.create(Object.getPrototypeOf(node)), node, {
        slugSegments: ["index"],
        children: [],
        isFolder: false,
        displayNameOverride: "Home",
      })
      node.children.unshift(home)
    }
    return node
  },
  sortFn: (a, b) => {
    if (a.data?.slug === "index") return -1
    if (b.data?.slug === "index") return 1
    if (a.isFolder !== b.isFolder) return a.isFolder ? -1 : 1
    return (a.displayName ?? "").localeCompare(b.displayName ?? "", undefined, {
      numeric: true,
      sensitivity: "base",
    })
  },
} satisfies Partial<ExternalPlugin.ExplorerOptions>)

const config = await loadQuartzConfig()
config.plugins.transformers.push(SiteTweaks())

// Markdown transforms run in transformer order, so PdfEmbeds has to sit ahead
// of the Obsidian plugin to see PDF wikilinks before they are rewritten (and
// their `#page=N` discarded). Appending it would be too late.
const ofmIndex = config.plugins.transformers.findIndex(
  (plugin) => plugin.name === "ObsidianFlavoredMarkdown",
)
config.plugins.transformers.splice(ofmIndex === -1 ? 0 : ofmIndex, 0, PdfEmbeds())

export default config
export const layout = await loadQuartzLayout()
