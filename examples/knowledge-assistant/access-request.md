# Access Request: Harbourline Insurance / Policy Assistant

> **Worked example.** A filled-in [`access-request`](../../skills/access-request/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**Requested by:** E. Marsh (lead FDE) · **Customer contact:** D. Whitfield (Head of Claims Operations), who routes each row to its approver · **Date sent:** week 0, day 1 · **Needed by:** week 1, day 1 (kickoff) for development; week 1, day 5 for production data

**Status at:** week 2, day 1. Everything granted except the two rows still open in the blocked-items table.

## People and accounts

| Who | Account needed | Why | Approver | Status | Date granted |
|---|---|---|---|---|---|
| E. Marsh, T. Osei | Corporate accounts in Harbourline's Entra tenant (not guest), with multifactor authentication | Sign in to Azure, SharePoint and Teams as a Harbourline user | J. Tan (Identity Lead) | Granted | Week 0, day 3 |
| Product engineer (part-time) | Guest account, development resource group only | Pair on the agent and evaluation code | J. Tan | Granted | Week 0, day 4 |
| E. Marsh, T. Osei | Harbourline virtual desktop | The file share is only reachable from the corporate network | S. Adeyemi (Platform team lead) | Granted | Week 0, day 5 |
| T. Osei | Low-privilege test user `svc-test-motor`: a Motor handler's groups, **no** Pricing access | Permission-trimming tests in the [evaluation plan](eval-plan.md) and the [threat model](threat-model.md#4-threats) | L. Moreau (SharePoint administrator) | Granted | Week 1, day 2 |

## Cloud permissions

| Scope (subscription / resource group / workspace) | Role | Time-limited? | Why | Approver | Status |
|---|---|---|---|---|---|
| `rg-policyassist-dev` in the non-production subscription | Contributor | Yes, 12 weeks | Build and deploy from the pipeline | S. Adeyemi | Granted week 0, day 4 |
| `rg-policyassist-prod` | Reader, with just-in-time elevation to Contributor for deployments | Yes, 4 hours per elevation | Diagnose; deployments run from the pipeline, not by hand | R. Okafor (Security Architect) | Granted week 1, day 3 |
| Shared APIM instance (platform team's) | API Management Service Contributor on one product and its APIs only | Yes, 12 weeks | Gateway policies: token limits, content safety, IP filter | S. Adeyemi | Granted week 1, day 1 |
| Log Analytics workspace (security operations) | Log Analytics Reader | Yes, 12 weeks | Check that gateway and agent logs arrive | R. Okafor | Granted week 1, day 3 |

💬 We asked for less than we needed in production on purpose. Reader plus just-in-time elevation was approved in two days; the same team took three weeks over standing Contributor on a previous project, according to S. Adeyemi.

## Identity for the solution

| Item | Detail | Approver | Status |
|---|---|---|---|
| Agent identity | Entra Agent ID for the Foundry prompt agent; keyless, no secrets | J. Tan | Granted week 1, day 4 |
| Indexer identity | Managed identity; read on the three SharePoint sites and the file share's `published` folder only. Site-scoped, not tenant-wide (later recorded as ADR-005) | J. Tan, L. Moreau | Granted week 1, day 5 (see blocked items) |
| Permission consent | SharePoint read with permissions metadata for the three named sites, so results can be trimmed | J. Tan (tenant admin) | Granted week 1, day 5 |
| Can we create app registrations or agent identities? | No. Via J. Tan's request form, two working days | J. Tan | Agreed |
| Teams publishing rights | Azure Bot Service rights on the production resource group. Foundry roles don't grant these ([technical reference, Phase 2](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)) | S. Adeyemi | Granted week 3, day 2 (added after the first request) |

## Network

| Path | From → to | Private or public | Firewall rule / private endpoint needed | Approver | Status |
|---|---|---|---|---|---|
| Agent to model, knowledge base and storage | Foundry project → Azure AI Search, storage | Private | Private endpoints in the platform team's spoke network | S. Adeyemi | Granted week 1, day 2 |
| Indexer to file share | Azure → on-premises file server | Private | Existing ExpressRoute; one firewall rule for the indexer's subnet | S. Adeyemi | Granted week 1, day 4 |
| Teams to the agent | Microsoft 365 → APIM gateway | **Public, source-IP-filtered.** Microsoft 365 can't connect to agents privately ([technical reference](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)) | Exception to Harbourline's "no public endpoints" standard | R. Okafor | Accepted week 2 in [ADR-006](adr-006-teams-public-route.md) |

## Data

| Dataset / system | Access level | Contains sensitive data? | Approver (data owner) | Status |
|---|---|---|---|---|
| SharePoint: Claims Policy (production) | Read-only | Internal | D. Whitfield; data-handling check by F. Lindqvist (Data Protection Officer) | Granted week 1, day 5 |
| SharePoint: Underwriting (production) | Read-only | Internal | A. Novak (Underwriting policy manager) | Granted week 1, day 5 |
| SharePoint: Pricing (production) | Read-only, **after** the oversharing fix | Confidential (drafts) | G. Patel (Head of Pricing) | Granted week 2, day 3, conditional on the fix |
| File share: legacy policies, `published` folder | Read-only; `drafts` folder excluded | Internal | A. Novak | Granted week 1, day 4 |
| Quality team's quarterly audit sample | Read-only export, claim numbers removed | Personal data removed before export | F. Lindqvist | Granted week 1, day 3 |

## Code and delivery

| Item | Detail | Status |
|---|---|---|
| Repository | `policy-assistant` in Harbourline's Azure DevOps; S. Adeyemi's team reviews and merges to `main` | Granted week 0, day 3 |
| Pipelines | We can deploy to development; production needs S. Adeyemi's approval in the pipeline | Granted week 1, day 1 |
| Work tracking | Azure Boards, project `Claims-AI` | Granted week 0, day 3 |
| AI coding assistants | Allowed, with the rules in [`AGENTS.md`](agent-instructions.md); no production data in prompts | Agreed with R. Okafor week 1, day 2 |

## Licences and capacity

| Item | Needed for | Owner | Status |
|---|---|---|---|
| Model quota in the Foundry project's region | Load test at 10× expected traffic (see the [threat model](threat-model.md#4-threats)) | S. Adeyemi | Granted week 2 |
| Agent 365 | Defender coverage of the agent ([technical reference, Phase 3](../../docs/microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)) | J. Tan, K. Brennan (IT Finance) | Open: see blocked items |

## Blocked items (escalate weekly)

| Item | Blocked since | Impact | Escalated to |
|---|---|---|---|
| ~~Production data approval for all three SharePoint sites~~ | Week 0, day 1. **Resolved week 1, day 5, nine working days after sending** | No real documents for the data audit; the team worked on a 40-document sample A. Novak exported by hand | Day 3: reminder to each data owner. Day 6: D. Whitfield raised it at the claims leadership meeting. Day 8: 15-minute call with F. Lindqvist, who wanted the retention period for indexed content in writing. Granted two days later |
| ~~Pricing site read~~ | Week 0, day 1. **Resolved week 2, day 3** | Pricing questions couldn't be tested | G. Patel would not approve until the "Everyone except external users" sharing was removed. L. Moreau scheduled the fix; G. Patel approved on the condition that indexing waits for it. Tracked in the [threat model](threat-model.md#4-threats) |
| Agent 365 licensing | Week 1, day 3 | Defender coverage of the agent unconfirmed; doesn't block the pilot | J. Tan and K. Brennan; on the [weekly status](weekly-status.md) until closed |
| Bot Service rights for Teams publishing | Week 2, day 4 (not in the first request) | Pilot publishing in week 4 at risk | S. Adeyemi; granted week 3, day 2 |

💬 What moved the production data approval was a named person in the room. Three emails over five days did nothing; one line on D. Whitfield's leadership agenda and one call answering F. Lindqvist's actual question cleared it in four.
