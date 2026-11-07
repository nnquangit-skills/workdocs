import { Composition } from "remotion";
import { SCENES, WorkdocsDemo } from "./WorkdocsDemo";

const FPS = 30;
const total = Math.round((SCENES.chat + SCENES.browser + SCENES.outro - SCENES.cut - SCENES.fade) * FPS);

export const RemotionRoot = () => {
  return (
    <>
      <Composition id="WorkdocsDemo" component={WorkdocsDemo} durationInFrames={total} fps={FPS} width={1920} height={1080} />
    </>
  );
};
