# Data Audit: <Customer> / <Domain>

> **Step:** 2 Understand · **Pillar:** 2 Data · **Scenarios:** all (critical for knowledge assistant and data agent)
>
> **How to use:** complete in week one, before promising any answer quality. Test every access path with a real, low-privilege account, not an administrator.

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
