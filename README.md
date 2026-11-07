# workdocs - six honest documentation pages, written by your agent from the code

**A free skill for Claude Code and any agent that supports the Agent Skills format (SKILL.md).** Say `workdocs` in a project and the agent writes or refreshes six reader-facing pages in `docs/`: **Overview, Setup, How it works, Security, API** and **Demo script**. Every claim comes from files the agent actually read; mocked and planned parts are labelled; the pages are plain static HTML that open from a folder or any static server.

```
docs/
├── index.html          Overview: what it is, status (real vs mocked), architecture, quick start
├── setup.html          Setup: prerequisites, install, configuration, run, test, verify, troubleshooting
├── how-it-works.html   How it works: animated flow + one request walked step by step
├── security.html       Security: trust boundaries, threats and controls, secrets, known gaps
├── api.html            API: endpoints or commands, shapes, errors, try it
├── demo.html           Demo script: a presenter's script with fallbacks and cleanup
└── assets/             workdocs.css, workdocs.js (presentation only)
```

## Why

Most project docs are either missing, out of date, or written from memory. workdocs makes the agent read the manifest, entry points, handlers, config and tests first, and write only what it can point at. Each page carries its sources; each section sits inside markers so a later run regenerates just what changed and keeps what you wrote by hand.

## What you get

- **Evidence first.** Versions, ports, commands, endpoints and guarantees come from the repository, never from memory. If a page does not apply, it says what is absent and what exists instead.
- **Static and honest.** Content is embedded at authoring time. An opened page fetches nothing, works over `file://` and stays readable with JavaScript off. Mock, simulated and flag-dependent behaviour is marked wherever it appears.
- **Motion that explains, nothing to click.** On How it works, an animated flow shows the real calls between the real components, and a sequence diagram walks one request through its steps on its own. The Demo script uses the same player as a timeline. Pure CSS and SVG; both stop under reduced motion.
- **One look.** A pale "map paper" background, one reading column, a sticky pill navigation, every section a card; light and dark with one toggle. The same visual language as the workmap skill, so the two sit side by side as one site.
- **Safe updates.** Managed sections carry `<!-- workdocs:begin id=… -->` markers; replaced files are backed up first; legacy pages are migrated, not deleted.
- **Optional video.** With a Remotion skill installed, the agent can render a short clip into `docs/media/` and embed it above the steps. Never required.

## Install

Copy this folder to your agent's skills directory:

```bash
git clone git@github.com:nnquangit-skills/workdocs.git ~/.claude/skills/workdocs
```

(or `<project>/.claude/skills/workdocs/` for one project). Then, inside a project, say **"workdocs"** (or `/workdocs`), or ask for the documentation to be written or refreshed. The agent reads the code, writes the six pages, runs the QA checklist and reports what it created, what it replaced, where the backups are and which claims it could not prove.

Requirements: a shell and a file editor for the agent. The pages need nothing: no runtime, no framework, no network. Optional helpers the skill uses when present: a diagram skill (archify, diagram-design), `playwright-cli` for browser QA, a Remotion skill for the video.

## workdocs + workmap: documentation and progress, one site

workdocs documents what the project **is**. **[workmap](https://www.agensi.io/skills/workmap-project-work-map-for-ai-agents)** tracks what the project is **doing**: a live map of Epics → Features → Tasks → Subtasks, every node with a stable id, a status and the name of the agent or person on it, kept up to date by the agents themselves.

What workmap adds, in one page and four commands:

- **`docs/workmap.html`** - the whole project as a mindmap with a progress bar, status-coloured chips, a running light on work in progress, owner tags, expand / collapse, full screen. One self-contained file that opens from `file://`.
- **A CLI the agents actually use** - `show`, `find`, `add`, `set`: a few tokens to see where work belongs, one command to log it. Parent status is computed, cancelled items stay struck through, nothing is ever deleted.
- **Markdown as the source of truth** - `docs/shared/workmap.md`, a nested list anyone can read or grep.
- **A mandatory reporting protocol** - loaded with the skill and written into the project's agent rules: log before starting, mark when done, pass the rules to every subagent, end every turn with a Workmap report. *Done means the map says done.*

Installed together, the two behave as one site: workdocs puts **Work map** in its navigation and on the Overview, the map page picks up the same navigation and the same light / dark choice. Without workmap, workdocs still writes all six pages and shows one small card pointing to it (easy to remove).

**Get workmap:** https://www.agensi.io/skills/workmap-project-work-map-for-ai-agents · 30-second demo: https://youtu.be/b1yCp2lN2aw

## Files

```
workdocs/
├── SKILL.md              instructions the agent loads (rules, run, writing pages, workmap rule)
├── LICENSE.txt           MIT
├── CHANGELOG.md
├── assets/               page.html (template), workdocs.css, workdocs.js, snippets.html (flow, step player, cards, video)
└── references/           pages.md (content per page), static.md (static rules, migration), dependencies.md, qa.md
```

## Licence and support

MIT. Files the skill writes into your project are yours. Questions and bug reports: nnquangit@gmail.com (Quang Ngo).
