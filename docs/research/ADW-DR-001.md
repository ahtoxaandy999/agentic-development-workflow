---
id: DR-001
artifact_status: draft
authority: evidence
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: 2026-09-03
owner: agentic-development-research
question: coordinator gates and artifact lifecycle before Workflow v1
scope: coordinator-gates-and-artifact-lifecycle-requirements-before-workflow-v1
decision_consumer: coordinator DR-001 recommendation-disposition decision before Workflow v1 design
repository: ahtoxaandy999/agentic-development-workflow
repository_state: "main@f9e6642118114ef991770f3d871023f2e4a5defb; accepted baseline 13b05e075ec04aa91494cd18f7d29f7249028cb5"
repository_state_at_authorization: "main@265f171502de8a2d8844ae4ccf277c58e56a20cb; verified 2026-09-03"
research_gate_ref: ADW-DR-001-GATE-001
research_gate_correction_ref: ADW-DR-001-GATE-CORR-001
supersedes: null
---

# DR-001: Coordinator gates and artifact lifecycle before Workflow v1

## Status and authority

- This file is a durable draft research contract.
- `artifact_status: draft` does not mean completed, reviewed, adopted, active, normative, or accepted.
- Mutable DR-001 research status, dependencies, artifact pointer, current disposition, supersession, and next gate belong to the Research Register.
- The research contract is authorized by `ADW-DR-001-GATE-001` as corrected by `ADW-DR-001-GATE-CORR-001`.
- Chat, memory, summaries, and handoffs are not substitutes for this durable contract.
- Workflow v1 remains unadopted.

## Canonical question

`coordinator gates and artifact lifecycle before Workflow v1`

Operational framing:

Determine the evidence-backed lifecycle, ownership, durability, safety, proportionality, and minimum-context requirements that a future Workflow v1 would need to satisfy.

This research does not design Workflow v1.

## Decision consumer

A later explicit coordinator DR-001 recommendation-disposition decision that may accept, reject, narrow, or defer evidence-backed requirements and constraints as inputs to a separately gated Workflow v1 design effort.

That later decision must identify the exact evidence identity and decision scope.

It does not itself adopt Workflow v1.

## Research owner and role separation

Research owner:

`agentic-development-research`

The researcher owns evidence production only.

The researcher may not independently:

- source-review their own completed evidence;
- adopt their own recommendations;
- update normative owners without authorization;
- accept their own artifact or candidate;
- expand the authorized research scope.

Independent source review and coordinator disposition remain separate gates.

## Scope

DR-001 investigates evidence concerning:

1. lifecycle states and transitions that must remain distinct;

2. which gates appear universal and which may be conditioned on:

   - risk;
   - uncertainty;
   - reversibility;
   - blast radius;

3. transition ownership across:

   - coordinator;
   - researcher;
   - executor;
   - independent reviewer;
   - human/maintainer;

4. durable versus ephemeral state;

5. authoritative ownership of:

   - task/work state;
   - research state;
   - decisions;
   - execution authorization;
   - candidate identity;
   - review evidence;
   - acceptance evidence;
   - handoff/navigation state;

6. controls against:

   - competing truth;
   - stale chat state;
   - executor self-acceptance;
   - implicit lifecycle transitions;
   - review of mutable targets;
   - passing checks being mistaken for acceptance;

7. proportionate scaling for small, clear, reversible tasks;

8. minimum safe execution and review context for a fresh agent;

9. unresolved questions that belong to later research;

10. the completed bootstrap lifecycle as an internal case study, including its corrections and post-acceptance state synchronization.

## Non-scope

DR-001 must NOT:

- design, specify, or adopt Workflow v1;
- codify the bootstrap sequence as Workflow v1;
- select GitHub Issues, Projects, pull requests, or another tracker;
- adopt a task schema or normative state machine;
- select or configure Apps, MCP servers, skills, hooks, automation, or tooling;
- design parallel scheduling or worktree orchestration;
- design AFK execution;
- create implementation code;
- change or supersede Bootstrap Context Baseline v0;
- reopen accepted bootstrap decisions without new contradictory evidence;
- perform dedicated research reserved for DR-002, DR-003, DR-004, or DR-005.

The report may identify requirements, evidence gaps, constraints, or open questions relevant to those later topics, but must defer their dedicated research.

## Evidence classes and source hierarchy

Use:

1. live immutable repository evidence;
2. accepted internal normative artifacts;
3. durable bootstrap lifecycle records;
4. internal negative evidence and correction history;
5. narrowly selected external primary evidence for generalizable governance principles;
6. explicit missing-evidence and contradiction records.

For load-bearing claims prefer:

1. live repository state, exact commits, diffs, configuration, and durable repository objects;
2. official vendor/platform documentation;
3. official standards, specifications, frameworks, or primary repositories;
4. original empirical research or first-party case studies when empirical behavior is material;
5. secondary sources only for discovery or explicitly qualified context.

There is no source-count quota.

Each material external source must record relevant date/version, scope, limitations, and applicability.

## Required internal evidence

At minimum inspect:

- AGENTS.md
- PROJECT-CHARTER.md
- docs/policies/research-evidence.md
- docs/research/research-register.md
- relevant portions of docs/research/ADW-BOOTSTRAP-RESEARCH-001.md
- Bootstrap Context Baseline v0 at: `13b05e075ec04aa91494cd18f7d29f7249028cb5`
- current repository state at explicit full SHA;
- Git commit history and relevant diffs;
- durable source-review/adoption/acceptance evidence where available;
- GitHub Issue #1 acceptance record;
- bootstrap correction history;
- post-acceptance state synchronization;
- observed missing durable records or stale-state incidents.

Trace the actual bootstrap path:

```text
research
→ source review
→ adoption
→ execution
→ correction
→ exact-SHA candidate review
→ coordinator acceptance
→ durable acceptance record
→ post-acceptance state synchronization
```

For each available transition identify:

- durable record;
- exact SHA or immutable identity where applicable;
- date;
- owner/actor;
- transition;
- correction or exception;
- missing durable evidence.

Chat or memory may help locate evidence but cannot replace durable evidence.

## Bounded external evidence

Use only the minimum external primary evidence needed for general principles not established sufficiently by the internal case.

Potential material areas:

- separation of duties and independent review;
- change authorization and traceability;
- immutable/content-addressed review targets;
- risk-based process tailoring;
- audit/evidence durability and provenance;
- human accountability for consequential transitions.

Do not broaden this into a survey of development methodologies.

## Explicit deferrals

Defer dedicated research on:

- Matt Pocock workflow patterns;
- OpenAI Codex, Harness, or Symphony patterns;
- parallel execution and worktree scheduling;
- AFK operation;
- Apps;
- MCP servers;
- skills;
- hooks;
- automation;
- tooling selection;
- tracker selection;
- task-schema design.

DR-001 may record dependencies or open questions for these topics but must not perform their dedicated research.

## Key subquestions

Gather evidence sufficient to evaluate:

1. Which state planes and lifecycle transitions require separation?

2. Which gates are invariant and which may be risk-conditional?

3. Who may initiate, authorize, execute, review, adopt, accept, and record each transition?

4. Which state requires durable, addressable evidence?

5. What should be the authoritative owner for each state class?

6. Which controls address each observed failure mode?

7. What evidence supports a reduced process for small, low-risk work?

8. What minimum task packet permits safe execution by a fresh agent?

9. What minimum evidence packet permits independent review by a fresh reviewer?

10. Which unresolved matters must be deferred to later research?

Do not presuppose the answers.

## Contradiction, negative-evidence, and missing-evidence handling

For conflicting credible claims record:

- source;
- authority;
- date/version;
- scope;
- configuration;
- actual contradiction.

Do not average incompatible claims or resolve them through assumption.

Distinguish:

- contrary evidence;
- absence of evidence;
- unavailable evidence;
- stale evidence;
- configuration-dependent evidence.

Missing decisive evidence must narrow or block the affected recommendation and state what could resolve it.

Contradiction with an accepted bootstrap decision must be surfaced for a separate coordinator gate.

DR-001 cannot amend Bootstrap Context Baseline v0.

Stale or unverifiable live repository state stops dependent analysis.

## Recommendation boundary

The final report may recommend:

- candidate lifecycle requirements;
- candidate invariants;
- conditionality criteria;
- ownership constraints;
- durability classifications;
- controls for observed failure modes;
- minimum-context requirements;
- later research questions.

It may NOT present as adopted:

- a Workflow v1 design;
- a task schema;
- a normative state machine;
- artifact or tracker selection;
- tooling choices;
- policy.

Facts, inferences, recommendations, and unresolved questions must remain visibly separate.

## Evidence date and freshness semantics

During evidence production:

- record actual evidence-collection dates;
- record exact GitHub SHAs for repository claims;
- record external source publication/version/access dates where material;
- reverify unstable repository state through the connected GitHub source;
- do not populate publication-only metadata yet.

At evidence freeze:

- set `evidence_as_of` to the final date on which load-bearing evidence was verified;
- record the full GitHub SHA used at freeze;
- record accepted baseline SHA separately;
- materially changed evidence requires a new frozen identity;
- no silent refresh is allowed.

## Stop boundary

Evidence production stops when:

- every contracted subquestion has supported findings or an explicit evidence gap;
- source register and citations are complete;
- contradictions and negative evidence are documented;
- material assumptions, uncertainty, limitations, and deferrals are recorded;
- live repository evidence has been reverified;
- bounded recommendations are complete;
- no substantive research edit remains planned.

Stop earlier on:

- authority conflict;
- unverifiable live state;
- unsafe evidence handling;
- unresolved scope expansion;
- dependency on deferred research required to answer a load-bearing question.

Do not proceed from evidence production into:

- source review;
- adoption;
- normative materialization;
- Workflow v1 design.

## Intended final report structure

The completed report is expected to contain:

1. Metadata and immutable identity
2. Executive evidence verdict
3. Question, scope, non-scope, method, and stop boundary
4. Source register and evidence classification
5. Bootstrap case-study chronology
6. Findings by subquestion
7. Candidate lifecycle and ownership requirements
8. Universal-versus-conditional gate evidence
9. Durability and authoritative-owner analysis
10. Failure modes and control evidence
11. Small-task proportionality evidence
12. Minimum fresh-agent context
13. Contradictions, negative evidence, and missing evidence
14. Deferred dependencies and open questions
15. Alternatives, tradeoffs, and recommendations
16. Limitations, freshness, and supersession conditions

This structure is an output contract, not evidence that the sections have already been researched.

## Independent source-review criteria

A later independent reviewer must verify:

- exact frozen report identity;
- compliance with scope and non-scope;
- claim-level evidence support;
- primary-source preference;
- live GitHub provenance and full-SHA use;
- completeness and accuracy of the bootstrap trace;
- freshness and source limitations;
- handling of corrections, contradictions, and negative evidence;
- separation of fact, inference, recommendation, and adoption;
- support for universal or conditional assertions;
- coverage of every contracted subquestion;
- explicit deferral of later research;
- absence of Workflow v1 design or tool selection;
- sensitive-information handling;
- sound evidence-to-recommendation reasoning.

Source review establishes evidence quality only.

It grants no adoption, execution, normative-update, Workflow v1, or acceptance transition.

## Exact-byte freeze and immutable identity

While DR-001 is in progress this file remains mutable and:

```yaml
artifact_status: draft
```

Publication-only fields remain absent.

Evidence freeze occurs only after the stop boundary is satisfied.

At freeze, populate:

```yaml
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: <actual final evidence-verification date>
repository_state: "main@<full SHA verified at freeze>; accepted baseline 13b05e075ec04aa91494cd18f7d29f7249028cb5"
```

`artifact_status` remains `draft` for the frozen source-review target.

After final content and metadata are complete:

1. serialize the exact complete file as UTF-8 using its actual final newline state;
2. calculate SHA-256 over the exact raw file bytes;
3. do not normalize whitespace, newline form, or Unicode;
4. identify the review target as: `DR-001@sha256:<lowercase-64-hex-digest>`;
5. record byte length alongside the digest.

Any byte change creates a new identity and invalidates review of the previous digest.

A later draft → active transition creates different bytes and therefore a new digest.

The source-review verdict remains tied to the frozen draft digest.

Any substantive evidence change after source review requires a new freeze identity and fresh source review.

## Later coordinator decision informed

The final evidence is intended to inform a separate coordinator DR-001 recommendation-disposition decision.

That decision determines which evidence-backed requirements, constraints, deferrals, or unresolved questions may become inputs to a separately gated Workflow v1 design effort.

It must identify:

- exact evidence identity;
- decision scope;
- any proposed normative owner.

It does not itself adopt Workflow v1.

## Preserved boundaries

Throughout DR-001:

- Bootstrap Context Baseline v0 remains: `13b05e075ec04aa91494cd18f7d29f7249028cb5`
- Workflow v1 remains unadopted.
- DR-002, DR-003, DR-004, and DR-005 remain unstarted.
- tooling selection remains deferred.
- tracker selection remains deferred.
- no normative artifact changes occur without a separate coordinator gate.

## A. Executive evidence verdict

The completed evidence is sufficient to support a later coordinator recommendation-disposition decision, subject to the explicit limitations, gaps, and deferrals recorded below. It strongly supports preserving semantic separation among evidence production, source review, recommendation disposition or adoption, execution authorization, candidate identity, verification, independent review, and acceptance. These are state and authority boundaries; the evidence does not require a distinct person or process for every compatible role.

The evidence supports one authoritative owner for each mutable state class, exact immutable identity for formal review targets, durable records for consequential authorizations, exceptions, reviews, and acceptance, fresh self-sufficient execution and review packets, and risk-based proportionality rather than universal heavyweight ceremony.

