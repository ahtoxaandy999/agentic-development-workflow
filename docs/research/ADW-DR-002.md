---
id: DR-002
artifact_status: draft
authority: evidence
owner: agentic-development-research
question: >
  Which tool-agnostic practitioner workflow patterns for question
  clarification, specification, decomposition, vertical slicing, review,
  documentation, context transitions, and qualitative proportionality should
  constrain Workflow v1?
scope: tool-agnostic-practitioner-workflow-formation-and-decomposition-evidence
decision_consumer: >
  Separate coordinator DR-002 recommendation-disposition decision feeding the
  Workflow v1 design gate.
repository: ahtoxaandy999/agentic-development-workflow
repository_state_at_authorization: "main@7d573ed97e16fe56b43a98ccaed93bb4764627e5; verified 2026-09-03"
research_gate_ref: ADW-DR-002-GATE-001
supersedes: null
---

# DR-002: Practitioner workflow formation and decomposition evidence

## Status and authority

This file is the durable draft research contract for DR-002.

The researcher owns evidence production only.

The researcher may not:

- source-review or adopt their own conclusions;
- design or adopt Workflow v1;
- modify normative artifacts;
- select tooling;
- accept a candidate;
- expand this research scope without a new coordinator gate.

Mutable research state belongs to the Research Register.

## Canonical question

Which tool-agnostic practitioner workflow patterns for question clarification,
specification, decomposition, vertical slicing, review, documentation, context
transitions, and qualitative proportionality should constrain Workflow v1?

## Decision consumer

A later separate coordinator DR-002 recommendation-disposition decision.

Only a durable coordinator disposition may feed DR-002 conclusions into the
Workflow v1 design gate.

Research completion and source review do not adopt recommendations.

## Scope

Investigate evidence concerning:

1. Question clarification and convergence before specification.
2. How intent, constraints, assumptions, non-goals, and acceptance conditions
   become sufficiently explicit.
3. Decomposition into independently understandable and verifiable units.
4. Vertical slicing across behavior, integration, and validation boundaries.
5. Dependency discovery, ordering, integration, and recomposition.
6. Review timing, feedback loops, correction, and verification practices.
7. Durable documentation versus ephemeral working context.
8. Context transitions and fresh-agent handoffs.
9. Qualitative proportionality using context, consequence, uncertainty,
   reversibility, and blast radius without presupposing a scoring model.
10. Failure modes, counterexamples, costs, limitations, and conditions under
    which a pattern should not be used.
11. Candidate tool-agnostic constraints and unresolved questions for later
    Workflow v1 design.

## Non-scope

DR-002 must not:

- design, specify, or adopt Workflow v1;
- define concrete lifecycle sequencing or gate mechanics;
- create a task, review, packet, or state schema;
- choose a tracker, storage model, synchronization mechanism, App, MCP server,
  skill, hook, automation, or other tool;
- prescribe a parallel-wave or worktree algorithm;
- research bounded autonomy and execution controls assigned to DR-003 except
  to record interface dependencies;
- adopt quantitative thresholds or claim a universal small-task rule;
- conduct post-v1 ceremony-cost optimization;
- reopen DR-001 conclusions without new contradictory evidence;
- change normative or live repository state.

## Contracted subquestions

The report must answer, or record an explicit evidence gap for:

1. What information must be clarified before useful specification can begin?
2. What makes a specification sufficiently actionable without requiring
   universal heavyweight ceremony?
3. What characteristics make decomposition coherent, independently
   reviewable, and recomposable?
4. What distinguishes a useful vertical slice from a merely horizontal
   activity split?
5. How should dependencies, integration points, and verification boundaries
   influence decomposition?
6. Where do review and correction provide value during formation and
   execution?
7. Which decisions and context need durable documentation, and which may
   remain ephemeral?
8. What makes a context transition usable by a fresh practitioner or agent?
9. How should qualitative proportionality alter depth or ceremony?
10. What recurring failure modes, tensions, and tradeoffs limit the candidate
    patterns?
11. Which conclusions are evidence-backed constraints, and which remain
    design-time choices or DR-003 dependencies?

No answer is presupposed.

