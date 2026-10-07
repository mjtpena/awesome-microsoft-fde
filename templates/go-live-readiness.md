# Go-Live Readiness: <Agent / System name>

> **Step:** 5 Harden · **Pillars:** 3 Cloud and networking, 4 Security and identity, 5 AI applications · **Scenarios:** core checklist for all, plus add-ons
>
> **How to use:** start ticking this in week three, not go-live week. Every unticked box needs an owner and a date, or a written risk acceptance. The Microsoft-specific checks at the end come from the [technical reference](../docs/microsoft-technical-reference.md).

**Target go-live:** · **Decision meeting:** · **Go / no-go owner:**

## Core checklist (every scenario)

### Identity and access
- [ ] The agent has its own managed identity; no secrets in code or config
- [ ] Least-privilege roles, scoped to specific resources; admin access is time-limited
- [ ] Callers only get the permissions they need to invoke the agent

### Network
- [ ] Private endpoints and private DNS tested end to end from the workload's own network
- [ ] All model traffic goes through the gateway, with token limits and logging
- [ ] Outbound traffic restricted to an approved list

### Data
- [ ] Permission trimming verified with a low-privilege test user
- [ ] Sensitive data labels respected; oversharing review done for indexed sources

### Quality and safety
- [ ] Golden set passes the agreed release bar (`eval-plan.md`)
- [ ] Red-team scan run; findings triaged and accepted or fixed
- [ ] Threat model reviewed and signed off by security (`threat-model.md`)

### Operations
- [ ] Tracing, dashboards and alerts live
- [ ] Budgets, cost alerts and caps in place (`cost-model.md`)
- [ ] Deployed from code via the pipeline, not by hand
- [ ] Preview features listed, each with a fallback
- [ ] Runbook tested by someone who didn't build the system (`runbook.md`)
- [ ] Named owner, RACI and handover accepted (`handover.md`)
- [ ] Kill switch documented and tested

## Scenario add-ons

### Knowledge assistant
- [ ] Every answer cites its source; citation correctness above the bar
- [ ] Refresh schedule for each source is running and monitored
- [ ] "I don't know" behaviour tested for questions with no answer in the documents

### Action agent
- [ ] Every write action requires approval, or has a signed risk acceptance for running without one
- [ ] Every action is audit-logged (who asked, what was approved, what happened)
- [ ] Rollback tested for each reversible action
- [ ] Rate limits on write tools

### Data agent
- [ ] Numbers match the trusted report for the golden set
- [ ] Queries are read-only and limited in time and rows
- [ ] The agent queries only the curated layer

### Regulated, private-only
- [ ] Every exception to "nothing public" approved in an ADR
- [ ] Logs stored where the regulator requires, for the required retention period
- [ ] Controls mapped to the customer's framework; residual risk accepted by the named risk owner

### Disconnected or sovereign
- [ ] Models, evaluation sets and updates staged locally
- [ ] Local identity integration tested
- [ ] Offline update procedure tested end to end
- [ ] Software bill of materials and signed artifacts in place
- [ ] Support diagnostics can be collected without internet

## Microsoft-specific checks

- [ ] Agent identity via Entra Agent ID or managed identity; agent registered in Agent 365 (if licensed)
- [ ] Agent 365 licences in place if Defender must protect Foundry or Copilot Studio agents (required since 1 Jul 2026)
- [ ] Callers who only invoke agents use the **Foundry Agent Consumer** role; keyless sign-in, because keys bypass role-based access
- [ ] API Management AI gateway: token limits, logging, `llm-content-safety` (also covers MCP and agent-to-agent payloads)
- [ ] Publishing to Teams / Microsoft 365 with public access disabled: `enable_m365_public_endpoint` approved by security; Bot Service rights granted
- [ ] Agent tools routed through the virtual network (separate template) if required
- [ ] Hosted agents: network egress policy set; protocol chosen (Responses vs Invocations) with publishing and agent-to-agent needs checked
- [ ] If the agent uses the Azure AI Search tool: groundedness measured with `context` in the dataset, not the tool-call evaluators
- [ ] Copilot Studio: environment and agent credit limits set
- [ ] Purview oversharing assessment reviewed for indexed SharePoint sites

**Decision:** Go / No-go / Go with conditions · **Signed:** · **Date:**
