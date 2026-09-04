---
id: ADW-WF1-DESIGN-DISPOSITION-001
artifact: workflow-v1-design-disposition
artifact_status: active
owner: chatgpt-coordinator
decision: accept-initial-tool-agnostic-workflow-v1-design
decision_subject_commit: 2b9532682ae77bf5037f1b2fa45b720e5865d0ad
decision_subject_path: docs/design/ADW-WF1-DESIGN-001.md
decision_subject_blob: afed983e7632caf3169dcbac7a80f8da8226d86d
independent_review_ref: docs/design/ADW-WF1-DESIGN-REVIEW-004.md
independent_review_blob: 3cdb92769bb955c8782dfa504843fd32a4736168
decided_on: 2026-09-03
normative_effect: none
supersedes: null
---

# ADW-WF1-DESIGN-DISPOSITION-001

## Exact subject and verified live basis

Repository: `ahtoxaandy999/agentic-development-workflow`.

The connected @GitHub app was explicitly invoked for the live verification required by regeneration task `ADW-WF1-DESIGN-DISPOSITION-001-REGEN-001`. Initial and final live main reads matched; the final main/Register check completed at 2026-09-03 21:12:44 UTC. The supplied coordinator decision is preserved. The previous local serialization supplies the wording to retain, while live GitHub reads establish the current repository evidence binding.

| Field | Verified value |
|---|---|
| Current main at regeneration verification | `3d63f1276555761e48b287ff7e98d79f31a12c2b` |
| Exact candidate-004 commit | `2b9532682ae77bf5037f1b2fa45b720e5865d0ad` |
| Candidate sole parent | `a19e700e93157b8b25eaab4f14c7c44fc3ea3f6e` |
| Candidate artifact | `docs/design/ADW-WF1-DESIGN-001.md` |
| Candidate Git blob | `afed983e7632caf3169dcbac7a80f8da8226d86d` |
| Candidate raw UTF-8 bytes | `109600` |
| Candidate SHA-256 | `f8ddb3626868289e44251088a2ddad291ce762dbb58ec824d70c5de5a7994411` |
| Independent review | `docs/design/ADW-WF1-DESIGN-REVIEW-004.md` |
| Review-004 Git blob | `3cdb92769bb955c8782dfa504843fd32a4736168` |
| Review-004 verdict | `accept-candidate-for-design-disposition` / ACCEPT CANDIDATE FOR DESIGN DISPOSITION |
| Review-004 findings | BLOCKER 0 / MAJOR 0 / MINOR 0; none |
| Research Register Git blob | `4b12209a7953b3dd5c244d2b6e662efe41d867d1` |
| Current repository gate | Workflow v1 design disposition gate |

The candidate bytes retrieved during regeneration reproduce both the expected SHA-256 and Git blob hash. Corrected review-004 names the same full candidate commit, parent, path, blob, byte length, and SHA-256. Its retrieved bytes reproduce corrected Git blob `3cdb92769bb955c8782dfa504843fd32a4736168`. The current tree retains the candidate-004 blob at the candidate path. The final live-main Register read was identical to the initial exact-main read.

The live Register selects review-004 as the current review. It records Workflow v1 as unadopted and DR-005 as `planned`, `deferred`, and `dependency_status: unsatisfied`. There is no competing current candidate or review in the authoritative Register and design directory; reviews 001-003 remain historical evidence for their exact subjects.

Sources: [candidate-004](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md), [review-004](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/3d63f1276555761e48b287ff7e98d79f31a12c2b/docs/design/ADW-WF1-DESIGN-REVIEW-004.md), [current Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/3d63f1276555761e48b287ff7e98d79f31a12c2b/docs/research/research-register.md).

## Regeneration and evidence rebinding

The correction commit `3d63f1276555761e48b287ff7e98d79f31a12c2b` has sole parent `76114f52e4fc9191476e5d017c77be6e3ee2a9da`, the historical initial review-004 persistence commit. Direct comparison of both commit trees shows exactly one changed file: `docs/design/ADW-WF1-DESIGN-REVIEW-004.md`. The design, Research Register, and all other file blobs are unchanged.

The complete pre-correction and corrected review files were retrieved through @GitHub and their Git blob hashes reproduced from raw UTF-8 bytes. The only changes remove transport backslashes from front-matter key underscores and replace the malformed closing delimiter with `---`. The substantive review body is byte-for-byte identical. The review target, verdict `accept-candidate-for-design-disposition`, findings BLOCKER 0 / MAJOR 0 / MINOR 0, and all substantive conclusions are unchanged.

