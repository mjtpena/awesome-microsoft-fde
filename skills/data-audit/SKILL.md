---
name: data-audit
description: "Audit every data source an AI solution depends on: system, format, volume, freshness, owner, access path, quality, sensitivity, permissions and the ingestion decision per source. Use in week one, before promising any answer quality; critical for knowledge assistants and data agents."
---

# Data Audit

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 2 Understand · **Pillar:** [2 Data](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/02-data.md)

A sheet that proves you know where the data is, how good it is, who can see it and how you'll get it.

## When to use

- Week one, before promising any answer quality.
- When a new source is added to scope.

## Rules

- Test every access path with a **real, low-privilege account**, not an administrator.
- Decide per source whether to reference data in place, replicate it or batch-copy it, and why.
- Write down how each source's permissions will be respected by the AI, and test it.

## Steps

1. Write the [template](#template) to `docs/engagement/data-audit.md` in the customer's repository.
2. List every source in the sources table, then make one ingestion decision per source.
3. Fill the scenario section that applies (documents for a knowledge assistant, business data for a data agent) and delete the others.
4. Finish with the top five data risks; carry them into the [threat model](../threat-model/SKILL.md) and the weekly status.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. **Critical** in: [knowledge assistant](../scenario-knowledge-assistant/SKILL.md), [data agent](../scenario-data-agent/SKILL.md). Those packs say what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Data Audit: <Customer> / <Domain>

## Sources

| Source | System | Structured / documents | Format (open / proprietary) | Volume | How fresh it must be | Owner | Access path | Quality issues | Sensitivity |
|---|---|---|---|---|---|---|---|---|---|

## Ingestion decision per source

| Source | Reference in place / Replicate / Batch copy | Why | Refresh schedule |
|---|---|---|---|

<!-- Microsoft: OneLake shortcuts reference open formats in place; mirroring adds a whole database or catalog,
     and is the only option for proprietary formats.
     Ref: https://learn.microsoft.com/en-us/fabric/onelake/unify-data -->

## Permissions

| Source | How permissions work today | Will the AI respect them? How? | Tested with a low-privilege user? |
|---|---|---|---|

## Quality checks

| Dataset | Check (complete / accurate / consistent / current / unique) | Rule | Current result | Automated? |
|---|---|---|---|---|

## Scenario sections

### Knowledge assistant: documents

| Collection | Doc types (PDF, scan, slides, web) | Count | Tables or images that matter? | Source of truth? | Out-of-date content? | Oversharing found? |
|---|---|---|---|---|---|---|

- Chunking approach:
- Metadata kept on each chunk (title, date, owner, permissions):

### Data agent: business data

| Question users ask | Tables needed | Trusted report it must match | Metric definition agreed by |
|---|---|---|---|

- Layer the agent will query (gold only, in our view):
- Disputed metric definitions:

### Regulated / disconnected

- Data that mustn't leave the country, region or site:
- Where indexes, logs and embeddings will be stored:

## Top five data risks

1.
2.
3.
4.
5.
````
