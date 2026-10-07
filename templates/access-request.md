# Access Request: <Customer> / <Engagement>

> **Step:** 1 Get access · **Pillars:** 3 Cloud and networking, 4 Security and identity · **Scenarios:** all (critical for regulated and disconnected)
>
> **How to use:** send this on day one, as one document, to one named person at the customer. Access delays are the most common reason engagements slip. Every row has an owner and a date.

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
