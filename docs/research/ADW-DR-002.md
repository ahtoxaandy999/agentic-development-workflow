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

# DR-002 evidence packet

## Status and boundary

- **Artifact:** DR-002 working evidence packet
- **Authority:** evidence only
- **Lifecycle:** draft; Research Register remains `in-progress`
- **Decision consumer:** later, separate coordinator DR-002 recommendation-disposition
- **Repository:** `ahtoxaandy999/agentic-development-workflow`
- **Verified repository state:** `main@79f5541113e7dfeedfde6f36f371031f3f3330fa`
- **External-source access date:** 2026-09-03
- **Recommendation status:** proposed only

Evidence content is complete at the authorized production boundary. No publication metadata, exact-byte digest, freeze, source review, coordinator disposition, normative materialization, Workflow v1 design, or tooling selection was performed.

## Executive evidence verdict

The evidence supports nine tool-agnostic candidate constraints:

1. Begin specification only after the intended outcome, stakeholders, authority, constraints, assumptions, exclusions, interfaces, material unknowns, and observable acceptance conditions are sufficiently clear for the next bounded action.
2. Treat specification sufficiency as a readiness condition, not a mandatory document size or one-time complete-up-front event.
3. Decompose work into coherent units that remain traceable to an outcome, have bounded interfaces, expose dependencies, and can be understood and verified without inventing material intent.
4. Prefer vertical slices when behavioral or user feedback is the objective, but allow explicit enabling work where an independently valuable slice is not technically or economically coherent.
5. Define integration and recomposition while decomposing, rather than postponing them until isolated parts are complete.
6. Place different feedback mechanisms where they answer different questions: formation review, rapid verification during execution, peer review with adequate context, integration validation, and outcome review.
7. Preserve durable information when downstream reliance, authority, audit, recovery, or cross-session coordination depends on it; allow disposable working detail to remain ephemeral.
8. Make context transitions self-sufficient for a fresh practitioner while keeping handoffs non-authoritative unless promoted into the applicable owner.
9. Tailor depth and ceremony qualitatively using context, consequence, uncertainty, reversibility, and affected scope, without a universal score or “small task” rule.

Support is strongest for requirements clarity and verifiability, explicit interfaces and integration, review-context needs, the costs of reconstructing interrupted work, and risk-based tailoring. Support is moderate for small independently testable batches and frequent integration. Direct comparative evidence that vertical slicing is universally superior is insufficient; that recommendation is therefore conditional.

## Preserved DR-001 boundary

The accepted DR-001 disposition requires DR-002 to preserve:

- separate meanings for evidence, disposition, authorization, candidate identity, verification, review, and acceptance;
- one current owner for mutable authoritative state within this control plane;
- durable records for material decisions where downstream reliance warrants them, but not every working note;
- tailoring by documented context and risk rather than task size alone;
- self-sufficient content for consequential fresh-agent work without adopting a fixed packet schema;
- chat, memory, local worktrees, and handoffs as working or navigation state unless explicitly promoted.

Those constraints are recorded in the [Research Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/research-register.md). DR-001’s source review accepted evidence quality for the exact target `DR-001@sha256:825204b8c45da36c4c7cd087d572e0b014352aee7a6fe1c54e0772aaec6acf0f`, with one non-blocking minor finding concerning its outdated NIST SP 800-53 release label. This packet does not rely on that stale release label and preserves the finding without modifying the frozen report. See the [DR-001 report](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001.md) and [source-review record](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001-SOURCE-REVIEW-001.md).

## Findings by contracted subquestion

### 1. Information required before useful specification

**Facts.** NASA’s requirements process begins with agreed stakeholder needs, goals, objectives, assumptions, constraints, external interfaces, operational scenarios, and effectiveness measures. It warns that written requirements alone do not establish shared understanding and requires iterative stakeholder communication. [NASA Systems Engineering Handbook, Rev. 2](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf)

