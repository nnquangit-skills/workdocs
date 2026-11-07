# workdocs (the skill repo)

The skill itself is at the repo root (SKILL.md, assets/, references/) and is what gets copied into `~/.claude/skills/workdocs/`. `.bak/` holds local backups and is not committed.

- Free skill (MIT). It documents a project: six static English HTML pages in the target project's `docs/`, written from the code. Documentation is read, not operated: animations run on their own, no buttons.
- It never bundles or recreates the paid workmap skill; it links the work map when workmap is installed and shows one pointer card otherwise (SKILL.md, "Work map" section).
- Keep the look in step with workmap: same tokens (`--wd-*` here, `--*` in the workmap template), same `docs-theme` localStorage key, the map page reuses the docs navigation.
- After changing `assets/`, refresh the demo in the workmap repo (`tracking/docs/assets/`) and check a page in a browser: light, dark, 375 px, no console errors, no external requests.
