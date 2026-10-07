# Go-Live Readiness

## Identity & access
- [ ] Managed identity / Entra Agent ID only; no secrets in code
- [ ] Least-privilege RBAC; PIM for admins
- [ ] Agent registered and governed (Agent 365 registry, if licensed)
- [ ] Agent 365 licences in place if Defender must protect Foundry / Copilot Studio agents (required since 1 Jul 2026)
- [ ] Callers that only invoke agents use Foundry Agent Consumer, not Foundry User

## Network
- [ ] Private endpoints + Private DNS validated end to end
- [ ] APIM AI gateway: token limits, logging, llm-content-safety (incl. MCP/A2A)
- [ ] If publishing to Teams/M365 with public access disabled: `enable_m365_public_endpoint` approved by security; Bot Service rights granted
- [ ] Agent tools routed through the VNet (separate template) if required

## Data
- [ ] ACL trimming verified with a low-privilege test user
- [ ] Purview labels / DLP respected; DSPM oversharing assessment reviewed

## Quality & safety
- [ ] Golden eval set passes agreed thresholds
- [ ] Evaluator limitations checked (e.g., Azure AI Search tool calls)
- [ ] AI Red Teaming Agent scan run; findings triaged
- [ ] If the agent uses the Azure AI Search tool: groundedness measured with `context` in the dataset, not the tool-call evaluators

## Operations
- [ ] Tracing + alerts in Application Insights
- [ ] Cost guardrails, budgets, Copilot Studio environment/agent credit limits
- [ ] Hosted agent network egress policy set (if hosted on Foundry)
- [ ] Hosted agent protocol chosen (Responses vs Invocations) with publishing/A2A needs checked
- [ ] Preview features listed with fallback plan
- [ ] Runbook, RACI, and named owner signed off
