import { Audio, Video } from "@remotion/media";
import { AbsoluteFill, Easing, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, sans } from "../theme";

// A browser window frame around the real screen recording of the six pages (public/chrome.mp4, 1920x1080).
export const BrowserScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg, alignItems: "center", justifyContent: "flex-start", paddingTop: 128, fontFamily: sans }}>
      <Audio src={staticFile("vo-browser.m4a")} />
      <div
        style={{
          width: 1600,
          height: 900,
          borderRadius: 22,
          overflow: "hidden",
          backgroundColor: "#ffffff",
          boxShadow: "0 40px 120px rgba(0,0,0,.5)",
          border: `1px solid ${colors.border}`,
          display: "flex",
          flexDirection: "column",
          opacity: interpolate(frame, [0, 0.4 * fps], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
          scale: String(interpolate(frame, [0, 0.7 * fps], [0.96, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) })),
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 10, padding: "12px 18px", backgroundColor: "#dfe3e6", borderBottom: "1px solid #c9ced3" }}>
          {["#ff5f57", "#febc2e", "#28c840"].map((c) => (
            <span key={c} style={{ width: 14, height: 14, borderRadius: 7, backgroundColor: c, display: "block" }} />
          ))}
          <div style={{ marginLeft: 16, flex: 1, backgroundColor: "#ffffff", borderRadius: 999, padding: "8px 18px", fontSize: 22, color: "#4a5560", fontFamily: sans }}>
            127.0.0.1:4590/docs/how-it-works.html
          </div>
        </div>
        <div style={{ flex: 1, position: "relative", overflow: "hidden" }}>
          <Video src={staticFile("chrome.mp4")} style={{ position: "absolute", left: 0, top: 0, width: 1598, height: 899, objectFit: "cover", objectPosition: "top left" }} muted />
        </div>
      </div>
      <div
        style={{
          position: "absolute",
          top: 44,
          fontSize: 40,
          fontWeight: 600,
          color: colors.muted,
          opacity: interpolate(frame, [0.3 * fps, 0.7 * fps], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
        }}
      >
        The result: six static pages in docs/, every claim traced to a file
      </div>
    </AbsoluteFill>
  );
};
