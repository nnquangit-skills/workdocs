# Static output and migration

## What "static" means

- At authoring time you read README, manifest, config, code and existing notes, and write the resulting prose, tables, commands and code samples **directly into the HTML**. The page is the finished artefact; it is not a viewer for another file.
- An opened page makes **no** requests for `.md`, `.json`, README, API endpoints or anything on another origin. Allowed requests: its own stylesheet, the optional `assets/workdocs.js`, local images, local media in `docs/media/` (optional video with `controls`, a poster and no autoplay) and local self-contained diagram files inside `docs/`.
- Navigation is real `<nav>` markup in every page. The current page carries `aria-current="page"` in the HTML itself.
- With JS disabled, every section, table, command and link is still present and readable. JS may only add presentation: the theme toggle, copy buttons, the animated flow and the sequence diagram of the step player, which is drawn from a list that is already in the HTML. It never inserts content and never adds controls.
- Motion: documentation is read, not operated. The animated flow (SMIL `animateMotion` and CSS) and the step player run on their own, with no buttons or keyboard controls; both stop under `prefers-reduced-motion: reduce` and while the tab is hidden, and the step player starts when it scrolls into view. No motion is required to understand a page.
- Pages work over `file://` and when a static server serves `docs/` alone. Therefore no link or asset may point outside `docs/` (no `../README.md`, no `../src/...`). Refer to repository files as code text (`src/server.ts`) instead of linking them. The only external links are deliberate ones: the hosted repository URL if the README states one, and the two links of the Work map pointer card.
- Themes: light/dark follows `prefers-color-scheme` in CSS; the toggle is added by JS and the choice is stored in `localStorage` under the key `docs-theme`, guarded so that `file://` or blocked storage cannot throw. The workmap page reads and writes the same key, so one choice applies to every page in `docs/`. The one-line script in the `<head>` of `page.html` applies the stored choice before the first paint.
- Diagrams: embed inline SVG, or link/iframe a self-contained HTML diagram inside `docs/`. Before linking, search it with `grep -nE 'fetch\(|XMLHttp[R]equest|@import|url\(https?:|(src|href)="https?:'` and confirm in the browser that it makes no network requests.
- When sources change later, re-run workdocs: re-read the sources and regenerate the affected sections. Record the date and source files in each page footer so readers know how fresh it is.

## Forbidden in the six pages

- Network APIs: the Fetch API, XHR, dynamic `import()` of content, `EventSource`, `WebSocket`.
- Attributes that tell a script to load content (any `data-*` attribute naming a source file, such as markdown or include attributes).
- Loader helpers such as markdown-include or JSON-table renderers, and "Loading…" placeholders.
- Web fonts, CDNs, analytics, external images.

## Migrating legacy pages

1. Back up every page you will change, in full, to `docs/.workdocs-backup/static-<YYYYMMDD-HHMMSS>/`, keeping file names. Back up the markdown/JSON sources the old pages loaded as well. Confirm the copies exist and match (checksum) before editing.
2. Inventory each old page: static text, dynamically loaded sections (and which source they loaded), unique details (numbers, commands, file:line references, caveats).
3. Write the new page from the current sources. Carry forward every unique detail that is still accurate. Consolidate duplicates into one place and link to it.
4. Drop stale claims: anything contradicted by current code, planned features written as present, and numbers you cannot trace.
5. Remove legacy load attributes and loader `<script>` includes from the six pages. Leave the old shared loader file on disk if other pages (for example a work-map page) still use it; do not modify those other pages.
6. Translate reader-facing text to English while doing so; keep identifiers and UI labels verbatim.
7. Report per file: what was removed, what was carried forward, what was dropped as stale, and where the backup is.
