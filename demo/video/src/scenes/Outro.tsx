import { Audio } from "@remotion/media";
import { AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, sans } from "../theme";

export const Outro = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inAt = (at: number) => ({
    opacity: interpolate(frame, [at * fps, (at + 0.4) * fps], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
    translate: `0px ${interpolate(frame, [at * fps, (at + 0.6) * fps], [24, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) })}px`,
  });
  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg, color: colors.text, fontFamily: sans, alignItems: "center", justifyContent: "center", overflow: "hidden" }}>
      <Audio src={staticFile("vo-outro.m4a")} />
      <Img
        src={staticFile("workdocs-dark-full.png")}
        style={{ position: "absolute", left: 0, top: -200, width: 1920, height: 2200, opacity: 0.18, scale: String(interpolate(frame, [0, 4 * fps], [1, 1.06], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })) }}
      />
      <div style={{ display: "flex", alignItems: "center", gap: 36, ...inAt(0.1) }}>
        <Img src={staticFile("logo-512.png")} style={{ width: 140, height: 140, borderRadius: 34 }} />
        <div style={{ fontSize: 120, fontWeight: 700, letterSpacing: -3, lineHeight: 1 }}>workdocs</div>
      </div>
      <div style={{ fontSize: 50, fontWeight: 600, marginTop: 40, ...inAt(0.6) }}>
        Written from the code. <span style={{ color: colors.accent }}>Read, not operated.</span>
      </div>
      <div style={{ fontSize: 36, color: colors.muted, marginTop: 24, ...inAt(1.0) }}>free · static HTML · no framework · pairs with workmap</div>
      <div style={{ fontSize: 36, color: colors.muted, marginTop: 70, ...inAt(1.5) }}>a skill for Claude Code and other SKILL.md agents · by Quang Ngo</div>
    </AbsoluteFill>
  );
};
