# Pillar 1: Software Engineering

> Part of the [six pillars](README.md). **Our stance:** production habits beat clever code. You're often the only engineer on site, so whatever you skip, nobody else will catch.

## In plain words

An FDE writes code that has to keep running after they leave, in someone else's environment, maintained by people they've just met. That changes what "good code" means. It means boring, readable, tested, observable, and deployable by someone else with one command.

## Our stance 💬

1. **Deploy from code from day one.** If a resource was created by clicking in a portal, it doesn't exist as far as the handover is concerned.
2. **Logs and traces before features.** On day one of production, the first question is always "what happened?", and you need an answer.
3. **Write code the customer's team can read.** Use their language, their conventions and their repository, even if you'd choose differently.
4. **AI coding assistants are mandatory, and so is reviewing their output.** They make you faster; they also produce confident mistakes at speed.
5. **Small pull requests, weekly demos.** Big-bang merges are how engagements slip.

## What you need to know

### Production habits

- **Tests at three levels:** unit tests for logic, integration tests against real services (in a test environment), and end-to-end tests of the user journey. For AI systems, add evaluation tests (see [Pillar 5](05-ai-applications.md)).
- **Configuration and secrets:** no secrets in code or config files. Use managed identities where the platform supports them, and a secrets vault where it doesn't.
- **Idempotent deployments:** running the deployment twice should produce the same result as running it once.
- **Error handling for networks:** every remote call can time out, be throttled or fail. Retry with backoff, set timeouts, and fail loudly.

### Working in someone else's codebase

- Read before you write: build a map of the repository, its conventions and its deployment path in your first two days.
- Ask who reviews and who approves merges, and what "done" means for their team.
- Leave the codebase better documented than you found it. The customer will read your README long after they've forgotten your name.

### Integration

Most FDE work is gluing systems together. You need to be comfortable with:

- **Web APIs:** REST, authentication headers, pagination, rate limits, webhooks.
- **Messaging:** queues and events, for work that shouldn't block a user.
- **Contracts:** define the inputs and outputs of every integration explicitly. With AI agents, every tool is an integration contract.

### Observability

Use **OpenTelemetry**, the open standard for traces, metrics and logs, so the customer can send telemetry to whatever monitoring tool they already own. Trace every request end to end, including each model call and tool call.

### AI-assisted engineering

The productive pattern is **research → plan → implement → review**: the assistant researches the codebase, you approve a written plan, it implements, and you review. This keeps the human in charge of decisions and the assistant in charge of typing.

## On Microsoft

| Concept | Microsoft tool | Key facts | More |
|---|---|---|---|
| AI-assisted method | **HVE Core** (open-source GitHub Copilot agents, prompts and skills) | Its RPI lifecycle runs Research → Plan → Implement → Review → Follow-up; research is read-only ([HVE RPI](https://microsoft.github.io/hve-core/docs/rpi/)). Its security and responsible-AI agents are assistive only and don't replace security testing or human review ([Marketplace](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)) | [Technical reference: Phase 5](../microsoft-technical-reference.md#phase-5-hyper-velocity-engineering-hve--rpi) |
| Coding agent | **GitHub Copilot cloud agent** | ⚠️ With MCP it supports tools only, can't use remote MCP servers that need OAuth, and runs tools **without asking for approval** ([GitHub Docs](https://docs.github.com/copilot/using-github-copilot/coding-agent/extending-copilot-coding-agent-with-mcp)) | [Phase 7](../microsoft-technical-reference.md#phase-7-fde-developer-toolchain-mcp-copilot-cloud-agent-azd) |
| Custom agents | **`.agent.md` files** | YAML front matter sets tools, model and MCP servers; prompts up to 30,000 characters ([GitHub Docs](https://docs.github.com/en/copilot/reference/custom-agents-configuration)) | [Phase 7](../microsoft-technical-reference.md#phase-7-fde-developer-toolchain-mcp-copilot-cloud-agent-azd) |
| Azure context for AI tools | **Azure MCP Server** | One server for Azure tools; tool access follows your Azure permissions ([Learn](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/get-started)) | [Phase 7](../microsoft-technical-reference.md#phase-7-fde-developer-toolchain-mcp-copilot-cloud-agent-azd) |
| Infrastructure-as-code | **Bicep or Terraform with Azure Verified Modules (AVM)** | AVM is the default starter for the Azure Landing Zone accelerator ([ALZ-Bicep](https://github.com/Azure/ALZ-Bicep)) | [Phase 2](../microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones) |
| Agent deploy loop | **`azd ai agent`** | `init` → `run` locally → `up` → `invoke` / `monitor` → `down` ([Learn](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/init-agent-project)) | [Phase 7](../microsoft-technical-reference.md#phase-7-fde-developer-toolchain-mcp-copilot-cloud-agent-azd) |

💬 Our default engagement setup: HVE Core agents in the customer's repository, an [`agent-instructions`](../../skills/agent-instructions/SKILL.md) file that encodes their rules, Azure MCP Server for cloud context, and `azd` for a repeatable deploy.

## Mistakes we keep seeing 💬

- Giving a coding agent write access to production because "it's faster". It's faster until it isn't.
- Building in your own subscription and "moving it over later". Later never comes cleanly; build in the customer's tenant from the start.
- No telemetry until the first incident, then guessing.
- One giant pull request in week five that nobody can review.

## Prove it

| Level | Project |
|---|---|
| Beginner | A small web API with unit tests, a CI pipeline that runs them, and structured logs |
| Intermediate | The same API deployed from Bicep or Terraform, with OpenTelemetry traces visible in a monitoring tool |
| Advanced | Join an unfamiliar open-source repository, use an AI assistant with a written plan to ship a reviewed change, and document how you verified it |

## Interview questions

1. You join a customer repository with no tests and a deadline in four weeks. What do you do first?
2. How do you stop an AI coding agent from doing damage in a customer environment?
3. Walk through how a request is traced from a user's click to a model call and back.
4. What makes a deployment idempotent, and why does it matter at handover?

## Skills for this pillar

[`agent-instructions`](../../skills/agent-instructions/SKILL.md) · [`adr`](../../skills/adr/SKILL.md) · [`runbook`](../../skills/runbook/SKILL.md)

---

← [Pillars index](README.md) · Next: [Pillar 2: Data](02-data.md) →