## Source hierarchy

Apply the Research Evidence Policy independently:

1. Live repository state and exact repository artifacts.
2. Official vendor or platform documentation when platform behavior is
   claimed.
3. Current primary repositories, standards, specifications, and research
   papers.
4. First-party case studies with context and limitations.
5. Documented practitioner evidence.
6. Secondary material only for discovery or explicitly qualified context.

Original practitioner material, including Family A material deferred by
DR-001, is direct evidence of what its author recommends. It is not by itself
proof of effectiveness or general applicability.

Generalized load-bearing claims require suitable primary or corroborating
evidence. Otherwise narrow and label them.

There is no source-count quota.

## Required evidence and output

The researcher must:

- inspect the Charter, Research Evidence Policy, current Register, and exact
  current repository state through GitHub;
- consume DR-001 through its accepted disposition, qualifications, deferred
  matters, and recorded source-review finding;
- preserve DR-001 distinctions among evidence, disposition, authorization,
  verification, review, candidate identity, and acceptance;
- maintain a source register recording identity, author, date/version, access
  date, supported claims, scope, and limitations;
- provide a coverage matrix for every contracted subquestion;
- distinguish evidence describing a practice from evidence supporting its
  effectiveness;
- compare credible alternatives and tensions rather than present one
  practitioner's method as universal;
- record negative evidence, counterexamples, costs, applicability conditions,
  and confidence;
- separate facts, inferences, recommendations, and unresolved questions;
- map every recommendation to supporting evidence, tradeoffs, and limiting
  conditions;
- state which matters remain unresolved for Workflow v1 design or DR-003.

## Contradictions and missing evidence

For each credible conflict record:

- both claims;
- authority;
- date/version;
- scope;
- configuration where applicable;
- the precise contradiction.

Do not average incompatible claims.

Distinguish:

- contrary evidence;
- absence of evidence;
- unavailable evidence;
- stale evidence;
- configuration-dependent evidence.

Missing decisive evidence must narrow or block the affected recommendation and
state what would resolve it.

A contradiction with the Charter, Research Evidence Policy, Research Register,
or accepted DR-001 disposition stops the affected conclusion and requires a
separate coordinator decision.

A material contradiction with DR-003 must be carried to the later join rather
than silently resolved.

## Stop boundary

Evidence production is complete only when:

- every contracted subquestion has supported findings or an explicit evidence
  gap;
- citations and source register are complete;
- alternatives, contradictions, negative evidence, assumptions, uncertainty,
  limitations, and deferrals are explicit;
- recommendations remain tool-agnostic and within scope;
- live GitHub evidence has been reverified;
- no substantive research edit remains planned.

Stop earlier for:

- stale or unverifiable repository state;
- authority conflict;
- unsafe evidence handling;
- scope expansion;
- a load-bearing dependency on deferred research.

Do not proceed into:

- source review;
- coordinator disposition;
- normative materialization;
- Workflow v1 design;
- tooling selection.

## Freeze and source review

While in progress:

artifact_status: draft

Publication-only metadata remains absent.

At freeze add:

research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: <actual final evidence-verification date>
repository_state: "main@<full SHA verified at freeze>; accepted baseline 13b05e075ec04aa91494cd18f7d29f7249028cb5"

Then serialize the exact complete UTF-8 bytes without normalization and
calculate:

- SHA-256;
- exact byte length;
- actual final-newline state.

Review identity:

DR-002@sha256:<lowercase-64-hex-digest>

Any byte change creates a different target.

A substantive post-review change requires a new frozen identity and fresh
independent source review.

The independent reviewer must verify:

- exact identity;
- scope compliance;
- complete contracted-question coverage;
- claim support;
- primary-source preference;
- freshness;
- practitioner-evidence limitations;
- contradictions and negative evidence;
- fact/inference/recommendation separation;
- DR-001 boundary preservation;
- sensitive-information handling;
- evidence-to-recommendation reasoning.

Source review establishes evidence quality only.

## Preserved boundaries

Workflow v1 remains unadopted.

DR-003 remains an independent parallel research task.

Tooling, tracker, schemas, orchestration, and implementation remain outside
DR-002.
