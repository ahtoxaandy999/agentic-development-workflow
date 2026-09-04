---
id: ADW-WF1-TOOLING-DESIGN-001
artifact: tooling-enforcement-design
artifact_status: draft
authority: evidence
maturity: bootstrap
owner: chatgpt-coordinator
normative_effect: none
design_stage: initial-design-complete
produced_on: 2026-09-04
gate_ref: docs/design/ADW-WF1-TOOLING-DESIGN-GATE-001.md
gate_commit: 5ddab4017fa3ef871c7221de112b9e7d5cf66c84
gate_blob: 9a899597471b8ad9cd48ebf59b974dbaeefa1bf5
gate_sha256: aa813bc57c3499f4908e3c1310bbd48fad0cc38ea9b624f1c90897655951059e
design_execution_base: 5ddab4017fa3ef871c7221de112b9e7d5cf66c84
register_ref: docs/research/research-register.md
register_blob_at_design: d8291147cae64954c1b9f313d685879284451391
workflow_design_ref: docs/design/ADW-WF1-DESIGN-001.md
workflow_design_subject_commit: 2b9532682ae77bf5037f1b2fa45b720e5865d0ad
workflow_design_blob: afed983e7632caf3169dcbac7a80f8da8226d86d
dr005_disposition_ref: docs/research/ADW-DR-005-DISPOSITION-001.md
dr005_disposition_basis_commit: e39befb0d9e13b8b556c98ac4dc5d8c118db4b0c
dr005_disposition_blob: 70cea63938bf4a8b908904d2b9c7b0c9aec1b401
supersedes: null
---

# Initial Workflow v1 tooling/enforcement design

Task: ADW-WF1-TOOLING-DESIGN-001. Repository: `ahtoxaandy999/agentic-development-workflow`. Intended later destination: `docs/design/ADW-WF1-TOOLING-DESIGN-001.md`.

## 1. Proposal and authority

This proposal resolves the initial representation and placement choices within S1/S5 and qualified S2/S3/S4/S6. It specifies repository Markdown records, exact Git identities, retained secret-safe evidence, one task-state recorder and manually supplied accountable decisions. Existing connected reads and supervised Codex are interfaces to those records. No new service, controller, validator, permission profile or integration is a component of the initial architecture.

All prescriptive language below describes proposed design behavior, not adopted operating policy or permission to implement it. The document owns this proposal and its design-stage metadata only. The Research Register retains current research dispositions, dependencies, controlling pointers and the ADW repository next gate. This document is neither an operational task record nor a second current-state tracker. Its observations are dated evidence snapshots.

The fixed tooling-design gate authorizes production and producer checking of this one local proposal. Persistence, immutable candidate creation, fresh independent candidate review, coordinator design disposition, implementation/control validation, normative adoption and baseline acceptance remain separate. The producer cannot supply its own independent review or acceptance. The local file digest is not a repository candidate SHA.

## 2. Verified entry basis and input bindings

The connected **@GitHub** app was explicitly invoked through read-only `github_fetch` and `github_fetch_file` operations. The entire gate and every artifact in its exact-input table were retrieved and read at the design-execution base below. Local clones, synced sources, chat, memory and general web search did not establish repository state. Local hashing operated on the content returned by the app; it did not substitute a local authority source.

Entry verification completed by **2026-09-04 10:20:27 UTC**. Final delivery rechecks are recorded in section 15.

| Observation | Verified value |
|---|---|
| Live main / design-execution base | `5ddab4017fa3ef871c7221de112b9e7d5cf66c84` |
| Main tree | `6d1c8857ca2bb22a5530720b6869608c970cfaea` |
| Sole parent / gate historical subject | `e39befb0d9e13b8b556c98ac4dc5d8c118db4b0c` |
| Current Register blob | `d8291147cae64954c1b9f313d685879284451391` |
| Repository and DR-005 current next gate | Workflow v1 tooling/enforcement design execution |
| Durable gate pointer / task ID | `docs/design/ADW-WF1-TOOLING-DESIGN-GATE-001.md` / `ADW-WF1-TOOLING-DESIGN-GATE-001` |
| Gate decision | `authorize-initial-tooling-enforcement-design` |
| DR-005 | reviewed / accepted / satisfied; `accept-scoped-dr-005-tooling-recommendations-for-design` |
| Workflow v1 | non-normative, unadopted, unimplemented |
| Branch response | `protected: false`; `protection.enabled: false`; required-status-check enforcement `off`; empty contexts/checks |
| Accepted bootstrap baseline, unchanged | `13b05e075ec04aa91494cd18f7d29f7249028cb5` |

The comparison from the historical gate subject to the execution base contains one commit, adding only the gate and modifying the Register. The Register diff adds the gate pointer/task ID, changes both current next-gate fields to design execution and states the bounded authorization. No unrelated content changed. Historical pre-persistence language inside fixed evidence and decisions does not compete with the current Register.

The complete recursive tree has 27 entries and `truncated: false`. The refs collection contains only `refs/heads/main`. All-state PRs and releases are empty. All-state Issues contain only closed bootstrap acceptance Issue #1, with zero comments and explicit exclusion of tooling/Workflow v1 adoption and new write authority. README points current work to the Register. No competing current tooling decision or existing substantive tooling design appears in these accessible repository owners, tree, refs and collections. This does not assert knowledge of unseen local drafts or inaccessible external records.

The private-plan protection limitation is preserved as a governance constraint. The fresh observation is the branch response above; no billing, entitlement, administrative-rule audit or rejection test occurred.

### 2.1 Exact inputs

All current-path reads use execution base `5ddab4017fa3ef871c7221de112b9e7d5cf66c84`. The accepted semantic subject was additionally read at `2b9532682ae77bf5037f1b2fa45b720e5865d0ad`, frozen DR-005 at `38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958`, and its disposition at `e39befb0d9e13b8b556c98ac4dc5d8c118db4b0c`; each matches its current-path content and blob.

| Path | Git blob | Role and binding result |
|---|---|---|
| `AGENTS.md` | `2294f13982045c54f3cb50071ab71373a3366c89` | Agent boundaries; match |
| `PROJECT-CHARTER.md` | `c521f6869662f39106bcac0365426eb0e9bdb327` | Normative authority/scope/acceptance; match |
| `docs/policies/research-evidence.md` | `90572c47463f2d2adc493f9978c1c720fd8f8275` | Normative evidence/freshness/promotion; match |
| `docs/research/research-register.md` | `d8291147cae64954c1b9f313d685879284451391` | Current owner; expected post-persistence identity |
| `docs/design/ADW-WF1-TOOLING-DESIGN-GATE-001.md` | `9a899597471b8ad9cd48ebf59b974dbaeefa1bf5` | Controlling complete contract; match |
| `docs/design/ADW-WF1-DESIGN-001.md` | `afed983e7632caf3169dcbac7a80f8da8226d86d` | Accepted exact semantic subject; match |
| `docs/design/ADW-WF1-DESIGN-REVIEW-004.md` | `3cdb92769bb955c8782dfa504843fd32a4736168` | Binds exact semantic subject/parent/path/blob/digest; match |
| `docs/design/ADW-WF1-DESIGN-DISPOSITION-001.md` | `35d3a8ba5c3901e90d070b000659541b1ef4975c` | Accepts exact initial semantic design and review-004; match |
| `docs/research/ADW-DR-005.md` | `615692060c7bf9d7372d5469550176f22caca9be` | Frozen evidence; match |
| `docs/research/ADW-DR-005-SOURCE-REVIEW-001.md` | `5dec63eccc9f219bfb3d04a288c747547a39ee4e` | Binds frozen report; match |
| `docs/research/ADW-DR-005-DISPOSITION-001.md` | `70cea63938bf4a8b908904d2b9c7b0c9aec1b401` | Controls scoped S/C/D/X/RG/DI dispositions; match |

Computed from app-returned UTF-8 content; all eight recomputed Git blob hashes match the returned identities:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Gate | 45768 | `aa813bc57c3499f4908e3c1310bbd48fad0cc38ea9b624f1c90897655951059e` |
| Register | 47602 | `5659ed361163468f68ecf9d79ad3c6b75657894b6eb387e657ab0363bda355e4` |
| Semantic design | 109600 | `f8ddb3626868289e44251088a2ddad291ce762dbb58ec824d70c5de5a7994411` |
| Semantic review-004 | 17172 | `4dc55616925a9989a7ea5745b835ce03df6bd45228aededf1803f5efd7750dad` |
| Semantic disposition | 24971 | `4e4c2ff69e19e6cc0aa1775ba983696bf5967ad44ff1428c993afd86ecdb82b2` |
| DR-005 | 149389 | `3c83c5b2ceea4ce0c545f2516287aa8c4ecc3f119e55de01597ac5a66a73163c` |
| DR-005 source review | 63238 | `e6557d10f8a2618fc9e79d40894e398405db4b253af5cdd54530c751a94357e9` |
| DR-005 disposition | 57631 | `14e9cd835add6b55c9227ffd06bc4c133e55647d157a36e0b1a27b3207e7ae63` |

The semantic review verdict is `accept-candidate-for-design-disposition`, and the semantic decision is `accept-initial-tool-agnostic-workflow-v1-design`. The DR-005 review verdict is `accepted-as-source-reviewed-evidence`. Both reviews have zero blocker, major and minor findings. Those existing verdicts supply their scoped inputs; this producer does not repeat their reviews. Historical MAJ-001 through MAJ-005 treatment remains in the semantic disposition and review-004. The resulting integrated-verification, intervention, reset and episode-reopening obligations are preserved below.

