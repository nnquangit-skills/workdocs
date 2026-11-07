# workdocs - listing copy (English, free listing)

Live at https://www.agensi.io/skills/workdocs-honest-docs-pages-written-from-the-code (free). Paste into the marketplace listing. Screenshots and the logo are next to this file; the demo video is `workdocs-demo.mp4` with `workdocs-demo.en.srt`, published at https://youtu.be/EuZ_iwpUpuc.

## Title

workdocs - six honest documentation pages, written from the code

## Tagline (one line)

Free. Your agent reads the code and writes Overview, Setup, How it works, Security, API and a Demo script as static HTML, each section naming the files it came from, with self-running animated flows and interactive diagrams. Pairs with workmap.

## Description

Documentation written from the code, not from memory.

Most project docs are missing, stale, or written from memory. **workdocs** puts the job on the agent. Say `workdocs` in a project and it reads the manifest, entry points, handlers, config and tests, then writes six reader-facing pages in `docs/`:

- **Overview** - what it is, status (real vs mocked), an interactive architecture diagram, quick start
- **Setup** - prerequisites, install, configuration, run, test, verify, troubleshooting
- **How it works** - an animated flow of the real calls, one request walked through a sequence diagram, and workflow and lifecycle diagrams when the project has them
- **Security** - trust boundaries, threats and controls, secrets, known gaps
- **API** - endpoints or commands, shapes, errors, try it
- **Demo script** - a presenter's script with fallbacks and cleanup

Each section names the files it came from. If a page does not apply, it says what is absent and what exists instead. Mocked, simulated and flag-dependent behaviour is labelled wherever it appears.

## What makes it different

- **Diagrams from the code.** With the archify skill installed, the agent draws interactive architecture, workflow, lifecycle and data-flow diagrams, each node citing the source lines it came from, and keeps their sources so the next run regenerates them. Without it, an inline SVG.
- **Static.** Content is embedded when the page is written. An opened page fetches nothing, works from `file://` and stays readable with JavaScript off.
- **Motion with nothing to click.** On How it works, an animated flow shows the real calls between the real components and a sequence diagram walks one request through its steps on its own. Both stop under reduced motion. CSS and SVG only; no framework, no build step.
- **One look.** A pale map-paper background, one reading column, pill navigation, every section a card, light and dark with one toggle.
- **Safe updates.** Managed sections carry markers; a later run regenerates only what changed, backs up what it replaces and keeps what you wrote by hand. Legacy pages are migrated, not deleted.

## Pairs with workmap

workdocs documents what the project **is**. [workmap](https://www.agensi.io/skills/workmap-project-work-map-for-ai-agents) tracks what it is **doing**: a live map of Epics → Features → Tasks → Subtasks with status and owner on every node, kept by the agents through a mandatory reporting protocol. Installed together they read as one site: workdocs links the map in its navigation and on the Overview, the map page picks up the same navigation and the same light / dark choice. Without workmap, workdocs still writes all six pages and shows one small card pointing to it.

## Requirements

A shell and a file editor for the agent; nothing for the pages (no runtime, framework or network). Optional helpers used when present: the archify skill for the diagrams (diagram-design as the alternative), `playwright-cli` for browser QA, a Remotion skill for an optional video.

## Privacy

No telemetry, no network calls. The agent writes only into the project's `docs/` and backs up anything it replaces.

## Licence

MIT. Files written into your project are yours.

## Support

nnquangit@gmail.com (Quang Ngo)

## Sample session

**Input**

Write the documentation for this repo (Acme Commerce). It is a TypeScript storefront API; payments are mocked by default.

**Output**

Wrote six pages in `docs/` from the code (commit 3f2a9c1).

**Created**: `docs/index.html`, `docs/setup.html`, `docs/how-it-works.html`, `docs/security.html`, `docs/api.html`, `docs/demo.html`, `docs/assets/workdocs.css`, `docs/assets/workdocs.js`. No existing pages, so no backups were needed.

**Evidence**: README.md, package.json (scripts, engines: node >=20), src/server.ts, src/routes/*.ts, src/payments/{index,mock,stripe}.ts, src/config.ts (PORT default 3000), .env.example (variable names only), test/ (42 tests). Marked as **mock by default**: payment capture (`PAYMENT_PROVIDER` unset). Marked **not found**: rate limiting.

**Checks run**: served `docs/` alone on 127.0.0.1:4590; 0 console errors on all six pages; no request for `.md`, `.json` or another origin; light and dark readable; 375 px: `scrollWidth` 375 on every page; nav identical on all six; every link resolves; the flow and the step player run and stop under reduced motion. Not verified: `file://` in Safari.

**Skills loaded**: workdocs; archify not installed (architecture diagram drawn as inline SVG from `src/server.ts`); playwright-cli used for QA.

**Work map**: workmap is not installed. The Overview shows one card pointing to it. Want a live work map for this project? Try Workmap – Project Work Map for AI Agents.

## FAQ

- **Does it need a build step or a server?** No. The pages are finished HTML; open them from a folder or serve `docs/` with any static server.
- **Can I edit the pages by hand?** Yes. Content outside the markers, and sections marked `data-workdocs="keep"`, survive the next run.
- **What if my project has no API or no security story?** The page still exists and says exactly what is absent and what exists instead. Nothing is invented.
- **Does it write diagrams?** Yes. The animated flow and the step player are always drawn from the real call sites. With the archify skill installed, the agent also draws interactive architecture, workflow, lifecycle and data-flow diagrams, each node citing its source lines, and keeps their JSON sources in `docs/diagrams/src/` so the next run regenerates them; without it, the architecture is an inline SVG.
- **Is workmap required?** No. workdocs is complete on its own; workmap is a separate skill it links to when installed.

## Known limitations

- English only for reader-facing text (code and UI labels stay verbatim).
- Six fixed pages; extra pages are up to you.
- The video on How it works is optional and needs a Remotion skill; by default the page uses the CSS/SVG animation.
- The agent can only document what it can read: generated or vendored code it skips stays undocumented and is listed as an evidence gap.

## Tags

documentation, docs, static html, technical writing, how it works, api docs, security docs, demo script, claude code, agent skills

## Category

Technical Documentation (also: Develop → Documentation)

## Price

Free
