---
name: nature-figure
description: >-
  Create, revise, or audit scientific figures for manuscripts and publication-quality
  reports using Python or R; preserve the chosen backend. Also supports explicit
  requests for AI-generated manuscript schematics or graphical abstracts as drafts.
  Do not use for exploratory plots without a publication target, interactive
  dashboards, data cleaning, ordinary image editing, or literature questions.
---

<!-- Modified by NNU Sky, 2026-09-12: portable distribution and task-scoped instruction review; see repository THIRD_PARTY_NOTICES.md. -->


# Nature Figure Making — Router

This skill is split into two layers:

- A **static layer** under `static/` that holds versioned, reusable content fragments (the figure contract and default stance, plus a per-backend quick-start for Python and R).
- A **dynamic layer** (this file plus `manifest.yaml`) that detects the plotting backend and loads only the fragment needed for the current job. The large design, API, pattern, and QA material lives in on-demand references.

Load the relevant core and selected fragments on first use. Reuse already loaded guidance in the same task; reread only changed or missing sections.

## Routing protocol

Use the relevant route for the current request; reuse prior decisions and loaded material in the same task.

### 0. Check for graphical-abstract and AI-schematic routes

For every graphical-abstract planning, generation, revision, or audit task that
uses AI, read
[references/ai-graphical-abstract-workflow.md](references/ai-graphical-abstract-workflow.md)
first. It owns the message/audience brief, composition and palette workflow,
policy gate, human scientific review, disclosure boundary, and provenance
requirements. A Nature Careers article is practitioner advice, not submission
clearance; verify the current official policy for the exact target journal.

If the request is planning or auditing only, do not ask for Python or R unless
the user also asks to render or revise a data-driven figure.

If the user explicitly asks to generate a manuscript schematic, graphical abstract, mechanism diagram, concept illustration, or paper schematic with OpenRouter, GPT Image 2, an image-generation API, or similar wording, do **not** ask "Python or R?". This is a non-plotting AI-schematic route.

For this route:

1. Read [manifest.yaml](manifest.yaml) and the `always_load` files.
2. Read [references/ai-graphical-abstract-workflow.md](references/ai-graphical-abstract-workflow.md).
3. Use the image-generation tool available in the current environment and honor a provider explicitly selected by the user.
4. Only for an explicit OpenRouter request, read [references/openrouter-image-generation.md](references/openrouter-image-generation.md) and use [scripts/generate_openrouter_schematic.py](scripts/generate_openrouter_schematic.py). Do not substitute this paid external service for an available built-in tool.
5. Treat output as a draft schematic / graphical abstract, not as a quantitative data panel. Do not invent experimental values, author logos, institutional marks, or unsupported mechanisms. Keep internal usefulness separate from submission eligibility.

Only continue to the Python/R backend gate for plotting, charting, data visualization, or manuscript figure assembly tasks that are not explicit OpenRouter AI image-generation requests.

### 1. Load the manifest and the core layer

Read [manifest.yaml](manifest.yaml). It declares the `backend` axis, the allowed values, and the file paths each value maps to.

Also read every file listed under `always_load` (`static/core/contract.md` and `static/core/stance.md`). These hold the figure contract, the backend gate, the missing-runtime rule, the privacy rule, and the default operating stance that apply to every figure job.

### 2. Resolve the backend

Honor the current user's choice, then the existing project plotting code, then a saved preference from `scripts/nature_figure_backend.py get`. With no preference or existing workflow, choose an available suitable backend and state the assumption; ask only when the choice materially affects the requested deliverable.

A task-specific choice does not authorize changing a global default. Use `scripts/nature_figure_backend.py set python|r` only when the user asks to remember a preference. Preserve the chosen backend for drawing and exports; external PDF/image viewers may inspect the existing output without redrawing it. This step does not apply to AI image generation.

### 3. Load the matching backend fragment

After the backend is resolved, Read the mapped fragment (`static/fragments/backend/python.md` or `static/fragments/backend/r.md`). It carries the backend-only execution rule and the publication quick-start (rcParams/theme and export helper). Do **not** load the other backend's fragment.

### 4. Build the figure using the loaded material

Apply the loaded material in this order:

