# ADR-006: Publish to Teams over a source-IP-filtered public route

> **Worked example.** A filled-in [`adr`](../../skills/adr/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

- **Status:** Accepted, as an exception to Harbourline's "no public endpoints" standard
- **Date:** week 2, day 5 (architecture review board)
- **Deciders:** R. Okafor (Security Architect), S. Adeyemi (Platform team lead), D. Whitfield (Head of Claims Operations), E. Marsh (lead FDE); consulted J. Tan (Identity Lead), F. Lindqvist (Data Protection Officer)
- **Pillar(s):** 3 Cloud/network · 4 Security

## Context

- **Users are in Teams.** About 900 claims handlers work in Teams all day. M. Costa was clear that a separate tool would be "one more tab nobody opens" ([discovery interviews](discovery-interview.md)). D. Whitfield's ask is answers in Teams ([canvas](ai-use-case-canvas.md)).
- **Harbourline's standard is "no public endpoints".** R. Okafor: "No exceptions without an ADR." Every Azure resource in the design sits behind private endpoints.
- **Microsoft 365 can't connect to agents privately.** With public network access disabled, Teams publishing needs a separately enabled, source-IP-filtered route for Microsoft 365 traffic only ([technical reference, Phase 2](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)). There is no fully private option for Teams today.
- **Two further Teams constraints**, from the same section of the [technical reference](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones): Foundry agents published to Teams don't support streaming or citations as a structured feature, and Teams processes and stores the agent's responses under Microsoft 365's own data-handling terms. Publishing also needs Azure Bot Service rights that Foundry roles don't grant.
- The assistant is read-only ([ADR-004](adr-004-read-only.md)) and retrieval is permission-trimmed, which limits what a caller on this route could ever get.

## Options considered

| Option | Pros | Cons | Maturity (generally available / preview) | Who maintains it after handover |
|---|---|---|---|---|
| **A. Teams over the source-IP-filtered public route, with compensating controls** | Meets users where they work; no new client; the route accepts only Microsoft 365 source ranges | An exception to the standard; no structured citations in Teams; responses also held under Microsoft 365 terms | Generally available ([technical reference: Foundry Agent Service](../../docs/microsoft-technical-reference.md#microsoft-foundry-agent-service)) | Platform team (gateway, IP filter, alerts) |
| B. Internal web app, private only, reached over the corporate network | Keeps the standard intact; full control of citation rendering and streaming | A new app for the platform team to build, secure and run; one more place for handlers to go; adoption risk M. Costa named directly | Generally available | Platform team, plus front-end skills they don't have |
| C. Copilot Studio agent in Teams | Simplest for Teams | Doesn't keep the gateway and logging in Harbourline's subscription, which security required; rejected in ADR-001 | Generally available | n/a |
| D. Wait for private connectivity from Microsoft 365 | No exception needed | Not offered; no date. Blocks the engagement | n/a | n/a |

## Decision

We will publish the agent to Teams over the source-IP-filtered public route, with the compensating controls below, because it's the only way to reach handlers in Teams and the controls reduce the exposure to a level R. Okafor accepts for a read-only, permission-trimmed assistant.

**Compensating controls** (each one is a row in [threat model section 4](threat-model.md#4-threats) or [section 5](threat-model.md#5-detection-and-response), with how it's tested):

| Control | Where | Tested how |
|---|---|---|
| Only Microsoft 365 source ranges accepted; everything else dropped | Route filter and APIM gateway policy | Call from an Azure VM outside the ranges; must fail, and must raise the alert below |
| Alert on any request from outside the allowed ranges | Log Analytics, read by security operations | Fired by the test above |
| Keyless Entra sign-in only, keys disabled; Entra Agent ID with one role | Foundry project and gateway | A call with an API key fails |
| Content safety on the gateway; alert above 20 blocks an hour | APIM | Red-team prompts in the [red-team report](red-team.md) |
| Per-user token limit and monthly budget alert | APIM | Load test at 10× expected traffic |
| Every request logged, with retrieved document IDs in tracing | Gateway and Foundry tracing; retention agreed with H. Ito | Reconstruct one test request end to end |
| Permission-trimmed retrieval; no write tools | Knowledge base; [ADR-004](adr-004-read-only.md) | Low-privilege pricing run, repeated after every re-index |
| Kill switch: disable the API on the gateway | Platform on-call, steps in the [runbook](runbook.md) | Rehearsed once before go-live |

## Consequences

- **Security and identity:** one public, filtered entry point: TB1 in the [threat model](threat-model.md#2-how-the-system-works). Residual risk accepted by R. Okafor. Reviewed again at [go-live readiness](go-live-readiness.md) and whenever Microsoft offers private connectivity for this path.
- **Citations:** because Teams doesn't render structured citations for this agent, the [agent instructions](agent-instructions.md) require the source title, version, effective-from date and link in the answer text. The [evaluation plan](eval-plan.md) checks every non-refusal answer has one. Raised as [field feedback](field-feedback.md).
- **Privacy:** F. Lindqvist reviewed Microsoft 365's handling of the responses and recorded it in the [responsible AI impact assessment](responsible-ai-impact-assessment.md). Claim numbers and customer names are kept out of questions by the instructions and the pilot briefing.
- **Cost (monthly, at expected usage):** no extra infrastructure beyond the existing gateway. See the [cost model](cost-model.md).
- **Operations and ownership:** S. Adeyemi's team owns the IP filter, the alerts and the kill switch. The allowed source ranges must be kept current; checking them against Microsoft's published ranges is a monthly task in the [runbook](runbook.md). Bot Service rights were added to the [access request](access-request.md).
- **Lock-in and exit path:** the agent sits behind the gateway, so a private web app (option B) could be added later without changing the agent or the knowledge base.
- **Preview dependencies and fallback:** none. Teams publishing is generally available per the [technical reference](../../docs/microsoft-technical-reference.md#microsoft-foundry-agent-service). Fallback if the exception is withdrawn: option B.
