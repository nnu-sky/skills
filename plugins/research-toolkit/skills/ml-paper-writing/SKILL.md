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

## Goal and principles

Write a coherent scientific argument supported by verified evidence. Apply these principles before drafting and during local revisions; an internal verification process is not a manuscript outline.

- Organize prose around the question, mechanism, method, findings, and significance. Choose each paragraph's role before its details; avoid execution chronology and code-step narration.
- Ground claims in source data, proofs, code, primary references, or user-provided evidence. Distinguish observations, deductions, and hypotheses; preserve mixed findings and never invent results or references.
- Include details that change scientific interpretation. Centralize reproduction settings in the experimental protocol, keep execution records in artifacts, and delete redundant prose rather than automatically moving it to the appendix.
- Express boundaries through accurately scoped claims. Retain necessary assumptions and controls, but explain consequential limitations once rather than repeatedly defending against hypothetical objections.
- Give text and displays distinct roles. Results explain patterns and meaning; captions explain the display; Discussion develops implications. Avoid repeating tables, contributions, or qualifications across them.
- Preserve the user's task scope, existing notation, source structure, and valid template. Follow current official venue requirements when relevant; bundled examples are not current submission authority.
- Verify citations against primary sources; never generate BibTeX from memory. Mark unresolved references explicitly. By default, omit displayed bibliography URLs while preserving verification metadata and requested code/data links; follow an explicit user or venue requirement when it differs.

## Task routing

Read only resources needed for the requested work and reuse unchanged guidance already loaded. A simple local edit can use the principles above without opening every reference.

| Task | Resource |
| --- | --- |
| Frame a contribution, outline, or substantially draft/revise sections | [writing-guide.md](references/writing-guide.md) |
| Resolve report-like prose, repetition, or defensive wording | [narrative-cleanup.md](references/narrative-cleanup.md): short self-check and examples |
| Find or verify citations; maintain bibliographic records | [citation-workflow.md](references/citation-workflow.md) |
| Check submission requirements, anonymity, disclosures, or reproducibility | [checklists.md](references/checklists.md), then the current official venue guide |
| Review acceptance risks, draft rebuttals, or respond to reviews | [reviewer-guidelines.md](references/reviewer-guidelines.md) |
| Check the provenance of writing guidance | [sources.md](references/sources.md) |
| Use a bundled LaTeX example | [templates/README.md](templates/README.md); confirm venue and year |
| Create or revise scientific figures | Use `nature-figure` when available |

## Working approach

1. **Read relevant material.** Inspect the requested text and the evidence needed to understand it. Reuse existing results, scripts, and project conventions; avoid broad repository audits for local prose edits.
2. **Identify the argument.** Clarify the claim, supporting evidence, and paragraph or section role. Write a separate claim–evidence map only when sources are dispersed, the argument is complex, or the user requests one. Choose the drafting order to suit the task.
3. **Revise within scope.** Use the strongest wording supported by the evidence. Ask only when uncertainty materially changes the argument or assignment. Keep internal verification details out of the paper unless they help readers interpret the result.
4. **Check what changed.** For numbers, check the source and statistical meaning; for theory, assumptions and scope; for experimental comparisons, relevant settings and consequential differences. Reuse unchanged verified evidence. Update affected citations, labels, protocols, and cross-references when moving or removing material.

## Completion

Check the revised scope for scientific purpose, necessary detail, repeated qualifications, and duplication between prose and displays. Use the narrative reference when examples help; a local edit does not require a full-paper review.

When delivering an edited PDF, compile and inspect affected pages and adjacent reflow for unresolved references, overflow, and readable figures or tables. Apply submission checks only when the request or changes involve them; preserve a valid existing template.

Report the actual changes, relevant verification, and any unresolved issue that affects the result. Do not require a full contribution, citation, or venue-status report for a small edit. Stop when the requested outcome is complete; do not expand into unrelated experiments or infrastructure.