The stale review blob has been removed from every current evidence binding in this record. Corrected review blob `3cdb92769bb955c8782dfa504843fd32a4736168` is the current independent-review identity. This regeneration preserves the prior coordinator decision, disposition scope, qualifications, finding treatment, and authority boundaries. It performs no new design disposition exercise, independent design review, or design correction.

Source: [transport-only metadata correction](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/3d63f1276555761e48b287ff7e98d79f31a12c2b).

## Decision

**ACCEPT INITIAL TOOL-AGNOSTIC WORKFLOW V1 DESIGN**

This record preserves the prior coordinator disposition of exact candidate-004. Review-004 supplies independent evidence; its passing verdict is not an acceptance command. The prior acceptance rests on the coherent accepted-input chain, exact review binding, reviewed correction history, required-behavior coverage, and preserved authority boundaries. The following rationale and assessments are carried forward from that decision. Regeneration verifies the corrected evidence binding and transport-only change; it does not reassess the design or repeat independent review.

## Scope

Accept only the initial tool-agnostic Workflow v1 design embodied in candidate commit `2b9532682ae77bf5037f1b2fa45b720e5865d0ad`, artifact `docs/design/ADW-WF1-DESIGN-001.md`, blob `afed983e7632caf3169dcbac7a80f8da8226d86d`.

Candidate-004 becomes the accepted initial tool-agnostic design basis and the controlling design basis for later authorized mechanism evaluation. The disposition accepts defined behavior and evidence obligations, with the accepted inputs' qualifications and exclusions preserved. It does not accept a new repository baseline or promote the design to normative policy.

## Evidence basis

### Accepted inputs and authorized contract

The Research Register is the sole current owner of research dispositions, dependencies, pointers, and the repository next gate.

- `ADW-DR-001-DISPOSITION-001` accepts all twelve DR-001 recommendations within their recorded scopes and qualifications: five ACCEPT and seven ACCEPT WITH QUALIFICATION. The frozen evidence target is `DR-001@sha256:825204b8c45da36c4c7cd087d572e0b014352aee7a6fe1c54e0772aaec6acf0f`. It supplies state separation, sole ownership, immutable identity, freshness, independence, reliance-based durability, and qualitative proportionality.
- `ADW-DR-002-003-DISPOSITION-001` accepts DR-002 R1-R9 and DR-003 PR01-PR12 only within their recorded scopes and qualifications. Targets are `DR-002@sha256:5458020be85cde909705fc1fbbc489c98e43ce0b6c058f6fd5d67901dc1ecb03` and `DR-003@sha256:8017e5fbe1ee7b2d7ad92ba76b89e69dc2b51c52e0d56c650a293e99e63b0d46`. They supply contextual readiness, executable/verifiable boundaries, decomposition and integration, bounded delegation, parallel joins, continuity, evidence, correction, containment, and operation-aware recovery.
- The same joint disposition records **PREREQUISITE RESEARCH JOIN PASS**, with no material contradiction in the accepted sets.
- The authorized design contract is `ADW-WF1-DESIGN-GATE-001`, embedded in the design artifact. Its initial materialization commit is `c30181db44c68ea9a68bcdb0bfa12afb4376bee7`, blob `9f96b429696f4e0e402901394d0d7258592e8c25`, based on `29581dc9b7d1f2c368e2eca9098500ddabbd3a49`. The embedded contract body is preserved in candidate-004. The accepted-input portion of the Register is unchanged from that design base.

The criterion is whether two competent implementers, given the same authoritative facts and decisions, can derive the same required tool-agnostic behavior without inventing material intent. Research reports remain evidence; their full recommendations do not override the scoped dispositions.

The contract's earlier statements that no substantive design existed describe the contract-durable stage. The proposal explicitly establishes that temporal scope at line 636; those statements and historical next gates do not compete with current proposal metadata or the Register.