1. Figure contract (`static/core/contract.md`) — write the core conclusion, map the evidence chain, classify the archetype, set the journal/export contract, before any code.
2. Multi-panel evidence architecture — when planning, restructuring, or auditing a labelled multi-panel figure, load `references/multipanel-evidence-architecture.md`. Make the figure answer one Results-level scientific question; assign panels different inferential roles, not merely different metrics. When figure order must follow the manuscript argument, also load `../nature-shared/core/nature-results-discussion.md`.
3. Default stance (`static/core/stance.md`) — archetype-first composition, hero panel, restrained palette, statistics/integrity as part of the figure.
4. Backend fragment — the exclusive Python or R quick-start and execution rule.
5. Template adaptation — when reusing built-in original examples, licensed external material, or user-provided plotting code, load `references/asset-adaptation.md` before mapping data or changing the script.
6. Match QA to the stage and affected behavior. During iteration, batch related edits and inspect the affected panel or region; recheck data and uncertainty when they change. Expand validation for shared styles, layout engines, panel geometry, or an unresolved defect. Do not run the complete audit suite after each edit.
7. Before final delivery, load [references/qa-contract.md](references/qa-contract.md). Run source validation, final-PDF text and collision checks, and the render-time alignment check for comparable multi-panel layouts. Inspect each panel and the assembled figure at final physical size. Complete this final review once; after corrections, rerun only checks invalidated by the change, expanding to the whole figure when effects are global. Never present an earlier-render report as validation of a changed final PDF.

The QA reference owns the exact commands, physical tolerances, exemptions, and
result meanings. Preserve those scientific and rendering requirements; stage-aware
validation changes when checks run, not what counts as accurate or readable.
A preview must not be presented as a submission-ready figure before its final
checks. Diagnostic overlays remain internal QA artifacts, not replacement figures.

When the target is the flagship journal Nature, also load
`references/nature-article-requirements.md`. It separates initial-review files
from accepted-in-principle main and Extended Data production contracts and owns
the flagship legend limit.

When the target is Nature Machine Intelligence, instead load
`../nature-shared/journal-formats/nature-machine-intelligence.md`. Apply its
combined six-item main display budget, ten-item Extended Data maximum,
initial-versus-production boundary, 300-dpi/180-mm production checks and source-
data contract. NMI's current live pages do not assign a standalone per-legend
number, but its official 2018 brief guide set a historical advisory ceiling of
fewer than 300 English words per complete figure legend. Count the whole legend,
not each panel; aim for 150–250 words and keep it below 300 unless the live
submission system or editor gives a newer instruction. Do not import flagship
Nature's limit.

The chart serves the scientific logic; aesthetic polish is subordinate to making the core conclusion clear, defensible, and reviewable.

### 5. Reach for references only when needed

The files under `references/` are deep references, not defaults. Open them on demand per the `references.on_demand` table in the manifest — for example `references/figure-contract.md` to build the contract, `references/multipanel-evidence-architecture.md` to turn one Results-level question into complementary panel roles and a claim-escalating figure sequence, `references/asset-adaptation.md` to reuse a plotting template safely, `references/template-catalog.md` for validated Python CSV templates, `references/api.md` for the Python palette and numerical/layout safety helpers, `references/r-workflow.md` for R, `references/design-theory.md` for color/typography/export rationale, `references/common-patterns.md` and `references/chart-types.md` for layout/chart recipes, `references/nature-2026-observations.md` for real Nature page archetypes, `references/qa-contract.md` before final delivery, `references/nature-article-requirements.md` for exact flagship Nature stage and upload rules, `../nature-shared/journal-formats/nature-machine-intelligence.md` for exact NMI figure rules, `references/ai-graphical-abstract-workflow.md` for AI-assisted graphical-abstract planning, policy gating, human verification, and provenance, and `references/tutorials.md` / `references/demos.md` for worked examples.

Do not infer flagship Nature or NMI requirements from a Nature Communications
corpus or from the visual-style examples in this skill.

## Why this split

- The static layer is versioned and reviewable. The backend gate is now explicit in the manifest rather than buried in prose.
- The dynamic layer keeps each invocation cheap: only the selected backend's quick-start enters context, and the 2,600+ lines of reference depth load only when a step needs them.
- The router itself is short on purpose. Update fragments and references, not this file, when adding scope.
- This structure mirrors `nature-writing`, `nature-polishing`, `nature-reader`, and `nature-paper2ppt`.

## Resource paths

Resolve scripts and references relative to the loaded SKILL.md directory, not the task working directory. Write generated outputs to the user or project output directory, not into the installed skill.
