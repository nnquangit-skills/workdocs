# Diagrams

Which diagram answers which reader question, where it goes, how it is made and kept regenerable. Every diagram is drawn from code you read; none is decoration. The animated flow and the step player on How it works stay as they are (they are workdocs' own); the diagrams below are added next to them when the project has something to show.

## Which diagram where

| Reader question | Diagram | Page and section (id) | Add it when |
|---|---|---|---|
| What are the parts and how do they connect? | **Architecture** | Overview → Architecture (`arch`) | always: archify or diagram-design when installed, otherwise an original inline SVG |
| What happens, in which lane, through which gates and branches? | **Workflow** | How it works → Process (`process`), after Step by step | the run has phases, approvals, retries or branches that the one-request sequence does not show |
| In which states can the main object be, and what moves it? | **Lifecycle** | How it works → States (`states`), after Process; on API when the states are API statuses | the project has an object with a status (order, job, node, page, invoice …) |
| Where does data come from, what transforms it, who consumes it? | **Data flow** | How it works → Data flow (`data`); or Security → Assets & trust boundaries when the point is what crosses a trust boundary; or API when the pipeline is the interface | data moves through stages (pipeline, lineage, ETL, render chain) |
| Who calls whom, in what order, for one request? | **Sequence** | How it works → Step by step is already a self-running sequence (the step player). An archify sequence goes on API → Request & response only when one request crosses more than three components and the step list would be too long | rarely |

Never two diagrams that say the same thing. Two to four diagrams per project is typical; only Architecture is required. A page that gets none says nothing about it.

## With archify (when installed)

1. Load archify's complete instructions (its `SKILL.md`, the authoring defaults and the schema and example of each type you use). Follow them for authoring and repair; this file only fixes where the files live and how they are embedded.
2. **Files.** Source `docs/diagrams/src/<name>.json`, output `docs/diagrams/<name>.html`, `meta.output` set to that output path relative to the project root, `meta.quality_profile` `"showcase"`. Names by type: `architecture`, `workflow`, `lifecycle`, `dataflow`, `sequence-<topic>`. Commit the sources with the pages: a later run edits the JSON (positions stay) and regenerates.
3. **Evidence.** For a real repository pin `meta.repository` (credential-free origin URL, the 40-character `HEAD`, `link_mode: "local-only"` for an SSH origin) and give each node `sources` with `path`, `line` and `end_line` of the code you read. Pass `--repo-root <project>`; archify checks the cited lines against the committed bytes. Cite committed lines; when you later edit a cited file, regenerate against the new commit.
4. **Command**, from the project root, one call per diagram:
   `node <archify>/bin/archify.mjs finalize <type> docs/diagrams/src/<name>.json docs/diagrams/<name>.html --repo-root . --quality showcase --json --out-dir <scratch>/<name>`
   The evidence receipts go to the scratch folder. archify also writes `docs/diagrams/<name>.delivery.json`, a small provenance receipt; keep it (nothing requests it). A non-zero exit is never success: edit the JSON as the diagnostics say and rerun. Never edit the HTML by hand.
5. **Embed** with block 6 of `assets/snippets.html`: `figure.wd-frame` holding an `iframe` to the file (with a `title`) and a caption with the "Open full screen" link. `assets/workdocs.js` adds `?embed=1` (drawing only) and, when the reader has chosen a theme, `&theme=light|dark`, so the frame matches the docs and follows the toggle; the link opens the full viewer (cards, export). Without JS the frame shows the full viewer following the system theme. The drawing scales with the column, so give the iframe `style="aspect-ratio: W / H"` with W and H from the drawing's viewBox (`grep -o 'viewBox="[^"]*"' docs/diagrams/<name>.html | head -1`), H plus about 50 for the legend; the stylesheet's `min-height` keeps the legend visible on a phone.
6. **Text first.** Each frame sits in a section that explains the same thing in a paragraph or list and ends with a Source line naming the files the diagram was drawn from. A reader with the frame blocked loses nothing essential.
7. **Attribution.** The generated file embeds archify's viewer (MIT, © 2026 tt-a1i, © 2025 Cocoon AI) without its licence text. Keep that notice in the project's `NOTICE` or licence file (or the page footer) when `docs/diagrams/` is distributed.
8. Mention archify's update notice, when its receipt asks for one, once in your report; never install or update it yourself.

## Without archify

`diagram-design` when installed, same placement, source kept next to the output. Otherwise an original inline SVG (`svg.wd-diagram`, the CSS tokens, `role="img"` with an `aria-label` that reads as a sentence) for the architecture only; do not hand-draw a lifecycle or a data flow unless it is tiny. Say in the report which path was used.

## QA for diagrams

- Network: `grep -nE 'fetch\(|XMLHttp[R]equest|@import|url\(https?:|(src|href)="https?:' docs/diagrams/*.html`; the only allowed hits are `xmlns` and licence or documentation URLs inside text or comments. Confirm in the browser: the frame loads from `docs/` served alone and from `file://`, with no request to another origin.
- Every frame has an `iframe title`, a caption, a working "Open full screen" link, and a `docs/diagrams/src/*.json` source.
- Both themes: toggle the docs theme and check the frame follows (with JS); check the frame also reads in the system theme without JS.
- 375 px: the frame scales to the column; the page does not scroll sideways.
