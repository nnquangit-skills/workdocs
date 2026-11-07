# Notices

## Third-party components

**None are bundled in the skill.** `SKILL.md`, `assets/` and `references/` are original work: plain HTML, CSS and JavaScript with no libraries, and no code is copied from other projects.

## Fonts

No web font is bundled or loaded. The stylesheet names **Be Vietnam Pro** first in its font stack (SIL Open Font License 1.1, copyright © 2021 The Be Vietnam Pro Project Authors); the browser uses it only if that font is already installed on the reader's machine, otherwise the system font. Nothing is downloaded.

## Demo video (not part of the skill)

`demo/` holds the source of the demo video, which is built with **Remotion** (remotion.dev; free licence for individuals and organisations of up to three people) and renders text with **Be Vietnam Pro** and **JetBrains Mono** (both SIL Open Font License 1.1, loaded through `@remotion/google-fonts` at render time). The narration is generated with **Kokoro-82M** (hexgrad, Apache License 2.0) running locally. The screen recording shows this skill's own pages.

## Documentation site (not part of the skill)

`docs/` holds the six pages about this skill, written with the skill itself; the package built by `scripts/package.sh` leaves it out. The interactive diagrams in `docs/diagrams/` were generated with **archify** (https://github.com/tt-a1i/archify) from the JSON sources in `docs/diagrams/src/`; each generated file embeds archify's viewer, which is distributed under the MIT License:

> Copyright (c) 2026 tt-a1i (Archify). Copyright (c) 2025 Cocoon AI.
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Trademarks

**Claude** and **Claude Code** are trademarks of Anthropic, PBC. This skill is an independent project and is not affiliated with or endorsed by Anthropic. It follows the open Agent Skills format (agentskills.io) and works with any compatible agent. **workmap** is a separate product by the same author; workdocs links to it and never bundles it.

## Privacy

The skill collects no data and makes no network requests. The agent that runs it reads the project it is pointed at and writes only into that project's `docs/` folder, backing up anything it replaces.
