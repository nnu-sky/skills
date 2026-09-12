# GPT-6 Astra compatibility review — 2026-09-12

Source: [OpenAI GPT-6 Astra prompting best practices](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices), retrieved from official documentation on 2026-09-12.

The guide emphasizes stronger instruction following, clarification behavior, task completion, communication, delegation calibration, and proportionate testing. The following are our scoped implementation decisions, not a verbatim copy of official guidance.

| Risk in previous instructions | Change |
|---|---|
| Ordinary tasks trigger full specialist workflows | Preserve narrowed skill descriptions and existing explicit-only policies |
| Repeated reading on every invocation | Reuse core guidance within the same task; load changed or relevant missing references |
| Figure task stops solely because Python/R was not previously saved | Honor user/project/saved choice; otherwise choose an available suitable backend and state the assumption |
| A single task silently changes global plotting preference | Save only when the user asks to remember a preference |
| All private file paths prohibited even in replies to the owner | Keep private material out of public artifacts, while allowing useful deliverable links and honest provenance |
| Named MCP tools assumed installed | Treat tool names as available-capability candidates; use documented fallback |
| Generic AI schematic routed to OpenRouter | Use the selected/available provider; OpenRouter helper only on explicit request |
| Bundled ethics text prohibits evidence-grounded argument drafting | Permit authorized drafting; preserve evidence checks and human scholarly responsibility |
| Every edit invokes complete figure validation | Preserve stage-aware, affected-region checks and final publication validation |
| Personal server aliases and router addresses act as universal defaults | Use local configuration and live observations; examples are not real targets |

No model ID, reasoning setting, API transport, account configuration, or tool credentials were changed. These are portable instruction files, not an API model migration. They can be used with GPT-6 Astra and other capable tool-using models, subject to the runtime's available capabilities.

Validation covers entrypoint/manifest structure, resource integrity, selected script behavior and packaging. It does not establish improved scientific quality, speed, or universal behavior across all thirteen skills. Real research cases should supply the next behavioral evidence before adding further rules.
