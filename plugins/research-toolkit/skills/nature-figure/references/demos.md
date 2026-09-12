<!-- Modified by NNU Sky, 2026-09-12: portable distribution and task-scoped instruction review; see repository THIRD_PARTY_NOTICES.md. -->

# figures4papers Reference Index

Use this file when a user asks for a `figures4papers` look, cites the older
`scientific-figure-making` skill, or needs a concrete Python/matplotlib reference.

Upstream source: <https://github.com/ChenLiu-1996/figures4papers>.
The public distribution does not bundle its scripts or images to keep this distribution separate from its CC BY-NC 4.0
noncommercial terms (upstream license checked 2026-09-12). Inspect the upstream material
only when relevant, and implement original code with the user's data.

## Use boundary

1. Study layout, palette, axes, legends, and export structure as reference patterns.
2. Reimplement with original code and the user's own data whenever the upstream
   license or written permission does not clearly authorize copying or modification.
3. Never reuse manuscript-specific labels, metric values, statistical results, or
   visual assets as placeholders for real evidence.
4. Record the external reference and implementation provenance in the internal QA
   record when it materially influenced the result.
5. Preserve the editable SVG/PDF/TIFF and source-data rules from `api.md` and
   `qa-contract.md`.

## Prefer repository-owned implementation paths

When copying is not clearly authorized, route the pattern through the repository's
own material:

| Requested pattern | Open and use |
|-------------------|--------------|
| Grouped bars, ablation bars, shared legends | `tutorials.md`, `common-patterns.md` |
| Radar or polar comparison | `chart-types.md`, then implement with original code |
| Trends, sweeps, and reference baselines | `tutorials.md`, `chart-types.md` |
| Heatmap or annotated matrix | `tutorials.md`, `template-catalog.md` |
| Probability or manifold concept panel | `chart-types.md` |
| Submission typography, palette, and export | `api.md`, `design-theory.md` |
| CSV-driven reproducible plots | `template-catalog.md`, `scripts/plot_templates.py` |

## Upstream source

<https://github.com/ChenLiu-1996/figures4papers>

Check the current upstream license and obtain permission when required before
redistributing, modifying, or publishing derived materials.
