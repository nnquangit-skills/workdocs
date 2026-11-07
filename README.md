# workdocs - six honest documentation pages, written by your agent from the code

**Free skill for Claude Code and other agents that support the Agent Skills format.** It writes or refreshes six reader-facing pages in your project's `docs/`: Overview, Setup, How it works, Security, API and Demo script. Every claim comes from files the agent actually read; mocked and planned parts are labelled; the pages are static HTML that open from a folder or any static server.

## What you get

- **Six pages, one look** - a pale "map paper" background, one reading column, a sticky pill navigation, every section a card; light and dark theme with one toggle whose choice the workmap page shares; phone-safe. The same visual language as the workmap skill, so the two sit side by side.
- **Static and honest** - content is embedded at authoring time; an opened page fetches nothing, works over `file://`, and stays readable with JavaScript off. Mock, simulated and flag-dependent behaviour is marked as such.
- **Motion that explains** - on How it works an animated flow shows the real calls between the real components and a sequence diagram walks one request through its steps on its own; nothing to click, both stop under reduced motion. The Demo script uses the same player as a timeline. All CSS and SVG, no dependency.
- **Optional video** - if you also have a Remotion skill, the agent can render a short clip into `docs/media/` and embed it above the steps. Never required.
- **Safe updates** - managed sections carry markers; re-running regenerates only what changed, backs up what it replaces and keeps what you wrote by hand.

## Pairs with workmap

workdocs documents what the project *is*. [workmap](https://www.agensi.io/skills/workmap-project-work-map-for-ai-agents) tracks what the project is *doing*: a live map of Epics → Features → Tasks → Subtasks with status and owner on every node, kept up to date by the agents that do the work, with a reporting protocol that makes logging mandatory. When workmap is installed, workdocs links its page from the navigation and the Overview; when it is not, the Overview shows one small card pointing to it (easy to remove). Workmap is a separate, paid skill; workdocs never copies or recreates it. 30-second demo: https://youtu.be/b1yCp2lN2aw

## Install

Copy this folder to your agent's skills directory (Claude Code: `~/.claude/skills/workdocs/` or `<project>/.claude/skills/workdocs/`). Then, in a project: say **"workdocs"** (or `/workdocs`), or ask for the documentation to be written or refreshed.

## Requirements

A shell and a file editor for the agent; nothing for the pages (no runtime, framework or network). Optional: a diagram skill for the architecture diagram, `playwright-cli` for browser QA, a Remotion skill for the optional video.

## Files

```
workdocs/
├── SKILL.md              instructions the agent loads (rules, run, writing pages, workmap rule)
├── LICENSE.txt           MIT
├── assets/               page.html (template), workdocs.css, workdocs.js, snippets.html (flow, step player, cards, video)
└── references/           pages.md (content per page), static.md (static rules, migration), dependencies.md, qa.md
```

## Licence and support

MIT. Files the skill writes into your project are yours. Questions and bug reports: nnquangit@gmail.com (Quang Ngo).
