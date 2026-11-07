# QA checklist

Serve **`docs/` alone** with a static server bound to localhost on a free port (e.g. `python3 -m http.server <port> --bind 127.0.0.1 --directory docs`), keep its log, note its PID, and stop only that PID when done. Never stop or probe processes you did not start.

Report only checks you actually ran. Anything skipped is listed as "not verified".

## Per page (all six)

- [ ] Opens with 0 console errors and 0 failed requests (a missing favicon is acceptable; say so).
- [ ] Network/server log shows no request for `.md`, `.json`, README or any other origin.
- [ ] No "Loading…", empty section, `TODO` or error box.
- [ ] Light **and** dark readable (`prefers-color-scheme` and the toggle, if present), including code blocks and tables.
- [ ] At 375 px: `document.documentElement.scrollWidth <= 375`; wide tables and code scroll inside their own box. Also check a desktop width.
- [ ] Nav lists exactly the allowed pages, identical on all six; current page marked; every internal link and `#anchor` resolves.
- [ ] One `h1`, headings in order, diagrams have text alternatives, focus visible.
- [ ] Animation (if any) runs on its own, with no buttons or keyboard controls on the page, and stops under `prefers-reduced-motion: reduce` (the flow shows no packets, the step diagram shows every step lit).
- [ ] Step player: the step list is readable with JS disabled; with JS, the highlight in the list and in the diagram advances by itself every few seconds and loops.
- [ ] Video (if any): local file in `docs/media/`, `controls`, a poster, no autoplay; the written steps are still on the page.
- [ ] Work map card and nav entry match the real workmap status (link only when workmap is installed and `docs/workmap.html` exists; otherwise the pointer card, Overview only).

## Static-delivery checks

- [ ] **JS disabled** (browser setting, or block `*.js` requests): nav and every required section still present.
- [ ] **file://**: open each page directly; content and nav present. Note honestly what differs (for example `localStorage` or iframes may behave differently).
- [ ] Linked diagrams load from `docs/` and make no network requests.
- [ ] Diagram frames (`figure.wd-frame`): the `iframe` has a `title`; the caption's "Open full screen" link resolves; the frame loads from `docs/` served alone and from `file://`; with JS the drawing follows the docs theme toggle; a source file exists in `docs/diagrams/src/` for every file in `docs/diagrams/` (see diagrams.md).

With **playwright-cli**: open each page, `resize 375 812` and a desktop size, `set-color-scheme light|dark`, `eval "document.documentElement.scrollWidth"`, `console`, `requests`; block scripts with `route "**/*.js" --status=404` (or a context with JS disabled) and check content; open `file://` URLs; then `close`.

## Static checks (no browser needed)

- Every `href`/`src` resolves to a file inside `docs/` or a deliberate external link.
- Diagram files make no network requests: `grep -nE 'fetch\(|XMLHttp[R]equest|@import|url\(https?:|(src|href)="https?:' docs/diagrams/*.html` shows only `xmlns` and URLs inside text or comments.
- Each `<!-- workdocs:begin id=x -->` has a matching `end`.
- Search the six pages for loaders and leftovers: `grep -nE 'fetch\(|XMLHttp[R]equest|data-(sr[c]|m[d]|wd-m[d]|includ[e])=|includeMarkdow[n]|Loading|TODO|lorem' docs/*.html`, and for anything that looks like a key (`sk-`, `AKIA`, `-----BEGIN`).
- Grep for non-English reader text (for a project previously documented in another language, search for that language's common words or diacritics).

## Honesty

- [ ] Every command appears in a manifest script, Makefile or README.
- [ ] Every version and port on Setup is traceable to the project.
- [ ] Every endpoint in `api.html` exists in the route/CLI definitions.
- [ ] Every security control cites code; gaps are listed, not hidden.
- [ ] Mocked, stubbed or planned parts are labelled wherever they appear.
- [ ] Unique accurate details from replaced pages were carried forward (compare with the backup).
