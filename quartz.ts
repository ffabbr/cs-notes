import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import * as ExternalPlugin from "./.quartz/plugins"
import { SocialImage } from "./quartz/components/SocialImage"
import { SiteTweaks } from "./quartz/plugins/transformers/siteTweaks"
import { PdfEmbeds } from "./quartz/plugins/transformers/pdfEmbeds"

ExternalPlugin.CustomOgImages({
  colorScheme: "darkMode",
  imageStructure: SocialImage,
})

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
