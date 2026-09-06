---
id: ADW-WF1-TASK-CONTROL-REFERENCE-CANDIDATE-PERSISTENCE-GATE-001
artifact: candidate-persistence-gate
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-gate
decision: authorize-exact-task-control-reference-candidate-persistence
subject_class: W
subject_path: docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md
subject_bytes: 31350
subject_sha256: f1a0ec857c7efe914a3c3cd5f3d8049763d8339b8c96cee0544e94126f577288
subject_git_blob: 1968993da7dded58d70d705ef3d23165667e94b4
gate_subject_main: fff0d67c2ef4af6db1f226cb02b1ccf8912d6a3a
decided_on: 2026-09-06
normative_effect: none
supersedes: null
---

# Workflow v1 task-control reference candidate-persistence gate

## Result

**AUTHORIZE EXACT TASK-CONTROL REFERENCE CANDIDATE PERSISTENCE**

Decision:

`authorize-exact-task-control-reference-candidate-persistence`

The exact local task-control reference W is eligible for one later bounded,
serialized, byte-for-byte repository persistence operation that creates an
immutable candidate C and performs only the minimum Research Register
transition needed to bind that candidate and move to independent review.

This authorization becomes executable only after this gate record is durably
persisted and the Research Register advances to the candidate-persistence
execution gate. It is not authorization to write from the current local
Command Center task.

## Exact live and authority basis

Connected `@GitHub` read-only verification at the point of decision confirmed:

- repository: `ahtoxaandy999/agentic-development-workflow`;
- live `main`: `fff0d67c2ef4af6db1f226cb02b1ccf8912d6a3a`;
- live tree: `4873f3ae07e0f1596883ce8949b4393e8cebd9f9`;
- sole parent: `d21e3e1de8e9bb2ea8453e0d1bec0f98ec07c004`;
- commit message: `docs: persist task-control reference producer assessment`;
- branch `protected`: `false`;
- protection `enabled`: `false`;
- required-status-check enforcement: `off`;
- Research Register blob:
  `eae64e7b28382e62bb6cd28d13d57e32bad4c459`;
- both current Register gates:
  `Workflow v1 task-control reference candidate persistence authorization gate`;
- producer-verification assessment blob:
  `585509fd3ae304b04b197d427a692b237744607a`;
- proposed candidate path remains absent at live `main`.

No competing persisted task-control reference candidate, review, disposition
or later current-gate decision was found in the controlling Register or the
target path.

## Accepted inputs

The authorization relies on the following current inputs without reopening
their accepted scopes:

- materialization gate:
  `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-MATERIALIZATION-GATE-001.md`,
  blob `64259a87d2a79e42dc1eef89acb680c7e4b471ba`, decision
  `authorize-one-non-operative-task-control-reference-materialization-with-ru1-evidence`;
- producer-verification assessment:
  `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-RU1-PRODUCER-VERIFICATION-ASSESSMENT-001.md`,
  blob `585509fd3ae304b04b197d427a692b237744607a`, decision
  `accept-local-task-control-reference-w-for-candidate-persistence-framing`;
- exact local W:
  `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`, 31,350 bytes,
  SHA-256
  `f1a0ec857c7efe914a3c3cd5f3d8049763d8339b8c96cee0544e94126f577288`,
  computed Git blob `1968993da7dded58d70d705ef3d23165667e94b4`;
- producer checks: `23-pass-0-fail-0-skipped`;
- RU-1 status: provisional utility evidence exists, but RU-1 remains open
  pending immutable-candidate review, disposition and final utility assessment.

The complete local package remains under user custody. Only the exact W is
selected as candidate content. The local manifest, raw payloads and utility
observations are supporting evidence and are not selected for repository
persistence.

## Gate assessment

Prerequisites pass:

- the materialization gate authorized the exact artifact class and path;
- production completed without repository effects;
- the W has stable byte, SHA-256 and computed Git-blob identities;
- all 23 required producer checks passed with no failure or skip;
- coordinator assessment found no BLOCKER, MAJOR or MINOR producer finding;
- the proposed destination is absent on the verified live subject;
- no new mechanism selection, semantic relaxation or mutable-state owner is
  required to publish the exact W;
- independent review can bind the future full candidate commit and exact file
  blob after publication;
- all missing technical enforcement remains representable as an execution
  prerequisite, procedural control or denied mode.

Therefore one bounded candidate-persistence operation is justified. The
unprotected branch prevents routine reliance on platform enforcement, so the
operation must remain separately dispatched, supervised, serialized,
exact-base-bound and guarded by an expected-old-SHA lease.

## Authorized future persistence operation

After this gate is persisted, one separately dispatched projectless Codex task
may:

1. verify a fresh exact live `main` through connected `@GitHub` and native Git;
2. require local `HEAD`, fetched `origin/main` and live remote `main` to equal
   that exact post-gate-persistence base;
3. require the expected repository, origin, one clean worktree, no unfinished
   Git operation or lock, and explicit human confirmation that no competing
   repository writer is active;
4. verify the canonical local W identity listed in this gate;
5. copy that W byte-for-byte to
   `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`;
6. update only `docs/research/research-register.md` with the minimum candidate
   identity and next-gate transition;
7. verify exact two-path scope, serialization, modes, byte equality, hashes,
   blobs and complete Register reconstruction;
8. create exactly one commit with the verified post-gate-persistence base as
   its sole parent;
9. perform exactly one guarded push to `main` with an explicit
   expected-old-SHA lease; and
10. perform read-only remote verification and stop.

If any exact input, destination-absence condition, authority statement,
worktree/exclusivity condition or remote ref differs, the executor must stop
without adapting, rebasing, replaying, rewriting or pushing.

## Exact changed-path boundary for candidate persistence

The future candidate-persistence execution may change exactly:

1. add
   `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`;
2. modify
   `docs/research/research-register.md`.

No evidence manifest, raw evidence payload, utility observation, assessment,
gate, accepted reference, tooling source, test, policy or other repository path
may change in that operation.

## Candidate identity and Register transition

The future persistence task must record the exact published candidate through
path, artifact ID, bytes, SHA-256, Git blob and persistence task ID. The
containing commit SHA is returned and independently verified after commit
creation; it must not be embedded through a self-referential commit rewrite.

The minimum candidate transition should add fields equivalent to:

```yaml
workflow_v1_task_control_reference_candidate: docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md
workflow_v1_task_control_reference_candidate_id: ADW-WF1-TASK-CONTROL-REFERENCE-001
workflow_v1_task_control_reference_candidate_blob: 1968993da7dded58d70d705ef3d23165667e94b4
workflow_v1_task_control_reference_candidate_sha256: f1a0ec857c7efe914a3c3cd5f3d8049763d8339b8c96cee0544e94126f577288
workflow_v1_task_control_reference_candidate_bytes: 31350
workflow_v1_task_control_reference_candidate_task_id: ADW-WF1-TASK-CONTROL-REFERENCE-CANDIDATE-PERSIST-001
```

Both current `next_gate` values must become exactly:

`Workflow v1 task-control reference independent review gate`

The current assessment narrative must become historical without being
rewritten as acceptance. A new current paragraph may state only that exact
candidate persistence established C identity, that producer W evidence was
bound to C by byte equality and remote readback, and that independent review
and coordinator disposition remain outstanding.

The Register must preserve all existing decisions and restrictions, including
Workflow v1 being non-normative, unadopted and unimplemented, RG1-RG12 being
unresolved, DI-1/DI-2, RU-1 remaining open, RU-2 remaining unselected and all
routine/parallel/automated/unattended/AFK write restrictions.

## Verification and acceptance contract

Candidate persistence passes only if:

