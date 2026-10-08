---
name: access-request
description: "Draft a single day-one access request listing every account, cloud role, network path, dataset, licence and repository permission an FDE needs at a customer, each with an approver and status. Use at the start of an engagement or when access is blocking work."
---

# Access Request

> Part of the [skills](../README.md) in the [Awesome Microsoft FDE](../../README.md) guide. **Step:** 1 Get access · **Pillars:** [3 Cloud and networking](../../docs/pillars/03-cloud-and-networking.md), [4 Security and identity](../../docs/pillars/04-security-and-identity.md)

One document, sent on day one to one named person, that lists everything you need access to. Access delays are the most common reason engagements slip.

## When to use

- Day one of any engagement, before you write code.
- Whenever a new system, dataset or environment comes into scope.
- Weekly, to update the blocked-items table and escalate.

## Rules

- Send it as **one document to one named person** at the customer, not a trickle of emails.
- Every row has an owner and a date.
- Ask for **least-privilege, time-limited** roles and say so in the request. Security teams approve faster when you ask for less.
- Never ask for secrets for the solution's own identity: request a managed identity or agent identity.

## Steps

1. Write the [template](#template) to `docs/engagement/access-request.md` in the customer's repository.
2. Ask for the customer, engagement name, named customer contact and the date access is needed by.
3. Fill each table from what you know about the architecture; mark unknowns as questions rather than guessing.
4. Add the regulated or disconnected add-ons if they apply; delete the ones that don't.
5. List anything already blocked in the last table, with the date it became blocked.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. **Critical** in: [regulated, private-only](../scenario-regulated-private/SKILL.md), [disconnected or sovereign](../scenario-disconnected-sovereign/SKILL.md). Those packs say what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Access Request: <Customer> / <Engagement>

**Requested by:** · **Customer contact:** · **Date sent:** · **Needed by:**

## People and accounts

| Who | Account needed | Why | Approver | Status | Date granted |
|---|---|---|---|---|---|
| FDE 1 | Guest / corporate account in the customer's directory | Sign in to customer systems | | Requested | |
| FDE 1 | Device / VPN / virtual desktop | Network access | | | |

## Cloud permissions

| Scope (subscription / resource group / workspace) | Role | Time-limited? | Why | Approver | Status |
|---|---|---|---|---|---|
| Dev subscription | Contributor | | Build and deploy | | |
| Prod subscription | Reader | | Diagnose only | | |

💬 Ask for **least privilege, time-limited** roles (for example via just-in-time elevation) and say so in the request. Security teams approve faster when you ask for less.

## Identity for the solution

| Item | Detail | Approver | Status |
|---|---|---|---|
| Agent / app identity | Managed identity or agent identity; no secrets | | |
| Permission consent | Which APIs (for example Microsoft Graph scopes) and why | Tenant admin | |
| Can we create app registrations or agent identities? | Yes / no / via request process | | |

## Network

| Path | From → to | Private or public | Firewall rule / private endpoint needed | Approver | Status |
|---|---|---|---|---|---|
| | | | | | |

## Data

| Dataset / system | Access level | Contains sensitive data? | Approver (data owner) | Status |
|---|---|---|---|---|
| | Read-only | | | |

## Code and delivery

| Item | Detail | Status |
|---|---|---|
| Repository | Where the code lives; who reviews and merges | |
| Pipelines | Can we run deployments? Which environments? | |
| Work tracking | Backlog tool and project | |
| AI coding assistants | Are they allowed in this repository? Any restrictions? | |

## Licences and capacity

| Item | Needed for | Owner | Status |
|---|---|---|---|
| | | | |

<!-- Microsoft examples: Fabric capacity (F2+ for data agents), Copilot Studio capacity/credits, Microsoft 365 Copilot,
     Agent 365 (needed for Defender coverage of Foundry/Copilot Studio agents since 1 Jul 2026),
     E5 / E5 Compliance for Purview AI posture features. See docs/pillars/04-security-and-identity.md -->

## Scenario add-ons

- **Regulated:** security clearance or vetting for each FDE; data-handling agreement; approved device list; where logs may be stored.
- **Disconnected:** physical site access; how software and models are transferred in (approved media, scanning); local directory accounts; who can approve updates.

## Blocked items (escalate weekly)

| Item | Blocked since | Impact | Escalated to |
|---|---|---|---|
````