The evidence does not support treating the bootstrap sequence as Workflow v1, requiring the full bootstrap ceremony for every task, adopting fixed risk thresholds or a normative state machine, or selecting a tracker, schema, tool, App, MCP server, skill, hook, or automation system.

Material limitations include missing standalone durable records for several bootstrap review, adoption, and gate transitions; missing durable reviewer identity and independence evidence; use of one GitHub publishing account across the durable events; no supported universal small-task threshold; and unresolved concrete storage, synchronization, retention, and enforcement mechanisms.

All conclusions below remain research evidence, inference, unresolved questions, and proposed candidate recommendations. Nothing in this packet is adopted policy.

## B. Repository evidence basis

- Repository: `ahtoxaandy999/agentic-development-workflow`
- Starting `main`: `14293cb67628e934a25fdc8fbe771093855f0876`
- Final observed `main`: `14293cb67628e934a25fdc8fbe771093855f0876`
- Accepted Bootstrap Context Baseline v0: `13b05e075ec04aa91494cd18f7d29f7249028cb5`
- Verification date: 2026-09-03
- Freshness result: starting and final SHAs match. No live-state claims became stale during research.
- Provenance: every repository-state claim below was established through the connected GitHub app. The local project mirror, chat history, and Project memory were not used to establish current repository state.
- No GitHub state was modified.

Artifacts inspected at the exact starting SHA:

- [`AGENTS.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/AGENTS.md)
- [`PROJECT-CHARTER.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/PROJECT-CHARTER.md)
- [`docs/policies/research-evidence.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/docs/policies/research-evidence.md)
- [`docs/research/research-register.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/docs/research/research-register.md)
- [`docs/research/ADW-DR-001.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/docs/research/ADW-DR-001.md)
- Relevant portions of [`docs/research/ADW-BOOTSTRAP-RESEARCH-001.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/docs/research/ADW-BOOTSTRAP-RESEARCH-001.md): publication state, transition model, candidate lifecycle, negative evidence, risks, limitations, and recorded next gate.

Baseline evidence inspected at `13b05e075ec04aa91494cd18f7d29f7249028cb5`:

