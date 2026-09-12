---
name: ml-paper-writing
description: Write, revise, and audit publication-ready ML/AI papers for NeurIPS, ICML, ICLR, ACL, AAAI, and COLM. Use for research-repository grounding, contribution framing, section drafting, citation verification, venue compliance, rebuttals, and camera-ready preparation.
license: MIT
metadata:
  version: 1.2.0-local.1
  author: Orchestra Research
  tags: [Academic Writing, ML, LaTeX, Citations, Research]
---

# ML Paper Writing

## Purpose

Turn verified research artifacts into a clear, defensible paper. The paper must present one coherent contribution, connect every major claim to evidence, and remain honest about scope and uncertainty.

## Non-negotiable rules

- Ground claims in the repository, experiment records, proofs, source data, or user-provided evidence. Never invent results, settings, comparisons, citations, or implementation details.
- Treat the current official venue author guide and style package as the source of truth. Bundled templates and checklist references are snapshots, not proof of current requirements.
- Never create BibTeX from memory. Discover papers broadly, verify metadata and the attributed claim, then retrieve citation data from an authoritative source.
- Distinguish demonstrated results, derived conclusions, hypotheses, and planned experiments. Do not turn mixed, approximately preserved, or single-seed evidence into significance, equivalence, or general improvement claims.
- Draft proactively when the evidence and target are clear. Ask only when an unresolved choice would materially change the contribution, protocol, venue, or cost.
- Preserve the user's existing source, template, notation, and project structure unless a change is required for the requested deliverable.

## Progressive routing

Load only the material needed for the current task. Do not open every reference by default.

| Task | Load |
| --- | --- |
| Frame a contribution, outline a paper, draft or rewrite sections, or polish prose | [writing-guide.md](references/writing-guide.md) |
| Find related work, verify citations, or maintain BibTeX | [citation-workflow.md](references/citation-workflow.md) |
| Check submission requirements, anonymization, disclosures, ethics, limitations, or reproducibility | [checklists.md](references/checklists.md), then the current official venue guide |
| Simulate reviewers, audit acceptance risks, prepare rebuttals, or respond to reviews | [reviewer-guidelines.md](references/reviewer-guidelines.md) |
| Verify the provenance of this skill's writing guidance | [sources.md](references/sources.md) |
| Start from a bundled LaTeX example | [templates/README.md](templates/README.md), but only after confirming venue and year against the official package |
| Create or revise publication figures | Use `nature-figure` when available; do not load figure-design material here as a substitute |

For a complete-paper task, start with `writing-guide.md`; add the citation, venue, or reviewer reference only when that stage begins. For a narrow section edit, load only `writing-guide.md`. For citation-only work, load only `citation-workflow.md`.

## Core workflow

### 1. Establish the evidence base

Read the project rules and only the artifacts relevant to the requested paper work:

- README, research log, existing draft, and contribution notes;
- method implementation and configuration needed to describe the approach;
- final tables, source data, logs, proofs, and evaluation protocol supporting claims;
- bibliography and already cited papers;
- target venue and submission stage.

Prefer existing scripts, tables, figure sources, and reusable paper structure. Do not create near-duplicate experiment or manuscript pipelines when parameters or content can be expressed through the existing one.

### 2. Build a claim-evidence map

Before substantial drafting, record:

- the one-sentence contribution;
- two to four specific supporting claims;
- the evidence artifact for each claim;
- the closest baseline or prior work;
- known limitations and unsupported claims that must not enter the paper.

If framing is uncertain, choose the best evidence-supported framing, state the assumption, and continue drafting. Ask the user only when competing framings would materially change the work.

### 3. Design the narrative

The introduction should make three elements clear:

- **What:** the precise new result, method, diagnosis, theorem, or empirical finding;
- **Why:** the evidence that establishes it;
- **So what:** why the result matters to the target community.

Organize experiments around claims, not around the order in which runs happened. Organize related work by technical distinction, not as a paper-by-paper list.

### 4. Draft in reviewer reading order

A useful default order is:

1. one-sentence contribution and title direction;
2. Figure 1 or the central evidence layout;
3. abstract;
4. introduction and contribution bullets;
5. method or theory;
6. experiments and limitations;
7. related work;
8. appendix, reproducibility, and required disclosures.

This order is a default, not a rigid template. Reuse a strong existing manuscript structure when one is already present.

### 5. Audit every claim

For each quantitative or comparative statement, verify:

- the source artifact exists and matches the manuscript number;
- the metric direction, unit, aggregation, hardware, seed count, and protocol are stated correctly;
- comparisons are fair or explicitly labeled as published or non-matched;
- uncertainty language matches the available evidence;
- theory assumptions and theorem scope are visible before the claim is used.

### 6. Verify citations

When Exa MCP is available, use it for discovery, not as the sole authority. For every citation:

1. identify the intended paper unambiguously;
2. confirm it in at least two appropriate sources when practical, such as the publisher or DOI record plus arXiv, Crossref, Semantic Scholar, OpenAlex, or the official proceedings;
3. inspect the paper to verify the attributed claim;
4. retrieve BibTeX or authoritative metadata programmatically;
5. add the entry with a consistent key and compile-check it.

If verification fails, use an explicit `[CITATION NEEDED]` or clearly marked placeholder and tell the user. Do not silently substitute a different paper.

### 7. Apply venue requirements after content decisions

- Fetch the current author guide and official style package for the target year.
- Copy the complete official template rather than merging preambles or editing style files.
- Check page limits, anonymity, supplementary rules, disclosure, checklist, ethics, limitations, and reproducibility requirements.
- Treat bundled templates as reusable examples only when they exactly match the target venue and year.
- Compile from a clean environment and inspect the rendered PDF, references, figures, fonts, overfull boxes, unresolved citations, and placeholders.

## Section quality gates

- **Abstract:** states the result, motivation, approach, evidence, and strongest defensible takeaway without a generic opening.
- **Introduction:** exposes the problem, gap, insight, contribution bullets, and evidence preview early.
- **Method or theory:** defines notation and assumptions; provides enough detail to reproduce or verify the contribution.
- **Experiments:** states which claim each experiment tests; documents protocol, baselines, seeds, uncertainty, compute, and selection rules.
- **Related work:** explains technical differences and claim boundaries; citations are verified.
- **Limitations:** states where conclusions do not apply and which evidence is missing.
- **Figures and tables:** use source data, consistent precision, metric directions, self-contained captions, and editable or vector formats when appropriate.

## Delivery

For a writing or revision task, report:

- the paper or source files changed;
- the contribution framing used;
- major evidence and citation decisions;
- unresolved placeholders or unsupported claims;
- venue and template status;
- compilation and visual-QA result when a PDF is part of the deliverable.

Stop once the requested manuscript outcome is supported and verified. Do not expand into unrelated experiments, exhaustive literature collection, or infrastructure work unless new evidence shows it is necessary.