Source links: [execution base](https://github.com/ahtoxaandy999/agentic-development-workflow/tree/5ddab4017fa3ef871c7221de112b9e7d5cf66c84), [gate](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/5ddab4017fa3ef871c7221de112b9e7d5cf66c84/docs/design/ADW-WF1-TOOLING-DESIGN-GATE-001.md), [Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/5ddab4017fa3ef871c7221de112b9e7d5cf66c84/docs/research/research-register.md), [semantic subject](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md), [tooling disposition](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/e39befb0d9e13b8b556c98ac4dc5d8c118db4b0c/docs/research/ADW-DR-005-DISPOSITION-001.md), [live branch](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/branches/main), [persistence comparison](https://github.com/ahtoxaandy999/agentic-development-workflow/compare/e39befb0d9e13b8b556c98ac4dc5d8c118db4b0c...5ddab4017fa3ef871c7221de112b9e7d5cf66c84).

## 3. Concrete initial architecture decisions

The TD identifiers below are proposal-local traceability labels, not adopted ADRs or independent selection decisions.

| ID | Resolved choice | Consequence |
|---|---|---|
| TD-01 | One repository Markdown control record per future product task, with fixed record/evidence conventions below | No Issue, chat or runner field becomes a second current owner |
| TD-02 | One named execution-state recorder performs all current control-file updates; decision and evidence authorities supply separately attributable inputs | No controller or side-effect owner becomes a co-writer of task/cancellation/recovery |
| TD-03 | Immutable contract revisions, decisions, transition events and evidence manifests; mutable control file holds only current projections and exact references | Corrections append successors and preserve historical subjects |
| TD-04 | Exact full Git SHAs for all repository candidates; single-parent, exact-delta, non-transforming narrow persistence model | No implicit merge/rebase/squash strategy or PR dependency |
| TD-05 | Repository-native retained evidence in the affected repository, with manifests and digest/size binding | A payload that cannot be safely retained there blocks reliance pending a separate storage decision |
| TD-06 | Manual pointer handoff and current-owner rehydration through existing eligible interfaces | No generated index, context service or automation becomes authoritative |
| TD-07 | Existing supervised executor receives a bounded assignment and verified surface-specific prerequisites | Unknown effects/permissions/exclusivity deny the affected action |
| TD-08 | Accepted cancellation/recovery transitions represented by linked immutable events and episodes, with one current projection | Requests, acknowledgement, containment, recovery, reset and closure remain distinct |
| TD-09 | One decomposition snapshot and one join decision for each task composition; exact obligation accounting | Missing dependencies and unsatisfied integrated verification deny downstream success; no parallel execution is enabled |
| TD-10 | Every reliance gate carries applicability, satisfaction, freshness and exact evidence references | Missing/skipped/failed/stale differs from pass and from legitimate non-applicability |
| TD-11 | No conditional/deferred integration is part of the initial dependency graph | Gaps produce denials or later prerequisites, never silent selection |

The information flow is: current authoritative owners -> exact-source rehydration -> bounded supervised work -> immutable producer evidence -> separately authorized candidate persistence -> fresh independent review -> separately authorized disposition. Raw process/platform observations feed the named decision/evidence owners. They do not directly advance the task's semantic state.

## 4. Placement and sole ownership

### 4.1 Fixed conventions for later product materialization

Let `P` be the explicitly authorized affected product repository and `T` its allocated task ID. No product is selected here. Within P, the proposed root is **`docs/adw/tasks/<T>/`**. The following conventions are fixed design choices, not choices left to implementers:

| Location | Content and authority |
|---|---|
| `control.md` | Sole current product-task record; current plane values, current exact pointers, open obligations and product-task next gate |
| `records/<record-id>.md` | Immutable semantic records: contract revision, readiness, authorization, ownership transfer, transition, candidate binding, impact analysis, review assignment, review, disposition, join, custody, resumption and terminal accounting |
| `evidence/<evidence-id>/manifest.md` | Immutable evidence package identity, subject, provenance, observations/results, payload inventory and publication-time custody requirements |
| `evidence/<evidence-id>/raw/<payload-name>` | Secret-safe retained payload bytes: textual output or other already available evidence; no executable validator or generated runtime is implied |

Record, evidence, operation, run and recovery-episode IDs are distinct opaque identifiers allocated once by the recorder, unique within the task and never reused. An ID gives addressability, not trust. A collision blocks publication. A future materialization gate must check the exact root for an existing owner; collision or an already authoritative task elsewhere requires owner resolution, not overwriting or duplicating it. No new global task index is selected. The task's explicit root pointer is the discovery entry.

Every repository evidence pointer is the tuple **repository, full containing commit SHA, path, blob, fragment when useful**. A relied-upon payload also carries byte count and SHA-256. A current-owner pointer additionally names its authoritative mutable ref and the last observed exact ref SHA; the latter is an observation, never a promise that the ref stayed still. Human-readable links accompany tuples but never replace identities.

The control file does not contain a purported hash of its own enclosing commit. Its revision is supplied by the live GitHub read. Each update identifies the previous control revision by full containing SHA/path/blob. New records may use relative links to other bytes in the same commit; the effective exact enclosing SHA is supplied from GitHub after persistence. Such links are not relied upon before readback. Evidence about a candidate always names an already existing full SHA; it never needs to embed its own future enclosing SHA.

### 4.2 Owner-placement matrix

`R` means the single named recorder for the task, appointed in the task contract and bounded persistence authorization. `A` means the task-contract authority; domain, review, integration and custody roles must be bound to named accountable actors before reliance. A role label alone does not appoint anyone. Current representations below are separate state classes in one file; decision records are historical immutable inputs, not competing current fields. A recorder's faithful update is not authority to make the supplied decision.

| State class | Sole current placement | Decision authority / sole recorder and permitted updater | Immutable basis; references and freshness |
|---|---|---|---|
| Task contract, objective, scope, constraints | `control.md`: `contract_ref` -> immutable contract revision | A owns content; R alone updates pointer on A's decision | Exact contract and authority; executor notes are references; changed scope denies old authorization |
| Readiness | `control.md`: `readiness_ref` and task-control projection | A; R alone records | Readiness finding tied to exact contract, criteria and unknowns; missing critical input denies ready |
| Authorization and task gate | `control.md`: `authorization_ref`, `gate_refs`, `product_task_next_gate` | Authorized coordinator/risk owner; R alone records | Exact bounded grant and gate evaluations; capability/host approval is not a grant; revocation/staleness denies dispatch |
| Task-control/execution progress | `control.md`: task-control plane, current run/operation pointers | Execution-control decision authority; R is sole execution-state recorder/updater | Immutable transition events and domain observations; UI progress is observation only |
| Cancellation | `control.md`: cancellation plane, current cancellation request/ack/domain references | Authorized cancellation/controller/domain findings; R alone records composite transition | Request, all-domain acknowledgement, containment and residual inventory; uncertainty prevents advancement |
| Recovery | `control.md`: recovery plane, current episode pointer, open obligations | State/side-effect owner and required risk authority decide; R alone records | Distinct episode authorization, attempts, target validation and intervention; prior success cannot discharge new obligation |
| Decomposition and dependencies | `control.md`: `decomposition_ref`, per-dependency result references | Named task/decomposition authority; R alone records | Immutable graph snapshot and dependency evaluations; child summaries do not satisfy obligations |
| Work product | `control.md`: work-product plane and output/candidate reference; mutable working bytes remain in the named executor's authorized local output location | Executor owns working bytes; R alone records current semantic pointer | Output manifest or exact candidate; local file is working output until immutable repository identity exists |
| Candidate/current candidate/supersession | `control.md`: `candidate_ref`, supersession reference | Named candidate-record authority under A; R alone updates | Immutable candidate binding record with C/base/tree/scope; candidate content has no mutable owner |
| Verification and current evidence references | `control.md`: verification plane and obligation/evidence map | Named verification-record authority, with verifier producing results; R alone records current projection | Immutable reports by subject/criterion/run; changed subject or required inputs invalidates current pass |
| Independent review/current review reference | `control.md`: review plane, assignment and review references | Review authority appoints; conflict-free reviewer owns verdict; R alone records current pointer | Exact unchanged candidate and review assignment/verdict; producer has no independent-review authority |
| Disposition | `control.md`: disposition plane and current decision reference | Authorized coordinator/accountable owner; R alone records | Immutable subject/scope decision; never derived from checks or persistence |
| Join/integration | `control.md`: join plane and `join_ref` | One named aggregation/integration authority; R alone records | Exact membership, results, I and integrated-verification gate; missing/failed/stale required work prevents pass |
| Normativity | `control.md`: normative plane as explicit reference-derived projection | Applicable adopted normative owner/adoption record; R only records supported reference | The normative owner remains in its existing authorized path; no normative owner is created here; absent adoption remains non-normative |
| Baseline acceptance | `control.md`: baseline plane and acceptance reference | Designated baseline-acceptance authority; R only records supported reference | Exact-SHA acceptance record in the applicable existing owner; no new owner inferred; bootstrap Issue #1 remains ADW's existing record |
| Custody/access/retention commitments | `control.md`: `custody_refs` keyed by evidence ID | Named evidence custodian decides; R alone records current commitment pointer | Immutable custody/redaction/retrieval records; custodian gains no authority over the underlying verdict |
| External side-effect/control state | Relevant live system, under its accountable domain/control owner | Only its separately authorized operator may change it; R cannot change it by recording | Timestamped observation in evidence package; task file references observation and handling obligations, never owns external state |
| ADW research dispositions, dependencies, pointers, current repository next gate | Existing `docs/research/research-register.md` in ADW | Existing Register governance/maintainer under separate exact-base authority; product R cannot update it | Existing fixed research/review/disposition records; product task next gate has no ADW gate effect |

All current task fields are written through R. Decision authorities author or approve fixed records within their own scope; evidence producers supply explicitly attributed content. No cryptographic signing mechanism is selected. R's role as persistence recorder does not transfer the originating decision authority. A later review record can be faithfully persisted by an executor without that executor becoming the reviewer.

For this ADW design stream, the product-task conventions are only proposed. The existing gate, proposal, review/disposition destinations and Register remain the actual artifact owners. No `control.md` is created for this task. Its proposal does not take ownership of the gate or a mutable acceptance status.

### 4.3 Updates, conflicts and transfer

R reads the live owning ref and exact previous control revision before each separately authorized update. It verifies current authority, affected evidence, the transition's source tuple and all guards, then proposes one replacement control snapshot plus new immutable records/payloads. It records old/new values, decision/evidence references, actor, time, scope and reason in a transition record. Prior immutable bytes are not edited; an error receives a successor/correction record with an explicit supersedes relation and impact assessment. Git history is retained; no force rewrite or deletion is part of this design.

Each persistence is independently subject to section 10, including control/evidence-only updates. This is deliberately low-throughput and does not assume continuous write authority. If a required transition cannot be made durable under current authority, new dependent effects stop. The executor can stop initiating effects and report a block without waiting for record publication; that report does not count as durable state. Only already authorized containment may proceed while evidence is preserved and a record-persistence decision is obtained. No emergency write power is invented.

If an Issue, runner, chat or another file claims the same current field, do not choose the newest timestamp or synchronize both. Deny dependent reliance and mutation, retain both claims as evidence, and ask the existing accountable owner to resolve authority. A labeled stale view can be ignored after the actual owner is verified; two credible owner claims require a decision.

Transfer requires a fixed decision naming state class, old/new owner and recorder, exact prior revision, effective point, affected in-flight effects, reconciled pending writes and evidence custody. The old recorder ceases updates; the new recorder verifies cessation/exclusivity and reads the reconciled state. Until all prerequisites hold, the old owner remains authoritative and affected mutations remain blocked. The effective semantic transfer is indivisible: there is never an interval authorizing both recorders. This is a procedural contract, not an atomic platform transfer or writer fence. Changing to Issue/external ownership requires a separate selection/migration gate. No transfer occurs here.

## 5. S2 task-control representation and lifecycle

### 5.1 Representation shape

The future `control.md` uses Markdown with a small metadata block for identifiers/references and tables for the state vector, obligations and current pointers. This is a prose-defined representation inside this proposal; no parser, standalone schema or operational sample is supplied.

| Portion | Required meaning and fields |
|---|---|
| Identity/ownership | task ID, product repository and authorized mutable ref, task root, A, R, applicable domain/review/integration/custody role bindings; previous exact control revision |
| Framing references | exact contract revision, readiness decision, assumptions/unknowns, scope and criteria references; material unknowns resolved, bounded into separately authorized learning, or blocking |
| Authority references | current bounded authorization, exact authorized execution base, named executor/supervisor, allowed files/actions/effect surfaces, ceilings, expiry/revocation conditions, stopping/escalation and evidence destinations |
| State vector | all ten accepted planes listed below; every value links to its last applicable transition or authoritative projection basis |
| Current subject pointers | run and operation IDs; output manifest; candidate C; verification obligations/results; review assignment/verdict; disposition; join I; cancellation inventory; recovery episode; custody commitments |
| Dependencies and open obligations | exact graph reference; per required/optional dependency result and validation; residual effects and responsible owners; unsatisfied gates with safe next action |
| Product continuation | product-task next gate, its decision reference and allowed next action; explicit declaration that it is not the ADW Register gate |

Fixed records store full contract content and decisions so the current file does not duplicate editable scope or verdict prose. A projection repeats a state label only as the single current value derived from its exact evidence/decision; changing the projection cannot amend the fixed decision. Current references are mutable under explicit authority. Historical records and published evidence are immutable. Working drafts and scratch output remain non-authoritative until promoted through a permitted exact persistence.

| Plane | Exact accepted vocabulary |
|---|---|
| task control | framing; ready; authorized; active; blocked; recovering; completed; cancelled; abandoned |
| work product | none; working; proposed-output; candidate-identified; superseded |
| verification | not-invoked; pending; passed; failed; stale |
| review | not-evaluated; not-applicable; required-pending; passed; rejected; stale |
| disposition | none; pending; accepted; rejected; deferred; superseded |
| normative status | non-normative; adopted; superseded |
| baseline acceptance | not-applicable; pending; accepted-exact-identity; rejected; superseded |
| join | not-applicable; planned; branches-active; pending; passed; partial; failed; conflicted |
| cancellation | none; requested; acknowledged; contained; residual-effects |
| recovery | not-applicable; assessment; retry-authorized; reconciling; compensated; recovered; intervention-required |

The presence of a value in this vocabulary does not enable the mode it describes. In particular, the record can describe a denied parallel plan or non-passing join; there is no initial authorized transition into parallel operation. Normative/adopted and baseline-accepted values require external applicable owner records; none is produced by this proposal.

### 5.2 Gate and event representation

A fixed gate-evaluation record contains: gate ID; named transition; exact subject tuple and scope; governing rule/authority; evaluator and decision owner; evaluation time; applicability (`required` or `not-applicable`); applicability rationale; satisfaction (`passed` or `unsatisfied`, only for required); relied-upon input/configuration/dependency identities and freshness (`current` or `stale`); evidence references; exceptions/open conditions; permitted destination if effective. Missing criteria, owner, identity or essential evidence invalidates it. An invalid pass is not retained as a usable pass.

The current verification projection is passed only when every required obligation has an actual current pass on the correct subject. Failed required work yields failed; changed relied-upon basis yields stale; incomplete/missing/skipped work yields pending or failed according to its actual result, never passed. A legitimate N/A is an explicit gate decision under an applicable rule; verification stays not-invoked for that omitted gate. Aggregate green output is merely an observation. With mixed obligations, N/A rows are excluded with their rationale and cannot offset any unsatisfied required row.

A transition event includes source and destination plane values, retained planes, exact prior control revision, task/run/operation/episode identifiers, decision reference, required domain findings, timestamp, recorder, reason and open obligations. A denial can be recorded with unchanged values and a blocked-next-action finding. Composite changes to task/cancellation/recovery are one semantic event and one control snapshot; independent domain acknowledgements remain evidence until the complete aggregate guard holds.

### 5.3 Lifecycle, applicability and correction

Frame -> ready requires A's executable/verifiable contract and classified unknowns. Ready -> authorized requires a separate current grant. Authorized -> active requires the dispatch decision, fresh identities/dependencies/permissions/exclusivity and applicable effective gates. Execution may refine only decisions explicitly left within scope; material new intent returns to A. Producer output moves work product to proposed-output and records verification honestly. Candidate identity exists only after authorized immutable persistence. Review applicability and conflict-free assignment precede any claimed independent result. Disposition, adoption, baseline acceptance and terminal task accounting remain separate.

The accepted semantic design's transition table is incorporated by exact reference, including its allowed sources, retained planes and invalid conditions. This representation introduces no additional transition. Sections 6-10 concretize its evidence and action boundaries; section 8 spells out its interruption/recovery cases. Unsupported source/destination pairs are denied. Reframing or reauthorization cannot bypass intervention, required recovery or containment.

Contract correction creates a new immutable revision and impact record. Readiness/authorization tied to the old revision cannot silently authorize the new one. Candidate correction creates a new C. Evidence/decision correction creates a new fixed record, preserving the old record's exact subject and verdict as historical; current pointers move only with the relevant authority and invalidation assessment. A terminal task's history is never erased to recycle its ID. New work after terminal closure requires a new bounded contract/task identity or a separately authorized semantic change; this design invents no terminal-to-active transition.

All material authority, relied-upon gates, cancellation/recovery evidence, review/disposition and cross-session state must be durable before dependent reliance. Disposable reasoning can remain local. Record size and ceremony can scale by combining related sections in a fixed record; required meanings, exact bindings and owner boundaries cannot be omitted.

## 6. Exact identity, verification, integration and publication

### 6.1 Identity relationships

The letters below are descriptive placeholders, not actual task records or abbreviated substitutes for stored full SHAs.

| Symbol | Representation and relationship |
|---|---|
| B | Full authorized execution/persistence base SHA, repository/ref, exact authority/control input references and allowed delta |
| W | Mutable local output; local absolute path, byte count/digest and proposed repository path. W is not a Git candidate |
| C | Immutable repository candidate: full commit SHA, sole parent B for the initial narrow persistence path, tree SHA and complete allowed-path blob/delta manifest |
| V | Verification record's subject: W for pre-persistence byte/content checks, or C for candidate checks; exact criteria/scope/run/configuration and evidence are explicit |
| Rv | Review record's subject: exact unchanged C, with defined scope and load-bearing base/input assumptions, reviewer assignment and evidence links |
| I | Exact integration subject; for a narrow non-composing persistence, I is C if an integration subject is relevant. A composition must identify all component results and exact integrated commit |
| Ppub | Actual published ref target returned/read through GitHub for the particular authorized publication; for the initial non-transforming path Ppub must equal C |
| Ecommit | A later commit storing evidence, review, decisions or current pointers about C. Ecommit differs from C and is not automatically reviewed, verified or accepted by evidence about C |

The initial path allows only a single-parent exact-delta persistence, without rebasing, squashing, merge commits, cherry-picking or implicit content transformation. All untouched tree entries must match B; changed entries must exactly match the authorized manifest. The later persistence gate supplies the actual currently available permitted operation and target ref within S1; this proposal selects no new client/ref wrapper or PR transport. If that operation cannot satisfy the contract, the assignment is blocked. No atomic compare-and-swap or technical fence is claimed.

Pre-persistence V(W) establishes properties of the local bytes and intended delta. It does not claim that a not-yet-existing C passed candidate checks. After persistence, readback proves which C was produced and whether its parent/tree/path/blob/content matches B plus the approved delta. A fixed candidate-binding/verification record explicitly relates V(W) to C. Byte equality can carry the checked document/content properties; it cannot prove commit provenance, runtime behavior or unrelated tree properties. Those require their own checks on C. A digest alone cannot upgrade W into C.

In this design lifecycle, candidate persistence precedes independent review. Publishing a non-normative proposal as a candidate therefore does not claim prior independent review or accepted integration. The later review is assigned to the returned exact C. If the intended effect requires review before publication, that is not satisfied by this candidate-persistence procedure: deny that publication until a separately authorized strategy and required evidence exist. No routine product publication strategy is activated here.

For any claim that the tested, reviewed and finally published repository candidate is the same subject, require **V.subject = Rv.subject = I = Ppub = C**, where the relevant gates apply, with matching scope and current assumptions. A gate may be legitimately N/A only by its recorded governing rule, not because equality is inconvenient. If a publication changes identity, equivalence is not assumed from equal file contents or trees. It creates a new candidate and requires explicit impact analysis, affected verification and applicable fresh review; the initial publication assignment stops rather than adapting itself.

An Ecommit that adds a review about C can retain C's exact review as historical evidence, but cannot claim that Ecommit's full repository state has received that review. Current-main acceptance must name and review the actual current candidate when required. Acceptance of a fixed C can name C while later evidence commits exist; it is never acceptance of whatever `main` resolves to. Evidence persistence does not rewrite the reviewed file merely to add a review status or its own SHA.

### 6.2 Invalidation and supported carry-forward

Before dispatch, resumption, persistence/publication, verification reliance, review, join and disposition/acceptance, reread current authority and every mutable dimension relied upon. Record observed ref/base, candidate head where applicable, contract/configuration versions, dependencies and evidence availability. All expected identities must match the assignment. A moved base before a bounded persistence invalidates that assignment even if a diff looks harmless; return for impact and fresh authority. There is no automatic rebase or retry.

Changed C invalidates prior current verification/review references for the new subject. Changed criteria, environment, dependency, governing rule or other load-bearing assumption can invalidate evidence even when C is unchanged. Wrong or inaccessible evidence denies reliance. Prior records remain available under their original identities; no verdict is edited from stale to passed.

Carry-forward is a new explicit claim: name old/new subjects, exact unaffected paths/properties, old evidence, unchanged criteria/configuration/inputs and the impact argument; identify the accountable verifier/review authority accepting its applicability. R records that decision. Affected checks run again. A formal review whose target or load-bearing basis changed requires applicable renewed review; the old verdict never simply changes subjects. Producer assertions cannot approve review carry-forward on behalf of the review authority.

### 6.3 Dependencies and joins without parallel enablement

The immutable decomposition record lists each unit's outcome and rationale, owner, input/output identities, read/write/effect domains, interfaces, dependencies, required/optional classification, local checks, integration point and final outcome criteria. Vertical slices remain a conditional preference; enabling/learning/infrastructure units have explicit value and dependencies. No universal size or concurrency number is introduced.

A dependency evaluation names the exact required result and specified validation state. Missing, partial, cancelled, failed, stale or substituted results cannot satisfy a required edge. The aggregation authority accounts for every declared unit in a fixed join record, including omissions, conflicts, side effects and exclusions. Required local evidence and current dependency identities precede a positive decision on I.

Required integrated verification must actually pass for exact I before join=passed. Failed integrated verification makes the join failed for I; pending/stale verification leaves it non-passing; missing required results produce partial/failed; unresolved ownership/content conflicts produce conflicted. Legitimate integrated-verification N/A retains the rule and rationale and leaves verification not-invoked for that gate. A material change to I or relied-upon evidence invalidates a previous join pass and returns it to pending for reevaluation.

Candidate formation, completion, publication reliance and disposition cannot rely on a non-passing join. An optional omission is recorded as omitted/N/A, never as a successful result. Reusing sound partial outputs or reducing the objective requires exact identity, impact assessment and explicit reframing/authorization. No scheduler, parallel workspace arrangement or automatic aggregation is selected; requested parallel execution remains denied under the present boundary.

## 7. Minimum durable evidence and custody contract

### 7.1 Common package

Each evidence manifest records its ID/type, task/contract/run/operation/episode as applicable, exact subject and scope, expected versus observed preconditions, source interface and retrieval/request/command description, observation time and relevant clock limitations, producing actor/role and authority reference, actual tool/runtime/configuration/input identities relied upon (including model identity/configuration when load-bearing), results and limitations, exceptions/unknowns, and payload inventory. Each payload has a relative path, media/encoding description, byte count and SHA-256. The persisted package is identified by containing commit/path/blob; an expiring source URL is provenance only.

The manifest records publication-time custodian, authorized readers, redaction treatment, retention obligation and required retrieval points. Subsequent custody changes are separate fixed records referenced by `control.md.custody_refs`. Neither a manifest nor a Git hash proves authenticity, independence, sufficient verification, availability or retention. The named owner must expectation-check producer/role/source provenance and actual access before relying on the claim. No signing or attestation system is selected.

Initial custody is repository-native: retain necessary secret-safe raw results with the corresponding manifest in P. The evidence custodian is accountable for accessibility, retention and integrity for the documented reliance interval. The authorization must establish that this repository is suitable for that content and those readers. If material cannot safely fit or remain accessible under that arrangement, block affected reliance and return for a separate bounded custody/storage decision. C6 or another external store is not silently activated. Logs in a local task window alone do not satisfy later-session custody.

### 7.2 Per-class records, producers and timing

All locations below are beneath the fixed task root from section 4.1. R performs any authorized persistence; the listed producer/decision owner remains attributable and accountable for its content.

| Evidence class and placement | Subject and minimum class-specific content | Producer / decision owner; durable timing |
|---|---|---|
| Producer verification: `evidence/<id>/manifest.md` plus `raw/` | W or C/I; enumerated required obligations and N/A decisions; actual executed method/command/request, input/checkout identity, run/attempt ID, versions/configuration, output, exit/conclusion, failures/skips, criteria coverage, limitations and impact/carry-forward references | Assigned verifier, possibly executor; capture before candidate promotion, review, join or other reliance |
| Candidate binding: `records/<id>.md` | B, W manifest/digest, C, parent/tree, allowed versus actual complete delta, path/blobs, V(W)-to-C relation, Ppub/readback, pending gates | Candidate-record authority using executor/readback evidence; durable before formal candidate review/reliance |
| Review assignment and independent review: separate `records/<id>.md` plus any evidence package | Assignment authority; named eligible reviewer and provenance/conflict assessment; no authorship/execution/acceptance stake; exact C/scope/requirements/criteria/inputs/V; read-before/after identity checks; findings, verdict, limitations and stop boundary | Review authority appoints; conflict-free reviewer authors verdict; assignment before review, result before disposition relies on it |
| Disposition: `records/<id>.md` | Exact C and scope, required gate outcomes and N/A rationales, exact review/evidence records, deciding owner/authority, accepted/rejected/deferred conclusion, conditions/residual risk and non-implications | Coordinator/accountable risk owner distinct from producer acceptance; before any reliance on decision |
| Interruption/generic stop: transition `records/<id>.md` and observation package | Trigger, current tuple, run/operation/domain inventory, last safe state, in-flight effects, observed progress/ceilings, allowed emergency containment, evidence gaps and escalation destination | Executor/controller supplies trigger/observations; R records blocked without changing cancellation; preserve immediately, persist before continuation or cross-session reliance |
| Cancellation request/acknowledgement: distinct transition records and observation packages | Authorizing requester; requested scope; per-domain controller/operation IDs; delivery versus acknowledgement evidence; complete inventory and unacknowledged domains | Authorized requester/controller; R records only the warranted aggregate; durable before treating a request/acknowledgement as a prerequisite |
| Containment: transition record plus domain findings | Every affected local/process/subprocess/queue/remote domain; observation methods/times, cessation or bounded isolation, continuing/unknown effects, residual effect IDs and owners, resource restrictions | Each domain owner supplies authoritative findings; R records aggregate only after all findings; durable before containment-dependent action/release/closure |
| Recovery: linked episode records plus attempt/validation evidence | Episode ID, predecessor if any, obligation ID and origin/distinction, prior-effect classification, authority/action scope, stable identifiers/version/deduplication conditions, target, attempts and observed effects, compensation, residual obligations, intervention and conclusion | State/side-effect owner authorizes and validates; risk owner decides where required; R records all current-plane transitions; each prerequisite/attempt outcome durable before dependent retry, conclusion or resumption |
| Rehydration: `evidence/<id>/manifest.md` | Supplied pointer set, actual current ref/control identities, authoritative sources read, critical evidence retrieval/digest results, authority/configuration/dependency checks, differences from summary and allowed/denied next action | Receiving actor produces; current state owners resolve conflicts; durable before consequential fresh-context continuation relies on it |
| Join: `records/<id>.md` plus integration evidence | Exact membership/results/status of each required/optional unit, conflicts/exclusions, dependency/effect accounting, exact I, integrated verification and current gate outcome | Named aggregation/integration authority; durable before join pass or downstream reliance |
| Resumption/terminal accounting: `records/<id>.md` | Explicit decision, current authorization, tuple, required recovery/containment/obligations, output/verification/join results, residual-risk disposition, retained resources/evidence, successor responsibility and next gate | Authorized task/execution-control owner, plus required risk owner; R records reset or terminal change; durable before resumption/closure reliance |
| Custody/redaction/retrieval: `records/<id>.md` and package metadata | Payload identity, owner/readers, retention trigger/interval, access test, redaction scope, retrieval digest/size result, expiry/unavailability and authorized treatment | Evidence custodian; before evidence is relied upon and at every specified continuation/retention boundary |

Review findings are fixed evidence authored by the reviewer. A separate current pointer can select a successor review; it cannot rewrite the old verdict. A reviewer must read the entire assigned required scope, not merely accept the producer's conformance table. A fresh context or display name does not prove independence; a documented conflict-free eligible assignment can satisfy the particular review while RG4 remains unresolved for general platform enforcement.

### 7.3 Failure and retention behavior

At reliance, retrieve the actual bytes through an authorized source; verify exact commit/path/blob and payload digest/size, provenance, access permission and current retention commitment. Missing, expired, inaccessible, mismatched or insufficiently redacted evidence invalidates the dependent gate. Name the custodian and missing item, preserve safe available evidence, and stop reliance. Do not replace absent raw results with a recollection or turn a mismatch into a warning-only pass.

Redact before repository persistence. Retained output is called raw only to the extent it is the actual secret-safe tool result; transformed/redacted output is identified as a derivative with its method, omissions and digest. Do not retain secret originals to prove a digest. If redaction removes a load-bearing fact that cannot be established safely, the affected conclusion is blocked. A custody correction produces a successor; it cannot conceal uncertainty or claim the historical source was always different. Exposure handling belongs to the responsible security owner under separate authority.

Retention duration is supplied contextually, not a universal number or promise of permanent storage. The custodian must support all specified downstream review/audit/recovery/continuation reliance; cleanup cannot delete required history while those obligations remain. Proposed cleanup, archival or migration requires its own authority and retrieval/accounting evidence. A successful retrieval now establishes only that retrieval, not resolution of RG8.

## 8. Stop, cancellation, recovery and terminal behavior

### 8.1 Recording the accepted transitions

For readability, tuples below are task-control / cancellation / recovery. The same transitions and guards as the accepted semantic design apply. A controller reports facts and a domain owner makes its scoped decision; only R changes the current tuple.

| Event | Permitted tuple change and required evidence |
|---|---|
| Generic stop | `active / c / r -> blocked / c / r`; preserve reason, last safe state, operations, effects and escalation. Local cessation makes no cancellation/containment claim |
| Request cancellation | `active or blocked / none / r -> blocked / requested / r`; authorized requester and complete intended domain inventory |
| Acknowledge | `blocked / requested / r -> blocked / acknowledged / r`; every relevant controller received and acted on the request. Partial acknowledgements are recorded as evidence without aggregate advance |
| Verify containment | `blocked / acknowledged / r -> blocked / contained or residual-effects / r`; all domains observed ceased/bounded. Unknown/continuing domains retain acknowledged. Residual-effects means verified containment with durable effects requiring handling |
| Begin recovery | `blocked / none, contained or residual-effects / not-applicable, intervention-required or recovered -> recovering / cancellation unchanged / assessment`; operation classification, effects, authorized scope/target, domain owners and containment predicates. Entry from recovered additionally requires the reopening guard below |
| Authorize action | `recovering / c / assessment -> recovering / c / retry-authorized or reconciling`; c is none/contained/residual-effects; operation-specific authority, prior effects and applicable deduplication/version preconditions |
| Record action | `recovering / c / retry-authorized or reconciling -> recovering / c / compensated or reconciling`; actual attempt/effect evidence. Compensation is a new authorized effect, not proof of reversal |
| Conclude recovery | `recovering / c / assessment, retry-authorized, reconciling or compensated -> blocked / c / recovered`; authoritative validation of the episode's target, required reconciliation and residual-risk disposition |
| Require intervention | From any of those four active recovery phases -> `blocked / c / intervention-required`; missing/conflicting evidence or authority, affected obligations and accountable decision owner. Successful validation is not required to record a block |
| Ordinary dispatch/resume | `authorized or blocked / none / not-applicable or recovered -> active / none / not-applicable`; explicit current dispatch/resumption authority, fresh prerequisites and complete required recovery |
| Cancellation-specific resume | `blocked / contained / not-applicable or recovered`, or `blocked / residual-effects / recovered` -> `active / none / not-applicable`; explicit resumption, verified containment, completed required handling, accepted/assigned residual risk and safe resources |

No recovery transition accepts cancellation=requested or acknowledged. Unknown containment denies retry, resumption, terminal closure and release of resources required for containment/reconciliation. If effects become newly uncertain while recovery is active, stop safe continuation and record the appropriate intervention/block; do not infer a containment value from a process exit. A record only describes available findings; it does not make the interruption control effective.

### 8.2 Episode identity and reopening

An episode is represented by an immutable opening record and a chain of attempt, intervention, validation and conclusion records carrying the same episode ID. `control.md` carries only the current episode pointer and recovery value; the records retain completed episodes and open residual obligations. Resuming from intervention renews the same unfinished episode after a fresh bounded decision addresses its blocker. It does not erase failed attempts or call the episode complete.

Reopening from `blocked / {none, contained, residual-effects} / recovered` creates a **new episode ID** only with positive evidence that the prior episode completed against its authorized target and that the new obligation is materially distinct or arose/was discovered afterward. The opening record links the completed predecessor and its validation, the new obligation/evidence, domain owners, bounded authority and new target. The prior episode stays completed. Mere reconsideration, an unresolved part of the prior target or a desire to reset the display does not qualify.

Cancellation request/acknowledgement retains recovered and cannot reopen. All-domain containment must first establish contained/residual-effects. Once reopened, the ordinary action/conclusion/intervention rules apply to the new episode. A retained old recovered value cannot satisfy a newly required obligation or permit resumption/completion/cancellation/abandonment while that obligation remains unsatisfied.

Before any retry, the domain owner classifies the operation as safely repeatable, conditionally repeatable with explicit identity/deduplication/version conditions, compensatable but not reversible, irreversible, nondeterministic or ambiguous. Ambiguous completion denies blind retry; inspection/reconciliation or a different authorized recovery action must first establish a safe basis. No generic retry count, automatic retry loop or autonomous compensation is selected.

Intervention is always `blocked / cancellation unchanged / intervention-required`, never a persistent recovering/intervention-required combination. Permitted next actions are fresh authorized renewal into assessment, remaining blocked/escalated, authorized cancellation from none followed by its protocol, or a separately guarded terminal decision. Unavailable risk authority means continued blocking. Reframing cannot launder intervention into active work.

### 8.3 Reset and terminal guards

Both resumption paths explicitly set active/none/not-applicable in the same transition. Reset is prohibited from incomplete recovery or intervention. It retains episode identities, decisions, attempts, effects, validation and outstanding assigned/accepted residual obligations; it does not accept risk or erase history. A later independent failure stops to blocked/none/not-applicable and can start a newly authorized episode. Terminal closure retains current recovery/cancellation values instead of applying this reset.

Complete task requires active or blocked with cancellation=none, objective/output/verification/join/effect/evidence accounting, no incomplete required recovery/intervention or hidden effect, and task-owner authority. Completed means the bounded assignment ended with its accounting; it does not accept a candidate.

Close cancelled requires blocked/contained with recovery not-applicable or recovered, or blocked/residual-effects/recovered; all-domain containment, complete required handling/reconciliation, terminal accounting and explicit task/execution-control closure authority are independent guards. Residual effects additionally require durable owners/obligations and accountable risk disposition. Request, acknowledgement, active recovery or stale old recovery success cannot close cancellation.

Abandon requires an explicit task-contract-owner discontinuation decision from framing/ready/authorized/blocked; no active/recovering work; cancellation none or verified containment; complete required recovery/residual-effect handling; output/dependency/evidence accounting and successor/no-successor responsibility. Executor preference or an unavailable owner is insufficient. Neither abandonment nor cancellation may release containment-critical resources while effects are unbounded.

## 9. Coordinator, fresh contexts and supervised executor

### 9.1 Interfaces and handoff

The persistent coordinator interface frames authorized work and presents decision requests/results. Fresh design, research, execution and review contexts read their own assignments and exact sources. Existing eligible Projects/Work/Codex surfaces may display and export artifacts; they own no current ADW or product task field. A fresh research context requires its own research authorization; this task launches none. A new/forked context alone cannot establish reviewer independence.

The minimal handoff contains: repository and authorized current ref; exact task root/control revision or, for this design stream, Register/gate pointers; accepted baseline and exact critical subjects; assignment/role/authority reference and scope; evidence root/custodian; expected next gate and stop boundary; unresolved blockers/obligations as navigation. It links the canonical records rather than copying their current fields into another editable list. No new helper, automation or service builds the handoff. Fewer duplicated pointers is a representation choice, not a measured productivity claim.

The receiving actor: (1) verifies live ref and reads governing instructions/owners; (2) follows the current Register or product control pointer; (3) retrieves exact contract/authorization, subject, review/disposition and critical evidence; (4) checks digests, access/custody and current authority/configuration/dependencies; (5) reconstructs all applicable planes, cancellation/recovery history and open obligations; (6) reconciles summary discrepancies under the owner hierarchy; (7) records the rehydration evidence and allowed/denied next action before consequential continuation. Readiness does not substitute for authorization.

Critical missing/stale authority, identity, evidence, dependency or containment blocks continuation. A non-authoritative stale summary may be corrected after exact owners agree. Conflicting actual owners require owner resolution. Surface unavailability permits only an already authorized equivalent interface with the same exact-source/access guarantees; otherwise stop. It grants no installation, connector scope expansion or background continuation. Before leaving a surface, the producing actor and custodian ensure relied-upon outputs are exported to the permitted evidence destination; transcripts alone are insufficient.

### 9.2 Bounded supervised Codex assignment

The existing Codex executor may produce local work and producer checks only under its explicit assignment. Every effectful assignment must bind: task/contract revision, repository and full B, executor/R/supervisor and escalation owner, allowed paths/deltas/actions/effect domains, exact inputs, observable criteria/checks, evidence/custody destination, applicable ceilings and observation method, approval prerequisites, stop/revocation boundary and permitted emergency containment. It excludes recursive delegation, automatic retry, self-acceptance and independent review of its own output. All proposed repository effects require section 10 authority.

The task owner supplies contextual time/resource/effect ceilings and the expected supervision/response arrangement before dispatch. No universal timer, retry budget, concurrency number, token allowance, review count or risk score is adopted. An unspecified ceiling that is material to the proposed effect, or inability to observe/enforce a required ceiling, denies that effect. A supervised deterministic content/byte check remains producer verification; it does not become controller-driven workflow automation.

Before reliance, the runtime/security owner supplies a dated inventory of actual host/client/runtime versions, chosen local/cloud execution surface, managed and user configuration/precedence, enabled tools, credential identities/scopes without secret values, account/workspace/region/entitlement where relevant, repository permissions, network path/control coverage, and compatible component versions. The executor checks the effective facts for each allowed effect, not just requested settings. Evidence of forbidden-action rejection/escalation and containment must come from separately authorized validation where the assignment relies on that enforcement; no such trial is authorized here.

| Effect surface | Required assignment-specific evidence before an effect |
|---|---|
| Local files/processes | Authorized roots/files, actual runtime/configuration, subprocess behavior, current workspace/process ownership and relevant containment/ceiling evidence |
| Git metadata/remote refs | Exact repository/base/ref/delta; named serialized executor; actual credential/ref reach and exclusive-use evidence; fresh owner state and permitted persistence operation |
| Network | Actual allowed destinations and enforcement path/configuration where relied upon; external effects, credentials and observing/containing owners |
| Connector/App/MCP | Actual exposed tools, scopes and credential owner; read versus mutation authority; independent permission/denial coverage and effect evidence |
| Browser | Actual profile/account/session and reachable application effects; site permission boundaries, backend effect ownership and containment evidence |
| Cloud/remote work | Actual runtime/worker/tools/configuration, remote queues/processes/credentials, observation/cancellation coverage and retained evidence |

Unknown coverage denies the affected action. An instruction, sandbox label, host approval or authentication success is not proof of coverage across these surfaces. Existing host-required tool approval remains in force independently; C11 auto-review remains deferred and is not selected as an ADW control. This task observed connected reads and local producer byte/file operations only; it does not certify installed security, routine execution or cross-surface enforcement.

Mandatory stops include stale/unverifiable basis, unexpected scope/content, competing owner or writer, authority loss, unknown external effect, missing required evidence/dependency, unsafe secret handling, ceiling breach, failed required verification invalidating continuation and an authorized cancellation request. Stop new effects, preserve available evidence and escalate to the named owner. Stop does not grant recovery or additional permissions.

## 10. Separately authorized serialized exact-base persistence

This is a description of the presently permitted narrow governance path. It is not authorization to execute it, and not a reusable routine direct-main workflow. It applies separately to proposal, evidence, review, disposition, control-record or Register persistence. Every mutation needs its own exact bounded grant.

### 10.1 Required gate contents

A persistence gate must name the repository, currently verified full B and target ref; exact source artifact/path/bytes/SHA-256/serialization if applicable; allowed repository paths and exact intended deltas, including any Register delta; designated bounded executor and the person responsible for serialization; current-owner and accepted-input evidence; verification requirements; permitted operation/effect surfaces/credentials and prerequisites; supervision; exclusivity evidence; stop conditions; post-operation readback and the next stop boundary. It also states whether the effect merely persists an unreviewed candidate or relies on existing review/disposition, and supplies any review required before that effect.

No field is inferred from the previous successful gate. The canonical source must exist and its identity must be verified before asking for final persistence authorization. The authorizer must be authorized for the effect and must preserve review/acceptance separation. This proposal supplies no actual new mutation grant.

### 10.2 Determined procedure

1. Rehydrate through @GitHub. Verify current ref equals B, current owners/Register/control and all governing identities, protection observation, expected path existence and complete allowed delta. Verify canonical bytes and serialization. Any drift, collision or unrelated delta stops the assignment; no rebase or scope expansion.
2. Establish the named single executor's serialized window. Inventory and account for relevant processes/workspaces, shared Git metadata/refs, credentials, remote actors/jobs and in-flight effects that could mutate the scope. The responsible runtime/repository owner supplies current evidence of exclusive use and stop/revocation handling. An assignment label or worktree name is insufficient. Uncertain exclusivity blocks this particular persistence.
3. Prepare only the authorized single-parent C from B and approved source/delta through the already permitted S1 surface. Check the complete proposed tree/delta and any available immutable object identity before moving a ref. Object creation is itself a repository write and requires the gate. Do not use an unselected wrapper, PR/queue, hook, Action or custom client to fill a gap.
4. Immediately before the authorized ref-affecting operation, reread B and the relied-upon owner/authority/exclusivity state. Proceed only if unchanged and all preconditions still hold. If the available permitted operation combines commit creation and ref update, the gate must explicitly cover that combined effect; preflight uses the exact intended bytes/delta and no prior-C claim. No technical atomicity is inferred for either operation shape.
5. Perform only the granted persistence. On an error, timeout or ambiguous response, stop and inspect through @GitHub before any further effect. Record possible objects/ref effects; never blindly repeat a mutation. Any recovery or renewed attempt requires operation-specific evidence and authority.
6. Read the actual ref, full C, parent(s), tree, changed/unchanged entries and published bytes through @GitHub. Require sole parent B, exact allowed delta and Ppub=C. Recompute byte/blob/digest identities where relied upon. Check intended Register/control changes faithfully and all excluded content unchanged. Record any remaining limitation and unexpected side effect.
7. Return the full resulting candidate SHA and producer/readback evidence, then stop. Do not perform review, acceptance, correction, follow-on Register work or another gate. A mismatch is a failure requiring escalation; readback cannot retroactively authorize a wrong publication. Do not automatically revert it.

The semantic procedure is one exact-base, exact-delta persistence; the tool's object-creation/readback shape is a gate-supplied operational fact, not an alternative mechanism architecture. If pre-publication requirements cannot be met with that surface, deny the assignment rather than weaken them. A changed base before any mutation blocks execution; drift detected after mutation blocks readiness/acceptance claims and requires accounting of the actual effect.

### 10.3 Procedural limits and downstream gates

Supervision and serialization are procedural controls. They do not prevent an unobserved competing credential/process from writing; manual SHA reads leave a check-to-write race; a branch flag does not establish effective protection; post-write readback detects some mismatches but cannot undo an unauthorized publication. This design claims no remote expected-old-SHA guarantee, global lock, technical fence or protected integration. RG1-RG3 remain unresolved.

The narrow path can create a non-normative candidate under its own explicit gate despite the current protection constraint. It cannot be repurposed for routine product writes/dogfooding, parallel execution, automated writes or unattended/AFK work. Fresh independent review follows the exact immutable candidate; coordinator disposition, any implementation/adoption and any baseline acceptance remain independent decisions. No next gate is executed in this task.

## 11. Scoped RG consequences and later validation obligations

This section is a fixed design trace to **DR-005 disposition section F and tooling-design gate section F**, not a mutable gap register. No RG gap is resolved. RG1-RG9 and RG12 retain their blocking dispositions in the specified scopes. RG10/RG11 remain non-blocking for the minimum design and block their optional candidates. A successful future test supplies evidence only; the proper owner must separately disposition the gap and authorize any operation.

| Gap | Concrete design consequence / denied reliance | Later responsible owner, required evidence and validation obligation |
|---|---|---|
| RG1 protection | Section 10 remains narrow/procedural; no protected integration, routine/dogfooding, parallel, automated or AFK authority | Repository owner: actual entitlement, adopted protection/bypass requirements and effective configuration; separately authorized isolated rejection tests for unauthorized, stale and failing changes. No plan/ruleset is chosen here |
| RG2 writer fencing | R is one recorder, not a technical lock. Unknown process/workspace/ref/credential exclusivity blocks the specific serialized assignment; no exclusive-writer or parallel/automated assurance | Runtime/execution owner: actual mutation boundary and ownership/identity controls; competing/stale-writer, process/credential, loss and revocation tests with retained evidence. A worktree/CODEOWNERS label cannot satisfy them |
| RG3 exact integration publication | B/W/C/V/Rv/I/Ppub relationships in section 6 and full readback in section 10; mismatched or unproved mapping denies publication/integration/join/acceptance reliance | Integration owner: explicitly adopted applicable publication strategy, complete subject/base/integration/final mapping; moved-base/head, changed-candidate and publication-path-drift tests. Post-write detection cannot cure invalid publication |
| RG4 reviewer identity | Exact review assignment and conflict test required; producer/forked self-review denied. Particular eligible conflict-free review can be supported without resolving general identity enforcement | Review/coordinator and repository owners: independently attributable role and platform identity mapping, conflict assessment, actual approval/staleness/bypass validation wherever relied upon |
| RG5 cross-surface permissions | Section 9 inventory required; unknown effectful surface denied. Local output/reads do not certify runtime permissions or routine/parallel/automated/AFK expansion | Security/runtime owner: actual versions, managed/user configuration, tool/credential inventory per surface; separately authorized isolated forbidden-action and escalation tests, recording coverage exceptions |
| RG6 cancellation/containment | Section 8 records request/ack/domain findings separately; uncertain effects deny containment-dependent retry/resumption/release/closure. Parallel/automated/AFK coverage is unproved | Execution/side-effect owners: authorized interruption/timeout/fault trials across processes, subprocesses, queues and remote effects; request/ack times, observed latency, residual inventory and retained evidence; continuing/unknown domains must fail closed |
| RG7 durable recovery | Operation-specific actions only; distinct episode history, positive reopening, mandatory resumption reset, intervention and independent terminal guards. No blind/autonomous retry/reconciliation or unvalidated recovery-dependent closure | Side-effect/recovery owners: idempotency/deduplication/version, reconciliation/compensation and residual-risk evidence; later implementation validation of new obligations before resumption, repeated cycles, intervention renewal and terminal denials |
| RG8 retention/integrity | Repository-native manifests/custody, actual retrieval/digest/redaction checks; missing/inaccessible/expired/mismatched/unsafe evidence blocks the affected design or later reliance | Evidence custodian: actual storage/readers/retention/redaction commitments and authorized retrieval-after-continuation, expiry/deletion/access-failure/mismatch tests. Current matching reads do not establish general retention |
| RG9 installed capabilities | Use only observed operations; future relied-upon version/configuration/entitlement/compatibility facts required; no deployed-control certification or routine/parallel/automated/AFK expansion | Tooling/runtime owner: actual chosen surface/client/runtime/component inventory, enabled tools, account/surface availability and compatibility; bounded capability tests tied to the specific relied-upon claim |
| RG10 integration leverage | All optional integrations omitted from initial architecture; availability/popularity cannot trigger selection | Project owner: representative target-task comparison against native search/direct documentation/available logs covering correctness, completeness, cost, maintenance and removal; separate selection decision. No benchmark is run here |
| RG11 documentation ambiguity | D5 app-server and C20 Sentry MCP remain deferred; no generic maturity/transport/auth/lifecycle assurance | Tooling/vendor and operations/security owners: exact chosen deployment/version/transport and authoritative resolution of documented distinctions, followed by authorized permission/lifecycle validation before selection/reliance |
| RG12 AFK end-to-end controls | All unattended/AFK operation and unattended scheduled/controller dispatch denied. No automatic task decisions/writes. Separately authorized supervised deterministic checks remain a different class | Coordinator/runtime/side-effect owners: end-to-end readiness/freshness, ceilings/isolation, observation, containment, protected evidence, recovery and unavailable-human trials; independent assessment and separate eligibility/authorization decision |

No operational trial, negative enforcement test, fault injection or control installation is performed in this task. Later validation assignments must state the precise gap/scope, exact implementation candidate/configuration, expected rejection/acceptance behavior, isolated test domains and credentials, risk/containment owners, retained evidence, stop boundary and separate authority. A test cannot broaden its own permissions or substitute for independent assessment where required.

### 11.1 DI boundaries retained

**DI-1 preserved:** retain orthogonal task-control, cancellation, recovery, work-product, verification, review, disposition, normativity, baseline-acceptance and join planes. Native product status is at most a referenced observation or derived view. Required-and-passed, required-but-unsatisfied and legitimately not-applicable remain distinct; absent or skipped evidence is not pass.

**DI-2 preserved:** materially stale authority blocks reliance; retries are operation-aware; containment and recovery are distinct; completed prior recovery episodes and relied-upon evidence remain durable; reopening requires a distinct qualifying obligation and authorization; intervention, resumption/reset and terminal guards cannot be bypassed.

These reproduce the controlling gate's boundary statements. The representation makes no semantic redesign or new selection necessary: unsupported transitions remain denied. If later implementation cannot preserve either, it must stop for a separate coordinator design-impact decision identifying changed behavior, load-bearing assumptions, exact new candidate requirements, affected verification and fresh independent review. It cannot adopt a controller's convenient status/retry/cleanup behavior by interpretation.

## 12. Selection exclusions and remaining contextual parameters

### 12.1 No conditional-selection leakage

Only S1/S5 and qualified S2/S3/S4/S6 supply initial components. S1 gives identity/evidence/owner records; S2 gives the product repository representation; S3 gives eligible replaceable interfaces; S4 gives bounded supervised production; S5 gives native retrieval; S6 gives available results and manifest/digest direction. None certifies a deployed enforcement stack.

C2-C8, C10, C12-C19 and C21-C22 remain conditional, with triggers, owners and validation controlled by disposition section E2. C1 retains only a future noncompeting Issue intake/discussion qualification; it is absent from this architecture. C9 retains only separately authorized bounded-delegation consideration; no agent delegation is performed or required here. C11 and C20 remain deferred. D1-D14 remain deferred; X1-X9 remain rejected for their stated claims/architectures. This is a fixed consequence of the controlling disposition, not a new mutable selection table.

No initial step requires Serena, ast-grep/IDE MCP, Context7, publisher MCP, Ref, Playwright integration, Sentry/MCP, OpenTelemetry, Actions/checks/artifact services, CODEOWNERS, PR transport, environments, merge queues, worktree parallelism, extra Apps, custom skills/scripts/hooks, task runners, SDK/app-server clients, schedules/goals/webhooks, LangGraph/Deep Agents, Temporal, OpenHands, Symphony or a Git ref wrapper. Describing future interface evidence requirements does not choose them. Existing native search or local producer byte-check commands do not install a deferred helper. C22's conditional application use cannot activate D11 for ADW coordination.

The five source-review qualifications remain scoped: R09 historical observation is not current/billing proof; O16 does not establish generic app-server production maturity; E312/E313 do not settle Sentry deployment transport/auth/scope/maturity; E314 is not a procurement quote. No new external capability research or deployment claim is used to fill these uncertainties.

### 12.2 Parameters with owners, supply points and denial

These values depend on the eventual product/task. Their meanings, owner and failure behavior are fixed; implementers cannot invent them. Material initial representation, location, identity relationships and responsibility boundaries are already resolved above.

| Parameter | Owner/source and required evidence | Supply point / denial if absent |
|---|---|---|
| Product P, task T, authorized mutable ref and applicable governance | Product maintainer/task authority; exact repository/current baseline, existing owner inspection and authorized materialization contract | Before root creation or task dispatch; deny creation if missing/conflicting. No product selected now |
| Named A/R/executor/supervisor/domain/review/integration/custody actors | Accountable task authority and relevant role owner; explicit scope/identity mapping, conflict assessment and escalation destination | Before any role-dependent decision/effect; role labels alone do not authorize it |
| Objective, criteria, scope, inputs, dependencies and boundaries | Task/product engineering owner; exact contract, observable local/integrated/outcome criteria, classified unknowns and dependency identities | Before readiness/authorization; unresolved material intent blocks commitment; learning requires its own scope |
| Applicability of verification/review/integration/acceptance gates | Applicable governance/task/risk owner; governing rule and contextual rationale, consequence/uncertainty/privilege analysis | Before relying on omission or advancing the governed transition; absent evaluation means unsatisfied, never pass or implicit N/A |
| Concrete ceilings and supervision response | Task/risk/runtime owners; authorized time/resource/effect bounds, observation/enforcement evidence where required and safe response to breach/loss | Before effectful dispatch; deny if material bound/observation/response missing; no universal numeric default |
| Actual versions, effective permissions and surfaces | Runtime/security/tooling owner; actual inventory/configuration/credential scope/compatibility and applicable authorized validation evidence | At dispatch and whenever changed; deny affected effect on unknown/stale coverage |
| Exclusive-use evidence for one persistence | Serialization/runtime/repository owner; current process/workspace/ref/credential/in-flight inventory and loss/revocation handling | Immediately before each granted persistence; uncertainty denies that assignment, no reusable fence claim |
| Operation class, recovery action, validation target, residual-risk handling | Actual domain/side-effect owner and required risk authority; prior-effect evidence, stable IDs/preconditions, bounded recovery decision and target validation | Before every recovery action/reopening/conclusion/resumption/closure; ambiguous effects deny retry; missing authority remains intervention/block |
| Retention interval, readers and redaction constraints | Evidence custodian under project/security governance; documented reliance interval, access/retention suitability, retrieval and safe-data treatment | Before persistence/reliance and at continuation boundaries; missing/sensitive/expired evidence blocks reliance; no universal retention default |
| Concrete persistence gate source/delta/tool operation | Authorized repository task/coordinator owner; exact live B, canonical bytes, allowed delta, actual available permitted S1 operation and prerequisites | Each persistence independently; no inherited write license or automatic retry |

No concrete product deployment, runtime permission configuration, review identity, risk policy or retention period is presumed supplied by this document. Their absence does not leave an architectural choice unresolved: it denies the named transition. A future product integration strategy beyond the defined narrow path is a separate design/adoption prerequisite under RG3, not a hidden implementer parameter.

Assumptions used for design: the accepted semantic/disposition identities remain controlling; repository-native secret-safe text evidence can be a suitable proposal direction without asserting its fitness for every future payload; low-throughput manual decisions are acceptable for the stated supervised serialized boundary; current interfaces can be replaced only by already permitted equivalents. These are bounded design assumptions. If an actual task violates them, the affected task stops for its accountable owner; no new tool is selected automatically.

## 13. Accepted-input traceability

DD numbers refer to `ADW-WF1-DD-001` through `ADW-WF1-DD-014` in the accepted semantic subject. Named transitions/scenarios refer to that same exact artifact. S/RG/DI identifiers refer to the exact DR-005 disposition, not the frozen report's unqualified SELECT NOW or conditional C11/C20 labels.

| Proposal decision | Accepted semantic obligation and concrete scenario/transition | Permitted mechanism input / consequence |
|---|---|---|
| TD-01 placement | DD-003/010/014; authoritative-state ownership, false owner and fresh-context cases | S1, qualified S2/S6; existing Register remains sole research/gate owner |
| TD-02 one recorder | DD-001/003/007/011; composite cancellation/containment/recovery transitions and transfer | Qualified S2/S4; RG2/4/5 remain prerequisites |
| TD-03 immutable history/current pointers | DD-005/009/010/011; correction, repeated recovery, new episode before resumption | S1, qualified S2/S6; RG7/8; DI-2 |
| TD-04 identity/publication | DD-005/009; identify/correct candidate, review, stale-state and carry-forward cases | S1, qualified S4/S6; RG1/3/4; no C2/D14 activation |
| TD-05 evidence/custody | DD-010, reconstructable evidence and inaccessible-evidence failure | S1, qualified S6; RG8; no C6 store selected |
| TD-06 contexts | DD-005/007/010; exact-pointer rehydration and stale-summary scenario | Qualified S3, S5; RG5/8/9; X1 remains rejected |
| TD-07 executor boundary | DD-004/005/007/012/013; authorize/dispatch, scope expansion, incomplete unattended evidence | Qualified S4, S5; RG1/2/5/6/9/12 |
| TD-08 interruption/recovery | DD-011; generic stop, requested/acknowledged, residual effects, reopening, intervention, reset and terminal guards | Qualified S2/S4/S6; RG6/7; DI-1/DI-2 |
| TD-09 dependency/join | DD-006/008; missing/failed/optional result, integrated verification fail/pass/N/A | S1, qualified S2/S6; RG2/3/6; parallel execution remains denied |
| TD-10 gate representation | DD-001/002/004/009/012; legitimate omission versus false pass; review/correction/disposition | S1, qualified S2/S4/S6; DI-1; no aggregate status promotion |
| TD-11 exclusion | DD-013/014 and scoped tooling disposition; unattended denial and mechanism deferral | Only S inputs; every conditional/deferred prerequisite remains outside initial dependency graph |

| Controlling gate output | Coverage |
|---|---|
| E1 ownership and placement | Sections 4.1-4.3, all state classes including adoption/baseline/external domains and existing Register |
| E2 task-control representation | Section 5; immutable/current split, lifecycle, gates, evidence, correction, no operative schema |
| E3 exact identities/publication | Sections 6 and 10; B/W/C/V/Rv/I/Ppub/Ecommit and stale/carry-forward rules |
| E4 durable evidence | Section 7 and section 8; every required evidence class, custody, timing, provenance and failure |
| E5 coordinator/context surfaces | Section 9.1; pointer handoff, rehydration, export/custody, drift and unavailable surface |
| E6 bounded Codex | Section 9.2; assignment, ceilings, surfaces, verification and denied effects |
| E7 permitted persistence | Section 10; exact base/delta/serialization/executor/evidence/readback/stop and procedural limits |
| E8 traceability/gaps/validation | Sections 11-14; all RG consequences, DI boundaries, contextual parameters and scenarios |

The semantic design carries accepted DR-001 state/authority/identity/evidence constraints, DR-002 contextual readiness/decomposition/feedback/continuity constraints and DR-003 delegation/freshness/join/correction/containment/recovery/security constraints. This proposal preserves those scoped qualifications through their accepted DD mapping; it does not reread publication recommendations as new policy. No universal review invocation, heavy ceremony, numerical threshold or product rule is inferred.

## 14. Producer conformance and implementer-consistency checks

These are producer design walkthroughs and structural checks, not independent review, implementation tests, operational trials or control-effectiveness validation. Symbols identify hypothetical subjects/episodes; no actual task, candidate, cancellation or recovery record was created. A PASS below means the design determines the required behavior and excludes the stated nonconforming result.

### 14.1 All sixteen required scenarios

| # | Non-operational walkthrough and decisive representation | Producer outcome |
|---|---|---|
| 1 | `control.md` owns current cancellation; an Issue/chat/runner independently claims it is closed. Section 4 rejects that second authority. R retains the actual authoritative value; disputed ownership blocks reliance until the existing owner resolves it. A labeled derived view may be corrected from the owner, never co-written as truth | PASS: no duplicate owner or status-based closure |
| 2 | Receiver follows repository/ref + exact control/contract/evidence pointers, reads current owners, verifies blobs/digests/authority, reconstructs planes and open obligations, and records rehydration. A stale narrative cannot override the current record. Remove a critical input or change an authoritative identity: continuation is denied | PASS: exact-source reconstruction and missing/stale denial are specified |
| 3 | Persistence was granted on B; the final live read resolves another full SHA. Section 10 step 1 or 4 stops the assignment. The old grant is historical; impact and a new bounded authorization are required. No automatic rebase, retry or claim that an unrelated change is harmless | PASS: changed base blocks the original assignment |
| 4 | Verified/reviewed C changes to C2, or a load-bearing criterion/configuration changes while C remains. Section 6.2 invalidates affected current references, retains old evidence and requires explicit impact plus affected checks/applicable rereview. Metadata-only commit changes still have a new full identity | PASS: no stale verdict inheritance or identity reuse |
| 5 | V names one subject, Rv another and Ppub cannot be mapped to the reviewed/tested I. No matching tree/green status repairs the missing relationship. Sections 6/10 deny publication reliance, join and acceptance; if the bad publication already happened, record the actual effect and escalate without retroactive authorization | PASS: unproved mapping remains non-success |
| 6 | Required obligations include one skipped/missing/failed/stale result despite a green aggregate. The gate is unsatisfied/invalid and verification is pending/failed/stale as warranted. A separate legitimately N/A obligation has a rule/rationale and is not-invoked, never passed; it cannot offset the failed required one | PASS: all required verification and N/A distinctions preserved |
| 7 | The producer, a fork of the producer, or another materially conflicted actor offers an independent verdict or acceptance. Section 7 rejects independence; review remains required-pending and disposition/acceptance is denied. A later named conflict-free eligible assignment must evaluate exact C under its own scope | PASS: producer checks and host approval cannot replace independent review |
| 8 | Start active/none/not-applicable. Generic stop -> blocked/none/not-applicable; authorized request -> blocked/requested/not-applicable; complete acknowledgement -> blocked/acknowledged/not-applicable. A queued remote effect remains uncertain, so no containment advance, retry, resumption, closure or resource release. Available evidence can be recorded without pretending the missing observation exists | PASS: distinct planes and uncertain-containment denial |
| 9 | Episode A validates its target and concludes blocked/none/recovered; no resumption. Cancellation request and acknowledgement retain recovered. All-domain containment finds a newly required withdrawal and records blocked/residual-effects/recovered. A's pass cannot close cancellation. Positive new-obligation evidence and fresh domain/risk authority open distinct B -> recovering/residual-effects/assessment, linked to A. B may enter intervention -> blocked/residual-effects/intervention-required; only supported renewal returns to assessment. B's authorized action and target validation yield blocked/residual-effects/recovered; separate terminal guards then permit cancellation | PASS: A remains completed, B is distinct, intervention remains reachable and stale-success closure is denied |
| 10 | From blocked/none/recovered after A, authorized ordinary resumption explicitly resets to active/none/not-applicable while retaining A. A later independent failure stops to blocked/none/not-applicable and a new bounded recovery opens assessment. If completion of its external operation is ambiguous, classify/reconcile and obtain authority before retry/compensation; unsafe continuation becomes blocked/intervention-required. Cancellation-specific resumption uses the same explicit reset | PASS: repeated cycles are representable without history loss or blind retry |
| 11 | A required payload is absent, expired, inaccessible, has a wrong digest or includes unsafe sensitive material. Section 7 names its custodian, preserves safe available evidence and invalidates the dependent gate. Neither a hash without bytes, transcript recollection nor an expiring URL supplies custody. No required conclusion survives on unsafe or unverifiable evidence | PASS: all five evidence-failure conditions deny reliance |
| 12 | The runtime owner cannot establish actual connector permissions, or a persistence assignment lacks process/ref/credential exclusivity evidence. Section 9/10 denies that specific action, even if the workspace says isolated or a prompt says read-only. Already authorized unaffected reads may continue; no permissions are expanded | PASS: instructions/labels do not establish enforcement |
| 13 | All supplied units pass locally but one required dependency is missing, or required verification fails on exact I. The join is partial/failed or failed respectively, never passed. Candidate formation/completion/downstream success cannot rely on it. Optional omissions are separately justified; reducing required scope requires reframing/authorization. This is a denial walkthrough only | PASS: no passing join from incomplete/failed required work; no parallel enablement |
| 14 | A conditional tool is callable or a deferred service is installed. Section 12 leaves it outside the initial dependency graph, with its existing disposition and prerequisites. Missing evidence remains a block; it cannot be filled by silently activating C5/C6/C7/C11/C20 or any D item. C22 does not select ADW Temporal | PASS: availability is not selection or authority |
| 15 | Routine direct-main, parallel, automated, product dogfooding or AFK execution is requested while current main is unprotected. Sections 10-12 deny each mode. A past narrow persistence, supervision, manual SHA check or successful deterministic producer check cannot license it | PASS: all requested restricted modes remain unauthorized |
| 16 | A hypothetical later persistence gate supplies exact live B, canonical bytes/digest, allowed paths/delta, named executor/serialization owner, surface/exclusivity evidence, verification and stop. Section 10 determines prepare -> fresh recheck -> only granted write -> exact readback -> stop. Any missing prerequisite/drift denies execution. Passing readback creates a candidate identity only; later fresh review/disposition/adoption stay separate | PASS: concrete narrow procedure with explicit limits, without executing it |

### 14.2 Structural and consistency assessment

The producer checked metadata against gate J, all exact bindings against GitHub/tree and computed digests, E1-E8 coverage, all ten planes, each current owner's sole representation/recorder, every evidence class, all twelve scoped RG consequences, both DI statements, the complete conditional/deferred/rejected boundary and all sixteen scenario outcomes. No actual operational conformance test or separate review was performed.

The implementer-consistency test was applied by asking whether two implementers supplied the same future task facts could choose materially different compliant architectures or gate outcomes:

| Material choice | Determined answer / rejected divergence |
|---|---|
| Owner and task object | Both use P's `docs/adw/tasks/<T>/control.md`, one R and fixed decision/evidence records; an Issue/file or harness/file co-owner fails |
| Representation/history | Both use exact accepted plane vocabulary, explicit gate applicability/freshness and immutable record successors; a single done field or edited old verdict fails |
| Subject identity | Both use full B/C and exact path/blob/digest/scope; W is local output; V/Rv/I/Ppub relations are explicit; branch aliases or implicit transformed publication fail |
| Evidence placement | Both retain necessary secret-safe evidence beneath the task root with manifests/custody; chat-only retention or silently selected external storage fails |
| Review/decisions | Both require an eligible conflict-free exact-subject assignment and separately attributable verdict/disposition; producer self-review/acceptance fails |
| Context/executor | Both rehydrate actual owners and check effective surface-specific prerequisites; interfaces own no state and unknown effects are denied |
| Persistence | Both use one separately granted exact-base/delta serialized operation and full readback/stop; routine direct-main, automatic rebase/retry, fencing or atomicity claims fail |
| Recovery | Both preserve completed A, create distinct B only under the positive reopening guard, support intervention renewal, apply mandatory resumption reset and independent terminal guards |
| Missing values/mechanisms | Both ask the specified owner for evidence/decision at the defined supply point and deny the affected transition; no implementer chooses a tool, risk threshold or parameter by default |

**Producer result: PASS within the authorized initial design scope.** No material initial architecture choice is left as an unresolved menu, and no unselected mechanism is required. Contextual values remain owned inputs with explicit denial behavior. This is a producer sufficiency claim for persistence consideration only. A later independent reviewer must evaluate the exact unchanged repository candidate, the controlling gate and accepted basis, including all material ownership, identity, negative-scenario and selection-boundary claims; this table cannot predecide that review.

## 15. Delivery boundary and proposed next gate

The design scope is complete as a local non-normative proposal: E1-E8, accepted-input traceability, RG1-RG12 consequences, exact DI preservation, contextual parameter ownership, all sixteen walkthroughs and the implementer-consistency producer check are present. Producer checks do not establish independent review, operating safety or acceptance.

Final delivery rechecks through @GitHub completed by **2026-09-04 11:59:12 UTC**. Live main remained `5ddab4017fa3ef871c7221de112b9e7d5cf66c84`; the complete 27-entry tree was non-truncated and retained every controlling blob. The live-main Register remained blob `d8291147cae64954c1b9f313d685879284451391`, 47602 bytes, SHA-256 `5659ed361163468f68ecf9d79ad3c6b75657894b6eb387e657ab0363bda355e4`, with both current tooling next-gate pointers at design execution. The gate reread reproduced blob `9a899597471b8ad9cd48ebf59b974dbaeefa1bf5`, 45768 bytes and its expected SHA-256. Main remained protected:false with protection disabled and check enforcement off. Ref, all-state Issue and all-state PR rereads remained unchanged: sole main ref, only closed bootstrap Issue #1 with zero comments, and no PRs. No drift or competing current tooling decision was detected in those accessible surfaces. These observations do not guarantee that a later persistence gate will see the same state; it must reverify its own base.

Local structural checks found all required metadata, fifteen proposal sections, eleven TD decisions, all RG1-RG12 rows and exactly sixteen consecutively numbered scenario outcomes, all PASS as producer walkthroughs. Direct comparison against the newly retrieved gate confirmed both DI boundary statements are preserved verbatim. UTF-8 decoding, no BOM, LF-only and one final LF were checked. The canonical path was absent at the initial local path check and was created as a new artifact outside synced sources; no pre-existing proposal was overwritten. These checks establish producer completeness/serialization only.

Canonical local path: `/Users/antony/.codex/.chatgpt-projects/g-p-6a987c876f908191b803764d8df6d9b7/ADW-WF1-TOOLING-DESIGN-001.md`.

Serialization: UTF-8 without BOM, LF-only, exactly one final LF. The final byte count and SHA-256 are reported externally after serialization to avoid a self-referential digest. This identity describes local bytes, not an immutable repository candidate SHA.

Explicit non-actions: no GitHub writes or Register updates; no commits, pushes, PRs, review publication or repository acceptance; no new research or DR-005 reopening; no installation/configuration, implementation, scripts/hooks/Actions/MCP/App/skill/custom-client/orchestration/protection changes; no operational trials, fault injection or enforcement negative tests; no product migration, actual task record, operative standalone schema or dogfooding; no delegation, parallel execution, automation or unattended/AFK enablement; no independent review of this proposal; no normative Workflow v1 adoption or new write authority. Local changes are limited to this proposal and its producer serialization checks; synced sources remain untouched.

Proposed next gate, requiring a separate bounded persistence authorization:

**Workflow v1 tooling/enforcement design candidate persistence**

Stop after local delivery and producer-verification reporting. Fresh independent review follows only after an exact immutable candidate exists. Coordinator disposition and any implementation/adoption remain separate. This task does not execute the proposed next gate.
