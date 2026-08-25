import type { QuartzTransformerPlugin } from "../types"

const enhanceSite = String.raw`
const pdfViewerOptions = {
  toolbar: "0",
  navpanes: "0",
  scrollbar: "0",
  statusbar: "0",
  messages: "0",
}

function applySiteTweaks() {
  document.querySelectorAll("iframe.pdf").forEach((frame) => {
    const url = new URL(frame.src, window.location.href)
    const hash = new URLSearchParams(url.hash.replace(/^#/, ""))
    Object.entries(pdfViewerOptions).forEach(([key, value]) => hash.set(key, value))
    url.hash = hash.toString()
    const nextSource = url.toString()
    if (frame.src !== nextSource) frame.src = nextSource
    frame.setAttribute("scrolling", "no")
    frame.setAttribute("tabindex", "-1")
  })

  document.querySelectorAll("footer a[href^='http']").forEach((link) => {
    link.setAttribute("target", "_blank")
    link.setAttribute("rel", "noopener noreferrer")
  })
}

document.addEventListener("nav", applySiteTweaks)
document.addEventListener("render", applySiteTweaks)
`

export const SiteTweaks: QuartzTransformerPlugin = () => ({
  name: "SiteTweaks",
  externalResources() {
    return {
      additionalHead: [<meta name="robots" content="noindex, nofollow" />],
      js: [
        {
          loadTime: "afterDOMReady",
          contentType: "inline",
          script: enhanceSite,
          spaPreserve: true,
        },
      ],
    }
  },
})
