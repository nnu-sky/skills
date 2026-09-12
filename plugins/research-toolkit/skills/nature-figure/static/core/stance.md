<!-- Modified by NNU Sky, 2026-09-12: portable distribution and task-scoped instruction review; see repository THIRD_PARTY_NOTICES.md. -->

# Default operating stance

The older Python/matplotlib rules in this skill remain valid. The skill also supports R, especially `ggplot2 + patchwork + ComplexHeatmap + ggrepel + svglite/cairo_pdf + ragg`.

## Color policy

Prefer **unified method families across all panels** over maximal hue separation. For dense Nature Machine Intelligence-style figure pages, use the low-saturation `NMI pastel` family described in `references/api.md` and reserve green/red mainly for gains, drops, and other directional cues.

## Stance

- Start by classifying the requested figure into one of four archetypes: `quantitative grid`, `schematic-led composite`, `image plate + quant`, or `asymmetric mixed-modality figure`.
- Prefer one **hero panel** plus subordinate evidence panels over filling the canvas with equal-sized subplots.
- If the user asks for a single chart, still identify its role in the manuscript claim: discovery, mechanism, validation, comparison, robustness, or clinical/biological relevance.
- Keep the background white for plots and diagrams; switch to black only for microscopy / volume-rendering image plates.
- Prefer direct labels over legends when categories are spatially fixed or the legend would force unnecessary eye travel.
- Keep one restrained palette per figure: usually one neutral family, one signal family, and one accent family.
- Treat perceptual separation as necessary but not sufficient: verify that the intended hero series is more salient than baselines after rendering, and do not reuse a sequential light-to-dark scale as unrelated categorical colors.
- Treat statistics, `n`, error-bar definitions, source-data traceability, and image-integrity notes as part of the figure, not as optional caption cleanup.
- When panels show comparable seed/fold/split aggregates, use the same uncertainty definition in every comparable panel or state why a panel is exempt.
- Preserve canonical model capitalization in display labels. Legend entries use display-style initial capitalization; prose follows normal sentence grammar. Never apply blind `.title()` transformations to names such as `XGBoost`, `DeepSeek`, `GPT-5.2`, or `RF`.
- Before final delivery, require render-time alignment checks for comparable multi-panel layouts and a final-size, panel-by-panel inspection. During iteration, check affected regions and rerun only invalidated checks; broaden for global changes or unresolved defects. Source validation alone cannot establish rendered quality.
- When the user asks for broad `Nature` style rather than ML/NMI-specific style, read `references/nature-2026-observations.md` before choosing layout.
- When the user references `figures4papers` or the older `scientific-figure-making` skill, treat this skill as the successor and open `references/demos.md` for the third-party demo map, copyright boundary, and original reimplementation guidance.

## User-facing provenance

Keep credentials, unrelated private materials, and internal environment details out of public figures and manuscripts. In the user's own task, provide useful links to generated deliverables and relevant source files. Preserve attribution and explain material template or data provenance; do not hide it behind generic labels.

## Scope

Use the capability and exclusions in SKILL.md to determine applicability. A chart keyword alone does not turn exploratory work into publication preparation.
