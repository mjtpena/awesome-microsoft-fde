# Microsoft FDE Interview Prep

> Part of the [Awesome Microsoft FDE](../README.md) guide. The reported interview loop, case studies and rapid-fire questions.
> New to the topic? Start with the [README](../README.md) first: it explains the ideas in plain language. This page is the detailed, fully sourced reference.

**Last verified:** 7 October 2026.

## 🎯 Interview Blackbook

### The Microsoft FDE interview loop (reported)

Candidate reports describe a 4–6 week process: recruiter screen → online assessment (often Azure/AI services) → one or two LeetCode-style phone screens → onsite with two coding rounds focused on production-grade code, a system-design round (e.g. a recommender on Azure) and a combined hiring-manager/behavioural round ([fdeinterviews.com](https://fdeinterviews.com/company/microsoft)). ⚠️ This is self-reported and unofficial, and loops vary by org (ISE, Frontier Company, product groups), so confirm with your recruiter.

### Case studies (practise out loud) 💬

1. **The locked tenant:** no app registrations, private endpoints only, 4 weeks to ship a RAG agent. *Expected answer covers:* Entra Agent ID blueprint, AI Landing Zone, Foundry IQ with ACL trimming, APIM.
2. **SAP + SharePoint variance agent:** *covers:* Mirroring vs Shortcuts, Gold semantic model, Fabric data agent → Copilot Studio, DSPM oversharing assessment.
3. **The hallucination incident:** *covers:* tracing, retrieval vs generation root cause, eval gate, Agent Optimizer.
4. **Copilot Studio vs Foundry at the ARB:** *covers:* Copilot Credits and harness billing, ALM, WAF-AI scope, skills available in the customer team.
5. **Air-gapped Defence site:** *covers:* ALDO, management cluster sizing, Foundry Local (preview risk), local AD, SQL Server on Azure Local.
6. **Agent sprawl:** *covers:* Agent 365 registry, Foundry Control Plane, Entra Agent ID, Defender (Agent 365 licence since July), DSPM, licensing (E5/E7).
7. **"Private-only" bank wants the agent in Teams:** *covers:* Standard Setup BYO VNet, `enable_m365_public_endpoint`, Bot Service rights, compensating controls.

### Rapid-fire

Each answer has a source in the [technical reference](microsoft-technical-reference.md) or the [role research](fde-role-and-market.md).

- Shortcuts vs Mirroring: when is Mirroring the only option?
- What does the MAF harness enable by default, and what is opt-in?
- Name the five MAF orchestration patterns. Which one uses a manager agent that re-plans when the team stalls?
- MCP vs A2A vs AG-UI?
- Which Foundry IQ API version for GA vs preview knowledge sources?
- What's not supported for SQL Server on Azure Local when disconnected?
- Is GitHub Copilot harness usage in Copilot Studio covered by an M365 Copilot licence?
- Is Agent 365 licensed per agent or per user, and who must be licensed?
- Hosted agents: Responses vs Invocations protocol, and how long do sessions persist?
- What can Agent Optimizer change for a prompt agent vs a hosted agent?
- What does an Agent 365 licence unlock in Entra?
- Why is IRAP not a certification?
- Your Foundry project has public network access disabled. How do you publish an agent to Teams?
- Since July 2026, what licence does Defender need to protect Foundry and Copilot Studio agents?
- Which evaluators should you avoid when the agent uses the Azure AI Search tool, and what's the workaround?
- Work IQ vs Microsoft Graph + your own RAG: when do you choose each?
- What are a Palantir Delta and Echo, and why does the role need both?
- Which Microsoft organisation has run its FDE function for over a decade, and what delivery method does it use?
- What did Microsoft announce on 2 Jul 2026, and how does it say it differs from "FDE"?
- How do OpenAI's, Anthropic's, AWS's and Microsoft's 2026 deployment organisations differ in funding and structure?
- Answer the "isn't this just consulting with a better title?" critique.
- A CIO asks whether a Frontier Company engagement locks them into Microsoft. How do you answer honestly?
