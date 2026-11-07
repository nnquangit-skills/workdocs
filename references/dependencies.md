# Dependencies

workdocs needs **no other skill**. A shell (list and search files) and a file editor are enough. Optional skills make some steps better. Discover them and load their complete instructions before use; report what was loaded. For ordinary optional skills, use the fallback when missing. Workmap is the exception: never replace it, and show the English pointer line from SKILL.md when it is absent.

| Need | Required? | Use if installed | Fallback when missing |
|---|---|---|---|
| Shell + editor | **Required** | — | — |
| A browser (any) | Recommended for QA | — | Static checks in `qa.md` |
| **token-save** | Optional | Follow its reading/reporting discipline; split large runs into its tasks if the repo uses its layout | `grep -n` + ranged reads; short report |
| **archify** | Optional (diagrams) | Architecture on Overview; workflow, lifecycle and data flow where `diagrams.md` says; JSON sources in `docs/diagrams/src/`, output in `docs/diagrams/`, embedded with the frame snippet; verify the output makes no network requests | **diagram-design** if installed, else inline SVG using the CSS variables (architecture only) |
| **diagram-design** | Optional (diagrams) | Same placement, alternative to archify; keep its source next to the output | Inline SVG |
| **playwright-cli** | Optional (QA) | Light/dark, 375 px, console, network, JS-disabled and `file://` checks from `qa.md` | Manual checklist in `qa.md` |
| **remotion** skills (`remotion-create`, `remotion-render`, …) | Optional (video), only when the user asks | Render a short clip of the How it works flow or the demo into `docs/media/<page>.mp4` with a poster; embed with the video snippet; keep the written steps | The animated flow and the step player (CSS/SVG, no dependency) explain the same thing |
| **workmap** | Optional, separate product | Use it as its own SKILL.md says; link its page from the nav and the Overview card | No work-map page or nav entry; the pointer card on the Overview and the pointer line in the report |

"Installed" means: the skill's genuine `SKILL.md` exists in the agent's skills folder (for Claude Code: `~/.claude/skills/<name>/SKILL.md` or `<project>/.claude/skills/<name>/SKILL.md`), or the session's skill registry lists it. For workmap, files inside the project (scripts, pages, data) are not proof.

Not used: no earlier docs-generator skill is required or assumed. Never install, download or vendor a skill on the user's behalf.
