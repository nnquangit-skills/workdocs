import { loadFont as loadSans } from "@remotion/google-fonts/BeVietnamPro";
import { loadFont as loadMono } from "@remotion/google-fonts/JetBrainsMono";

export const sans = loadSans("normal", {
  weights: ["400", "500", "600", "700"],
  subsets: ["latin", "vietnamese"],
}).fontFamily;

export const mono = loadMono("normal", {
  weights: ["400", "600"],
  subsets: ["latin"],
}).fontFamily;

// Same palette as the product page (docs.css + workmap.template.html, "Balanced").
export const colors = {
  bg: "#121716",
  surface: "#1a2120",
  border: "#2e3a37",
  text: "#e6ebe8",
  muted: "#97a5a0",
  accent: "#4cc2b1",
  teal: "#0f6e63",
  paper: "#f4f6f2",
  ink: "#1c2426",
  done: "#5fcf90",
  doing: "#6aa6e6",
  pause: "#e3b14a",
  cancel: "#ec8484",
  pending: "#8a95a1",
};
