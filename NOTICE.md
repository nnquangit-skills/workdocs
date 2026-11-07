# Notices

## Third-party components

**None are bundled in the skill.** `SKILL.md`, `assets/` and `references/` are original work: plain HTML, CSS and JavaScript with no libraries, and no code is copied from other projects.

## Fonts

No web font is bundled or loaded. The stylesheet names **Be Vietnam Pro** first in its font stack (SIL Open Font License 1.1, copyright © 2021 The Be Vietnam Pro Project Authors); the browser uses it only if that font is already installed on the reader's machine, otherwise the system font. Nothing is downloaded.

## Demo video (not part of the skill)

`demo/` holds the source of the demo video, which is built with **Remotion** (remotion.dev; free licence for individuals and organisations of up to three people) and renders text with **Be Vietnam Pro** and **JetBrains Mono** (both SIL Open Font License 1.1, loaded through `@remotion/google-fonts` at render time). The narration is generated with **Kokoro-82M** (hexgrad, Apache License 2.0) running locally. The screen recording shows this skill's own pages.

## Trademarks

**Claude** and **Claude Code** are trademarks of Anthropic, PBC. This skill is an independent project and is not affiliated with or endorsed by Anthropic. It follows the open Agent Skills format (agentskills.io) and works with any compatible agent. **workmap** is a separate product by the same author; workdocs links to it and never bundles it.

## Privacy

The skill collects no data and makes no network requests. The agent that runs it reads the project it is pointed at and writes only into that project's `docs/` folder, backing up anything it replaces.