- the published candidate is byte-identical to the exact W;
- bytes, SHA-256, Git blob, mode and serialization match this gate;
- the candidate commit has exactly the authorized base as sole parent;
- its complete changed-path set contains exactly the candidate and Register;
- the Register reconstruction contains only the authorized transition;
- live `main`, fetched `origin/main` and local `HEAD` equal the resulting
  candidate commit after push;
- the candidate remains explanatory, non-operative, non-normative and draft;
- no local supporting evidence file was published; and
- no review, disposition, acceptance, operational authority or Workflow v1
  adoption is claimed.

Candidate persistence creates immutable C identity only. Producer verification
does not substitute for independent review. The next review must use a fresh
Independent Review context, reread the exact full candidate commit and
controlling sources, and bind findings to the exact candidate path/blob.

## RG and design-impact boundary

RG1 through RG12 remain unresolved. This gate resolves none of them.

RG1 and RG2 require procedural serialization, exact-base checks, sole-writer
confirmation and a guarded lease because branch protection and writer fencing
are absent. RG3 requires exact publication and remote readback. RG4 prevents
the producer or persistence executor from substituting for independent review.
RG5-RG9 remain external prerequisites or evidence limitations. RG10-RG11 do
not select optional integrations. RG12 continues to deny unattended and AFK
execution. Missing prerequisites fail closed.

DI-1 is preserved: orthogonal state planes and legitimate N/A are not collapsed
into a native product status or pass.

DI-2 is preserved: exact-subject freshness, operation-aware retry,
containment/recovery separation, durable episode history, reopening,
resumption/reset and independent terminal guards are unchanged.

## Non-goals

This gate does not authorize or perform:

- persistence of this gate record without a separate exact-base task;
- candidate persistence before gate persistence;
- modification or regeneration of the W;
- persistence of local evidence or utility observations;
- independent review, correction, disposition or acceptance;
- operational task-control use or schema materialization;
- validators, recorders, automation, hooks, Actions, Apps, MCPs or skills;
- routine, parallel, automated, unattended or AFK writes;
- branch-protection or permission changes;
- RU-2 selection;
- Workflow v1 adoption or a new baseline;
- resolution of RG1 through RG12.

## Intended Register transition after gate persistence

A separately authorized exact-base gate-persistence task should:

- add a durable pointer to
  `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-CANDIDATE-PERSISTENCE-GATE-001.md`;
- record task ID
  `ADW-WF1-TASK-CONTROL-REFERENCE-CANDIDATE-PERSISTENCE-GATE-001`;
- record decision
  `authorize-exact-task-control-reference-candidate-persistence`;
- preserve the exact W and producer-assessment fields already in the Register;
- preserve all earlier decisions, statuses and restrictions; and
- change both current next-gate fields to
  `Workflow v1 task-control reference candidate persistence execution`.

No candidate pointer or review status may be invented during gate persistence.

## Lifecycle and stop boundary

The intended sequence is:

candidate-persistence authorization
→ gate persistence
→ exact W candidate persistence
→ immutable candidate C
→ fresh independent candidate review
→ corrected new candidate and renewed review if required
→ coordinator disposition
→ RU-1 final utility assessment
→ only then consider RU-2 selection or another tooling/materialization gate.

This gate stops before repository persistence. The current next action is gate
persistence, not candidate publication.

## Next gates

Immediate next gate:

`Workflow v1 task-control reference candidate persistence gate persistence`

Post-persistence gate:

`Workflow v1 task-control reference candidate persistence execution`

## Explicit non-actions

This gate did not:

- modify GitHub, the repository or Research Register;
- modify the local W or evidence package;
- create a candidate, commit or push;
- perform independent review, disposition or acceptance;
- run the persistence checker;
- execute an operational task-control workflow;
- create a schema, parser, validator, recorder or automation;
- select RU-2;
- change protection or permissions;
- authorize routine, parallel, automated, unattended or AFK work;
- adopt Workflow v1;
- resolve RG1 through RG12;
- establish a baseline.
