# Pillar 2: Data

> Part of the [six pillars](README.md). **Our stance:** every AI project is a data project in disguise. Audit the data before you promise anything.

## In plain words

AI answers are only as good as the data behind them. In a real organisation, that data is spread across old databases, spreadsheets, file shares and software-as-a-service tools. It's often out of date, duplicated or locked behind permissions nobody remembers granting. The FDE's data job is to find it, judge its quality, get it to where the AI can use it, and keep the original permissions intact.

## Our stance 💬

1. **Do a data audit in week one.** Half of "AI problems" turn out to be data problems you could have found on day three.
2. **Leave data where it is when you can.** Every copy is something to secure, refresh and explain to an auditor.
3. **Permissions must travel with the data.** If a user can't open a document, the AI mustn't quote it to them.
4. **Unstructured data needs as much engineering as tables.** PDFs, scans and slide decks are where most RAG quality is won or lost.
5. **Model the data for questions people actually ask.** Ask the users for their top 20 questions before designing anything.

## What you need to know

### The data audit

For every source, answer: what system holds it, what format it's in, how big it is, how fresh it needs to be, who owns it, how you get access, what's wrong with it, and how sensitive it is. Use the [`data-audit`](../../skills/data-audit/SKILL.md) skill.

### Getting data in: reference, replicate or copy

| Approach | What it means | Use when |
|---|---|---|
| **Reference in place** | The platform reads the data where it lives | The source uses an open format and performance is fine |
| **Replicate** | A continuously updated copy is kept in sync | The source is an operational database you mustn't load heavily, or uses a proprietary format |
| **Copy (batch)** | A scheduled job copies and transforms data | You need heavy cleaning or reshaping |

### Layers: raw, clean, ready

Most teams organise data in three layers, often called **bronze, silver and gold** (the "medallion" pattern). Bronze is raw, as received. Silver is cleaned and conformed. Gold is modelled for a specific use, such as a report or an AI agent. The value of the layers is that you can always trace an answer back to the raw data.

### Modelling for questions

- A **star schema** (one table of events or transactions surrounded by descriptive tables such as customer, product and date) is still the most reliable shape for analytics and for AI agents that query data.
- **Slowly changing dimensions:** decide whether history matters. If a customer moves region, should old sales count under the old region or the new one?

### Unstructured data for AI

- **Extraction:** text from PDFs, scans (optical character recognition), tables and images. Layout matters: a table split into loose words is useless.
- **Chunking:** split documents into passages that make sense alone. Keep the title and headings with each chunk.
- **Metadata:** source, date, owner and permission information on every chunk, so search can filter and trim results.

### Quality and freshness

Measure quality along a few simple dimensions: complete, accurate, consistent, current and unique. Write automated checks for the ones that matter to the use case, and alert when they fail.

## On Microsoft

| Concept | Microsoft tool | Key facts | More |
|---|---|---|---|
| Reference vs replicate | **OneLake shortcuts vs mirroring** (Microsoft Fabric) | Shortcuts reference data in place and need open formats; mirroring brings in a whole database or catalog. For proprietary formats, mirroring is the only option ([Learn](https://learn.microsoft.com/en-us/fabric/onelake/unify-data)) | [Phase 1](../microsoft-technical-reference.md#phase-1-data-engineering-on-microsoft-fabric) |
| Deployment from code | **`fabric-cicd`** | ⚠️ `token_credential` is now required; the default-credential fallback was removed ([docs](https://microsoft.github.io/fabric-cicd/1.3.0/how_to/getting_started/)) | [Phase 1](../microsoft-technical-reference.md#phase-1-data-engineering-on-microsoft-fabric) |
| Questions over business data | **Fabric data agents** | Generally available; need F2 capacity or higher and run under the user's own identity and data permissions ([Learn](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent)) | [Phase 4](../microsoft-technical-reference.md#copilot-studio--m365-copilot-extensibility) |
| Document knowledge | **Foundry IQ** (built on Azure AI Search) | Permission-aware knowledge bases ([Learn](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)); layout-aware ingestion is in preview ([Foundry IQ blog](https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/)) | [RAG blueprint](../microsoft-technical-reference.md#enterprise-rag-blueprint-azure) |
| Sensitivity | **Microsoft Purview** | Sensitivity labels and data-loss prevention; the oversharing assessment checks the top 100 SharePoint sites by usage weekly ([Learn](https://learn.microsoft.com/en-us/purview/dspm-for-ai)) | [Phase 3](../microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents) |

💬 Our default for a Fabric engagement: mirror operational databases into bronze, clean in silver with notebooks, model gold as a star schema, and point the data agent only at gold.

## Mistakes we keep seeing 💬

- Indexing a whole SharePoint estate "to see what happens", then discovering the AI happily quotes HR files to everyone. Oversharing is the default state of most file systems.
- Copying everything into a new store "for performance" without a refresh plan. Within a month the AI is answering from stale data.
- Pointing an AI agent at raw tables with cryptic column names and expecting good answers.
- Testing only with an administrator account, which can see everything.

## Prove it

| Level | Project |
|---|---|
| Beginner | Load a public dataset, clean it with SQL, and write five automated quality checks |
| Intermediate | Build bronze, silver and gold layers with a slowly changing dimension, and a report on gold |
| Advanced | Index 500 mixed documents (PDFs, scans, slides) with permission metadata, and prove a low-privilege user can't retrieve restricted content |

## Interview questions

1. When would you replicate a source instead of reading it in place?
2. A user says the AI's numbers don't match their report. How do you investigate?
3. How do you make sure an AI assistant respects document permissions?
4. How would you chunk a 200-page policy manual with tables?

## Skills for this pillar

[`data-audit`](../../skills/data-audit/SKILL.md) · [`ai-use-case-canvas`](../../skills/ai-use-case-canvas/SKILL.md) · [Data and analytics agent pack](../../skills/scenario-data-agent/SKILL.md)

---

← [Pillar 1: Software engineering](01-software-engineering.md) · Next: [Pillar 3: Cloud and networking](03-cloud-and-networking.md) →
