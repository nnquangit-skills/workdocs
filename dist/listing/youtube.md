# YouTube video (channel @hackathonchallenges)

Published 2026-11-07, public, English subtitles: https://youtu.be/EuZ_iwpUpuc

## Title (≤100 characters)

workdocs — six honest documentation pages your AI agent writes from the code (Claude Code skill)

## Description

Documentation written from the code, not from memory.

Most project docs are missing, stale, or written from memory. workdocs puts the job on the agent: say "workdocs" in a project and it reads the manifest, the entry points, the handlers, the config and the tests, then writes six pages in docs/ — Overview, Setup, How it works, Security, API and a Demo script. Each section names the files it came from. Mocked and planned parts are labelled as such.

The pages are plain static HTML. They open from a folder, fetch nothing, and stay readable with JavaScript off. On How it works, an animated flow shows the real calls between the real components, and a sequence diagram walks one request through its steps on its own.

Get workdocs (free): https://github.com/nnquangit-skills/workdocs

Pairs with workmap, the skill that tracks what the project is doing: a live map of Epics → Features → Tasks → Subtasks with status and owner on every node, kept up to date by the agents through a mandatory reporting protocol.
https://www.agensi.io/skills/workmap-project-work-map-for-ai-agents
workmap demo: https://youtu.be/b1yCp2lN2aw

Chapters
0:00 One command: /workdocs
0:19 The six pages in the browser
0:36 Free, no framework, pairs with workmap

Requirements: a shell and a file editor for the agent; nothing for the pages. MIT licence.

#ClaudeCode #AIAgents #AgentSkills #Documentation #workdocs #workmap

(Add the Agensi listing link under "Get workdocs" once the listing is approved.)

## Tags

workdocs, workmap, claude code, agent skills, ai agent, documentation, static html, technical writing, developer tools
