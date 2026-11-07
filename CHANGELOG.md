# Changelog

## 1.2.0 - 2026-11-07

- Diagrams: `references/diagrams.md` says which diagram answers which reader question and where it goes: architecture on the Overview (required), workflow (Process), lifecycle (States) and data flow on How it works, or on Security / API when that is where the question is asked. Made with the archify skill when installed, from cited source lines, with the JSON source kept in `docs/diagrams/src/` for regeneration; inline SVG otherwise.
- Frames: `figure.wd-frame` (snippet 6) embeds a self-contained diagram file with a caption and an "Open full screen" link; `workdocs.js` shows only the drawing (`?embed=1`) and keeps it in the docs theme (`?theme=`) once the reader has chosen one; the frame keeps the drawing's shape through `aspect-ratio`, so nothing is clipped at any width.
- QA: diagram checks (no network, `iframe title`, caption link, source present, both themes, 375 px).

## 1.1.0 - 2026-11-07

- Look: same visual language as the workmap skill (map-paper background, teal accent, pill navigation, section cards, tinted status tags, eyebrow above the title), in workdocs' own stylesheet and `--wd-` tokens. No workmap file is used.
- Motion: animated flow (`section.wd-flow`, SMIL packets along real calls) and a step player (`ol.wd-steps[data-player]`: sequence diagram drawn above the list that walks the steps on its own, looping, from the moment it scrolls into view). No controls: documentation is read, not operated. Both stop under reduced motion and while the tab is hidden; the HTML list is the content.
- `assets/snippets.html`: ready-made blocks for the flow, the step player, the Work map card (installed / not installed), the nav entry and the optional local video.
- Work map pairing: nav entry and link card when workmap is installed; one pointer card on the Overview (`data-workdocs="promo"`) plus the report line when it is not. Optional video with a Remotion skill, only on request.
- Theme choice stored under the shared key `docs-theme` (the workmap page uses the same one) and applied from the page head before the first paint.
- Frontmatter metadata (author, version, licence), MIT licence, README and this changelog.

## 1.0.0

- Six static, evidence-based English pages with managed sections, backups and migration rules; theme toggle and copy buttons; QA checklist.
