import { SocialImageOptions } from "../util/og"

export const SocialImage: SocialImageOptions["imageStructure"] = ({
    cfg,
    title,
    description,
    fileData,
    fonts,
    iconBase64,
}) => {
    // Theme colors from request:
    // Background: #161618
    // Accent: #fed588
    // White text

    const bg = "#161618"
    const accent = "#fed588"
    const text = "#ffffff"
    const gray = "#d4d4d4" // Using darkgray from theme for secondary text

    const fontBreakPoint = 22
    const useSmallerFont = title.length > fontBreakPoint

    const bodyFont = fonts[1].name
    const headerFont = fonts[0].name

    return (
        <div
            style={{
                display: "flex",
                flexDirection: "row",
                justifyContent: "flex-start",
                alignItems: "center",
                height: "100%",
                width: "100%",
                backgroundColor: bg,
                padding: "4rem",
            }}
        >
            <div
                style={{
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "space-between",
                    height: "100%",
                    width: "100%",
                }}
            >
                <div style={{ display: "flex", flexDirection: "column" }}>
                    <div
                        style={{
                            display: "flex",
                            alignItems: "center",
                            gap: "1rem",
                            marginBottom: "2rem",
                        }}
                    >
                        {iconBase64 && (
                            <img
                                src={iconBase64}
                                width={64}
                                height={64}
                                style={{
                                    borderRadius: "50%",
                                }}
                            />
                        )}
                        <p
                            style={{
                                color: accent,
                                fontSize: 32,
                                fontFamily: headerFont,
                                fontWeight: 600,
                                margin: 0,
                            }}
                        >
                            {cfg.pageTitle}
                        </p>
                    </div>

                    <h1
                        style={{
                            color: text,
                            fontSize: useSmallerFont ? 72 : 96,
                            fontFamily: headerFont,
                            fontWeight: 700,
                            lineHeight: 1.1,
                            marginBottom: "1.5rem",
                        }}
                    >
                        {title}
                    </h1>

                    <p
                        style={{
                            color: gray,
                            fontSize: 40,
                            fontFamily: bodyFont,
                            lineHeight: 1.4,
                            display: "-webkit-box",
                            WebkitLineClamp: 3,
                            textOverflow: "ellipsis",
                            overflow: "hidden",
                            maxWidth: "90%",
                        }}
                    >
                        {description}
                    </p>
                </div>

                <div
                    style={{
                        display: "flex",
                        justifyContent: "space-between",
                        alignItems: "flex-end",
                        width: "100%",
                    }}
                >
                    <div style={{ display: "flex", gap: "1rem" }}>
                        {fileData.frontmatter?.tags?.slice(0, 4).map((tag: string) => (
                            <span
                                style={{
                                    backgroundColor: "rgba(254, 213, 136, 0.1)",
                                    color: accent,
                                    padding: "0.5rem 1rem",
                                    borderRadius: "8px",
                                    fontSize: 24,
                                    fontFamily: bodyFont,
                                }}
                            >
                                #{tag}
                            </span>
                        ))}
                    </div>
                    <p
                        style={{
                            color: text,
                            fontSize: 28,
                            fontFamily: bodyFont,
                            opacity: 0.6,
                            margin: 0,
                        }}
                    >
                        {cfg.baseUrl}
                    </p>
                </div>
            </div>

            {/* Decorative accent bar */}
            <div
                style={{
                    position: "absolute",
                    top: 0,
                    right: 0,
                    width: "16px",
                    height: "100%",
                    backgroundColor: accent,
                }}
            />
        </div>
    )
}
