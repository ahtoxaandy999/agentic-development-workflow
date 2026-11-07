# Decisions

Agents decide most things themselves and write the reason down. The owner
decides what only the owner can: product, money, trust, taste and anything
public or irreversible.

## Owner-class or minor

Split every open point of a new task before planning.

**Owner-class** (ask the owner):

- a product, visual or wording choice with more than one reasonable answer;
- a rule, spec value, format or interface change beyond the plan item;
- spend, a new runtime dependency, an external service or a paid tool;
- a release, deploy, publication, or anything irreversible;
- a security finding at P1;
- a step only the owner can take (a password, a dashboard, a signature).

**Minor** (the agent decides, with a one-line reason in the brief or change
description):

- ordering inside approved priorities;
- implementation inside an approved spec or design;
- process, tests, tooling and docs that change no rule;
- flaky checks, and wording forced by a check.

Nobody downgrades an owner-class point. The only way out is a reference to
an existing decision file that already covers it. The project profile may add
items to either list.

## Asking

- Answer first what the repository answers: specs, plan, decision log, code.
  Never ask what is derivable or already decided.
- Ask in `<owner language>`, with `<question tool>`, at most four questions
  per round, each with two to four concrete options, the recommended one
  first with its trade-off in one line.
- Batch questions. Keep working on everything they do not block.
- Owner away: park the questions in the plan file's **Owner questions**
  table and take the next ready item. Never guess an owner-class answer.
- Confirm a 5-10 line brief before a large task: goal, scope in and out,
  acceptance, decisions taken, assumptions, deferred items.

Agents started by another agent never ask the owner; they return their
questions to the session that started them.

## The decision log

Durable decisions (rules, formats, interfaces, architecture, look, process)
get one file each in `<decision dir>`:

```markdown
# <YYYY-MM-DD> - <title>

Status: accepted | superseded by <file>
Context: why a decision was needed (2-4 lines).
Decision: what was decided, precisely enough to check.
Consequences: what changes, what is now forbidden or required.
Source: the owner answer, review or evidence it rests on.
```

- One file per decision; an index, if any, is generated, not hand-edited.
- A decision is never edited after acceptance. A successor names what it
  supersedes, and the old file only gets its `Status` line changed.
- The decision and the change that applies it land together.

## Evidence is not policy

Research, benchmarks, reviews and tool output are evidence. They change a
rule only through a decision that names the rule, the target file and the
scope. Publishing a finding never changes a rule by itself.