- [Complete baseline tree](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/git/trees/13b05e075ec04aa91494cd18f7d29f7249028cb5?recursive=1)
- [`ADW-BOOTSTRAP-RESEARCH-001.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/13b05e075ec04aa91494cd18f7d29f7249028cb5/docs/research/ADW-BOOTSTRAP-RESEARCH-001.md)
- [`research-register.md`](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/13b05e075ec04aa91494cd18f7d29f7249028cb5/docs/research/research-register.md)

The canonical research question was preserved verbatim:

> coordinator gates and artifact lifecycle before Workflow v1

## C. Method and source register

### Method

The analysis:

1. Froze the repository evidence basis at the expected starting SHA.
2. Read the durable contract and controlling artifacts at that SHA.
3. Reconstructed the bootstrap from commits, diffs, tree identities, and Issue #1.
4. Searched for negative evidence: stale state, missing decision records, identity gaps, mutable targets, and capability-dependent controls.
5. Used external primary sources only for principles the bootstrap case could not establish by itself.
6. Classified every substantive conclusion as verified fact, inference, candidate recommendation, or unresolved question.
7. Re-queried live `main` immediately before completion.

### Internal repository evidence

| ID | Evidence | Role and limitation |
|---|---|---|
| I1 | [`main` branch endpoint](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/branches/main) | Starting and final SHA; current branch reports `protected: false`. Mutable evidence, verified twice on 2026-09-03. |
| I2 | [Initial bootstrap commit `319fdf5…`](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/319fdf5ec1449f432ec2196a675640d581a9d6c1) | First durable six-file materialization. Does not prove the identities or times of prior research, source review, or adoption. |
| I3 | [Correction/freeze commit `13b05e0…`](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/13b05e075ec04aa91494cd18f7d29f7249028cb5) | Replaced the unavailable protection path with a temporary manual SHA freeze. This is the accepted baseline. |
| I4 | [Issue #1](https://github.com/ahtoxaandy999/agentic-development-workflow/issues/1) | Durable acceptance record and retrospective summary of exact-SHA review. It is not a standalone review record and does not establish reviewer identity. |
| I5 | [State-synchronization commit `265f171…`](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/265f171502de8a2d8844ae4ccf277c58e56a20cb) | Synchronizes the register after acceptance and distinguishes accepted baseline from later state. |
| I6 | [DR-001 start commit `14293cb…`](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/14293cb67628e934a25fdc8fbe771093855f0876) | Materializes the DR-001 contract and changes its register state to in progress. |
| I7 | [`PROJECT-CHARTER.md` at start SHA](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/PROJECT-CHARTER.md) | Adopted repository authority, roles, state-plane separation, and acceptance semantics. Authoritative for its owned scope. |
| I8 | [`research-evidence.md` at start SHA](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/docs/policies/research-evidence.md) | Adopted research lifecycle and distinction between evidence review and adoption. |
| I9 | [`research-register.md` at start SHA](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/docs/research/research-register.md) | Current repository-owned mutable research state at the evidence basis. |
| I10 | [`ADW-DR-001.md` at start SHA](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/14293cb67628e934a25fdc8fbe771093855f0876/docs/research/ADW-DR-001.md) | Authoritative DR-001 research contract. |
| I11 | [`ADW-BOOTSTRAP-RESEARCH-001.md` at baseline](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/13b05e075ec04aa91494cd18f7d29f7249028cb5/docs/research/ADW-BOOTSTRAP-RESEARCH-001.md) | Bootstrap case-study evidence and publication-time state. Its mutable next-gate text is historical, not current authority. |

### External primary evidence

All sources were accessed and verified on 2026-09-03.

| ID | Source, version/date, canonical URL | Claims supported | Scope, limitation, applicability |
|---|---|---|---|
| E1 | NIST, *SP 800-53 Rev. 5 / Release 5.1.1*, September 2020 with updates; [DOI](https://doi.org/10.6028/NIST.SP.800-53r5) | AC-5 separation of duties; CM-3 authorization, impact review, implementation, documentation and retained change records; CA-2 assessor independence; AU-3 audit provenance; AU-9 protection of audit information; SA-11 verification evidence. | Primary federal security/privacy control catalog. Requirements apply when selected by an applicable regime; they are not automatically universal software-workflow rules. |
| E2 | NIST, *SP 800-53B*, September 2020, updates December 2020; [publication page](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final) | Risk- and impact-based control baselines and documented tailoring. Controls differ across low, moderate, and high-impact baselines. | Federal control baselines, not a task-scoring algorithm. Supports proportionality and documented rationale, not exact small-task thresholds. |
| E3 | NIST, *SP 800-37 Rev. 2*, December 2018; [DOI](https://doi.org/10.6028/NIST.SP.800-37r2) | Current authorization evidence, version/change control, explicit accountable authorization, conflict-aware role assignment, and separation of assessment/remediation from risk acceptance. | Federal information-system risk management. Applicable by analogy to consequential authorization; it does not establish a universal coordinator role. |
| E4 | NIST, *Secure Software Development Framework v1.1, SP 800-218*, February 2022; [DOI](https://doi.org/10.6028/NIST.SP.800-218) | Outcome-oriented, risk-based tailoring; documented requirements, criteria, approvals, rejections, and exceptions. | Recommendations, not a prescriptive workflow. It explicitly leaves implementation formality and applicability context-dependent. |
| E5 | Git project, *Git Data Model*, current documentation checked 2026-09-03; [official documentation](https://git-scm.com/docs/gitdatamodel.html) | Git objects are content-addressed and immutable once created; commits bind a tree and parents; changing a commit creates another identity. | Establishes technical identity and immutability, not authorization, reviewer identity, authenticity, acceptance, or indefinite retention. |
| E6 | Git project, *git-update-ref*, current documentation checked 2026-09-03; [official documentation](https://git-scm.com/docs/git-update-ref) | References are mutable and can be updated with compare-and-swap checks. | Supports separating mutable branch/ref state from immutable commit identity. |
| E7 | GitHub, *Getting permanent links to files*, current documentation checked 2026-09-03; [official documentation](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files) | Branch-based links can change; commit-based links preserve the selected version. | Permanence of addressing does not prove approval, authorship, or continued object availability. |
| E8 | NIST, *AI Risk Management Framework 1.0*, January 2023; [publication page](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) and [Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Documented roles, leadership accountability for risk decisions, and defined human oversight for consequential AI use. | Voluntary AI-specific framework under revision at access time. Supports human-accountability reasoning only in comparable consequential contexts. |

### Secondary or discovery evidence

None was used in a load-bearing conclusion.

## D. Bootstrap lifecycle case study

| Transition | Before | After | Actor/role | Durable evidence | SHA/identity | Date | Exception/correction |
|---|---|---|---|---|---|---|---|
| Research | Bounded bootstrap question; no GitHub artifact | Completed research note awaiting materialization | Research owner recorded as `agentic-development-research` | Publication metadata and report body in I11 | Blob `aac9e88a82521235f7a5445c3029a12d91989b58`; first durable in I2 | Evidence as of 2026-09-02; committed 2026-09-03 06:10:48Z | Pre-commit draft identity and exact completion event are unavailable. |
| Source review | Completed research | Research recorded as reviewed | Independent reviewer asserted; identity unavailable | I9 at I2; I11’s lifecycle assertions | Register blob `b0f3045045a8e84900865c141a0f95f9e4bff35a` | Between 2026-09-02 and 2026-09-03 06:10:48Z | No standalone review record, immutable reviewed-draft digest, verdict body, actor, or timestamp. |
| Adoption | Reviewed research | Specified bootstrap recommendations recorded as accepted for materialization | Coordinator role asserted; decision actor unavailable | I7, initial register at I2, retrospective reference in I4 | `ADW-BOOTSTRAP-ADOPT-001` is a reference, not an addressable GitHub object | Before 2026-09-03 06:10:48Z | No standalone adoption decision body, actor, or timestamp. |
| Execution/materialization | Adopted content contract | Six-file repository candidate | GitHub publishing account `ahtoxaandy999`; functional executor role | I2 and exact six-file tree | `319fdf5ec1449f432ec2196a675640d581a9d6c1` | 2026-09-03 06:10:48Z | Register states candidate was not yet reviewed or accepted. |
| Protection-path correction | Candidate expected branch protection | Corrected candidate under manual SHA freeze | Publishing account `ahtoxaandy999`; maintainer/executor function | I3 diff and corrected register | `13b05e075ec04aa91494cd18f7d29f7249028cb5` | 2026-09-03 07:20:36Z | Branch protection unavailable under recorded plan/configuration; material correction created a new candidate. |
| Exact-SHA candidate review | Frozen candidate awaiting review | Review verdict summarized as acceptable for coordinator acceptance | Independent reviewer asserted; identity unavailable | Retrospective summary in I4 | Target `13b05e075ec04aa91494cd18f7d29f7249028cb5` | Between 07:20:36Z and 07:59:29Z on 2026-09-03 | No separate review object, detailed findings, output, reviewer identity, or exact time. |
| Coordinator acceptance | Reviewed candidate | Baseline accepted | GitHub author/closer `ahtoxaandy999`; coordinator function asserted by record | I4 | Issue ID `5333941581`; decision `ADW-BOOTSTRAP-ACCEPT-001`; accepted SHA `13b05e…` | Created 07:59:29Z; closed 08:01:06Z, 2026-09-03 | GitHub account provenance does not prove separation from executor or reviewer. |
| Durable acceptance record | Acceptance event not separately observable | Addressable audit record | Publisher `ahtoxaandy999` | I4 | Issue #1 | 2026-09-03 | Safest interpretation is that acceptance and its durable record are co-located; no earlier durable acceptance act is visible. |
| Post-acceptance synchronization | Accepted baseline, but baseline register still described review as next gate | Current register records acceptance, completed freeze, and DR-001 readiness | Publishing account `ahtoxaandy999`; state-maintenance function | I5 | `265f171502de8a2d8844ae4ccf277c58e56a20cb` | 2026-09-03 08:03:50Z | Accepted baseline remains `13b05e…`; later state does not replace it. |
| DR-001 durable start | DR-001 planned and unblocked | Contract materialized; research in progress | Publishing account `ahtoxaandy999`; coordinator/research-start functions asserted by artifacts | I6, I9, I10 | `14293cb67628e934a25fdc8fbe771093855f0876` | 2026-09-03 08:43:35Z | Gate IDs exist as references, but no standalone GitHub gate records were found. |

### Missing durable records

No independently addressable GitHub record was found for:

- The pre-materialization source-review verdict, reviewed bytes, reviewer identity, or review timestamp.
- `ADW-BOOTSTRAP-ADOPT-001`.
- `ADW-BOOTSTRAP-PROTECTION-DEC-001`.
- A standalone exact-SHA candidate-review report.
- `ADW-DR-001-GATE-001`.
- `ADW-DR-001-GATE-CORR-001`.
- The identity relationship among researcher, executor, reviewer, coordinator, and human maintainer.

The repository contains one Issue, zero pull requests, zero Issue comments, and no accepted-candidate commit comments. Issue #1 retrospectively summarizes several earlier transitions, but that does not create independent contemporaneous records for them.

## E. Findings by contracted subquestion

### 1. Which state planes and lifecycle transitions require separation?

**Verified facts.** I7 and I8 already distinguish research evidence, research disposition, normative adoption, artifact lifecycle, candidate review, and acceptance. The bootstrap then used distinct commits and Issue #1 for candidate correction, acceptance, and current-state synchronization. E5–E7 establish a separate technical distinction between mutable references and immutable commit identities.

**Inference.** The evidence supports separating at least:

- Evidence production from source review.
- Source review from adoption.
- Authorization from execution.
- Implementation and verification from acceptance.
- Mutable current status from immutable candidate identity.
- Decision authority from mechanical recording.
- Authoritative state from handoff/navigation copies.

These are state and role separations; they do not require a unique person for every state.

**Contrary evidence and limitations.** Neither NIST nor the internal case requires five distinct humans. E3 explicitly permits one person to hold multiple roles where duties do not conflict.

**Confidence:** High for semantic state-plane separation; medium for how it should be instantiated outside the repository’s adopted bootstrap scope.

**Candidate recommendation.** Preserve the semantic separations while permitting compatible roles and lightweight mechanisms to collapse where risk permits.

### 2. Which gates appear invariant and which are conditional?

**Verified facts.** E1 separates controlled-change approval, implementation, assessment, and authorization, but applies controls according to system context. E2 and E4 support risk-based tailoring. E1’s assessor independence is explicitly risk-conditioned. I3 shows a planned protection mechanism had to be replaced when capability assumptions failed.

**Inference.**

- Invariant when the corresponding claim is made: evidence is not adoption; checks are not acceptance; a mutable ref is not an immutable review identity; an actor cannot truthfully be called independent when reviewing its own work; later transitions cannot be inferred merely from earlier completion.
- Conditional: whether formal authorization, independent review, human acceptance, durable decision records, or strong freeze/protection mechanisms are required for a particular task.
- Candidate conditioning dimensions supported directly or by close inference: consequence/impact, uncertainty, privilege, scope, and feasible control strength.
- Reversibility and blast radius are plausible dimensions, but the consulted primary sources do not establish them as standalone mandatory criteria.

**Contrary evidence.** E2 shows that some controls are omitted from low-impact baselines. E4 says not every practice applies with equal formality.

**Confidence:** High for the invariant semantic distinctions and risk tailoring; medium for the candidate dimensions; low for numerical thresholds.

**Candidate recommendation.** Classify gates by semantic necessity and task-specific application. Do not create a normative risk score from this evidence.

### 3. Who may initiate, authorize, execute, review, adopt, accept, and record transitions?

**Verified facts.** I7 assigns framing, adoption, and acceptance to the coordinator; execution to an authorized maintainer or bounded agent; and exact-candidate evaluation to an independent reviewer. E1 requires separation where conflicting duties are identified. E3 permits multi-role assignments without conflicts while retaining accountable authorization.

**Inference.**

- Initiation may come from a requester, coordinator, researcher, or maintainer within a recognized remit.
- Authorization belongs to the accountable scope or risk owner.
- Execution belongs to a bounded executor or maintainer.
- Verification may be performed by the executor or automated mechanisms, but its result is evidence rather than acceptance.
- Independent review requires a conflict-free reviewer when that gate is invoked.
- Adoption and consequential acceptance belong to an accountable coordinator or human decision owner, not to the recommendation’s author merely by implication.
- Recording may be delegated as a clerical act if it faithfully records an already-made decision and does not manufacture authority.

**Limitation.** GitHub shows the same publishing account for all four commits and Issue #1. This neither proves nor disproves actual role independence.

**Confidence:** High for role conflicts; medium for generic role labels outside this repository.

**Candidate recommendation.** Define roles by authority and conflict boundary, not by requiring one person or agent per label.

### 4. Which state requires durable evidence and which may remain ephemeral?

**Verified facts.** E1 requires retained change and audit information for applicable controls; E3 requires current authorization evidence; E5 supplies immutable content identity. I4 demonstrates an addressable acceptance record, while I5 demonstrates the need to update mutable current state separately.

**Inference.**

Durable state or evidence is warranted when later execution, review, authorization, acceptance, audit, or recovery depends on it. Working exploration may remain ephemeral unless it becomes load-bearing.

Likely durable classes include:

- Authoritative objective and scope for consequential work.
- Research contracts and findings.
- Dispositions, authorizations, review results, exceptions, and acceptance decisions.
- Exact candidate identity.
- Verification evidence relied upon by another decision maker.
- Current task status and next gate when coordination persists across sessions.

Likely ephemeral classes include:

- Scratch reasoning.
- Local exploration not cited by a decision.
- Transient navigation or handoff notes that merely point to authority.

**Limitation.** The sources do not define universal retention periods or storage owners.

**Confidence:** High for load-bearing evidence; medium for low-risk task status.

**Candidate recommendation.** Apply durability according to downstream reliance, consequence, and reproducibility.

### 5. What should be the authoritative owner for each state class?

**Verified facts.** I7 and I8 require one authoritative owner for current state and reject competing truth. I9 owns current research status and disposition within the adopted bootstrap repository. E1 and E3 assign decision accountability and record protection to designated organizational roles.

**Inference.**

- Objective/scope and authorization: accountable task or decision owner.
- Research contract and findings: research artifact owner.
- Research disposition and adoption: coordinator or authorized governance owner.
- Working implementation: executor/workspace owner until proposed.
- Candidate identity: version-control object referenced by the task.
- Verification evidence: producer with protected linkage to the candidate.
- Review result: reviewer or review-record owner.
- Acceptance: accountable coordinator/human decision owner.
- Current next gate: a single state-index owner.
- Handoff: no authoritative ownership; it should point to the applicable owner.

**Confidence:** High for single-owner and decision/evidence separation; medium for implementation-specific placement.

**Candidate recommendation.** Assign one authoritative owner class per mutable state class and use references elsewhere.

### 6. Which controls address the named failure modes?

**Verified facts.** The bootstrap exposed a stale next gate, a capability mismatch, a correction before review, a need for exact-SHA freezing, a distinct acceptance record, and post-acceptance synchronization. E1 supports authorization, separation, evidence provenance, and audit protection. E5–E7 support immutable review targets.

**Inference.** Suitable candidate controls are detailed in Section I. No single control solves all failures: immutable identity does not prove approval; an acceptance record does not establish reviewer independence; a current register can still become stale.

**Confidence:** High for the technical and semantic controls; medium for universal application.

### 7. What supports a reduced process for small work?

**Verified facts.** E2 establishes impact-based baselines. E4 explicitly supports varying applicability and formality. E3 permits compatible roles to be combined. No primary source consulted mandates full bootstrap ceremony for every change.

**Inference.** Clear, local, low-impact, readily reversible, mechanically verifiable work may use:

- One bounded authorization artifact instead of separate planning records.
- The same actor for initiation, execution, and verification.
- Automated checks as sufficient verification evidence.
- Ephemeral working notes.
- No independent-review or formal-acceptance artifact when no consequential reliance or conflicting duty exists.

Semantic distinctions still survive: scope precedes mutation; the changed object remains identifiable; verification is not falsely labeled acceptance; and “independent” is not claimed for self-review.

**Contrary evidence.** E1’s change-control requirements can remain stringent where the governing context selects them, regardless of task size.

**Confidence:** High that proportionality is supported; medium for the listed collapse mechanisms; low for exact eligibility thresholds.

**Candidate recommendation.** Permit reduced ceremony through documented tailoring, not by silently skipping an applicable control.

### 8. What minimum task packet permits safe execution by a fresh agent?

**Verified facts.** E1’s assessment and development controls require scope, procedures, roles, criteria, and evidence. E4 calls for known and documented requirements and criteria. The bootstrap required exact repository state and a bounded authorized contract before work began.

**Inference.** A fresh executor needs enough information to identify authority, constrain mutation, verify completion, and stop safely:

- Repository and authoritative owner.
- Baseline/ref.
- Bounded objective.
- Authoritative inputs.
- Allowed scope.
- Non-goals.
- Acceptance criteria.
- Required verification.
- Stop/escalation conditions.
- Required output or evidence destination when durability is needed.

**Negative evidence.** No consulted source proves that every field must be a distinct schema field or separate document.

**Confidence:** High for the information categories; medium for mandatory use on trivial tasks.

**Candidate recommendation.** Treat these as a content minimum for consequential delegated execution, while allowing compatible fields to be combined.

### 9. What minimum evidence packet permits independent review by a fresh reviewer?

**Verified facts.** E1 requires approved assessment scope, procedures, roles, evidence, reporting, and suitable independence. E5–E7 support an immutable target. I4 shows the value—and limitations—of recording a verdict without preserving detailed review evidence.

**Inference.** A fresh reviewer needs:

- Exact immutable target.
- Authoritative requirements.
- Claimed change scope.
- Verification evidence.
- Relevant interfaces and context.
- Review criteria.
- Explicit independence expectation.
- Stop boundary and disposition options.
- A durable place to record findings or verdict when the review is relied upon.

**Negative evidence.** Issue #1 lacks a standalone review body, reviewer identity, and detailed evidence, so the bootstrap cannot establish that its actual review packet was independently reproducible.

**Confidence:** High for target, requirements, evidence, and criteria; medium for document form.

**Candidate recommendation.** Require enough evidence for the reviewer to reproduce the claimed basis without depending on executor chat.

### 10. Which matters remain deferred?

**Verified facts.** The DR-001 contract excludes workflow design, task-schema design, tracker/product selection, Apps, MCP, skills, hooks, automation, orchestration, and later research tasks.

**Unresolved questions.**

- Exact thresholds for invoking formal review or human acceptance.
- Whether reversibility and blast radius should become formal tailoring dimensions.
- Retention periods and evidence-protection strength.
- Concrete state storage and synchronization mechanism.
- Concrete fresh-agent packet schema.
- Enforcement mechanisms for role independence.
- Tool and tracker capabilities.
- Empirical performance costs and benefits of alternative ceremony levels.

**Confidence:** High that these remain unresolved or out of scope.

**Candidate recommendation.** Preserve them as deferred research or later design inputs. Do not infer solutions from this report.

## F. Lifecycle separation evidence

| State/transition | Separation evidence | Classification | Rationale | Evidence |
|---|---|---|---|---|
| Research findings → source review | Internal contract and research policy; assessor independence principles | Evidence supports conditional application | Research relied upon for governance benefits from review; ordinary direct inspection may not require a research lifecycle. | I8, E1 |
| Source review → adoption | Explicitly separate in adopted policy | Evidence supports invariant separation | Evidence adequacy does not itself grant normative authority. | I7, I8, E3 |
| Task framing/authorization → execution | Change authorization and repository role model | Evidence supports conditional application | Formality varies, but an executor needs some bounded authority before consequential mutation. | I7, E1, E4 |
| Execution → verification | Developer testing and evidence requirements | Evidence supports conditional application | Mechanical verification may be performed by the executor; formal separate testing is risk-dependent. | E1, E4 |
| Verification/checks → acceptance | Charter and Issue #1 separately record checks and acceptance | Evidence supports invariant separation | Passing evidence cannot itself identify the accountable risk owner’s decision. | I4, I7, E3 |
| Candidate creation → independent review | Exact-SHA bootstrap review and CA-2 independence | Evidence supports conditional application | Independence is materially useful where consequence or conflict warrants it. | I4, E1 |
| Mutable ref/current status → immutable review target | Git data model and bootstrap SHA freeze | Evidence supports invariant separation when repeatable review is claimed | Branches and status may move; review must bind to an identified object. | I3, E5–E7 |
| Review result → adoption/acceptance | Internal policy and authorization evidence | Evidence supports invariant separation | A reviewer evaluates; the accountable authority decides. | I7, I8, E3 |
| Acceptance → durable acceptance record | Issue #1 and audit-record principles | Evidence supports conditional application | Durable records are strongest where later reliance, audit, or coordination is material. | I4, E1, E3 |
| Acceptance record → current-state synchronization | Bootstrap required a later register commit | Internal case suggests value but external support is insufficient | A separate current-state index can remain stale after an immutable decision record. | I4, I5 |
| Handoff/navigation → authoritative state | Repository authority hierarchy and stale-state controls | Evidence supports invariant separation | Copies aid navigation but create competing truth if treated as authority. | I7, I9 |

## G. Role and transition evidence

| Transition class | Candidate authorized role | Independence requirement | Evidence strength | Limitations |
|---|---|---|---|---|
| Initiate bounded work | Requester, coordinator, researcher, or maintainer within remit | None inherently | Medium | Initiation authority is organization-specific. |
| Authorize execution | Accountable scope/risk owner; repository coordinator in current adopted context | Separate from executor where conflicting duty or consequence warrants | High for conflict principle; medium generically | No universal coordinator model. |
| Execute | Authorized maintainer or bounded executor | Cannot manufacture or expand its own authority | High internally | Same person may also initiate or verify low-risk work. |
| Verify | Executor, test system, or separate verifier | Separate verifier conditional on risk | High | Verification is evidence, not acceptance. |
| Independent review | Conflict-free reviewer | Required for the review to be described as independent | High | Whether the gate is necessary is conditional. |
| Adopt research | Coordinator or authorized governance owner | Researcher cannot self-adopt merely by publishing | High internally | External frameworks use different role names. |
| Accept consequential candidate | Accountable coordinator/human decision owner | Separate from executor/reviewer where self-interest or consequence creates conflict | Medium-high | Generic human-acceptance threshold remains unresolved. |
| Record a decision | Designated record/state maintainer | May be delegated if purely clerical | Medium | Record provenance must not be confused with decision authority. |
| Synchronize mutable state | Owner or maintainer of the authoritative state index | No separate person necessarily required | Medium | External support for a distinct synchronization gate is limited. |

Role separation is not equivalent to person separation. One actor may hold multiple compatible roles. The key constraint is that incompatible claims—especially independence and accountable acceptance—must not be manufactured by relabeling self-action.

## H. Durability and ownership evidence

| State class | Candidate durability class | Candidate authoritative owner class | Duplication risk | Evidence |
|---|---|---|---|---|
| Task objective/scope | Durable authoritative state for consequential/delegated work; conditional for trivial work | Task/coordinator owner | Competing scope in chat or handoff | I7, E1, E4 |
| Task status | Durable authoritative state when work crosses sessions/actors | Single state-index owner | Stale tracker/chat/register copies | I9, I5 |
| Research contract | Durable authoritative state | Research-contract owner | Research drifting beyond authorization | I10 |
| Research findings | Durable evidence | Research artifact owner | Summaries becoming uncited substitutes | I8, E1 |
| Research disposition | Durable authoritative decision state | Coordinator/governance owner | Publication status confused with current disposition | I8, I9 |
| Execution authorization | Durable for consequential work; lightweight reference may suffice for small work | Accountable scope/risk owner | Executor interpreting chat as authority | E1, E3, E4 |
| Implementation working notes | Ephemeral unless made load-bearing | Executor/workspace | Old notes mistaken for current state | E4 |
| Candidate identity | Durable immutable reference | Version-control object plus task reference | Moving branch reviewed instead of exact content | I3, E5–E7 |
| Verification results | Durable evidence when relied upon | Evidence producer with candidate linkage | Results detached from candidate or environment | E1 |
| Independent review result | Durable evidence when relied upon | Reviewer/review-record owner | Retrospective summary without reproducible basis | I4, E1 |
| Acceptance decision | Durable authoritative state for consequential acceptance | Accountable coordinator/human | Checks or merges treated as implicit acceptance | I4, I7, E3 |
| Current next gate | Durable authoritative state when coordination persists | Single state-index owner | Stale mutable copies; historical snapshot treated as current | I5, I9, I11 |
| Handoff/navigation information | Ephemeral or durable reference only | No decision authority; pointer maintainer | Competing truth and stale context | I7 |
| Local worktree state | Ephemeral working state unless promoted to candidate | Executor | Uncommitted state mistaken for shared evidence | E5 |

No concrete tracker or storage product is selected.

## I. Failure modes and controls

| Failure mode | Observed/internal evidence | External support | Candidate control | Classification |
|---|---|---|---|---|
| Competing truth | I7 rejects duplicate authority; I9 owns current research state | E1/E3 require designated records and accountability | One owner per mutable state; other locations carry references | Evidence supports invariant separation |
| Stale chat or memory | Repository hierarchy rejects chat as authority | E3 requires current evidence | Re-read the authoritative source at the transition gate | Evidence supports invariant separation for state-dependent decisions |
| Executor self-acceptance | Charter forbids implied self-acceptance; GitHub cannot prove actual independence | E1/E3 conflict and authorization controls | Separate verification from acceptance; require conflict-free reviewer/acceptor when invoked | Conditional gate; semantic distinction invariant |
| Implicit lifecycle transition | Research review does not imply adoption; checks do not imply acceptance | E1/E3 require explicit decisions | Record explicit transition, authority, target, result, and date for material decisions | Conditional durability; invariant semantics |
| Review of mutable targets | Manual SHA freeze used before review | E5–E7 | Review an exact immutable identity; material changes create a new candidate | Invariant for repeatable formal review |
| Passing checks mistaken for acceptance | I4 separately lists checks and acceptance | E3 separates assessment from authorization | Label checks as evidence and require a distinct acceptance event when acceptance is needed | Evidence supports invariant separation |
| Capability/protection mismatch | I2 expected protection; I3 records unavailability; I1 reports `protected: false` | E4 supports context-aware tailoring | Verify capability before relying on it; record bounded exception and compensating control | Conditional/configuration-dependent |
| Stale mutable next gate | Accepted SHA retained pre-acceptance register state until I5 | General current-evidence principles in E3 | Synchronize the authoritative state index promptly; expose pending-sync state | Internal case suggests value; universal requirement unresolved |
| Dangling decision/gate references | Several IDs lack standalone GitHub objects | E1 audit provenance controls | For material decisions, make references resolve to addressable records with actor, target, date, and outcome | Conditional |
| Durable record without independence provenance | Issue #1 is addressable but reviewer identity is missing | E1 assessor-independence evidence | Preserve reviewer identity or declared relationship where independence is relied upon | Conditional |

## J. Small-task proportionality

### Separation that appears irreducible

Even for small work, the following distinctions should remain intelligible:

- Some bounded objective and authority must precede mutation.
- The changed object must be identifiable.
- Verification evidence must not be mislabeled as independent review or acceptance.
- Mutable current state must not silently override an immutable reviewed object.
- A handoff or chat summary must not displace the authoritative source.

These distinctions can exist within one lightweight artifact and do not require separate ceremonies.

### Ceremony that may plausibly collapse

For clear, local, low-impact, readily reversible, mechanically verifiable work:

- One actor may initiate, execute, and verify.
- A task request may carry both scope and authorization.
- Working notes may remain ephemeral.
- Automated checks may provide sufficient verification.
- A separate independent-review gate may be omitted.
- A formal acceptance record may be omitted if no consequential reliance or governance requirement exists.
- Status and next-step state may remain local if no cross-session coordination depends on them.

### Unsupported or unresolved

- No primary source establishes a universal definition of “small.”
- No supported numerical threshold exists for consequence, uncertainty, reversibility, or blast radius.
- Reversibility and blast radius are reasonable candidate considerations, but direct external support as independent decision dimensions is insufficient.
- The bootstrap’s full ceremony is not evidence of proportionality for ordinary development.

This section is evidence for tailoring, not a complete small-task workflow.

## K. Minimum fresh-agent context

### Execution context

| Candidate minimum field | Evidence basis | Confidence/qualification |
|---|---|---|
| Repository and authoritative state owner | I7, I9 | High for cross-agent work |
| Baseline/ref | I3, E5–E7 | High where repository state matters |
| Bounded objective | I10, E1, E4 | High |
| Authoritative inputs | I7, E3 | High |
| Allowed scope | I10, E1 | High |
| Non-goals | I10; bootstrap scope discipline | Medium-high |
| Acceptance criteria | E1, E4 | High |
| Required verification | E1, E4 | High |
| Stop/escalation conditions | I10; risk/accountability principles | Medium-high |
| Required evidence/output destination | E1, E3 | Conditional on downstream reliance |

A single task contract or message may combine these categories. The evidence does not require a fixed schema.

### Independent review context

| Candidate minimum field | Evidence basis | Confidence/qualification |
|---|---|---|
| Exact immutable target | I3, E5–E7 | High |
| Authoritative requirements | I7, I10, E1 | High |
| Claimed scope | E1, E4 | High |
| Verification evidence linked to target | E1 | High |
| Relevant interfaces and context | E1 assessment-scope principles | Medium-high |
| Review criteria | E1, E4 | High |
| Independence expectation and conflicts | E1, E3 | High when independence is claimed |
| Stop boundary and allowed dispositions | I7, I10 | Medium-high |
| Durable findings/verdict destination | E1, I4 | Conditional on reliance and consequence |

The Issue #1 review summary is insufficient to prove that a fresh reviewer could reproduce the bootstrap review: detailed findings, reviewed inputs, and reviewer identity are missing.

## L. Contradictions, negative evidence, and gaps

| ID | Classification | Gap or negative evidence | Affected conclusion | Materiality | Effect on recommendation | Resolving evidence |
|---|---|---|---|---|---|---|
| G1 | Absence of evidence | No standalone bootstrap source-review record or reviewed-draft identity | Provenance of source-review transition | High | Narrow claims to “recorded as reviewed” | Contemporaneous review artifact with target, reviewer, date, criteria, and verdict |
| G2 | Absence of evidence | `ADW-BOOTSTRAP-ADOPT-001` is not an addressable GitHub object | Adoption actor, rationale, and time | High | Do not infer coordinator identity from the reference alone | Durable adoption decision |
| G3 | Absence of evidence | Protection decision ID lacks standalone record | Decision rationale beyond register summary | Medium | Rely only on the committed correction | Addressable capability/exception decision |
| G4 | Absence of evidence | Exact-SHA review exists only as an acceptance-record summary | Independence and reproducibility | High | Block claims that reviewer identity was durably proven | Standalone review record and evidence packet |
| G5 | Absence of evidence | DR-001 gate and correction IDs lack standalone records | Full authorization provenance for starting research | Medium | Contract and register prove durable start, not complete pre-start gate history | Durable gate records |
| G6 | Configuration-dependent evidence | `main` currently reports unprotected; detailed protection endpoint access is limited and ruleset capability was plan-dependent | Reliability of enforced freeze/protection | Medium | Any protection recommendation must be conditional | Effective configuration export or verified ruleset/protection record |
| G7 | Stale evidence | Accepted baseline register correctly preserves pre-acceptance state but became stale as current state until I5 | Current next gate | Medium | Require current-state lookup; do not rewrite accepted baseline | Timely authoritative synchronization |
| G8 | Stale evidence | Bootstrap report’s final next gate remains a publication snapshot | Use of research report as current status | Medium | Treat report status as historical | Current register or explicit disposition record |
| G9 | Absence of evidence | All durable GitHub events use one publishing account | Role/person independence | High | Do not claim self-review or independence as fact | Actor attestations or separate authenticated review/decision records |
| G10 | Contrary to overbroad ceremony | NIST baselines and SSDF permit risk-based tailoring | Universal formal review for every task | High | Narrows recommendation to conditional application | Context-specific risk and governance requirements |
| G11 | Absence of evidence | No supported universal small-task threshold or scoring model | Proportionality mechanism | High | Blocks normative thresholds | Later empirical or governance research |
| G12 | Absence of evidence | Reversibility and blast radius lack direct support as standalone criteria | Candidate tailoring dimensions | Medium | Keep as hypotheses | Primary control or empirical evidence |
| G13 | Unavailable/unresolved | Retention duration and record owner are organization-defined | Durability implementation | Medium | Recommend durable classes, not retention periods | Applicable legal, contractual, and organizational requirements |
| G14 | Technical limitation | Commit identity does not prove authorship, approval, acceptance, reviewer identity, or permanent availability | Immutable-target conclusions | Medium | Use SHA only as content identity | Signatures, protected retention, and separate decision records where required |
| G15 | Dependency on deferred research | Concrete state store, task schema, and enforcement mechanism are excluded | Implementation feasibility | High for design, not findings | No product or schema recommendation | Later accepted research/design task |

No material contradiction with the accepted bootstrap baseline was found. Therefore:

- `COORDINATOR CONTRADICTION GATE REQUIRED` is **not triggered**.
- Missing provenance remains an explicit limitation.
- Historical stale states are explained by later correction or synchronization and are not silently rewritten.

## M. Deferred dependencies

The following remain intentionally deferred:

- Workflow v1 sequencing or state-machine design.
- Normative risk scoring or small-task thresholds.
- Concrete task or evidence schemas.
- Tracker or source-of-truth product selection.
- Apps, MCP servers, skills, hooks, and automation.
- Parallel-agent or AFK orchestration.
- Branch-protection implementation selection.
- Concrete synchronization or dual-write architecture.
- Identity, signing, and reviewer-authentication mechanisms.
- Empirical comparison of alternative ceremony levels.
- DR-002, DR-003, DR-004, and DR-005.

No later research task was created or started.

## N. Candidate recommendations

All recommendations are proposed and non-normative.

1. **Preserve distinct state planes for evidence, disposition, authorization, candidate identity, verification, review, and acceptance.**  
   Evidence: I7–I10, E1, E3. Strength: high. Tradeoff: more explicit state management. Boundary: not a Workflow v1 sequence.

2. **Give each mutable state class one authoritative owner and make other copies references.**  
   Evidence: I7, I9, G7–G8. Strength: high internally. Tradeoff: consumers must resolve references. Dependency: concrete storage remains deferred.

3. **Bind a formal review to an immutable candidate identity.**  
   Evidence: I3–I4, E5–E7. Strength: high. Tradeoff: material corrections require a new candidate and potentially new review. Boundary: an SHA proves content identity, not approval.

4. **Keep verification, review, and acceptance semantically distinct.**  
   Evidence: I4, I7, E1, E3. Strength: high. Tradeoff: potentially additional transition records. Boundary: small work may omit formal review or acceptance rather than falsely conflate them.

5. **Use conflict-free independent review when consequence, uncertainty, privilege, or applicable governance warrants it.**  
   Evidence: E1–E3. Strength: high for the principle, medium for invocation criteria. Tradeoff: latency and reviewer cost. Dependency: thresholds remain deferred.

6. **Reserve consequential authorization and acceptance for an accountable coordinator or human risk owner.**  
   Evidence: I7, E3, E8. Strength: medium-high. Tradeoff: creates a human/coordinator gate. Boundary: evidence does not require human acceptance for every ordinary change.

7. **Preserve addressable records for material authorizations, exceptions, reviews, adoption, and acceptance.**  
   Evidence: I4, E1, E3, G1–G5. Strength: high. Tradeoff: record maintenance. Boundary: retention periods and tools are unresolved.

8. **Tailor ceremony according to documented context and risk rather than task size alone.**  
   Evidence: E2, E4. Strength: high. Tradeoff: requires judgment and rationale. Boundary: no scoring algorithm is proposed.

9. **Verify that a proposed enforcement control is actually available before relying on it.**  
   Evidence: I2–I3, I1. Strength: high internally. Tradeoff: capability checks and exception handling. Boundary: no protection product or mechanism is selected.

10. **Re-read live authoritative state at transition gates and after acceptance.**  
    Evidence: I4–I6, G7–G8, E3. Strength: medium-high. Tradeoff: extra reads and synchronization discipline. Boundary: a distinct synchronization gate is not proven universally necessary.

11. **Give fresh executors and reviewers self-sufficient bounded packets.**  
    Evidence: E1, E4, I10, G4. Strength: high for information categories. Tradeoff: preparation effort. Boundary: no fixed schema is proposed.

12. **Treat chat, memory, local worktrees, and handoffs as working or navigation state unless explicitly promoted.**  
    Evidence: I7, I9, E3, E5. Strength: high internally. Tradeoff: users must follow references. Boundary: these media may still contain useful non-authoritative context.