Cucumber’s Example Mapping makes rules, examples, assumptions, unanswered questions, and newly discovered out-of-scope stories visible before development. [Cucumber Example Mapping](https://cucumber.io/docs/bdd/example-mapping/)

**Inference.** Before useful specification, the next bounded action should have:

- intended outcome and beneficiary;
- relevant authority and current baseline;
- scope and non-goals;
- binding constraints;
- material assumptions and unknowns;
- behavioral examples or scenarios;
- interfaces and known dependencies;
- observable acceptance conditions.

Every possible detail need not be known. A material unanswered question must either be resolved, converted into a bounded learning activity, or recorded as limiting/blocking the affected work.

**Confidence:** high for the categories; medium for their universal minimum.

### 2. Actionable specification without universal heavyweight ceremony

**Facts.** NASA describes good requirements as clear, correct, feasible, unambiguous, singular, traceable, and verifiable, with explicit assumptions and interfaces. The Scrum Guide instead treats refinement as ongoing and domain-dependent; work becomes selectable after acquiring enough transparency, and the execution plan remains updateable as learning occurs. [NASA requirements checklist](https://www.nasa.gov/reference/system-engineering-handbook-appendix/), [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html?from=hub)

Bill Wake describes stories as conversation-and-confirmation devices rather than complete specifications and later cautions that INVEST is only a small diagnostic, not a complete method. [INVEST, 2003](https://xp123.com/invest-in-good-stories-and-smart-tasks/), [Wake’s 2021 qualification](https://xp123.com/all-you-need-is-invest-no/)

**Inference.** A specification is actionable when a fresh, qualified executor can proceed without inventing material intent and a verifier can determine whether the outcome satisfies the stated conditions. The required detail varies with consequence, uncertainty, coupling, and the cost of correction. Actionability does not imply exhaustive up-front design.

**Confidence:** high.

### 3. Coherent, reviewable, recomposable decomposition

**Facts.** NASA logical decomposition examines functions, behavior, time, data flow, states, modes, architecture, and interfaces to understand interactions. Wake’s INVEST model favors independent, valuable, small, and testable stories while acknowledging that full independence is not always possible. Scrum requires increments to be usable, verified, additive, and able to work with prior increments. [NASA system design processes](https://www.nasa.gov/reference/4-0-system-design-processes/), [INVEST](https://xp123.com/invest-in-good-stories-and-smart-tasks/), [Scrum Guide](https://scrumguides.org/scrum-guide.html?from=hub)

**Inference.** A useful unit:

- advances a traceable outcome or an explicitly justified enabling dependency;
- has one intelligible responsibility;
- declares inputs, outputs, interfaces, and preconditions;
- can be verified at its stated boundary;
- minimizes—but need not eliminate—coupling;
- has an explicit path for integration with the whole;
- is small enough to review and correct before its context becomes stale.

“Independent” means independently understandable and schedulable where practicable, not isolated from all system dependencies.

**Confidence:** high for coherence and verification; medium for preferred unit size.

### 4. Vertical slice versus horizontal activity split

**Facts.** Wake’s original vertical-cake metaphor recommends slicing through presentation, logic, persistence, and other necessary layers so that each story provides customer-visible value. Cockburn’s Elephant Carpaccio exercise similarly requires demonstrable real input and output and rejects UI-only or data-structure-only slices. Scrum defines an increment as usable rather than merely partially constructed. [Wake](https://xp123.com/invest-in-good-stories-and-smart-tasks/), [Cockburn exercise](https://alistair.cockburn.us/wp-content/uploads/2018/02/Elephant-Carpaccio-exercise-instructions.pdf), [Scrum Guide](https://scrumguides.org/scrum-guide.html?from=hub)

**Inference.**

- A **vertical slice** traverses the boundaries necessary to produce an observable behavior, usable capability, or valid learning result and includes its verification.
- A **horizontal split** partitions work by layer or activity—such as database, API, UI, documentation, or testing—without a standalone behavioral result.

A vertical slice need not contain every production concern, be independently deployable, or expose a graphical interface. It must provide a meaningful end-to-end observation at its declared boundary.

**Evidence limitation.** Wake and Cockburn describe practitioner techniques. DORA’s small-batch evidence indirectly supports fast feedback and correction, but does not isolate vertical slicing as the causal factor. A universal superiority claim is not supported.

**Confidence:** medium.

### 5. Dependencies, integration points, and verification boundaries

**Facts.** NASA’s integration guidance connects decomposition to interfaces, integration order, participant responsibilities, required resources, and verification strategy. Its requirements guidance calls for weak coupling, explicit internal and external interfaces, and examination of requirements both individually and as an integrated set. [NASA integration guidance](https://www.nasa.gov/reference/system-engineering-handbook-appendix/)

Current DORA guidance reports that independently completable small batches predict delivery and organizational performance and support rapid testing and correction; this is observational research and contextual guidance, not a universal causal law. [DORA: Working in small batches](https://dora.dev/capabilities/working-in-small-batches/)

Fowler’s practitioner account of continuous integration argues for small, frequently integrated changes with automated checks so conflicts and interaction defects are exposed while the change context is fresh. [Continuous Integration, 2024](https://martinfowler.com/articles/continuousIntegration.html)

**Inference.** Decomposition should record:

- ordering dependencies and prerequisites;
- shared interfaces and change-sensitive seams;
- integration owner or recomposition point;
- what can be verified locally;
- what requires integrated or end-to-end verification;
- what evidence closes each boundary.

Dependency discovery may justify re-slicing, combining inseparable units, or creating a time-boxed learning unit. It does not justify indefinitely postponing integration.

**Confidence:** high for explicit dependency and integration treatment; medium for optimal batch shape.

### 6. Review and correction during formation and execution

**Facts.**

- Requirements and examples benefit from stakeholder clarification before execution. [NASA](https://www.nasa.gov/reference/4-0-system-design-processes/), [Cucumber](https://cucumber.io/docs/bdd/example-mapping/)
- Scrum places inspection and adaptation throughout work and reviews usable outcomes with stakeholders. [Scrum Guide](https://scrumguides.org/scrum-guide.html?from=hub)
- A multi-organization empirical study found contemporary peer review usually occurred regularly and quickly before integration, commonly with two reviewers but with variation based on complexity. It also found substantial knowledge-spread effects, while acknowledging dataset and proxy limitations. [Rigby and Bird, 2013](https://www.cabird.com/static/93aba3256c80506d3948983db34d3ba3/rigby2013convergent.pdf)
- A Microsoft field study found understanding the reason and context for a change to be a major review difficulty. Defect comments were a minority of observed review comments, and reviewers familiar with the affected code reported deeper feedback. The authors warn against relying on code review alone for defect detection. [Bacchelli and Bird, 2013](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICSE202013-codereview.pdf)

**Inference.** Different review points serve different questions:

- **Formation review:** Are intent, assumptions, boundaries, and examples understood?
- **Execution feedback:** Does the evolving work satisfy fast, local checks?
- **Peer review:** Is the change understandable, technically coherent, and consistent with relevant context?
- **Integration validation:** Do composed parts work together at their interfaces?
- **Outcome review:** Does the usable result meet stakeholder expectations?

Automated verification, peer review, independent review, and acceptance must not be represented as interchangeable. Invocation of formal independent review remains governed by DR-001 and later design.

**Confidence:** high.

### 7. Durable versus ephemeral context

**Facts.** The Charter and accepted DR-001 disposition require durable, addressable state where authority or downstream reliance depends on it and prohibit chat or handoffs from displacing authoritative owners. [Project Charter](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/PROJECT-CHARTER.md), [Research Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/research-register.md)

Architecture Decision Records are practitioner evidence for preserving a decision’s context, rationale, alternatives, consequences, and supersession history in a concise record. They do not prove that every decision needs such a record. [Fowler, Architecture Decision Record, 2026](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)

Cucumber distinguishes transient discovery questions from rules and examples that become part of the lasting specification. [Gherkin Rules](https://cucumber.io/blog/bdd/gherkin-rules/)

**Inference.** Preserve durably when later work depends on:

- governing intent, scope, constraints, or non-goals;
- a material assumption or unresolved blocker;
- a decision and enough rationale to understand it;
- an interface or dependency contract;
- acceptance or verification conditions and relied-upon results;
- current authoritative state or an immutable candidate identity;
- the safe continuation point across people, agents, or sessions.

Raw brainstorming, superseded wording, locally recoverable navigation, and resolved questions whose resolution is captured elsewhere may remain ephemeral.

**Confidence:** high for the reliance criterion; medium for retention duration, which remains governance-specific.

### 8. Usable context transition

**Facts.** Parnin and Rugaber’s exploratory study of 10,000 sessions from 85 programmers found that rapid resumption was uncommon and that programmers usually navigated or sought other context before editing. It identifies plans, intentions, progress, component mechanisms, and domain representations as relevant working state. The evidence concerns human programmers and tool sessions, not autonomous agents. [Parnin and Rugaber, 2009](https://chrisparnin.me/pdf/parnin-icpc09.pdf)

The Microsoft review study found that unfamiliar reviewers needed change rationale, file purpose, invariants, APIs, and wider impact context; small diffs were not necessarily easy when the surrounding code was unfamiliar. [Bacchelli and Bird](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICSE202013-codereview.pdf)

**Inference.** A fresh-practitioner transition should make recoverable:

- objective and reason for the work;
- authoritative inputs and exact current baseline;
- completed, attempted, and remaining work;
- material decisions, assumptions, and rejected paths;
- touched components, interfaces, and dependencies;
- verification already performed and its result;
- known failures, uncertainty, and open questions;
- next safe action and stop/escalation conditions.

This is a content constraint, not a packet schema. Agent autonomy, observability, stopping, recovery, and execution mechanics remain DR-003 dependencies.

**Confidence:** medium-high for practitioners; medium for transfer to agents.

### 9. Qualitative proportionality

**Facts.** NIST SP 800-53B permits risk-based tailoring according to system and organizational context, cost, schedule, performance, mission needs, and applicable obligations, while requiring defensible rationale and forbidding arbitrary removal of applicable controls. [NIST SP 800-53B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf)

NIST SSDF recommends additional rigor for higher-risk software areas while allowing its high-level practices to be integrated into different lifecycle models. [NIST SP 800-218 v1.1](https://csrc.nist.gov/pubs/sp/800/218/final)

Amazon’s 2015 shareholder letter distinguishes consequential, difficult-to-reverse decisions from reversible decisions, but explicitly notes survivorship bias; it is first-party management practice, not general effectiveness proof. [Amazon 2015 shareholder letter](https://ir.aboutamazon.com/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF)

Google’s SRE Workbook shows, specifically for deployments, how partial exposure and rollback can reduce the affected population and cost of learning when tests cannot reproduce all production behavior. [Canarying Releases](https://sre.google/workbook/canarying-releases/)

**Inference.** Increase clarification, documentation, review diversity, integrated verification, and correction safeguards as one or more of these rise:

- **Context:** applicable governance, domain criticality, novelty, coordination distance.
- **Consequence:** harm if intent or implementation is wrong.
- **Uncertainty:** unknown requirements, behavior, dependencies, or evidence.
- **Reversibility:** difficulty and time required to restore prior conditions.
- **Blast radius:** people, systems, data, or downstream decisions exposed.

Reduce ceremony only when the rationale is defensible and no applicable control is silently removed. No evidence supports fixed weights, numeric cutoffs, or a universal “small task” exemption.

**Confidence:** high for qualitative tailoring; low for universal thresholds.

### 10. Failure modes, costs, and limiting conditions

| Failure mode | Consequence | Limiting evidence or countermeasure |
|---|---|---|
| Specification begins before outcome or constraints converge | Correct implementation of the wrong interpretation | Iterative stakeholder clarification and concrete examples |
| Story/card treated as the complete specification | Hidden rules and assumptions | Conversation plus testable confirmation; INVEST is not a complete method |
| Exhaustive specification attempted too early | Delay, false certainty, expensive change | Emergent refinement and bounded readiness |
| Horizontal layers completed independently | No usable behavior; delayed integration learning | Prefer end-to-end observable slices where coherent |
| Every unit forced to be user-visible | Necessary enabling or risk-reduction work becomes distorted | Permit explicit enabling dependencies and learning units |
| Dependencies remain implicit | Ordering conflicts, rework, late integration | Declare interfaces, preconditions, recomposition, and integrated verification |
| Large batches or long integration delay | Slower feedback and harder conflict isolation | Small batches and frequent integration, subject to system constraints |
| Review receives only a diff | Shallow or delayed feedback | Include intent, rationale, affected context, interfaces, and verification |
| Code review treated as complete defect assurance | Missed deep or integration defects | Layer automated, peer, integrated, and outcome verification |
| All working conversation is preserved | Noise, maintenance burden, stale duplication | Preserve decisions and relied-upon state, not every utterance |
| Nothing is preserved because conversation is preferred | Reconstruction cost and authority ambiguity | Durable handoff and authoritative-state references |
| Uniform ceremony | Either excessive delay or under-controlled consequential work | Qualitative tailoring with explicit rationale |

### 11. Constraints versus later choices and DR-003 dependencies

**Evidence-backed candidate constraints**

- readiness before execution;
- clear, testable, traceable acceptance;
- bounded and coherent units;
- observable vertical outcomes where appropriate;
- explicit dependencies, interfaces, recomposition, and verification boundaries;
- feedback at formation, execution, integration, and outcome;
- context-rich review;
- reliance-based durability;
- self-sufficient transitions;
- qualitative proportionality.

**Workflow v1 design choices not resolved**

- lifecycle sequence and gate mechanics;
- document or packet representation;
- whether named activities are separate events;
- exact granularity or batch-size targets;
- definition of ready or done;
- retention periods;
- state-placement and synchronization mechanics;
- correction/review iteration structure.

**DR-003 dependencies**

- delegated-execution controls;
- concurrency and parallel-wave behavior;
- execution observability;
- agent stopping and recovery;
- fresh-state enforcement during execution;
- unattended-operation limits;
- agent identity and independence enforcement.

## Coverage matrix

| SQ | Coverage | Principal evidence | Gap/qualification |
|---|---|---|---|
| 1 | Supported | NASA; Cucumber; DR-001 R11 | Universal minimum not empirically established |
| 2 | Supported | NASA; Scrum; Wake | Domain-specific rigor varies |
| 3 | Supported | NASA; Scrum; INVEST | Optimal size unresolved |
| 4 | Supported with qualification | Wake; Cockburn; Scrum; DORA indirect | No direct universal comparative proof |
| 5 | Supported | NASA integration guidance; DORA; Fowler CI | No sequencing algorithm adopted |
| 6 | Supported | NASA; Scrum; Bacchelli/Bird; Rigby/Bird | Review invocation remains contextual |
| 7 | Supported | Charter; DR-001; Cucumber; ADR practice | Retention and concrete owner unresolved |
| 8 | Supported with qualification | Parnin/Rugaber; Bacchelli/Bird; DR-001 R11–R12 | Human-to-agent transfer is inferential |
| 9 | Supported with qualification | NIST 800-53B; SSDF; Amazon; Google SRE | No weights or thresholds |
| 10 | Supported | Cross-source negative evidence | Costs remain context-dependent |
| 11 | Supported | Contract; Register; DR-001 disposition | DR-003 join still required |

## Proposed recommendation map

| ID | Proposed constraint | Evidence | Tradeoff | Limiting condition | Confidence |
|---|---|---|---|---|---|
| R1 | Require bounded clarification readiness before specification/execution | NASA, Cucumber, DR-001 | Up-front discovery cost | Unknowns may be explicitly bounded rather than fully resolved | High |
| R2 | Define specification sufficiency by executability and verifiability, not document weight | NASA, Scrum, Wake | Requires judgment | Safety/regulatory contexts may require fuller baselines | High |
| R3 | Require coherent, traceable, independently understandable and verifiable units | NASA, Scrum, INVEST | Decomposition overhead | Some dependencies cannot be removed | High |
| R4 | Prefer observable vertical slices for behavioral feedback | Wake, Cockburn, Scrum; DORA indirect | Cross-layer coordination | Enabling or learning work may be legitimate; superiority evidence limited | Medium |
| R5 | Make dependency, integration, recomposition, and verification boundaries explicit during decomposition | NASA, DORA, CI | Additional planning and integration work | Exact ordering remains design-specific | High |
| R6 | Use distinct, timely feedback mechanisms and provide reviewers with change context | NASA, Scrum, empirical review studies, CI | Review latency and attention cost | Formal independence remains conditional under DR-001 | High |
| R7 | Preserve context according to downstream reliance; allow disposable working detail to remain ephemeral | Charter, DR-001, Cucumber, ADR practice | Documentation maintenance | Retention and representation remain unresolved | High |
| R8 | Make fresh-practitioner transitions self-sufficient without promoting handoffs to authority | DR-001, Parnin/Rugaber, Bacchelli/Bird | Packet preparation cost | Agent execution controls belong to DR-003 | Medium-high |
| R9 | Scale depth qualitatively using context, consequence, uncertainty, reversibility, and blast radius | DR-001, NIST, Amazon, Google SRE | Inconsistent judgment without later guidance | No score, threshold, or universal exemption is supported | High for principle; low for thresholds |

## Contradictions and tensions

| Claims in tension | Authority/date/scope | Precise issue | Disposition |
|---|---|---|---|
| NASA emphasizes complete, validated, traceable requirements; Agile/Scrum emphasize change and emergent refinement | Primary government guidance, Rev. 2; practitioner framework, 2001/2020 | Complete baseline versus continuing refinement | Scope-dependent, not irreconcilable: require sufficient completeness at the next commitment boundary and permit controlled refinement |
| Vertical user-value slices; NASA recognizes interdependent enabling products | Practitioner guidance, 2003/2009; government systems guidance, Rev. 2 | Every unit user-visible versus necessary infrastructure/enabling work | Narrow R4: prefer vertical outcomes, allow explicitly justified enabling work |
| Agile conversation and Wake’s dynamic interplay; Charter/DR-001 require durable authoritative records | Practitioner principles, 2001/2021; current internal normative/accepted disposition | Conversation-only work could displace authoritative state | No same-scope contradiction: conversation may convey information, but cannot own authoritative state in this repository |
| Lightweight frequent review; formal independent review for consequential work | Empirical contemporary review, 2013; accepted DR-001 governance principle | Speed and low ceremony versus independence and formality | Conditional application based on consequence, uncertainty, privilege, and governance |
| Cucumber treats answered question cards as transient; DR-002 requires unresolved questions to be explicit | Practitioner method, current/2015; durable DR-002 contract | Whether questions must persist | Persist unresolved or reliance-bearing questions; resolved discovery artifacts may be discarded once the resolution is captured |
| Reversibility permits lighter decisions; erroneous “two-way door” classification can expose material harm | Amazon first-party practice, 2015 | Reversibility may be overestimated | Treat reversibility as one qualitative input, not a controlling rule |

No same-scope contradiction with the Charter, Research Evidence Policy, Research Register, or accepted DR-001 disposition was found.

**Coordinator contradiction gate:** **not triggered**.

A later material conflict with DR-003 must still be carried to the prerequisite-research join.

## Explicit evidence gaps and limitations

- No direct comparative primary study establishes that vertical slices outperform every horizontal or enabling decomposition.
- No universal, empirically validated specification-readiness checklist was found.
- No universal handoff content minimum has been validated for both humans and agents.
- DORA findings are survey-based associations and contextual models, not proof that batch size alone causes performance.
- The two principal code-review studies date from 2013 and reflect particular organizations and repositories.
- Parnin and Rugaber studied human programmer resumption, not agent handoffs.
- ADR, Example Mapping, INVEST, Elephant Carpaccio, continuous-integration guidance, and Amazon’s decision model are practitioner or first-party evidence of recommended practice; they do not alone prove general effectiveness.
- Reversibility and blast radius have direct support in decision and deployment contexts, but not as universally weighted workflow dimensions.
- Applicable regulation, safety obligations, and organizational governance may require controls that proportional tailoring cannot remove.
- Ceremony-cost optimization requires later empirical observation and remains outside DR-002.

## Source register

All sources were accessed on 2026-09-03.

### Internal repository sources

| ID | Identity | Supported claims | Limitation |
|---|---|---|---|
| I1 | [`main@79f5541113e7dfeedfde6f36f371031f3f3330fa`](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/79f5541113e7dfeedfde6f36f371031f3f3330fa) | Exact live repository state | State claim only |
| I2 | [DR-002 contract](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-002.md), blob `af09e6fd165bf3b7aa835364a4013ed3ec9c2b5c` | Question, scope, required output, stop boundary | Draft evidence contract, not policy |
| I3 | [Research Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/research-register.md), blob `8d86d84fc00a2e2c468ed68f82a580c869fb8ddb` | Current status, DR-001 disposition, dependencies, next gate | Does not contain findings |
| I4 | [Project Charter](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/PROJECT-CHARTER.md), blob `c521f6869662f39106bcac0365426eb0e9bdb327` | Authority, role, research/policy, acceptance boundaries | Does not design Workflow v1 |
| I5 | [Research Evidence Policy](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/policies/research-evidence.md), blob `90572c47463f2d2adc493f9978c1c720fd8f8275` | Evidence hierarchy, fact/inference/recommendation separation, lifecycle | Research governance only |
| I6 | [DR-001](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001.md), blob `f142919d1ed1f6b1717cc965ab9232bbc60d4389` | Accepted-input evidence, deferrals, fresh-context and proportionality bounds | Frozen evidence, non-normative |
| I7 | [DR-001 source review](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001-SOURCE-REVIEW-001.md), blob `d2b96bbf15dab1e21a1a17dee134644f5f1fb003` | Evidence-quality verdict and minor freshness finding | Review does not adopt recommendations |

### External sources

| ID | Source identity and date/version | Supported claims | Scope and limitations |
|---|---|---|---|
| E1 | NASA, [Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), NASA/SP-2016-6105 Rev. 2 | Stakeholder expectations, requirements quality, assumptions, interfaces, decomposition, integration, V&V | Aerospace/system-engineering guidance; rigor is not universal |
| E2 | Schwaber & Sutherland, [Scrum Guide](https://scrumguides.org/scrum-guide.html?from=hub), Nov. 2020 | Emergent refinement, actionable plan, usable verified increments, inspection/adaptation | Describes Scrum; does not prove universal efficacy |
| E3 | Agile Manifesto authors, [Principles](https://agilemanifesto.org/principles.html), 2001 | Frequent value delivery, collaboration, working results, reflection, simplicity | Practitioner principles, not controlled evidence |
| E4 | Cucumber, [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/), updated Aug. 29, 2026 | Rules, examples, questions, assumptions, scope clarification | Method description; effectiveness largely practitioner-reported |
| E5 | Bill Wake, [INVEST in Good Stories and SMART Tasks](https://xp123.com/invest-in-good-stories-and-smart-tasks/), Aug. 17, 2003 | Independence, value, size, testability, vertical slicing, time-boxed learning | Original practitioner guidance |
| E6 | Bill Wake, [All You Need is INVEST? No!](https://xp123.com/all-you-need-is-invest-no/), Aug. 4, 2021 | Limits of INVEST; end-to-end capability; conversational context | Author’s qualification, not empirical study |
| E7 | Alistair Cockburn, [Software/Elephant Carpaccio](https://alistair.cockburn.us/wp-content/uploads/2018/02/Elephant-Carpaccio-exercise-instructions.pdf), 2009 | Demonstrable thin vertical slices with real input/output | Training exercise, not comparative research |
| E8 | DORA, [Working in small batches](https://dora.dev/capabilities/working-in-small-batches/), updated Dec. 8, 2025 | Small batches, independent completion, feedback, performance association | Research synthesis; association and context limitations apply |
| E9 | Martin Fowler, [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html), Jan. 18, 2024 | Frequent integration, automated feedback, small changes | Practitioner synthesis |
| E10 | Bacchelli & Bird, [Expectations, Outcomes, and Challenges of Modern Code Review](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICSE202013-codereview.pdf), ICSE 2013, DOI `10.1109/ICSE.2013.6606617` | Review context, understanding, actual outcomes, limits of defect finding | Microsoft field study; dated and organization-specific |
| E11 | Rigby & Bird, [Convergent Contemporary Software Peer Review Practices](https://www.cabird.com/static/93aba3256c80506d3948983db34d3ba3/rigby2013convergent.pdf), ESEC/FSE 2013, DOI `10.1145/2491411.2491444` | Review timing, lightweight review, reviewer count variation, knowledge spread | Multiple-case observational study with proxy measures |
| E12 | Parnin & Rugaber, [Resumption Strategies for Interrupted Programming Tasks](https://chrisparnin.me/pdf/parnin-icpc09.pdf), ICPC 2009, DOI `10.1109/ICPC.2009.5090030` | Context-recovery behavior and resumption costs | Exploratory human-programmer study |
| E13 | Martin Fowler, [Architecture Decision Record](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html), Mar. 24, 2026 | Concise preservation of decision context, rationale, consequences, supersession | Practitioner guidance; architecture decisions only |
| E14 | NIST, [SP 800-53B](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf), Oct. 2020 with Dec. 2020 errata | Contextual, documented, risk-based tailoring | U.S. federal security/privacy-control context |
| E15 | Souppaya, Scarfone & Dodson, [NIST SP 800-218 v1.1](https://csrc.nist.gov/pubs/sp/800/218/final), Feb. 2022 | Lifecycle-independent practices and greater rigor for higher-risk areas | Secure-software scope |
| E16 | Jeff Bezos/Amazon, [2015 shareholder letter](https://ir.aboutamazon.com/files/doc_financials/annual/2015-Letter-to-Shareholders.PDF), 2016 publication | Consequence and reversibility as decision-process considerations | First-party practice; letter acknowledges survivorship bias |
| E17 | Warner et al., Google, [Canarying Releases](https://sre.google/workbook/canarying-releases/), *The Site Reliability Workbook*, 2018 | Partial exposure, rollback, production uncertainty, limiting affected scope | Deployment-specific practitioner guidance |

## Final gate statement

GitHub was reverified after evidence synthesis:

- `main` still resolved to `79f5541113e7dfeedfde6f36f371031f3f3330fa`.
- All six inspected authoritative or required DR-001/DR-002 blobs remained unchanged.
- Every contracted subquestion has a supported finding or explicit limitation.
- No substantive evidence edit remains planned.
- No coordinator-gated contradiction was found.

The packet therefore stops at the DR-002 evidence-production boundary and is ready for a separately authorized exact-byte freeze gate.
