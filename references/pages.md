# Page standard

Each page: one `<h1>`, the required sections below in this order (section ids in brackets, used in the workdocs markers), and a footer line "Written from <commit or date>; sources: <files>". Optional sections go after the required ones. All text in English; all content embedded statically (see static.md).

General mistakes to avoid on every page:
- Copying README paragraphs wholesale; summarise instead and name the README section.
- Numbers (versions, ports, limits, timeouts) typed from memory. Read them from manifest/config/code; if env-driven, give the variable name and its default.
- Marketing language with no evidence.
- Planned or mocked features written in the present tense as if they ship.
- Placeholder text (`TODO`, "Lorem", "coming soon") in a finished page.

---

## index.html — Overview

Required:
- **What it is** [`what`]: 2–4 sentences: the problem, the user, what the project does. Source: README intro, manifest description.
- **Status** [`status`]: maturity; what is real vs mocked/stubbed; known limits and open blockers. Source: README, flags, stub classes, review notes.
- **Architecture** [`arch`]: main components and how they connect (diagram plus a short list). Source: layout, entry points, imports.
- **Pages** [`pages`]: cards linking the other five pages, plus the Work map card in the state that matches reality (installed → link card; absent → pointer card; both in `assets/snippets.html`).
- **Quick start** [`run`]: the shortest install + run commands and a link to Setup for everything else.

## setup.html — Setup

Required:
- **Prerequisites** [`prereq`]: runtimes, package manager and tools, with versions only as stated in the manifest, lockfile, engines field, toolchain files or README. If no version is pinned, say "not pinned" rather than inventing one. External services or accounts, and whether they are needed for the default mode.
- **Install** [`install`]: exact commands from the README/manifest, in order.
- **Configuration** [`config`]: table of environment variable **names**, purpose, default (from code), and when required. Never values from any `.env`. Say whether a config file is needed at all.
- **Run** [`run`]: dev and production commands from manifest scripts; the URL/port the code or framework actually uses (cite where it comes from).
- **Test** [`test`]: each test/check script and what it needs (e.g. a running server).
- **Verify** [`verify`]: how a reader confirms the install worked: a request, a page, an expected output line.
- **Troubleshooting** [`trouble`]: real failure modes from code, error messages, review notes or tests (port in use, missing variable, wrong default URL), each with the fix.

Avoid: commands not present in a script or README; versions or ports not found in the project.

## how-it-works.html — How it works

Required:
- **Big picture** [`flow`]: the main path as the animated flow from `assets/snippets.html` (`section.wd-flow`: real components as boxes, real calls as wires, packets moving along them) plus one paragraph; a static inline SVG when there is nothing that flows.
- **Step by step** [`steps`]: numbered steps of one representative request/run as the step player from `assets/snippets.html` (`ol.wd-steps` with `data-player`, `data-lanes`, `data-from` / `data-to`), each step naming `path/file.ext:function`. The list is readable without JS; the self-running diagram is the enhancement (no controls).
- **Key components** [`components`]: table: component, responsibility, file.
- **Failure paths** [`errors`]: what happens on the main errors, from the actual error handling.
- **Real vs simulated** [`real-vs-mock`]: which parts have mock and real implementations, which runs by default.

## security.html — Security

Required:
- **Assets & trust boundaries** [`assets`]: what must be protected and where untrusted input enters.
- **Threats and controls** [`threats`]: table: threat, control, file/line, status (implemented / partial / simulated / none).
- **Secrets handling** [`secrets`]: how secrets are supplied (variable names), where they must never appear.
- **Known gaps** [`gaps`]: honest list of unfixed issues, including anything safe only because it is mocked.
- **Reporting** [`report`]: how to report a vulnerability, or "not stated".

Avoid: claiming a control without pointing at code; generic lists not tied to the project.

## api.html — API

Required:
- **Interface type** [`kind`]: HTTP, RPC, CLI, library, events, or "no public API" plus the real public surface.
- **Endpoints / commands** [`endpoints`]: table from the route/CLI definitions: method + path, purpose, auth, source file.
- **Request & response** [`shapes`]: body/parameters and an example per main endpoint (mark hand-written examples as such).
- **Errors** [`errors`]: status codes and error shapes the code actually returns.
- **Try it** [`try`]: one `curl` or CLI example against a local run, placeholders for secrets.

## demo.html — Demo script

The page is a complete script a presenter can follow without asking anyone. Required:
- **Goal & audience** [`goal`]: what the demo proves, to whom, target length, and the mode it runs in (mock / real).
- **Prerequisites** [`prereq`]: machine, tools, accounts (none if mock), browser size, what must not be on screen (keys, private tabs).
- **Setup commands** [`setup`]: exact commands to reach the start state, plus how to confirm it is ready.
- **Script** [`script`]: numbered steps as a step player (`ol.wd-steps` with `data-player`; lanes such as presenter, screen, terminal); for each: the user action (exact UI label or command), what to say, and the expected visible result. Every step must be possible with current code. A local video (optional, see SKILL.md) goes above the list, never instead of it.
- **Genuine vs simulated** [`claims`]: every claim the narration makes, marked genuine or simulated, with evidence (file, test, page section). Simulated parts are said aloud as simulated.
- **Fallbacks** [`fallback`]: per failure (timeout, server not starting, step fails, wrong port), what to do live: restart, alternate preset, pre-recorded clip, skip.
- **Cleanup** [`cleanup`]: stop processes by the PID you started, delete downloaded files, close tabs, reset state.

Avoid: features that are not built; narration implying real infrastructure when the run is mocked; steps needing the presenter's private accounts.
