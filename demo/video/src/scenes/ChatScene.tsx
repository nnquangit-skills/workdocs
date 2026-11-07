import { Audio } from "@remotion/media";
import { AbsoluteFill, Easing, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, mono, sans } from "../theme";

// A chat with the agent: the user types only "/workdocs"; the agent streams its reply.
const USER_TEXT = "/workdocs";
// Timed against public/vo-chat.m4a: "…you type one command: slash workdocs" lands at about 4-7 s.
const USER_AT = 4.4; // seconds: typing starts
const SEND_AT = 6.6; // seconds: Enter pressed, bubble lands
const REPLY_AT = 7.3; // seconds: agent reply starts streaming

type Line = { at: number; text: string; color?: string; bold?: boolean };
const REPLY: Line[] = [
  { at: 0.0, text: "workdocs skill loaded. Reading the project…", bold: true },
  { at: 0.6, text: "  read: README.md, package.json, src/server.ts, src/routes/*.ts, test/" },
  { at: 1.6, text: "Writing six pages from the evidence…", bold: true },
  { at: 2.6, text: "  created: docs/index.html         Overview", color: colors.done },
  { at: 3.4, text: "  created: docs/setup.html         Setup", color: colors.done },
  { at: 4.2, text: "  created: docs/how-it-works.html  flow + sequence diagram", color: colors.done },
  { at: 5.0, text: "  created: docs/security.html      Security", color: colors.done },
  { at: 5.8, text: "  created: docs/api.html           API", color: colors.done },
  { at: 6.6, text: "  created: docs/demo.html          Demo script", color: colors.done },
  { at: 8.0, text: "QA: 6 pages · 0 console errors · 375px ok · no external requests", bold: true },
  { at: 8.8, text: "  work map: installed → linked in the navigation", color: colors.doing },
  { at: 9.6, text: "  ← opening docs/index.html in Chrome", color: colors.accent },
];

const Typed = ({ text, startAt, cps }: { text: string; startAt: number; cps: number }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const n = Math.max(0, Math.min(text.length, Math.floor(((frame - startAt * fps) / fps) * cps)));
  const typing = frame >= startAt * fps && n < text.length;
  return (
    <span>
      {text.slice(0, n)}
      {typing && <span style={{ color: colors.accent }}>▍</span>}
    </span>
  );
};

const ReplyLine = ({ line }: { line: Line }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const start = (REPLY_AT + line.at) * fps;
  if (frame < start) return null;
  return (
    <div
      style={{
        whiteSpace: "pre",
        color: line.color ?? (line.bold ? colors.text : colors.muted),
        fontWeight: line.bold ? 600 : 400,
        opacity: interpolate(frame, [start, start + 0.25 * fps], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
        translate: `0px ${interpolate(frame, [start, start + 0.3 * fps], [8, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) })}px`,
      }}
    >
      {line.text}
    </div>
  );
};

export const ChatScene = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const sent = frame >= SEND_AT * fps;
  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg, fontFamily: sans, color: colors.text, alignItems: "center", justifyContent: "center" }}>
      <Audio src={staticFile("vo-chat.m4a")} />
      <div
        style={{
          width: 1560,
          height: 900,
          borderRadius: 28,
          backgroundColor: colors.surface,
          border: `1px solid ${colors.border}`,
          boxShadow: "0 40px 120px rgba(0,0,0,.45)",
          display: "flex",
          flexDirection: "column",
          overflow: "hidden",
          opacity: interpolate(frame, [0, 0.4 * fps], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
          scale: String(interpolate(frame, [0, 0.6 * fps], [0.97, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) })),
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 12, padding: "18px 26px", borderBottom: `1px solid ${colors.border}`, fontSize: 24, color: colors.muted }}>
          <span style={{ width: 12, height: 12, borderRadius: 6, backgroundColor: colors.done, display: "block" }} />
          Claude Code · acme-commerce
        </div>
        <div style={{ flex: 1, padding: "34px 40px", display: "flex", flexDirection: "column", gap: 26, fontSize: 30, lineHeight: 1.5 }}>
          {sent && (
            <div style={{ display: "flex", gap: 18, alignItems: "flex-start", order: 2 }}>
              <div style={{ width: 44, height: 44, borderRadius: 12, backgroundColor: colors.teal, color: "#fff", display: "grid", placeItems: "center", fontWeight: 700, fontSize: 20, flex: "none" }}>wd</div>
              <div style={{ fontFamily: mono, fontSize: 27, lineHeight: 1.55, backgroundColor: colors.bg, border: `1px solid ${colors.border}`, borderRadius: 18, padding: "20px 26px", minWidth: 900 }}>
                {REPLY.map((l) => (
                  <ReplyLine key={l.at} line={l} />
                ))}
              </div>
            </div>
          )}
          {sent && (
            <div style={{ display: "flex", justifyContent: "flex-end", order: 1 }}>
              <div
                style={{
                  backgroundColor: colors.teal,
                  color: "#fff",
                  borderRadius: 18,
                  padding: "14px 24px",
                  fontFamily: mono,
                  fontSize: 30,
                  opacity: interpolate(frame, [SEND_AT * fps, (SEND_AT + 0.3) * fps], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
                  translate: `0px ${interpolate(frame, [SEND_AT * fps, (SEND_AT + 0.35) * fps], [40, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) })}px`,
                }}
              >
                {USER_TEXT}
              </div>
            </div>
          )}
        </div>
        <div style={{ margin: "0 40px 34px", borderRadius: 18, border: `1px solid ${colors.border}`, backgroundColor: colors.bg, padding: "18px 26px", fontFamily: mono, fontSize: 30, minHeight: 78, display: "flex", alignItems: "center", gap: 14 }}>
          <span style={{ color: colors.muted }}>›</span>
          {sent ? <span style={{ color: colors.muted }}>Type a message…</span> : <Typed text={USER_TEXT} startAt={USER_AT} cps={9} />}
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
        One command. Six pages written from the code.
      </div>
    </AbsoluteFill>
  );
};
