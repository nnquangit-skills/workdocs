#!/usr/bin/env python3
"""Writes the six workdocs pages about the workdocs skill itself into docs/ (run from the repo root).
Content was written from SKILL.md, assets/, references/, scripts/package.sh and CHANGELOG.md; update the text here
when those change, then run this script. docs/ is not part of the skill package."""
import pathlib
OUT = pathlib.Path("docs")
DATE = "2026-11-07"
NAV = [("index.html", "Overview"), ("setup.html", "Setup"), ("how-it-works.html", "How it works"),
       ("security.html", "Security"), ("api.html", "API"), ("demo.html", "Demo script")]

def page(file, title, lead, body, sources):
    body = "".join(body) if not isinstance(body, str) else body
    links = "\n".join(f'    <a class="wd-link" href="{h}"{" aria-current=\"page\"" if h == file else ""}>{l}</a>' for h, l in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} · workdocs</title>
  <meta name="generator" content="workdocs">
  <link rel="stylesheet" href="assets/workdocs.css">
  <script>try{{var t=localStorage.getItem("docs-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
</head>
<body>
<header class="wd-nav">
  <nav class="wd-bar" aria-label="Documentation">
    <a class="wd-name" href="index.html">workdocs docs</a>
{links}
  </nav>
</header>
<main>
  <header class="wd-hero">
    <div class="wd-eyebrow">workdocs</div>
    <h1>{title}</h1>
    <p class="wd-lead">{lead}</p>
  </header>

{body}
  <footer class="wd-foot">Written from the repository on {DATE}; sources: {sources}</footer>
</main>
<script src="assets/workdocs.js" defer></script>
</body>
</html>
'''
    (OUT / file).write_text(html, encoding="utf-8")
    print("wrote", OUT / file)

def sec(id_, title, inner, source, cls=""):
    src = f'\n    <p class="wd-source">Source: {source}</p>' if source else ""
    c = f' class="{cls}"' if cls else ""
    return f'''  <!-- workdocs:begin id={id_} -->
  <section id="{id_}"{c}>
    <h2>{title}</h2>
{inner}{src}
  </section>
  <!-- workdocs:end id={id_} -->

'''

C = lambda s: f"<code>{s}</code>"

# ---------------------------------------------------------------- Overview
arch = '''    <figure>
      <svg class="wd-diagram" viewBox="0 0 900 230" role="img" aria-label="The agent loads SKILL.md and its references, reads the project's files, copies the assets and writes six pages into docs/, which the reader opens in a browser.">
        <path class="edge" d="M190 60 H330"/><path class="edge" d="M190 130 H330"/>
        <path class="edge" d="M530 95 H610"/><path class="edge" d="M330 130 H270 V180 H330"/>
        <path class="edge" d="M740 117 V150"/>
        <rect class="box" x="30" y="30" width="160" height="56" rx="12"/><text x="110" y="52" text-anchor="middle">SKILL.md + references/</text><text class="muted" x="110" y="72" text-anchor="middle">rules, page standard, QA list</text>
        <rect class="box" x="30" y="100" width="160" height="56" rx="12"/><text x="110" y="122" text-anchor="middle">Your project</text><text class="muted" x="110" y="142" text-anchor="middle">README, manifest, src, tests</text>
        <rect class="box" x="330" y="40" width="200" height="110" rx="12"/><text x="430" y="70" text-anchor="middle">Agent</text><text class="muted" x="430" y="92" text-anchor="middle">survey · draft · back up · write</text><text class="muted" x="430" y="112" text-anchor="middle">QA · report</text>
        <rect class="box" x="330" y="160" width="200" height="50" rx="12"/><text x="430" y="181" text-anchor="middle">assets/</text><text class="muted" x="430" y="199" text-anchor="middle">page.html, css, js, snippets</text>
        <rect class="box" x="610" y="73" width="260" height="44" rx="12"/><text x="740" y="100" text-anchor="middle">docs/ · six static pages</text>
        <rect class="box" x="610" y="150" width="260" height="44" rx="12"/><text x="740" y="177" text-anchor="middle">Reader's browser (file:// or any server)</text>
      </svg>
      <figcaption>Everything the reader needs ends up inside <code>docs/</code>; the skill itself stays in the agent's skills folder.</figcaption>
    </figure>
    <ul>
      <li><strong>The skill</strong>: <code>SKILL.md</code> (hard rules, the run, the work-map rule) and <code>references/</code> (what each page must contain, what "static" means, optional helpers, the QA checklist). The agent loads these when you say <code>workdocs</code>.</li>
      <li><strong>The assets</strong>: <code>assets/page.html</code> (page skeleton), <code>workdocs.css</code> (one look, light and dark), <code>workdocs.js</code> (theme toggle, copy buttons, the self-running animations) and <code>snippets.html</code> (the flow, the step player, the Work map card, the video block). Copied into <code>docs/assets/</code> once; never fetched.</li>
      <li><strong>The output</strong>: six HTML files in <code>docs/</code> with the content embedded, each section between <code>workdocs:begin</code> / <code>workdocs:end</code> markers and a line naming its sources.</li>
    </ul>'''
over = (
    sec("what", "What it is",
        '''    <p>workdocs is an Agent Skill, a folder with a <code>SKILL.md</code> that an agent such as Claude Code loads when you say <code>workdocs</code>. It makes the agent write six reader-facing pages about your project from the project's own files: Overview, Setup, How it works, Security, API and Demo script. Every claim on those pages comes from a file the agent read, each section names those files, and anything mocked, simulated or planned is labelled as such.</p>
    <p>The pages are plain static HTML in <code>docs/</code>. They open from a folder, fetch nothing, and stay readable with JavaScript off. You can keep them in the repository and hand them to anyone.</p>''',
        f'{C("SKILL.md")} (frontmatter, "Hard rules"), {C("references/static.md")}'),
    sec("status", "Status",
        '''    <div class="wd-table"><table>
      <thead><tr><th>Area</th><th>State</th><th>Evidence</th></tr></thead>
      <tbody>
        <tr><td>Six pages with managed sections, backups and migration</td><td><span class="wd-tag real">real</span></td><td><code>SKILL.md</code> "Run" and "Writing pages", <code>references/static.md</code>, <code>assets/page.html</code></td></tr>
        <tr><td>Animated flow and step player, self-running, no controls</td><td><span class="wd-tag real">real</span></td><td><code>assets/workdocs.js</code> (<code>startFlows</code>, <code>startStepPlayers</code>), <code>assets/snippets.html</code></td></tr>
        <tr><td>Light / dark toggle shared with the workmap page</td><td><span class="wd-tag real">real</span></td><td><code>assets/workdocs.js</code> key <code>docs-theme</code>; one-line script in <code>assets/page.html</code></td></tr>
        <tr><td>Architecture diagrams through a diagram skill</td><td><span class="wd-tag partial">optional</span></td><td><code>references/dependencies.md</code>: archify or diagram-design when installed, otherwise inline SVG</td></tr>
        <tr><td>Video on How it works</td><td><span class="wd-tag partial">optional</span></td><td><code>SKILL.md</code> "Writing pages": only with a Remotion skill and on request</td></tr>
        <tr><td>Automated test suite for the skill</td><td><span class="wd-tag none">none</span></td><td>no test script in the repository; quality comes from the QA checklist the agent runs per project (<code>references/qa.md</code>)</td></tr>
      </tbody>
    </table></div>
    <p class="wd-note">The rules in <code>SKILL.md</code> are instructions to the agent, not code that enforces them. An agent that ignores them can still write a page. The checklist in <code>references/qa.md</code> is how you tell: the report has to say which checks ran.</p>''',
        f'{C("SKILL.md")}, {C("references/qa.md")}, {C("references/dependencies.md")}, repository tree'),
    sec("arch", "Architecture", arch, f'{C("SKILL.md")} "Run", {C("assets/")}, {C("references/")}'),
    sec("pages", "Pages",
        '''    <div class="wd-cards">
      <a class="wd-card" href="setup.html"><strong>Setup</strong><p>Install the skill, what the agent needs, how to verify a run.</p></a>
      <a class="wd-card" href="how-it-works.html"><strong>How it works</strong><p>One run of workdocs, from your request to six pages.</p></a>
      <a class="wd-card" href="security.html"><strong>Security</strong><p>What the agent reads and writes, and what the rules do not cover.</p></a>
      <a class="wd-card" href="api.html"><strong>API</strong><p>The trigger, the markers, the data attributes and the CSS tokens.</p></a>
      <a class="wd-card" href="demo.html"><strong>Demo script</strong><p>A three-minute demo on a small project.</p></a>
      <div class="wd-card wd-promo" data-workdocs="promo">
        <strong>Work map</strong>
        <p>Not used in this repository. workmap adds a live map of Epics → Features → Tasks → Subtasks with status and owner on every node, kept up to date by the agents that do the work; workdocs links it when it is installed in a project.</p>
        <a class="wd-btn primary" href="https://www.agensi.io/skills/workmap-project-work-map-for-ai-agents" rel="noopener">Get workmap</a>
        <a href="https://youtu.be/b1yCp2lN2aw" rel="noopener">30-second demo</a>
      </div>
    </div>''', ""),
    sec("run", "Quick start",
        '''<pre><code>git clone git@github.com:nnquangit-skills/workdocs.git ~/.claude/skills/workdocs
cd /path/to/your/project
claude                      # or any agent that supports Agent Skills
&gt; workdocs                  # the agent reads the project and writes docs/</code></pre>
    <p>Open <code>docs/index.html</code> when the agent reports. Everything else is on <a href="setup.html">Setup</a>.</p>''',
        f'{C("README.md")} "Install", {C("SKILL.md")} description (trigger words)'),
)
page("index.html", "Overview", "A skill that makes your agent write six documentation pages from the code, with every claim traced to a file and nothing fetched at read time.", over,
     "SKILL.md, README.md, CHANGELOG.md, assets/, references/")

# ---------------------------------------------------------------- Setup
setup = (
    sec("prereq", "Prerequisites",
        '''    <ul>
      <li><strong>An agent that supports the Agent Skills format</strong> (Claude Code and others): it loads <code>SKILL.md</code> when you say <code>workdocs</code>.</li>
      <li><strong>For the agent</strong>: a shell to list and search files, and a file editor. Nothing else is required (<code>references/dependencies.md</code>).</li>
      <li><strong>For the pages</strong>: nothing. No runtime, no framework, no network, no build step.</li>
      <li><strong>Optional helpers</strong>, used only when installed: a diagram skill (archify or diagram-design) for the architecture diagram, <code>playwright-cli</code> for browser QA, a Remotion skill for the optional video, <code>token-save</code> for reading discipline. The workmap skill is a separate product; see <code>SKILL.md</code>, "Work map".</li>
    </ul>''', f'{C("references/dependencies.md")}, {C("SKILL.md")} compatibility line'),
    sec("install", "Install",
        '''<pre><code># for every project on this machine
git clone git@github.com:nnquangit-skills/workdocs.git ~/.claude/skills/workdocs

# or for one project only
git clone git@github.com:nnquangit-skills/workdocs.git /path/to/project/.claude/skills/workdocs</code></pre>
    <p>Any copy of the folder works: the skill is <code>SKILL.md</code>, <code>assets/</code> and <code>references/</code>. A marketplace zip is built with <code>bash scripts/package.sh</code> (one top-level folder, <code>dist/</code>, <code>docs/</code>, <code>demo/</code> and local files left out).</p>''',
        f'{C("README.md")} "Install", {C("scripts/package.sh")}'),
    sec("config", "Configuration",
        '''    <p>There is no configuration file and no environment variable. Behaviour is set by what you say and by three conventions in the pages:</p>
    <div class="wd-table"><table>
      <thead><tr><th>Where</th><th>Effect</th><th>Default</th></tr></thead>
      <tbody>
        <tr><td>Your request</td><td>"workdocs" or "/workdocs" starts a run; "refresh the docs" regenerates only sections whose sources changed; "no promo" leaves the Work map card out</td><td>all six pages, Work map card shown when workmap is absent</td></tr>
        <tr><td><code>data-workdocs="keep"</code> on a section</td><td>The section is never regenerated</td><td>managed sections are regenerated when their sources change</td></tr>
        <tr><td><code>docs-theme</code> in the browser's localStorage</td><td>Light or dark for every page in <code>docs/</code>, shared with the workmap page</td><td>follows the system theme</td></tr>
      </tbody>
    </table></div>''', f'{C("SKILL.md")} "Writing pages" and "Work map", {C("assets/workdocs.js")}, {C("assets/page.html")}'),
    sec("run", "Run",
        '''    <p>In a project, say <code>workdocs</code>. The agent surveys the tree, reads README, manifest, entry points, handlers, auth, config, environment example and test scripts, inventories any existing pages, drafts the six pages with an evidence list, backs up what it will replace, writes the pages and the two asset files, runs the QA checklist and reports. There is no server to start: open <code>docs/index.html</code> in a browser, or serve <code>docs/</code> with any static server (for example <code>python3 -m http.server 4590 --bind 127.0.0.1 --directory docs</code>).</p>''',
        f'{C("SKILL.md")} "Run" steps 1-8, {C("references/qa.md")}'),
    sec("test", "Test",
        '''    <p>The skill ships no automated test. Each run ends with the checklist in <code>references/qa.md</code>: serve <code>docs/</code> alone, open every page with zero console errors and no request for <code>.md</code>, <code>.json</code>, README or another origin, check light and dark, 375 px with no horizontal scroll, identical navigation on all six pages, one <code>h1</code>, animations that run on their own and stop under reduced motion, then the static checks (links resolve, markers paired, no loader leftovers, no key-shaped strings). The report lists what ran and what is unverified.</p>''',
        f'{C("references/qa.md")}'),
    sec("verify", "Verify",
        '''    <ol class="wd-steps">
      <li><code>docs/</code> holds <code>index.html</code>, <code>setup.html</code>, <code>how-it-works.html</code>, <code>security.html</code>, <code>api.html</code>, <code>demo.html</code> and <code>assets/workdocs.css</code>, <code>assets/workdocs.js</code>.</li>
      <li>Open <code>docs/index.html</code> straight from the file system: the navigation lists the six pages and every section ends with a "Source:" line.</li>
      <li>The agent's report names created, replaced and untouched pages, the backup folder if any, the evidence gaps, the checks it ran, and the workmap status.</li>
    </ol>''', f'{C("SKILL.md")} "Run" step 8 and "Done means"'),
    sec("trouble", "Troubleshooting",
        '''    <div class="wd-table"><table>
      <thead><tr><th>Symptom</th><th>Cause</th><th>Fix</th></tr></thead>
      <tbody>
        <tr><td>The agent writes a generic README instead of six pages</td><td>The skill was not loaded</td><td>Say <code>workdocs</code> or <code>/workdocs</code> explicitly; check the folder sits in the agent's skills directory</td></tr>
        <tr><td>A page shows a loading placeholder or an empty section</td><td>A legacy page that fetched markdown at open time</td><td>Run workdocs again: the migration in <code>references/static.md</code> backs the page up and embeds the content</td></tr>
        <tr><td>The flow does not move, the step player shows every step lit</td><td>The reader's system has reduced motion on, or the tab is hidden</td><td>Expected: both stop under <code>prefers-reduced-motion</code> and while the tab is hidden</td></tr>
        <tr><td>The agent reports an assets mismatch</td><td><code>docs/assets/workdocs.css</code> or <code>.js</code> differs from the skill's copy</td><td>Your files are kept; replace them with the skill's copies if you want the current look</td></tr>
        <tr><td>The Work map card shows the wrong state</td><td>workmap's <code>SKILL.md</code> is not readable, or <code>docs/workmap.html</code> is missing</td><td>See <code>SKILL.md</code>, "Work map": a link card only when both exist; otherwise the pointer card</td></tr>
      </tbody>
    </table></div>''', f'{C("SKILL.md")}, {C("references/static.md")}, {C("assets/workdocs.js")}'),
)
page("setup.html", "Setup", "Clone one folder into your agent's skills directory; the pages it writes need nothing at all.", setup,
     "README.md, SKILL.md, references/dependencies.md, references/qa.md, scripts/package.sh")

# ---------------------------------------------------------------- How it works
flow = '''    <p>You say one word in the chat. The agent loads the skill, reads the project, writes the pages and checks them. The reader opens a folder.</p>
    <svg class="wd-diagram" viewBox="0 0 900 230" role="img" aria-label="Your request goes to the agent; the agent reads SKILL.md and the project files, writes six pages into docs/, and the reader opens them in a browser.">
      <path id="w1" class="wire" d="M200 68 H290 V113 H350"/>
      <path id="w2" class="wire" d="M200 158 H290 V113"/>
      <path id="w3" class="wire" d="M450 54 V85"/>
      <path id="w4" class="wire" d="M550 113 H700"/>
      <path id="w5" class="wire" d="M450 160 V141"/>
      <rect class="box" x="350" y="10" width="200" height="44" rx="12"/><text x="450" y="37" text-anchor="middle">you: "workdocs"</text>
      <rect class="box" x="30" y="40" width="170" height="56" rx="12"/><text x="115" y="62" text-anchor="middle">SKILL.md</text><text class="muted" x="115" y="82" text-anchor="middle">rules · run · references</text>
      <rect class="box" x="30" y="130" width="170" height="56" rx="12"/><text x="115" y="152" text-anchor="middle">project files</text><text class="muted" x="115" y="172" text-anchor="middle">README, manifest, src, tests</text>
      <rect class="box" x="350" y="85" width="200" height="56" rx="12"/><text x="450" y="107" text-anchor="middle">Agent</text><text class="muted" x="450" y="127" text-anchor="middle">survey · draft · write · QA</text>
      <rect class="box" x="350" y="160" width="200" height="44" rx="12"/><text x="450" y="187" text-anchor="middle">assets/ (template, css, js)</text>
      <rect class="box" x="700" y="85" width="170" height="56" rx="12"/><text x="785" y="107" text-anchor="middle">docs/</text><text class="muted" x="785" y="127" text-anchor="middle">six pages, file:// ok</text>
      <g aria-hidden="true">
        <circle class="packet" r="5"><animateMotion dur="1.6s" repeatCount="indefinite"><mpath href="#w3"/></animateMotion></circle>
        <circle class="packet" r="5"><animateMotion dur="1.6s" begin=".4s" repeatCount="indefinite"><mpath href="#w1"/></animateMotion></circle>
        <circle class="packet" r="5"><animateMotion dur="1.6s" begin=".9s" repeatCount="indefinite"><mpath href="#w2"/></animateMotion></circle>
        <circle class="packet" r="5"><animateMotion dur="1.6s" begin="1.1s" repeatCount="indefinite"><mpath href="#w4"/></animateMotion></circle>
      </g>
    </svg>'''
steps = '''    <p>One run of workdocs on a project, in the order <code>SKILL.md</code> prescribes. The diagram walks through the steps below on its own.</p>
    <ol class="wd-steps" data-player data-lanes="you=You|chat;agent=Agent|SKILL.md;src=Project files|README, src/, tests;docs=docs/|six pages;qa=Browser|QA">
      <li data-from="you" data-to="agent" data-label="workdocs"><b>Trigger</b> — you say <code>workdocs</code>; the agent loads <code>SKILL.md</code> and the references it names (<code>SKILL.md</code>, first paragraph).</li>
      <li data-from="agent" data-to="src" data-label="survey the tree"><b>Survey</b> — README, manifest, entry points, handlers, auth, config, environment example and test scripts, with targeted searches and ranged reads (Run step 1).</li>
      <li data-from="agent" data-to="docs" data-label="inventory pages"><b>Inventory</b> — each of the six files is missing, workdocs-managed (markers present) or foreign/legacy (Run step 2).</li>
      <li data-from="agent" data-to="agent" data-label="discover skills"><b>Discover helpers</b> — token-save, a diagram skill, playwright-cli, a Remotion skill; check whether workmap is installed under the commercial rule (Run step 3).</li>
      <li data-from="agent" data-to="agent" data-label="draft + evidence list"><b>Draft</b> — all six pages from <code>references/pages.md</code>, keeping a claim-to-source list; a page that does not apply says what is absent (Run step 4, Hard rule 4).</li>
      <li data-from="agent" data-to="docs" data-label="back up, write pages + assets"><b>Write</b> — existing pages are backed up to <code>docs/.workdocs-backup/</code>, then the pages are written; <code>workdocs.css</code> and <code>workdocs.js</code> are copied only when absent (Run step 5, <code>references/static.md</code>).</li>
      <li data-from="agent" data-to="docs" data-label="flow, step player, diagram"><b>Diagrams and motion</b> — the architecture diagram on Overview, the animated flow and the step player on How it works, the step player on Demo script, all from real call sites and the blocks in <code>assets/snippets.html</code> (Run step 6).</li>
      <li data-from="agent" data-to="qa" data-label="serve docs/ alone, check"><b>QA</b> — <code>docs/</code> served alone: console, requests, light and dark, 375 px, navigation, markers, links; browser checks marked unverified when no browser is available (Run step 7, <code>references/qa.md</code>).</li>
      <li data-from="agent" data-to="you" data-kind="ret" data-label="report"><b>Report</b> — pages created, replaced, untouched; backups; evidence gaps; checks run; skills loaded; workmap status and, when it is absent, the pointer line (Run step 8).</li>
    </ol>'''
how = (
    sec("flow", "Big picture", flow, f'{C("SKILL.md")} "Run", {C("assets/")}', cls="wd-flow playing"),
    sec("steps", "Step by step", steps, f'{C("SKILL.md")} "Run" steps 1-8 and "Hard rules", {C("references/static.md")}, {C("references/qa.md")}'),
    sec("components", "Key components",
        '''    <div class="wd-table"><table>
      <thead><tr><th>Component</th><th>Responsibility</th><th>File</th></tr></thead>
      <tbody>
        <tr><td>Skill instructions</td><td>Hard rules, the eight-step run, how to write pages, the work-map rule, what "done" means</td><td><code>SKILL.md</code></td></tr>
        <tr><td>Page standard</td><td>Required sections and section ids per page, mistakes to avoid</td><td><code>references/pages.md</code></td></tr>
        <tr><td>Static rules and migration</td><td>What a page may load, what is forbidden, how legacy pages are backed up and migrated</td><td><code>references/static.md</code></td></tr>
        <tr><td>Optional helpers</td><td>Which skills improve a step and the fallback when missing</td><td><code>references/dependencies.md</code></td></tr>
        <tr><td>QA checklist</td><td>Per-page, static-delivery, static and honesty checks</td><td><code>references/qa.md</code></td></tr>
        <tr><td>Page skeleton</td><td>Nav, hero, one managed section, footer, theme script</td><td><code>assets/page.html</code></td></tr>
        <tr><td>Look</td><td>Tokens (<code>--wd-*</code>), light and dark, cards, tables, tags, diagram and stage styles</td><td><code>assets/workdocs.css</code></td></tr>
        <tr><td>Presentation script</td><td><code>addToggle</code>, <code>addCopyButtons</code>, <code>startFlows</code>, <code>startStepPlayers</code>; never inserts content</td><td><code>assets/workdocs.js</code></td></tr>
        <tr><td>Snippets</td><td>Flow, step player, Work map cards, nav entry, video block to copy and adapt</td><td><code>assets/snippets.html</code></td></tr>
        <tr><td>Packaging</td><td>Builds <code>dist/workdocs-&lt;version&gt;.zip</code> with one top-level folder</td><td><code>scripts/package.sh</code></td></tr>
      </tbody>
    </table></div>''', ""),
    sec("errors", "Failure paths",
        '''    <ul>
      <li><strong>No evidence for a page</strong> (no API, no auth): the page is still written and says what is absent and what exists instead; nothing is invented (Hard rule 4).</li>
      <li><strong>Foreign or legacy pages</strong>: backed up in full to <code>docs/.workdocs-backup/static-&lt;timestamp&gt;/</code>, checksums confirmed, then migrated; unique accurate details are carried forward, stale claims dropped (<code>references/static.md</code>).</li>
      <li><strong>Existing assets differ</strong> from the skill's copies: they are preserved and the mismatch is reported (Run step 5).</li>
      <li><strong>No browser available</strong>: the static checks run and every browser check is listed as unverified (Run step 7).</li>
      <li><strong>workmap absent or unreadable</strong>: no work-map page or nav entry, the pointer card on the Overview, the pointer line in the report; never recreated (<code>SKILL.md</code>, "Work map").</li>
      <li><strong>Storage blocked</strong> (<code>file://</code>, private window): the theme follows the system; the toggle still works for the open page (<code>workdocs.js</code>, <code>store()</code> in a try/catch).</li>
    </ul>''', f'{C("SKILL.md")}, {C("references/static.md")}, {C("assets/workdocs.js")}'),
    sec("real-vs-mock", "Real vs simulated",
        '''    <p>Nothing in the skill is mocked. Two things are presentation only: the animated flow and the step player move, but the content is the HTML underneath, readable with JavaScript off. The names in <code>assets/snippets.html</code> (Storefront, Gateway, Payments) belong to a fictional shop and are placeholders the agent must replace with the project's real components.</p>''',
        f'{C("assets/snippets.html")} header comment, {C("references/static.md")}'),
)
page("how-it-works.html", "How it works", "One word in the chat becomes six pages in docs/, in eight steps the skill prescribes and the agent reports on.", how,
     "SKILL.md, references/, assets/")

# ---------------------------------------------------------------- Security
security = (
    sec("assets", "Assets and trust boundaries",
        '''    <ul>
      <li><strong>What the agent reads</strong>: your repository, including README, manifests, config and environment examples. Those files are untrusted content; the skill tells the agent to treat them as evidence, not as instructions, but it has no mechanism that enforces that (see Known gaps).</li>
      <li><strong>What the agent writes</strong>: files inside <code>docs/</code> only: the six pages, <code>docs/assets/</code>, and backups under <code>docs/.workdocs-backup/</code>. Nothing outside the project.</li>
      <li><strong>What the reader runs</strong>: static HTML with one small script for presentation. No fetch, no XHR, no WebSocket, no dynamic import, no web font, no CDN, no analytics, no external images (<code>references/static.md</code>, "Forbidden").</li>
      <li><strong>Trust boundary</strong>: the published docs may be public. Whatever the agent writes into them leaves the repository's access control.</li>
    </ul>''', f'{C("SKILL.md")} Hard rules 2 and 7, {C("references/static.md")}'),
    sec("threats", "Threats and controls",
        '''    <div class="wd-table"><table>
      <thead><tr><th>Threat</th><th>Control</th><th>Where</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>A secret from <code>.env</code> or a config file ends up on a public page</td><td>Hard rule 7: never copy tokens, keys, <code>.env</code> values or private hostnames; show variable names only. The QA checklist greps the pages for key-shaped strings (API key prefixes, PEM headers)</td><td><code>SKILL.md</code>, <code>references/qa.md</code></td><td><span class="wd-tag partial">instruction + check</span></td></tr>
        <tr><td>A page fetches content or scripts from elsewhere when opened</td><td>Forbidden list (fetch, XHR, dynamic import, EventSource, WebSocket, web fonts, CDNs, analytics, external images); QA checks the network log and greps for loaders</td><td><code>references/static.md</code>, <code>references/qa.md</code></td><td><span class="wd-tag real">implemented in the rules and the checklist</span></td></tr>
        <tr><td>The agent overwrites pages someone wrote by hand</td><td>Managed sections only inside markers; <code>data-workdocs="keep"</code>; full backup with checksum before any replacement; never delete a file that cannot be backed up</td><td><code>SKILL.md</code> "Writing pages", <code>references/static.md</code></td><td><span class="wd-tag real">implemented in the rules</span></td></tr>
        <tr><td>Invented facts on a page (ports, versions, endpoints)</td><td>Hard rule 1: evidence first; each section names its sources; the honesty section of the checklist</td><td><code>SKILL.md</code>, <code>references/qa.md</code></td><td><span class="wd-tag partial">instruction + check</span></td></tr>
        <tr><td>Script injection through page content</td><td>The pages are written by the agent at authoring time; no runtime user input is rendered. <code>workdocs.js</code> builds its SVG with <code>createElementNS</code> and <code>textContent</code>, never <code>innerHTML</code></td><td><code>assets/workdocs.js</code></td><td><span class="wd-tag real">implemented</span></td></tr>
        <tr><td>Instructions hidden in project files steer the agent</td><td>None in this skill</td><td></td><td><span class="wd-tag none">none</span></td></tr>
      </tbody>
    </table></div>''', ""),
    sec("secrets", "Secrets handling",
        '''    <p>The skill needs no secret and stores none. It tells the agent to show environment variable <em>names</em>, their purpose and defaults from code, and never values from any <code>.env</code> file. If you keep secrets in files the agent reads, review <code>docs/</code> before publishing; the checklist's grep for key-shaped strings is a net, not a guarantee.</p>''',
        f'{C("SKILL.md")} Hard rule 7, {C("references/pages.md")} "Configuration", {C("references/qa.md")}'),
    sec("gaps", "Known gaps",
        '''    <ul>
      <li>Every control above is an instruction to the agent or a check it runs on itself. Nothing in the skill can stop a careless agent from writing a wrong or sensitive line.</li>
      <li>No defence against instructions planted in the project's own files (a README that tells the agent to do something). The skill reads them as evidence and does not say what to do with embedded instructions.</li>
      <li>The pages are static files: anyone who can read the repository or the folder reads the docs. Access control is the repository's.</li>
      <li>Backups accumulate under <code>docs/.workdocs-backup/</code> and are never pruned by the skill.</li>
    </ul>''', f'{C("SKILL.md")}, {C("references/static.md")}'),
    sec("report", "Reporting",
        '''    <p>Report a security concern to <strong>nnquangit@gmail.com</strong> (Quang Ngo). There is no bug bounty.</p>''',
        f'{C("README.md")} "Licence and support", {C("SKILL.md")} metadata'),
)
page("security.html", "Security", "The agent reads your repository and writes into docs/ only; the pages load nothing. What the rules cover, and what they cannot enforce.", security,
     "SKILL.md, references/static.md, references/qa.md, assets/workdocs.js")

# ---------------------------------------------------------------- API
api = (
    sec("kind", "Interface type",
        '''    <p>workdocs has no HTTP API, no library and no command-line tool. Its public surface is a <strong>trigger</strong> (what you say to the agent) and a set of <strong>conventions in the pages it writes</strong> (markers, data attributes, CSS classes and tokens, one localStorage key) that you can rely on when you edit the pages or style them.</p>''',
        f'{C("SKILL.md")} description and "Writing pages", {C("assets/")}'),
    sec("endpoints", "Triggers and conventions",
        '''    <div class="wd-table"><table>
      <thead><tr><th>Element</th><th>Purpose</th><th>Values</th><th>Source</th></tr></thead>
      <tbody>
        <tr><td><code>workdocs</code>, <code>/workdocs</code>, "write / refresh the documentation"</td><td>Starts a run</td><td>natural language in the chat</td><td><code>SKILL.md</code> description</td></tr>
        <tr><td><code>&lt;!-- workdocs:begin id=x --&gt;</code> … <code>&lt;!-- workdocs:end id=x --&gt;</code></td><td>Marks a managed section; only these are regenerated</td><td>section ids from <code>references/pages.md</code> (<code>what</code>, <code>status</code>, <code>arch</code>, <code>pages</code>, <code>run</code>, <code>prereq</code>, …)</td><td><code>SKILL.md</code> "Writing pages"</td></tr>
        <tr><td><code>data-workdocs="keep"</code></td><td>A section the agent never touches</td><td>on any <code>&lt;section&gt;</code></td><td><code>SKILL.md</code> "Writing pages"</td></tr>
        <tr><td><code>data-workdocs="promo"</code></td><td>The Work map pointer card, easy to find and remove</td><td>on the card in the Pages section</td><td><code>SKILL.md</code> "Work map", <code>assets/snippets.html</code></td></tr>
        <tr><td><code>section.wd-flow.playing</code> + <code>svg.wd-diagram</code> with <code>.wire</code> / <code>.packet</code></td><td>Animated flow; packets follow wires with <code>animateMotion</code></td><td>wires have ids, packets reference them with <code>mpath</code></td><td><code>assets/snippets.html</code>, <code>assets/workdocs.js:startFlows</code></td></tr>
        <tr><td><code>ol.wd-steps[data-player]</code></td><td>Step player; the diagram is drawn above the list</td><td><code>data-lanes="id=Label|subtitle;…"</code>, per item <code>data-from</code>, <code>data-to</code>, <code>data-label</code>, <code>data-kind="ret"</code></td><td><code>assets/snippets.html</code>, <code>assets/workdocs.js:startStepPlayers</code></td></tr>
        <tr><td><code>.wd-tag</code> with <code>real</code>, <code>mock</code>, <code>partial</code>, <code>none</code></td><td>Status tags in tables</td><td>class names</td><td><code>assets/workdocs.css</code></td></tr>
        <tr><td><code>.wd-note</code>, <code>.wd-source</code>, <code>.wd-cards</code> / <code>.wd-card</code>, <code>.wd-table</code>, <code>.wd-diagram</code></td><td>Note box, source line, card grid, scrolling table, diagram frame</td><td>class names</td><td><code>assets/workdocs.css</code></td></tr>
        <tr><td><code>--wd-bg</code>, <code>--wd-panel</code>, <code>--wd-fg</code>, <code>--wd-accent</code>, …</td><td>Theme tokens; redefine them to re-brand</td><td>CSS custom properties on <code>:root</code>, dark values under <code>prefers-color-scheme</code> and <code>html[data-theme="dark"]</code></td><td><code>assets/workdocs.css</code></td></tr>
        <tr><td><code>docs-theme</code></td><td>Stored theme choice, shared with the workmap page</td><td><code>"light"</code> or <code>"dark"</code> in localStorage</td><td><code>assets/workdocs.js</code>, <code>assets/page.html</code></td></tr>
      </tbody>
    </table></div>''', ""),
    sec("shapes", "Shapes",
        '''    <h3>A managed section</h3>
<pre><code>&lt;!-- workdocs:begin id=run --&gt;
&lt;section id="run"&gt;
  &lt;h2&gt;Quick start&lt;/h2&gt;
  &lt;pre&gt;&lt;code&gt;npm install
npm run dev&lt;/code&gt;&lt;/pre&gt;
  &lt;p class="wd-source"&gt;Source: &lt;code&gt;package.json&lt;/code&gt; scripts&lt;/p&gt;
&lt;/section&gt;
&lt;!-- workdocs:end id=run --&gt;</code></pre>
    <h3>A step player</h3>
<pre><code>&lt;ol class="wd-steps" data-player data-lanes="client=Storefront|browser;api=API|src/server.ts;db=PostgreSQL"&gt;
  &lt;li data-from="client" data-to="api" data-label="POST /checkout"&gt;&lt;b&gt;Request&lt;/b&gt; — … (&lt;code&gt;src/routes/checkout.ts:post&lt;/code&gt;)&lt;/li&gt;
  &lt;li data-from="api" data-to="db" data-label="reserve stock"&gt;&lt;b&gt;Reserve stock&lt;/b&gt; — …&lt;/li&gt;
  &lt;li data-from="api" data-to="client" data-kind="ret" data-label="201"&gt;&lt;b&gt;Response&lt;/b&gt; — …&lt;/li&gt;
&lt;/ol&gt;</code></pre>
    <p class="wd-source">Both shapes are taken from <code>assets/page.html</code> and <code>assets/snippets.html</code>; the names are the snippet's fictional shop.</p>''', ""),
    sec("errors", "Errors",
        '''    <p>There is no runtime, so there are no runtime errors. At authoring time the failure modes are reported, not thrown: a claim with no evidence becomes "not stated"; a check that could not run is listed as unverified; a mismatch in <code>docs/assets/</code> is reported and the existing files are kept; a page that does not apply says what is absent.</p>''',
        f'{C("SKILL.md")} Hard rule 4 and "Run" steps 5, 7, 8'),
    sec("try", "Try it",
        '''<pre><code>git clone git@github.com:nnquangit-skills/workdocs.git ~/.claude/skills/workdocs
cd /path/to/a/small/project
claude
&gt; workdocs
open docs/index.html</code></pre>''', f'{C("README.md")} "Install"'),
)
page("api.html", "API", "No endpoints and no CLI: a trigger word, and the markers, attributes, classes and tokens the written pages follow.", api,
     "SKILL.md, assets/page.html, assets/snippets.html, assets/workdocs.css, assets/workdocs.js")

# ---------------------------------------------------------------- Demo script
demo = (
    sec("goal", "Goal and audience",
        '''    <p>Show, in about three minutes, that one word in the chat gives a project six documentation pages whose every claim points at a file, and that the pages are plain files anyone can open. Audience: developers who run coding agents and leads who are tired of stale docs. Everything in the demo runs for real on a local project.</p>''',
        f'{C("SKILL.md")} intro, {C("README.md")}'),
    sec("prereq", "Prerequisites",
        '''    <ul>
      <li>Claude Code (or another agent that supports Agent Skills) with workdocs installed in <code>~/.claude/skills/workdocs</code>.</li>
      <li>A small project with a README, a manifest and a few source files; a copy you do not mind writing into. Not a client repository.</li>
      <li>A terminal and a browser side by side, about 1400 px wide; no private tabs, no keys on screen.</li>
      <li>No accounts and no network needed beyond the agent itself.</li>
    </ul>''', f'{C("README.md")} "Install", {C("SKILL.md")} compatibility line'),
    sec("setup", "Setup commands",
        '''<pre><code>git clone git@github.com:nnquangit-skills/workdocs.git ~/.claude/skills/workdocs   # once
cp -R /path/to/small-project /tmp/docs-demo &amp;&amp; cd /tmp/docs-demo
rm -rf docs &amp;&amp; ls                       # start without a docs folder
claude</code></pre>
    <p>Ready when the agent prompt is up and <code>ls</code> shows no <code>docs/</code>.</p>''',
        f'{C("README.md")} "Install"'),
    sec("script", "Script",
        '''    <p>Lanes: what the presenter says, what is typed in the chat or terminal, what the audience sees in the browser. The diagram walks through the steps below on its own.</p>
    <ol class="wd-steps" data-player data-lanes="say=Presenter|narration;chat=Chat / terminal|/tmp/docs-demo;web=Browser|docs/">
      <li data-from="say" data-to="chat" data-label="the problem"><b>Open</b> — say: "Docs go stale because someone has to write them after the work. Let's give that job to the agent, with one rule: no claim without a file." Show the project tree without <code>docs/</code>.</li>
      <li data-from="say" data-to="chat" data-label="workdocs"><b>Trigger</b> — type <code>workdocs</code>. Say: "One word. The skill tells the agent what to read and what each page must contain."</li>
      <li data-from="chat" data-to="chat" data-label="reads README, manifest, src, tests"><b>Watch it read</b> — point at the files the agent opens: README, the manifest, entry points, tests. Say: "Nothing from memory. If it did not read it, it cannot write it."</li>
      <li data-from="chat" data-to="web" data-label="writes docs/*.html"><b>Watch it write</b> — six files appear in <code>docs/</code> plus <code>assets/</code>. Expected: the agent's report lists created pages, evidence gaps, checks run and the workmap status.</li>
      <li data-from="chat" data-to="web" data-label="open docs/index.html"><b>Open the Overview</b> — open <code>docs/index.html</code> from the file system. Expected: navigation with six entries, the Status table with real / mock tags, every section ending in a "Source:" line.</li>
      <li data-from="web" data-to="web" data-label="How it works"><b>How it works</b> — click the nav entry. Expected: the flow is moving; scroll to Step by step and the sequence diagram walks the steps by itself. Say: "Nothing to click. It is documentation, you read it."</li>
      <li data-from="web" data-to="web" data-label="toggle theme, view source"><b>Plain files</b> — toggle dark with the ◐ button, then view the page source. Expected: the content is in the HTML, between <code>workdocs:begin</code> and <code>workdocs:end</code> markers; no fetch anywhere.</li>
      <li data-from="say" data-to="chat" data-label="edit by hand, run again"><b>Keep your edits</b> — add <code>data-workdocs="keep"</code> to one section, change its text, then say "refresh the docs". Expected: that section is untouched, the rest regenerated, the old files backed up under <code>docs/.workdocs-backup/</code>.</li>
      <li data-from="say" data-to="web" data-kind="ret" data-label="close"><b>Close</b> — say: "Six pages, every claim traced, nothing fetched, and it pairs with workmap when you want the map of what the project is doing." Show the Work map card on the Overview.</li>
    </ol>''', f'{C("SKILL.md")} "Run", "Writing pages", "Work map"; {C("assets/workdocs.js")}'),
    sec("claims", "Genuine vs simulated",
        '''    <div class="wd-table"><table>
      <thead><tr><th>Claim in the narration</th><th>Kind</th><th>Evidence</th></tr></thead>
      <tbody>
        <tr><td>"no claim without a file"</td><td><span class="wd-tag real">genuine</span></td><td>Hard rule 1 and the "Source:" line per section (<code>SKILL.md</code>, <code>assets/page.html</code>)</td></tr>
        <tr><td>"one word"</td><td><span class="wd-tag real">genuine</span></td><td>trigger words in the <code>SKILL.md</code> description</td></tr>
        <tr><td>"nothing to click"</td><td><span class="wd-tag real">genuine</span></td><td><code>workdocs.js</code> adds no controls; <code>SKILL.md</code> "Writing pages"</td></tr>
        <tr><td>"no fetch anywhere"</td><td><span class="wd-tag real">genuine</span></td><td><code>references/static.md</code> forbidden list; QA network check</td></tr>
        <tr><td>"that section is untouched"</td><td><span class="wd-tag real">genuine</span></td><td><code>data-workdocs="keep"</code> rule in <code>SKILL.md</code></td></tr>
        <tr><td>"it pairs with workmap"</td><td><span class="wd-tag partial">genuine, but a separate product</span></td><td><code>SKILL.md</code> "Work map": linked when installed, never bundled</td></tr>
      </tbody>
    </table></div>''', ""),
    sec("fallback", "Fallbacks",
        '''    <ul>
      <li><strong>The agent does not load the skill</strong>: type <code>/workdocs</code>, or check the folder is in <code>~/.claude/skills/</code>.</li>
      <li><strong>The run takes longer than the slot</strong>: keep a finished <code>docs/</code> from a rehearsal in a sibling folder and open that; say so.</li>
      <li><strong>The flow does not move</strong>: the machine has reduced motion on; the pages are meant to stop then. Show the step list instead.</li>
      <li><strong>No browser</strong>: show <code>docs/index.html</code> in the terminal with <code>sed -n '1,60p'</code>: markers and sources are visible in the source.</li>
      <li><strong>Running out of time</strong>: skip steps 7 and 8.</li>
    </ul>''', ""),
    sec("cleanup", "Cleanup",
        '''<pre><code>rm -rf /tmp/docs-demo</code></pre>
    <p>No process was started; close the browser tab that shows <code>file:///tmp/docs-demo/docs/</code>.</p>''',
        f'{C("SKILL.md")} "Run" step 5 (writes only into docs/)'),
)
page("demo.html", "Demo script", "A three-minute demo: one word, six pages, every claim traced, then a hand edit that survives the next run.", demo,
     "SKILL.md, README.md, assets/workdocs.js, references/static.md")