Sources: [accepted input dispositions and join](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/3d63f1276555761e48b287ff7e98d79f31a12c2b/docs/research/research-register.md#L85), [authorized contract](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/c30181db44c68ea9a68bcdb0bfa12afb4376bee7/docs/design/ADW-WF1-DESIGN-001.md), [proposal status clarification](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L634).

### Complete candidate/review correction chain

Each corrected candidate has a new immutable full commit identity. All candidate artifacts use `docs/design/ADW-WF1-DESIGN-001.md`; each review path is `docs/design/ADW-WF1-DESIGN-REVIEW-NNN.md` for its listed number.

| Candidate | Exact candidate commit | Candidate blob | Review / review blob | Review outcome |
|---|---|---|---|---|
| 001 | `24b378832f4edc8ec55d7f3063114dc536d7e24e` | `d164c7f9c4461572f26707fd747ed886e6b0ed93` | 001 / `f2df1186f72374f8386d531117b13a80bc42b1bb` | REQUIRE NEW DESIGN CANDIDATE; 0/2/0 |
| 002 | `bca878ea3a2576ef2c354bac00e0049041d616e1` | `f76c7df6686b3c338d261860e9c4aa3f72da5480` | 002 / `b18aeaa0e86c3cf2ce02afaf36106e19a8e7de78` | REQUIRE NEW DESIGN CANDIDATE; 0/2/0 |
| 003 | `fd047c7563a9c44be5b3a4bde7d12f9e88d27414` | `229a5a16cd93e41c9bdf19da47a488947e8dbb29` | 003 / `e02dc3b300922a10c035bf6eb20527b46bbd0a8c` | REQUIRE NEW DESIGN CANDIDATE; 0/1/0 |
| 004 | `2b9532682ae77bf5037f1b2fa45b720e5865d0ad` | `afed983e7632caf3169dcbac7a80f8da8226d86d` | 004 / `3cdb92769bb955c8782dfa504843fd32a4736168` | ACCEPT CANDIDATE FOR DESIGN DISPOSITION; 0/0/0 |

Counts are BLOCKER/MAJOR/MINOR. Direct GitHub commit and file reads establish the single-parent progression:

```text
candidate-001: 24b378832f4edc8ec55d7f3063114dc536d7e24e
review-001 persistence: c8db8c04ec8843f0cbe6e3b05a93d8962e47d08e
candidate-002: bca878ea3a2576ef2c354bac00e0049041d616e1
review-002 persistence: 8969335926967af14d0b05b94e34708cfa41a4d6
candidate-003: fd047c7563a9c44be5b3a4bde7d12f9e88d27414
review-003 persistence: a19e700e93157b8b25eaab4f14c7c44fc3ea3f6e
candidate-004: 2b9532682ae77bf5037f1b2fa45b720e5865d0ad
review-004 initial persistence (historical): 76114f52e4fc9191476e5d017c77be6e3ee2a9da
review-004 metadata correction / current main: 3d63f1276555761e48b287ff7e98d79f31a12c2b
```

Historical review-001 through review-003 blobs remain unchanged at current main. Each negative verdict remains bound only to its old subject; it does not become a current objection to changed content that received applicable independent rereview. Historical review metadata such as `active` or `supersedes: null` preserves the evidence record and does not override exact-subject binding or the Register's current pointer.

### Review finding treatment

Review-004 has **no findings**: BLOCKER 0 / MAJOR 0 / MINOR 0.

| Historical finding | Explicit treatment |
|---|---|
| ADW-WF1-DR-MAJ-001 | Candidate-001 join-pass/integrated-verification contradiction. Review-002 resolved it; reviews 003/004 preserve passing join regression evidence. |
| ADW-WF1-DR-MAJ-002 | Candidate-001 cancellation planes and terminal-transition ambiguity. Review-002 confirmed the original defects corrected but classified the result as REGRESSION INTRODUCED, recording new recovery defects as MAJ-003/004. This history is not compressed into an unconditional review-002 resolution. Review-004 passes cancellation, containment, and terminal safeguards. |
| ADW-WF1-DR-MAJ-003 | Candidate-002 recovery-intervention sink. Review-003 resolved it; review-004 independently exercises intervention during a reopened episode and passes the regression. |
| ADW-WF1-DR-MAJ-004 | Candidate-002 missing ordinary-resumption recovery reset. Review-003 resolved it; review-004 replays explicit reset and a subsequent recovery cycle with a passing regression result. |
| ADW-WF1-DR-MAJ-005 | Candidate-003 could not open a newly required recovery episode after prior recovery completed but before resumption. Review-004 resolves it through explicit guarded reopening, distinct durable episode identity, containment prerequisites, and separate terminal guards. |

No historical finding is silently discarded. The complete correction and rereview chain accounts for MAJ-001 through MAJ-005, and none remains an unresolved finding in review-004.

Sources: [review-001](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/c8db8c04ec8843f0cbe6e3b05a93d8962e47d08e/docs/design/ADW-WF1-DESIGN-REVIEW-001.md), [review-002](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/8969335926967af14d0b05b94e34708cfa41a4d6/docs/design/ADW-WF1-DESIGN-REVIEW-002.md), [review-003](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/a19e700e93157b8b25eaab4f14c7c44fc3ea3f6e/docs/design/ADW-WF1-DESIGN-REVIEW-003.md), [review-004](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/3d63f1276555761e48b287ff7e98d79f31a12c2b/docs/design/ADW-WF1-DESIGN-REVIEW-004.md).

## Coordinator assessment of design sufficiency

The prior coordinator assessment below is preserved unchanged in substance. It supports the implementer-consistency objective using exact candidate-004 and independent review-004. The review's substantive body remains identical after the metadata correction, so the transport rebinding preserves this assessment without a new design review.

| Criterion | Disposition basis |
|---|---|
| Lifecycle and gates | Distinct state planes, explicit transition owners and guards, freshness, and required-pass versus legitimate non-applicability prevent implicit state promotion. |
| Authority and ownership | Sole mutable ownership, explicit transfer, bounded roles, and separate evidence/decision/recording responsibilities are defined. |
| Readiness and task formation | Executability and observable validation govern commitment; material unknowns are resolved, bounded as learning, or block work. |
| Delegation | Parent-bounded authority, exact relied-upon inputs, constraints, validation, evidence, ceilings, stopping, and escalation are explicit. |
| Candidate identity and correction | Full immutable commit identity, impact analysis, new identity after content change, affected reverification, and applicable rereview are required. |
| Verification, review, acceptance | Producer checks, independent review, coordinator disposition, normative adoption, and baseline acceptance remain separate. |
| Durable and ephemeral state | Downstream reliance determines durability; explicit promotion and sole ownership prevent competing mutable truth. |
| Fresh-context rehydration | Authoritative pointers, identity/freshness checks, current authority, and reconciliation precede loss-sensitive continuation. |
| Decomposition and parallel joins | Dependencies, interfaces, exact result accounting, isolation and aggregation ownership are defined; required integrated verification must pass before join success. |
| Observability and evidence | Protected, secret-safe evidence must reconstruct authority, identities, effects, validation, failures, and unresolved uncertainty. |
| Stop, cancellation, containment, recovery | Local stop, request, acknowledgement, verified containment, operation-specific recovery, residual-risk handling, and terminal closure remain distinct. |
| Recovery-episode reopening | Positive evidence of a new obligation and completed prior episode permits an explicitly authorized, durably linked episode; old recovery success cannot discharge new handling. |
| Proportionality | Context scales representation and ceremony while authority, ownership, identity, freshness, failure visibility, and stopping invariants remain. |
| Unattended denial boundary | Missing applicable evidence denies eligibility; even complete necessary evidence does not supply sufficient safety or execution authority. |
| Failure behavior | Missing results, stale state, failed verification, review rejection, uncertainty, incomplete containment, and unreconciled effects retain explicit non-success outcomes. |
| DR-005 deferral | Capability and enforcement requirements are determined; later mechanism evaluation cannot redefine them for convenience. |

Review-004 supplies explicit implementer-consistency, conformance, accepted-input, recovery, and regression assessments. Its semantic replay and structural scan are design evidence, not implementation testing or proof of operational control effectiveness. That limitation is appropriate to this design disposition.

Sources: [current proposal](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L646), [recovery rules](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L777), [review-004 assessment](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/3d63f1276555761e48b287ff7e98d79f31a12c2b/docs/design/ADW-WF1-DESIGN-REVIEW-004.md).

## Unresolved and deferred item classification

Every remaining item has a defined later owner or gate and is non-blocking for this tool-agnostic disposition.

| Candidate item | Classification | Why required behavior is determined |
|---|---|---|
| Persistence, identity, review, disposition, adoption, baseline acceptance | Later lifecycle gates | Each governs its own claim. Persistence/identity/review now have exact evidence; this record supplies disposition. Normative adoption and new baseline acceptance remain absent. |
| Concrete schemas and packet formats | DR-005 mechanism/tooling decision | Semantic content, authority, evidence, and ownership requirements are already specified. |
| Tracker, storage, synchronization, logging, tracing, identity, credentials, attestation, orchestration, queues, worktrees, isolation, automation | DR-005 mechanism/tooling decision | Capability obligations precede product and representation choices. |
| Effective enforcement controls and branch-protection alternatives | DR-005 mechanism decision plus applicable later governance gate | Existing protection restrictions remain controlling and deny modes without required enforcement. |
| Contextual review invocation, risk acceptance, ceilings, retention, recovery parameters | Project-specific parameters | Named task/project/risk owners supply contextual decisions; absence blocks the affected gate. |
| Side-effect classifications, acceptance criteria, architecture, operating rules | Project-specific parameters | These belong to the affected project/system owner and are prerequisites before affected execution. |
| Ceremony-cost and generally applicable retention optimization | Post-v1 empirical optimization | Optimization is not required to determine the current semantic invariants. |
| Identity and effective-configuration mechanism validation | DR-005 mechanism/enforcement decision | A transition cannot rely on an unverified required control. |

The design does not require inventing material semantics when a mechanism or contextual parameter is missing: the corresponding required transition remains blocked. Implementation details are therefore not prerequisites to this disposition.

Source: [candidate unresolved/deferred items](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L1147).

## Evidence-chain assessment

| Assessment | Result |
|---|---|
| Accepted input chain | PASS |
| Immutable candidate/review binding | PASS |
| Correction history | PASS |
| Unresolved/deferred classification | PASS |
| Independent-review sufficiency | PASS |
| Authority boundary | PASS |

## Accepted design implications and normative boundary

1. **Accepted design disposition:** this record accepts exact candidate-004 as the initial tool-agnostic design basis.
2. **Normative Workflow v1 adoption:** absent. The design artifact retains `normative_effect: none`; acceptance does not rewrite its metadata or create adopted policy. Normativity requires a later explicit adoption decision naming the normative owner, exact subject and scope, followed by faithful materialization.
3. **Implementation/tooling selection:** absent. Later authorized evaluation may consume this design basis, but no mechanism is selected or implemented here.
4. **Baseline acceptance:** absent for this candidate and current main. The previously accepted Bootstrap Context Baseline v0 at `13b05e075ec04aa91494cd18f7d29f7249028cb5` is not replaced.

The disposition record owns this design decision. The Research Register continues to own current repository gate/dependency state; this local record is not a competing mutable tracker.

Sources: [Charter acceptance and authority](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/3d63f1276555761e48b287ff7e98d79f31a12c2b/PROJECT-CHARTER.md), [design ownership and adoption boundary](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L817).

## DR-005 boundary

The initial-design-disposition prerequisite for DR-005 becomes satisfied only once this disposition record is durably persisted. Regeneration of this local canonical source does not claim durable repository persistence or a Register update.

DR-005 must remain `planned` and `deferred`. The verified live Register still records its dependency as `unsatisfied`. A separate explicit **DR-005 research gate** must confirm the durable disposition and applicable dependency state before authorizing research. This task does not satisfy or bypass the complete DR-005 dependency/gate sequence and does not start DR-005. No tool or mechanism is selected.

After durable disposition persistence, the next eligible coordinator gate is **DR-005 research gate**. This consequence does not claim that the repository's current next-gate field has changed.

## Branch-protection and write boundary

The controlling Register and authorized contract preserve the accepted current-plan restriction: branch protection remains unavailable for this private repository. This disposition preserves that decision; it does not redesign protection, test alternative mechanisms, or assert newly verified operational protection.

Routine agent writes, parallel direct-main writes, automated writes, unattended execution, and AFK writes remain unauthorized. The existing requirement for effective protection before the restricted modes remains. This disposition grants none of those authorities and grants no implementation, repository-write, or automation authority. Any later repository persistence requires its own explicit bounded execution gate.

## Non-implications and explicit non-actions

This disposition does not:

- make Workflow v1 normative or adopt normative policy;
- accept a new baseline;
- implement Workflow v1;
- select tools, Apps, MCP servers, skills, hooks, or automation;
- start DR-005;
- authorize routine agent writes or parallel direct-main writes;
- authorize automated, unattended, privileged, externally consequential, or AFK execution;
- amend the accepted bootstrap protection decision.

No GitHub write, new design review, design correction, normative adoption, baseline acceptance, DR-005 start, tooling selection, implementation, or new write authority occurred in this regeneration task. Only the stale canonical local disposition source was replaced as the authorized deliverable. Byte verification does not create another authoritative repository state owner.

## Change control

A material change to the accepted design requires a new exact candidate identity, impact analysis identifying changed behavior and load-bearing assumptions, affected verification and applicable independent review, and an explicit new disposition or other authorized change process as applicable. Prior review and acceptance do not automatically apply to changed content. Historical candidates, findings, decisions, and supported evidence remain addressable.

## Next gate

**Workflow v1 design disposition persistence**

Durable repository persistence requires its own explicit bounded execution gate. After disposition persistence, the next gate is **DR-005 research gate**. DR-005 remains deferred until that separate explicit gate. Stop at this regenerated local disposition source and its serialization report.
