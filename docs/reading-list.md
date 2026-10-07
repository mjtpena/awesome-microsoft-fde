# Reading List & Official Sources

> Part of the [Awesome Microsoft FDE](../README.md) guide. Every primary source used in this guide, grouped by topic.
> New to the topic? Start with the [README](../README.md) first: it explains the ideas in plain language. This page is the detailed, fully sourced reference.

**Last verified:** 7 October 2026.

**The FDE role**

- [Wikipedia: Forward deployed engineer](https://en.wikipedia.org/wiki/Forward_deployed_engineer) · [Palantir: Dev versus Delta](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87) · [a16z: Trading Margin for Moat](https://a16z.com/services-led-growth/)
- [Microsoft Frontier Company announcement](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/) · [ISE Code-With Engineering Playbook](https://microsoft.github.io/code-with-engineering-playbook/ISE/) · [Accenture Microsoft FDE practice](https://newsroom.accenture.com/news/2026/accenture-launches-microsoft-forward-deployed-engineering-practice-to-help-organizations-scale-ai-across-the-enterprise)
- What ISE engineers actually ship, from recent [ISE Developer Blog](https://devblogs.microsoft.com/ise/) posts: context passing in multi-agent A2A systems, orchestration patterns for multi-agent systems, choosing between keyword and hybrid search, separating deterministic extraction from AI inference
- [Microsoft FY26 recap (Forward Deployed Engineering team, Novo Nordisk)](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/) · [Directions on Microsoft on Frontier Company](https://www.directionsonmicrosoft.com/microsoft-launches-its-own-forward-deployed-engineering-unit-the-frontier-company/?type=All)
- [Bloomberry: 1,000 FDE postings analysed](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/) · [The Pragmatic Engineer: FDE heats up again](https://blog.pragmaticengineer.com/the-pulse-forward-deployed-engineering-heats-up-again/)

**Frameworks**

- [ALZ-Bicep (AVM migration notes)](https://github.com/Azure/ALZ-Bicep)
- [Well-Architected Framework: AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/)
- [Azure AI Landing Zones](https://github.com/Azure/AI-Landing-Zones)

**Agents & AI**

- [Foundry Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) · [Foundry What's New (monthly)](https://devblogs.microsoft.com/foundry/category/whats-new/)
- [Microsoft Agent Framework repo](https://github.com/microsoft/agent-framework) · [Orchestrations 1.0](https://devblogs.microsoft.com/agent-framework/agent-frameworks-orchestration-patterns-reach-1-0/) · [AG-UI](https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/ui/ag-ui/)
- [Foundry IQ](https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/) · [Agentic retrieval](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)
- [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) · [AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent)
- [Declarative vs custom engine agents](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-overview) · [Copilot Studio billing](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management) · [GitHub Copilot harness costs](https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-github-copilot-harness)
- [Hosted agent sessions](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-sessions) · [Toolbox](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/toolbox-overview) · [Agent Optimizer](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview) · [Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview) · [Agent networking](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/networking-options) · [Work IQ](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/)

**Data**

- [OneLake: Shortcuts vs Mirroring](https://learn.microsoft.com/en-us/fabric/onelake/unify-data) · [fabric-cicd](https://microsoft.github.io/fabric-cicd/1.3.0/how_to/getting_started/) · [Sept 2026 Fabric feature summary](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/fabric-september-2026-feature-summary/5325825)
- [FabCon/SQLCon 2026 Barcelona announcements](https://azure.microsoft.com/en-us/blog/fabcon-and-sqlcon-2026-in-barcelona-building-the-data-foundation-for-microsoft-copilot-and-agents/)

**Identity, security, governance**

- [Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id) · [Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) · [Agent 365 licensing FAQ](https://www.microsoft.com/licensing/faqs/122) · [Purview DSPM](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about)
- [Zero Trust Workshop: AI guidance](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/AI/AI_046) · [Defender agent security → Agent 365](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365) · [Foundry RBAC](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry)
- [Azure IRAP](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-australia-irap)

**Sovereign**

- [Azure Local disconnected operations](https://learn.microsoft.com/en-us/azure/azure-sovereign-clouds/private/azure-local/disconnected-operations-overview) · [Management cluster](https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-control-plane-appliance?view=azloc-2607) · [Foundry Local disconnected](https://learn.microsoft.com/en-us/azure/azure-sovereign-clouds/private/foundry-local/disconnected-operations/concept-overview) · [SQL Server on Azure Local (disconnected)](https://learn.microsoft.com/en-us/sql/sql-server/azure-local/deploy-disconnected?view=sql-server-ver17)

**Velocity & toolchain**

- [Azure MCP Server](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/) · [azd Foundry agent extension](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/extensions/azure-ai-foundry-extension) · [Copilot custom agents](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

- [HVE Core](https://microsoft.github.io/hve-core/) · [RPI](https://microsoft.github.io/hve-core/docs/rpi/) · [Agent catalog](https://microsoft.github.io/hve-core/docs/agents/) · [Repo](https://github.com/microsoft/hve-core)

**Feeds to follow**

- [Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/) · [Agent Framework Blog](https://devblogs.microsoft.com/agent-framework/) · [Fabric Updates Blog](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs) · [Azure SQL Dev Corner](https://devblogs.microsoft.com/azure-sql/)
