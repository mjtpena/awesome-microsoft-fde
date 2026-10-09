# Instructions for AI Coding Assistants: Harbourline Policy Assistant

> **Worked example.** A filled-in [`agent-instructions`](../../skills/agent-instructions/SKILL.md) file for a fictional engagement; see [examples](../README.md). Everything below, including names, paths and pull request numbers, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**What this is:** `AGENTS.md` at the root of Harbourline's `policy-assistant` repository in Azure DevOps. The repository had no instructions file, so the FDEs created this one in week 4. AI coding assistants were allowed by R. Okafor in week 1, with no production data in prompts ([access request](access-request.md)). The platform team uses GitHub Copilot in VS Code and the FDEs use Claude Code. Claude Code reads `CLAUDE.md` rather than `AGENTS.md` when both exist, so `CLAUDE.md` holds one line, `@AGENTS.md`, and no rules of its own ([technical reference](../../docs/microsoft-technical-reference.md#phase-7-fde-developer-toolchain-mcp-copilot-cloud-agent-azd)).

Everything below the line is the file as merged.

---

```markdown
# Instructions for AI Coding Assistants

These rules apply to every AI coding assistant working in this repository. Customer rules take precedence over everything below.

## Customer rules (Harbourline platform team)

- Language and framework: Python 3.12 for the agent definition, ingestion and evaluation; Bicep for infrastructure. Nothing else without the platform team's agreement.
- Style and linting: `ruff check` and `ruff format` (config in `pyproject.toml`); the Bicep linter with `bicepconfig.json`. Both run in CI and must pass.
- Tests: `pytest`. New Python code comes with tests in `tests/`, next to the module it tests.
- Branching and review: branch from `main`, pull request into `main`. One approval from S. Adeyemi's team is required; production deployments are approved by S. Adeyemi. Required checks: lint, unit tests, Bicep what-if, and the 30-case evaluation subset.
- Pipelines: Azure DevOps YAML in `pipelines/`. Don't add a new pipeline without asking the platform team.
- Forbidden:
  - No new Python packages without approval from the platform team in the pull request. Pin every version in `requirements.txt`.
  - No production data in prompts to any AI assistant, in test fixtures or in the golden set. Use the synthetic policies in `tests/fixtures/`.
  - No API keys or connection strings anywhere. Keys are disabled on the Foundry account; use Entra sign-in.
  - No changes made by hand in the Azure portal. If something can only be done in the portal, write it in the runbook and tell S. Adeyemi.

## Decisions from ADRs

| Area | Decision | ADR |
|---|---|---|
| Agent platform | Foundry prompt agent behind the shared APIM gateway; not Copilot Studio | `docs/adr/ADR-001-foundry-prompt-agent.md` |
| Knowledge layer | Foundry IQ knowledge base on Azure AI Search. Don't write chunking, embedding or vector code | `docs/adr/ADR-002-foundry-iq.md` |
| What gets indexed | Current version of each policy only. File-share copies that duplicate a SharePoint document are excluded unless on `ingestion/fileshare-allowlist.csv` (amended week 6) | `docs/adr/ADR-003-current-version-only.md` |
| Agent tools | Read-only. The agent has one tool, the knowledge-base query. **Don't add a tool that writes, sends or changes anything**; that needs a new ADR | `docs/adr/ADR-004-read-only.md` |
| Indexer permissions | Site-scoped read on the three SharePoint sites and the file share's `published` folder; never tenant-wide | `docs/adr/ADR-005-site-scoped-indexer.md` |
| Channel and network | Teams over the source-IP-filtered public route; everything else private | `docs/adr/ADR-006-teams-public-route.md` |
| Infrastructure-as-code tool | Bicep, Azure Verified Modules where one exists (platform team standard, recorded in ADR-001) | ADR-001 |
| Identity model | Agent has its own Entra Agent ID; callers use the Foundry Agent Consumer role; keyless only | ADR-001; `docs/security/threat-model.md` |

## Engagement conventions (agreed in pull request !14)

- Small pull requests. Each says what changed, how it was tested and which ADR it relates to.
- For any change touching more than five files, write a short plan in the pull request description before the code.
- Never commit secrets, keys, connection strings or customer data.
- Mark any dependency on a preview feature with a `PREVIEW:` comment and a link to its documentation. There are none in the request path today; keep it that way unless an ADR says otherwise.
- Reference built-in roles by ID, not name, in Bicep: Foundry role names have changed before.
- Emit OpenTelemetry traces for every request, model call and knowledge-base query, including the retrieved document IDs. The runbook's "reconstruct a request" steps depend on them.
- Don't change the agent's instructions, the knowledge-base configuration or ingestion rules without running the full evaluation (`docs/quality/eval-plan.md`) and pasting the result into the pull request.
- Never read from or write to production data stores from local development. Use the test environment.
- AI coding assistants get no Azure role in production. In test, Reader only.

<!-- Removed in review of !14: the HVE Core Research → Plan → Implement → Review flow (the platform team prefers its
     own plan-in-the-PR habit) and the rule that every tool has typed inputs (doesn't apply: one read-only tool). -->

## Knowledge assistant rules

- Retrieval passes the asking user's identity through so results are permission-trimmed. Never query the index as the agent's own identity on a user's behalf. Every change to retrieval code includes a test run as the low-privilege user `svc-eval-lowpriv`.
- The low-privilege pricing suite (`eval/pricing-lowpriv.jsonl`, 25 questions) must return zero Pricing-site documents. A change that makes it fail doesn't merge, whatever else it fixes.
- Every non-refusal answer includes the source title, version, effective-from date and link in the text, because Teams doesn't show structured citations for this agent (ADR-006). Don't remove or reformat this without updating the evaluation rubric.
- Changes to `ingestion/` must keep `scripts/check_duplicate_versions.py` passing at zero. Never edit `ingestion/fileshare-allowlist.csv`: only A. Novak's team changes it.
- A re-index is a release. Don't add code or pipeline steps that re-index production without the test-first gate in the runbook.
- New golden-set cases go in `eval/golden-set.jsonl` through a pull request that M. Costa or A. Novak approves. Don't generate expected answers with an AI assistant: the subject-matter experts write them.
```

---

**What happened in review.** S. Adeyemi's team accepted nine of the eleven proposals in pull request !14 and rejected two, recorded in the comment so nobody proposes them again. The "A re-index is a release" line was added in week 6 after the [incident review](incident-review.md), in a separate pull request, alongside the [ADR-003](adr-003-current-version-only.md) amendment. The links to [eval-plan.md](eval-plan.md) and [runbook.md](runbook.md) are what the rules point at.
