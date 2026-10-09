# Cost Model: Harbourline Policy Assistant

> **Worked example.** A filled-in [`cost-model`](../../skills/cost-model/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names, volumes and token counts, is invented. **There are no real prices on this page:** every unit rate is a labelled placeholder (rate A, rate B, and so on) that shows the method. In the engagement, K. Brennan filled them from Harbourline's own price sheet. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**Version:** 2.0 (final) · **Date:** week 8 · **Agreed with:** K. Brennan (IT Finance, budget owner) · **Draft:** week 2, alongside the [use-case canvas](ai-use-case-canvas.md) · **Scope:** release 1 only (internal Motor and Property handlers, after the [scope reset](scope-reset.md))

## Usage assumptions

| Assumption | Value | Source / reasoning |
|---|---|---|
| Users | About 900 Motor and Property handlers | Release 1 scope ([scope reset](scope-reset.md)). Not the original 4,000 staff |
| Questions per user per day | 6 | Pilot: the 60 handlers in week 7 averaged 5.2 a day; rounded up because pilot users were also checking answers against the old way |
| Working days per month | 21 | Harbourline's standard planning figure |
| **Questions per month** | **About 113,000** (900 × 6 × 21) | Derived |
| Model calls per question | 1 | One answer call. Knowledge-base query planning isn't enabled in release 1, so there's no second model call. Follow-up questions count as new questions |
| Average input tokens per call | About 6,000 | Gateway logs from week 7: instructions about 1,200, five retrieved passages about 4,000, question and the last three turns about 800 |
| Average output tokens per call | About 350 | Gateway logs from week 7. Includes the source title, section, effective date and link written into the answer, because Teams shows no native citations for Foundry agents |
| Tool calls per question | 1 knowledge-base query | The only tool ([ADR-004](adr-004-read-only.md)) |
| Documents indexed | About 3,600 current documents, about 36M tokens for a full re-index | After [ADR-003](adr-003-current-version-only.md) removes superseded versions: Claims Policy, Underwriting, Pricing (permission-trimmed) and the file share's `published` folder. About 20 chunks of 500 tokens per document, measured on the week-7 index |
| Re-index pattern | Incremental nightly (about 2% of documents change); full re-index monthly; **each run happens twice**, test then production | The week-6 incident made the test run mandatory ([runbook](runbook.md)) |
| Scanned PDFs needing OCR (optical character recognition) | 140 documents, about 1,700 pages, one-off | [Data audit](data-audit.md) |

## Monthly cost

Placeholders: **A** = rate per 1M input tokens, **B** = rate per 1M output tokens, **C** = rate per 1M embedding tokens, **D** = rate per 1,000 pages of OCR, **S** = monthly rate per search unit, **G** = monthly charge-back for a share of the gateway, **L** = rate per GB of log ingestion.

| Component | Pricing unit | Units / month | Unit price | Monthly cost | Notes |
|---|---|---|---|---|---|
| Model usage: input | per 1M tokens | 678 (113,000 × 6,000) | Rate A | 678 × A | **Biggest line** on Harbourline's price sheet. Driven by passages retrieved, not by the question |
| Model usage: output | per 1M tokens | About 40 (113,000 × 350) | Rate B | 40 × B | Second-biggest model line. Compare rate B with rate A on the price sheet: output is often priced differently per token |
| Embeddings for indexing | per 1M tokens | About 102: nightly 15 + monthly full 36, × 2 environments | Rate C | 102 × C | Small, but doubled by the test-first rule |
| OCR of scanned PDFs | per 1,000 pages | 1.7, **one-off** (week 4) | Rate D | 1.7 × D, once | Not a running cost; listed so nobody asks where it went |
| Agent hosting | n/a | n/a | n/a | No separate line assumed | Prompt agent; consumption is the model and tool lines. Re-check the current Foundry meters before each budget year |
| Search / knowledge index | per search unit / month | 3: two replicas in production, one unit in test | Rate S | 3 × S | Fixed. Second-biggest line overall. Doesn't grow with questions until peak load needs a third replica |
| Data platform capacity | | | | Doesn't apply | No Fabric or data warehouse in this design |
| Gateway | share of the shared APIM (Azure API Management) instance | 1 | Rate G | G | Platform team's existing instance, charged back by API share |
| Monitoring and logs | per GB ingested | About 5 (2.3 from gateway request and response logs, the rest traces and diagnostics) | Rate L | 5 × L | Retention agreed with H. Ito; retention beyond the included period is a separate meter |
| Licences (per user) | per user / month | **Open** | n/a | Pending | Agent 365 is licensed per user, not per agent, and is needed if Defender must cover the agent ([technical reference](../../docs/microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)). J. Tan is confirming which users need a licence. Teams: no change, existing licences |
| **Total** | | | | 678A + 40B + 102C + 3S + G + 5L (+ licences) | K. Brennan's workbook holds the figure from Harbourline's price sheet |
| **At 3× usage** | | | | 2,034A + 120B + 102C + 3S to 4S + G + 15L | Model and log lines triple; search and gateway don't |

The method in one line: **price what grows with questions (tokens, logs) separately from what's fixed (search, gateway), and indexing separately from both.** For a knowledge assistant the indexing line can surprise you; here it's small because ADR-003 indexes current versions only.

## Sensitivity

| What if | What changes | Model tokens per month (input / output) | Effect on cost |
|---|---|---|---|
| Base case | | 678M / 40M | |
| **Usage doubles** (more questions per handler, or Property teams adopt faster) | Questions to 226,000 | 1,356M / 80M | Model and log lines double. Search stays at two replicas: the week-7 load test held at 10× expected peak |
| 3× usage | Questions to 339,000 | 2,034M / 120M | Model and log lines triple. Search may need a third replica (one more S) |
| **Answers get longer** (handlers ask for "full detail"; output 350 → 700) | Output tokens double | 678M / 80M | Output line doubles; the total rises much less, because input tokens outnumber output about 17 to 1. p95 latency moves towards the 8 s bar: watch it in the [evaluation](eval-plan.md) |
| More context per answer (10 passages instead of 5) | Input per call to about 10,000 | 1,130M / 40M | Input line up about two-thirds. Only worth it if retrieval at 5 results drops below the 90% bar |
| Conversation history uncapped | Input grows with each turn | Unbounded | Why history is capped at the last three turns in the agent's instructions |
| All 4,000 staff (the deferred scope) | About 4.4× questions | About 3,000M / 180M | Needs its own cost model, threat model and budget. Not in release 1 |
| Weekly full re-index instead of monthly | Embedding tokens about 2.4× | No change | Small; the evaluation run each re-index triggers costs more in people's time |

## Cost controls

- [x] **Per-user token limit at the gateway,** keyed on the caller's Entra identity. Set at roughly three questions a minute per user; normal use is under one. Load-tested at 10× expected traffic in week 7 ([threat model](threat-model.md))
- [x] **Budget with alerts** on the resource group: 50% (to S. Adeyemi), 80% (to platform on-call and K. Brennan, and an alert the [runbook](runbook.md) covers), 100% (S. Adeyemi and K. Brennan decide together whether to lower the per-user limit; the assistant isn't switched off for cost alone)
- [ ] Caching for repeated questions: **not used.** Answers are permission-trimmed per user, so a shared cache could serve one user's answer to another. The gateway's semantic cache also needs Redis access-key authentication ([technical reference](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)), which R. Okafor's policy doesn't allow. Revisit if usage triples
- [x] Loop and retry limits: one knowledge-base query per question, one retry on a throttled model call, history capped at three turns
- [ ] Credit or capacity caps for low-code environments: doesn't apply (no Copilot Studio, per ADR-001)

## Scenario notes

- **Knowledge assistant:** indexing uses about 102M embedding tokens a month against about 718M answer tokens, so on Harbourline's price sheet it's a small line (compare rate C with rate A on yours). It stays small because only current versions are indexed. If ADR-003 were reversed and every version indexed, the embedding line would grow by about a third and the answers would get worse. The test-first re-index doubles indexing cost; K. Brennan accepted that as the price of not repeating week 6.

## One-slide summary

> At about 900 handlers asking about **113,000 questions a month**, the assistant costs **[monthly total from K. Brennan's workbook]**, mainly driven by **input tokens: the policy passages sent to the model with each question**. At 3× usage it's **[3× total]**, because search and the gateway don't grow with questions. Controls in place: a per-user token limit on the gateway, a budget with alerts at 50%, 80% and 100%, and capped conversation history. The open item is the Agent 365 licence (owner J. Tan), which is per user and isn't in the total yet.

**Agreed by:** K. Brennan (IT Finance) · **Date:** week 8 · **Review:** after the first full month in production, and before any scope change from the backlog
