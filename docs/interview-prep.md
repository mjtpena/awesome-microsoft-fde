# Microsoft FDE Interview Prep

> Part of the [Awesome Microsoft FDE](../README.md) guide. The reported interview loop, case studies with outline answers, and rapid-fire questions with answers.
> New to the topic? Start with the [README](../README.md) first: it explains the ideas in plain language. This page is the detailed reference.

**Last verified:** 8 October 2026.

Every rapid-fire answer links to the section of the [technical reference](microsoft-technical-reference.md) or the [role research](fde-role-and-market.md) where its source is cited. The case-study outlines are opinion (💬): they show one strong answer, not the only one.

## 🎯 Interview Blackbook

### The Microsoft FDE interview loop (reported)

Candidate reports describe a 4–6 week process: recruiter screen → online assessment (often Azure/AI services) → one or two LeetCode-style phone screens → onsite with two coding rounds focused on production-grade code, a system-design round (e.g. a recommender on Azure) and a combined hiring-manager/behavioural round ([fdeinterviews.com](https://fdeinterviews.com/company/microsoft)). ⚠️ This is self-reported and unofficial, and loops vary by org (ISE, Frontier Company, product groups), so confirm with your recruiter.

### Case studies (practise out loud) 💬

Talk through each one before you open the outline. Interviewers care more about your first three questions than your final architecture. Cases 1, 3, 4 and 6 are the detailed versions of the four scenarios in the [README](../README.md#12-practise-four-interview-scenarios).

#### 1. The locked tenant (README scenario 1)

No app registrations, private endpoints only, 4 weeks to ship a RAG agent.

<details>
<summary>Outline answer</summary>

- **First questions:** who can approve identities and network changes, and how long does that take? Which document collections, for which users? Must users reach it from Teams?
- **Identity:** no app registrations doesn't mean no identity. Propose an Entra Agent ID blueprint and managed identities, and submit the request on day one ([Phase 3](microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)).
- **Network:** AI Landing Zone with Foundry Standard Setup on the customer's own virtual network, and APIM as the gateway ([Phase 2](microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)).
- **Knowledge:** Foundry IQ knowledge base with permission trimming; test with a low-privilege user ([RAG blueprint](microsoft-technical-reference.md#enterprise-rag-blueprint-azure)).
- **The trap to name:** if they want it in Teams, publishing needs a source-IP-filtered public route. Raise that in week one, not week four (case 7).

</details>

#### 2. SAP + SharePoint variance agent

Finance wants an agent that explains budget variances using SAP actuals and SharePoint commentary.

<details>
<summary>Outline answer</summary>

- **First questions:** which numbers are authoritative, at what grain, and who signs them off? Who may see which cost centres?
- **Data:** bring SAP in with Mirroring (proprietary source) and keep open-format data in place with Shortcuts ([Phase 1](microsoft-technical-reference.md#phase-1-data-engineering-on-microsoft-fabric)). Build a Gold star schema and a semantic model the business already trusts.
- **Agent:** Fabric data agent over the Gold model, added to Copilot Studio as a tool; it runs under the user's identity, so row-level security still applies ([Copilot Studio](microsoft-technical-reference.md#copilot-studio--m365-copilot-extensibility)).
- **Documents:** run the Purview DSPM oversharing assessment on the SharePoint sites before indexing the commentary.
- **Watch out:** Fabric data agents need cross-geo AI tenant settings, which need a data-residency decision.

</details>

#### 3. The hallucination incident (README scenario 2)

The assistant gave an executive a confidently wrong answer.

<details>
<summary>Outline answer</summary>

- **First questions:** do we have the trace for that exact request? Which documents were retrieved? Is the right answer in the corpus at all?
- **Diagnose:** split retrieval from generation. If the right passage wasn't retrieved, it's a search, chunking or stale-content problem; if it was retrieved and ignored, it's instructions or model ([Evaluation](microsoft-technical-reference.md#evaluation--agentops)).
- **Fix and prove:** add the question to the golden set, fix the cause, and gate releases on the evaluation run.
- **Improve:** Agent Optimizer can tune instructions and tool descriptions, but only after the evaluation shows the cause.
- **Tell the executive** what happened, what changed, and how you'll know if it happens again.

</details>

#### 4. Copilot Studio vs Foundry at the architecture review board (README scenario 3)

<details>
<summary>Outline answer</summary>

- **First questions:** who maintains it after handover, and what skills does that team have? What usage do you expect?
- **Cost:** Copilot Studio bills Copilot Credits per answer and action, and agents are disabled at 125% of prepaid capacity; GitHub Copilot harness usage isn't covered by Microsoft 365 Copilot licences. ([Copilot Studio](microsoft-technical-reference.md#copilot-studio--m365-copilot-extensibility)).
- **Lifecycle:** Copilot Studio uses Power Platform environments and solutions; Foundry uses code, CI/CD and `azd`.
- **Architecture guidance:** the Well-Architected Framework for AI covers Foundry workloads; Copilot Studio is explicitly out of its scope and has its own reference architectures ([Phase 2](microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)).
- **Recommendation:** whichever the customer's team can run without you, with the reason recorded in an ADR.

</details>

#### 5. Air-gapped defence site

A document assistant with no internet connection; updates arrive by approved media once a month.

<details>
<summary>Outline answer</summary>

- **First questions:** what classification, and who accredits the system? How do updates and models get approved and transferred?
- **Platform:** Azure Local disconnected operations (ALDO) with a dedicated three-node management cluster; size it from the published minimums ([Sovereign](microsoft-technical-reference.md#-sovereign-air-gapped--tactical-edge-deployment)).
- **Models:** Foundry Local on Azure Local is in preview, so get written acceptance of the preview risk and pin versions. Models come from a local registry filled by expansion packs.
- **Identity and data:** local Active Directory; SQL Server on Azure Local, without the Arc extension when disconnected.
- **Operations:** a runbook for the monthly update, a support bundle you've tested, and signed artifacts with an SBOM.

</details>

#### 6. Agent sprawl (README scenario 4)

300 agents built by different teams, and nobody knows what they can access.

<details>
<summary>Outline answer</summary>

- **First questions:** where were they built (Copilot Studio, Foundry, elsewhere)? Who owns each? Which ones touch sensitive data or can write?
- **Inventory:** Agent 365 registry across the tenant and Foundry Control Plane across Foundry projects ([Phase 3](microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)).
- **Identity:** move agents to Entra Agent ID and assign an owner and sponsor to each.
- **Protection:** Defender coverage for Copilot Studio and Foundry agents needs Agent 365 licences, and Agent 365 is licensed per user, so model the licence cost before you promise coverage.
- **Data:** Purview DSPM to find which agents reach overshared or sensitive data. Retire what nobody claims.

</details>

#### 7. "Private-only" bank wants the agent in Teams

<details>
<summary>Outline answer</summary>

- **First questions:** does the security policy allow an inbound, source-IP-filtered route? Are cited answers a requirement?
- **The fact:** Microsoft 365 doesn't support private connectivity to agents. With public network access disabled, publish through the REST API with `enable_m365_public_endpoint`, which opens only the Activity Protocol route, filtered by source IP ([Phase 2](microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)).
- **Also needed:** Azure Bot Service rights, which Foundry roles don't grant.
- **Second trap:** Foundry agents in Teams don't support citations or streaming, and Microsoft 365 handles the responses under its own data terms.
- **Answer:** offer compensating controls (IP filtering, gateway logging, content safety) and let security decide, or propose Copilot Studio or a declarative agent instead.

</details>

### Rapid-fire

<details>
<summary>Shortcuts vs Mirroring: when is Mirroring the only option?</summary>

When the source uses a proprietary format. Shortcuts only work with open formats ([Phase 1](microsoft-technical-reference.md#phase-1-data-engineering-on-microsoft-fabric)).

</details>

<details>
<summary>What does the MAF harness enable by default, and what is opt-in?</summary>

Most features are on by default and can be removed one by one, including context compaction, planning, file memory, todo tracking, skills and tool approval. Shell, file access, background sub-agents and auto-looping are opt-in and emit warnings ([MAF](microsoft-technical-reference.md#microsoft-agent-framework-maf)).

</details>

<details>
<summary>Name the five MAF orchestration patterns. Which one uses a manager agent that re-plans when the team stalls?</summary>

Sequential, Concurrent, Handoff, Group Chat and Magentic. Magentic is the manager-led one ([Multi-agent orchestration](microsoft-technical-reference.md#multi-agent-orchestration-maf)).

</details>

<details>
<summary>MCP vs A2A vs AG-UI?</summary>

MCP connects an agent to tools and data. A2A connects agents to each other. AG-UI connects an agent to a user interface: streaming, approvals and shared state ([MAF](microsoft-technical-reference.md#microsoft-agent-framework-maf)).

</details>

<details>
<summary>Which Foundry IQ API version for GA vs preview knowledge sources?</summary>

`2026-04-01` for generally available knowledge sources; `2026-08-01-preview` for preview sources or LLM-based query planning on non-web sources ([Foundry IQ](microsoft-technical-reference.md#foundry-iq-enterprise-knowledge)).

</details>

<details>
<summary>What's not supported for SQL Server on Azure Local when disconnected?</summary>

The SQL Server Arc extension, so you manage it with local tools ([Sovereign](microsoft-technical-reference.md#-sovereign-air-gapped--tactical-edge-deployment)).

</details>

<details>
<summary>Is GitHub Copilot harness usage in Copilot Studio covered by an M365 Copilot licence?</summary>

No. Building, testing, evaluating and running those agents all consume Copilot Credits, and computer use is always billed ([Copilot Studio](microsoft-technical-reference.md#copilot-studio--m365-copilot-extensibility)).

</details>

<details>
<summary>Is Agent 365 licensed per agent or per user, and who must be licensed?</summary>

Per user. License the users who delegate to agents, and the owners, sponsors and managers of agents that have their own access ([Phase 3](microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)).

</details>

<details>
<summary>Hosted agents: Responses vs Invocations protocol, and how long do sessions persist?</summary>

Responses is mapped automatically to the Activity Protocol for one-click Microsoft 365 publishing, so default to it. With Invocations you own the schema and conversation state. Sessions persist for up to 30 days, with an idle timeout of 2–60 minutes (default 15) ([Phase 4](microsoft-technical-reference.md#microsoft-foundry-agent-service)).

</details>

<details>
<summary>What can Agent Optimizer change for a prompt agent vs a hosted agent?</summary>

For prompt agents, the portal wizard tunes instructions, tool descriptions and model choice. For hosted agents, the Foundry Toolkit or `azd ai agent optimize` can also add skills ([Phase 4](microsoft-technical-reference.md#microsoft-foundry-agent-service)).

</details>

<details>
<summary>What does an Agent 365 licence unlock in Entra?</summary>

Agent-related Entra ID Governance (access packages, lifecycle workflows) and Network Control for agents ([Phase 3](microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)).

</details>

<details>
<summary>Why is IRAP not a certification?</summary>

IRAP is a risk-based assessment framework, not a pass/fail exercise. Azure services being assessed up to PROTECTED doesn't remove the need for your own deployment's risk decision ([Phase 3](microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)).

</details>

<details>
<summary>Your Foundry project has public network access disabled. How do you publish an agent to Teams?</summary>

Use the REST API with `enable_m365_public_endpoint`, which opens only the source-IP-filtered Activity Protocol route. You also need Azure Bot Service rights ([Phase 2](microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)).

</details>

<details>
<summary>Since July 2026, what licence does Defender need to protect Foundry and Copilot Studio agents?</summary>

An Agent 365 licence. Defender for Cloud Apps or Defender for Cloud alone no longer covers them, and hunting moves from `AIAgentsInfo` to `AgentsInfo` ([Phase 3](microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)).

</details>

<details>
<summary>Which evaluators should you avoid when the agent uses the Azure AI Search tool, and what's the workaround?</summary>

Avoid Groundedness, Tool Output Utilization, Tool Call Accuracy, Tool Input Accuracy and Tool Call Success. Put the retrieved content in the dataset as `context` and use the Retrieval or Document Retrieval evaluators ([Evaluation](microsoft-technical-reference.md#evaluation--agentops)).

</details>

<details>
<summary>Work IQ vs Microsoft Graph + your own RAG: when do you choose each?</summary>

💬 Work IQ when the agent needs permission-trimmed Microsoft 365 grounding without you building and running a retrieval pipeline; it's billed in Copilot Credits. Graph plus your own index when you need control over chunking, ranking or data that Work IQ doesn't cover ([Work IQ](microsoft-technical-reference.md#work-iq-m365-context-for-any-agent)).

</details>

<details>
<summary>What are a Palantir Delta and Echo, and why does the role need both?</summary>

A Delta is a forward deployed software engineer; an Echo is a deployment strategist with domain depth who finds the problem worth solving. The Echo picks the right problem and the Delta builds it fast ([Origins](fde-role-and-market.md#origins-palantirs-deltas-and-echoes)).

</details>

<details>
<summary>Which Microsoft organisation has run its FDE function for over a decade, and what delivery method does it use?</summary>

Industry Solutions Engineering (ISE), using Hypervelocity Engineering (HVE) ([Microsoft FDE persona](fde-role-and-market.md#who-does-fde-work-in-the-microsoft-ecosystem)).

</details>

<details>
<summary>What did Microsoft announce on 2 Jul 2026, and how does it say it differs from "FDE"?</summary>

Microsoft Frontier Company: US$2.5B and 6,000 industry and engineering experts embedded at customers. Microsoft says it "goes beyond what has been labeled as Forward Deployed Engineering" by combining industry knowledge and change management with AI engineering ([Microsoft FDE persona](fde-role-and-market.md#who-does-fde-work-in-the-microsoft-ecosystem)).

</details>

<details>
<summary>How do OpenAI's, Anthropic's, AWS's and Microsoft's 2026 deployment organisations differ in funding and structure?</summary>

OpenAI's Deployment Company and Ode with Anthropic are separate companies funded by outside capital (over US$4B and US$1.5B). AWS (US$1B) and Microsoft Frontier Company (US$2.5B) are internal investments. AWS runs pods of 5–6 engineers in 45-day sprints ([Deployment-company wave](fde-role-and-market.md#the-20252026-deployment-company-wave)).

</details>

<details>
<summary>Answer the "isn't this just consulting with a better title?" critique.</summary>

💬 Concede that it can be. The difference that holds up is that an FDE ships production code inside the customer's environment and feeds what they learn back into the product. If neither happens, it's consulting ([Critiques](fde-role-and-market.md#the-critiques-know-them-before-the-interview)).

</details>

<details>
<summary>A CIO asks whether a Frontier Company engagement locks them into Microsoft. How do you answer honestly?</summary>

💬 Yes, it can, and say so. Analysts describe free deployment help as customer-acquisition cost paid back through consumption. Then show what reduces lock-in: open protocols (MCP, A2A), portable code, the customer owning the repository and decisions in ADRs, and a handover their team can run ([Critiques](fde-role-and-market.md#the-critiques-know-them-before-the-interview)).

</details>
