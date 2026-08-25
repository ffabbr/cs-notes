import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import * as ExternalPlugin from "./.quartz/plugins"
import { SocialImage } from "./quartz/components/SocialImage"
import { SiteTweaks } from "./quartz/plugins/transformers/siteTweaks"

ExternalPlugin.CustomOgImages({
  colorScheme: "darkMode",
  imageStructure: SocialImage,
})

const config = await loadQuartzConfig()
config.plugins.transformers.push(SiteTweaks())

export default config
export const layout = await loadQuartzLayout()
