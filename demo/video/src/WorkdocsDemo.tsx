import { linearTiming, TransitionSeries } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { useVideoConfig } from "remotion";
import { BrowserScene } from "./scenes/BrowserScene";
import { ChatScene } from "./scenes/ChatScene";
import { Outro } from "./scenes/Outro";

// Scene durations in seconds. Total = sum - the two transitions.
// Scene lengths follow the narration clips in public/ (vo-chat 17.5 s, vo-browser 19.9 s, vo-outro 6.1 s).
export const SCENES = { chat: 18.2, browser: 20.5, outro: 7.0, cut: 0.5, fade: 0.4 };

export const WorkdocsDemo = () => {
  const { fps } = useVideoConfig();
  const t = (s: number) => Math.round(s * fps);
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence name="Chat: the user types /workdocs" durationInFrames={t(SCENES.chat)}>
        <ChatScene />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={slide({ direction: "from-right" })} timing={linearTiming({ durationInFrames: t(SCENES.cut) })} />
      <TransitionSeries.Sequence name="Chrome: the six pages" durationInFrames={t(SCENES.browser)}>
        <BrowserScene />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={fade()} timing={linearTiming({ durationInFrames: t(SCENES.fade) })} />
      <TransitionSeries.Sequence name="Outro" durationInFrames={t(SCENES.outro)}>
        <Outro />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};
