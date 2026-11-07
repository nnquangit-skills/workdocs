# Changelog

## 1.1.0 - 2026-11-07

- Look: same visual language as the workmap skill (map-paper background, teal accent, pill navigation, section cards, tinted status tags, eyebrow above the title), in workdocs' own stylesheet and `--wd-` tokens. No workmap file is used.
- Motion: animated flow (`section.wd-flow`, SMIL packets along real calls) and a step player (`ol.wd-steps[data-player]`: sequence diagram drawn above the list that walks the steps on its own, looping, from the moment it scrolls into view). No controls: documentation is read, not operated. Both stop under reduced motion and while the tab is hidden; the HTML list is the content.
- `assets/snippets.html`: ready-made blocks for the flow, the step player, the Work map card (installed / not installed), the nav entry and the optional local video.
- Work map pairing: nav entry and link card when workmap is installed; one pointer card on the Overview (`data-workdocs="promo"`) plus the report line when it is not. Optional video with a Remotion skill, only on request.
- Theme choice stored under the shared key `docs-theme` (the workmap page uses the same one) and applied from the page head before the first paint.
- Frontmatter metadata (author, version, licence), MIT licence, README and this changelog.

## 1.0.0

- Six static, evidence-based English pages with managed sections, backups and migration rules; theme toggle and copy buttons; QA checklist.
