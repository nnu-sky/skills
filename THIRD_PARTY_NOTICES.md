# Sources and third-party licenses

This is a curated distribution with local adaptations, not a claim of sole authorship. File-specific notices and third-party licenses take precedence over the license for NNU Sky's original contributions.

| Material | Source | Terms and distribution treatment |
|---|---|---|
| Nature skills and shared references, including academic search, experiment log, figure and paper card | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills), also [Jiahao8595/nature-skills](https://github.com/Jiahao8595/nature-skills) | Current upstream Apache-2.0; [full license](licenses/Apache-2.0.txt). Existing author metadata is retained. Upstream may contain historical MIT labels; this distribution does not use them to relicense Apache material. |
| ML paper writing | [Orchestra Research AI Research Skills](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/main/20-ml-paper-writing/ml-paper-writing) | MIT, Copyright (c) 2025 Claude AI Research Skills Contributors; [full license](licenses/Orchestra-MIT.txt). Applies to skill material, not separately licensed venue packages. |
| Academic figure template/QA ideas referenced in figure guidance | [TingxiYu/academic-figure-skill](https://github.com/TingxiYu/academic-figure-skill) | Apache-2.0. Attribution retained; no claim that upstream endorses this distribution. |
| Conference LaTeX snapshots | Sources and copyright comments inside `ml-paper-writing/templates` | Original venue/package terms remain in effect, including LPPL for indicated LaTeX packages and bibliography styles. No blanket MIT relicensing. Standard natbib.sty copies are excluded; use the TeX distribution. Check current official venue packages before submission. |
| figures4papers | [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | Current upstream CC BY-NC 4.0, checked 2026-09-12. Scripts, preview images and PDFs from this collection are not bundled. The upstream reference link remains available. |

The local source was assembled from existing skills and private configuration repositories. Full historical per-file provenance was not available; the entries above state verified upstream associations, not an assertion that all files equal today's upstream versions.

NNU Sky modifications (2026-09-12) concern task scope, progressive loading, GPT-6 instruction behavior, available-tool routing, owner-facing provenance, portable server configuration and packaging. Modified Nature files carry a short modification notice. Research content and author attributions remain intact. Fictional experiment-log examples remain explicitly fictional.

Personal credentials, host addresses, machine-specific secret storage details, `.git` history from private repositories and compiled Python caches are excluded from the public distribution.

License source commits: Nature `c4e4c99fbeaf0168cda090f8739e1508017a610e`; Orchestra `773a52944ba4747a18bd4ae9ade53fff041adcbc`. Original license texts are reproduced without modification.

On 2026-10-13, selected correctness fixes and regression tests were merged from
[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills), reviewed at
`473e8d7b1b918fe37208d3a5e143a3ac9af4c91b`. The source commits are
`cfe9e5c2b95633aee4677c69fd4be524f5e96dd5`,
`4e4b4bdf5e4d114403491c0cbe3d4e100b6153f2`,
`afb69116b612d1ce2d7c133f8797480bf2b0a39e`,
`e605b35611ab2849af46d0cf7831aefdcf85be07` (academic-search parsing and conversion),
`5b05fe1ba3867b61ee2742a060d5cf05dad027a2`,
`9e10be27c8bd11f1738ffade0d10ef93a50a6d07` (figure audits and output handling), and
`e25620c4eb9544b83f2fc45c3255c83a2532a7cc` (shared consistency checks).
Local skill instructions, invocation policies, plotting-backend selection and
XML dependencies were preserved. This is a selective merge, not a claim that
the distribution matches the entire upstream tree. The license source commits
above remain the original license provenance.
