# Skill evaluations

> Part of the [Awesome Microsoft FDE](../README.md) guide. The skills are meant to be handed to AI agents, so we test them the way the guide tells you to test an agent: a fixed set of cases, a bar, and a run on every change.

**If you can't measure it, you can't ship it.** That applies to this repository too. A skill whose output drifts, or that an agent can't follow without inventing facts, is a broken skill even if it reads well.

## How it works

Each case in [`cases.json`](cases.json) pairs a skill with:

- **A task:** one line saying what to produce and when in the engagement.
- **The brief:** always the [Harbourline fact sheet](../examples/README.md#the-fact-sheet), so every case has the same, complete facts.
- **A reference answer:** the worked example for that skill, in [`examples/knowledge-assistant/`](../examples/knowledge-assistant/).
- **Must-include content:** facts from the brief that any correct output has to carry, such as the named owner or the release bar.

There are two levels of grading.

| Level | What it checks | How it runs |
|---|---|---|
| 1. Structure | Every required template section is present, no `<placeholder>` is left, and the must-include facts appear | [`scripts/grade_skill_output.py`](../scripts/grade_skill_output.py); automatic, deterministic |
| 2. Judgement | Is it specific, testable, consistent with the brief and free of invented product facts? | A person or an LLM judge, using the [rubric](#judgement-rubric) below and the reference answer |

On every pull request, CI grades the **reference answers** against their own skills at level 1. That catches a template change that silently breaks the examples, and an example that drifts from its template. When you change a skill's template, update its example in the same pull request.

## Run a skill through an agent

1. Give your agent the skill's `SKILL.md`, the fact sheet section of [`examples/README.md`](../examples/README.md#the-fact-sheet) and the case's `task`. Tell it to write the output to a file and not to look at `examples/`.
2. Grade the structure:

   ```bash
   python scripts/grade_skill_output.py eval-plan path/to/output.md
   ```

3. Grade the judgement with the rubric, comparing against the reference answer. An LLM judge works: give it the rubric, the brief, the reference and the output, and ask for a score per question with one line of evidence each.
4. If the output fails because the skill was unclear, fix the skill, not the case. Record what you changed in the [changelog](../CHANGELOG.md).

Run every case before a release, with at least one agent. 💬 Two different agents is better: a skill that only works with one tool isn't portable, and portability is the point of the format.

## Judgement rubric

Score each question 0 (no), 1 (partly) or 2 (yes). The bar for a skill is an average of 1.5 or more across its cases, and no 0 on questions 4 or 5.

1. **Specific.** Does it talk about this customer's systems, people and numbers, or could it be pasted into any engagement?
2. **Testable.** Does each control, defence or claim say how it's tested or measured?
3. **Owned.** Does every action, risk acceptance and decision have a named person?
4. **Consistent.** Does it agree with the brief and with the other documents it references (ADR numbers, weeks, measures)?
5. **Honest.** Does it avoid inventing product facts, prices or dates, and mark opinion and assumptions as such?
6. **Right-sized.** Did it delete what doesn't apply instead of padding it?

## Add a case

Add an entry to [`cases.json`](cases.json) with `skill`, `reference`, `task` and `must_include`. Use `optional_sections` for template sections the reference rightly left out. Keep `must_include` to facts the brief makes unavoidable; a phrase list that rewards copying the reference teaches agents nothing.
