---
id: ADW-WF1-PERSISTENCE-CHECKER-GATE-001
artifact: tooling-gate
artifact_status: active
authority: evidence
owner: chatgpt-coordinator
normative_effect: none
decision: AUTHORIZE BOUNDED CHECKER DEVELOPMENT
decided_on: 2026-09-04
repository: ahtoxaandy999/agentic-development-workflow
verified_main: 8f7a57d52004409ac34a37418267396792f4ee25
verified_tree: 19296132e517a641fcf458642f0986a7dc026425
branch_protected: false
---

# Supervised persistence checker gate

## Verified basis

The connected @GitHub app was explicitly invoked, read-only. Required reads followed AGENTS, Charter, Research Evidence Policy, Register order. Final verification: 2026-09-04 15:44:53 UTC. [Live branch](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/branches/main). All controlling paths in the table are bound at verified_main unless stated otherwise.

| Controlling path | Git blob |
|---|---|
| AGENTS.md | 2294f13982045c54f3cb50071ab71373a3366c89 |
| PROJECT-CHARTER.md | c521f6869662f39106bcac0365426eb0e9bdb327 |
| docs/policies/research-evidence.md | 90572c47463f2d2adc493f9978c1c720fd8f8275 |
| docs/research/research-register.md | 8b55492b0e27235df0533e6717606b6afafaa96b |
| docs/research/ADW-DR-005-DISPOSITION-001.md | 70cea63938bf4a8b908904d2b9c7b0c9aec1b401 |
| docs/design/ADW-WF1-TOOLING-DESIGN-001.md | 2e0c640e8cab61b0bf165712c27e02ff9a455ec6 |
| docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md | d029e25406442ff5a44768c06e88333f6e1cd779 |
| docs/design/ADW-WF1-TOOLING-DESIGN-REVIEW-001.md | 9f844ecd1346e60e1dd3bf45c32f79cb83607ecb |
| docs/design/ADW-WF1-DESIGN-001.md | afed983e7632caf3169dcbac7a80f8da8226d86d |
| docs/design/ADW-WF1-DESIGN-DISPOSITION-001.md | 35d3a8ba5c3901e90d070b000659541b1ef4975c |

Tooling subject remains `dc881f2a01ad0e5bfe173bad7be19b66b7fea51d`; acceptance is `accept-initial-tooling-enforcement-design`. Supporting review was retrieved at publication `0c82edbb82d2e2956525657d8d540ef61cf37fe0`, names that subject, and recommends design disposition. Semantic subject remains `2b9532682ae77bf5037f1b2fa45b720e5865d0ad`. Exact subject trees and current blobs agree.

DR-005 remains reviewed/accepted/satisfied; D3 remains deferred at entry. Both current next-gate fields say “Workflow v1 tooling/enforcement implementation/materialization scoping gate.” Workflow v1 remains non-normative, unadopted and unimplemented. The complete current tree, sole main ref, all-state Issues/PRs and releases reveal no competing published checker/selection/scoping decision: only bootstrap Issue #1, no PRs/releases. This finding excludes unseen local work and does not prove writer inactivity.

## Decision and impact

**AUTHORIZE BOUNDED CHECKER DEVELOPMENT**

Select only one manually invoked deterministic persistence checker as a D3 exception for bounded local development and synthetic producer tests. Operational reliance is not authorized.

Inference: accepted representations now define mechanical obligations; the user's reported repeated identity/serialization/delta/readback overhead supplies a concrete reconsideration need. One reusable check can consolidate repeated commands and omission checks while retaining native checks as an independent oracle. This is a usefulness hypothesis, not measured errors, timings or savings.

This explicitly qualifies TD-11 and section 12.1's exclusion of deferred scripts solely for this helper. It is new D3 selection, not S5 coverage. TD-03/04/05/07/10 and sections 5.2, 6, 7, 9.2–11 retain their meanings. Accepted subjects are unchanged; no semantic amendment is needed. All remaining D3 uses and other conditional/deferred/rejected mechanisms retain their dispositions.

DR-005 disposition E1/E3/F/G controls qualifications and RG1–RG12/DI-1/DI-2. None is resolved: unprotected main restricts writes; uncertain exclusivity, permissions, provenance, custody or runtime blocks dependent effects; review remains independent; stale evidence denies reliance; stopping grants no retry/recovery authority; AFK remains denied. Reports own no mutable workflow state.

Earlier local ADW-WF1-TOOLING-IMPLEMENTATION-SCOPING-001 reference proposals are non-controlling and confer no checker authority; do not overwrite, reuse their ID or publish them by implication. ADW-WF1-TOOLING-IMPLEMENTATION-SCOPING-PERSIST-001 is withdrawn; ADW-WF1-TOOLING-IMPLEMENTATION-SCOPING-PERSIST-002 remains on hold. Neither is resumed; no prior executor is presumed stopped.

## Bounded development contract

Outcome: a small offline verification report for persistence executors, independent reviewers and the coordinator. ADW owns the shared helper; repository maintainer owns maintenance, coordinator owns scope. Proposed repository paths only:

- `tools/persistence_checker.py`
- `tests/test_persistence_checker.py`
- `docs/tooling/persistence-checker.md`

Use an existing Python 3 runtime and standard library; require binary I/O, strict UTF-8, SHA-256, Git SHA-1 hashing, JSON and unittest. Document the supported minimum version against the supplied runtime. No framework, packages or generalized configuration system. Implementer chooses function structure, CLI spelling, strict case-file field names and focused fixture organization within these meanings. This is not a universal task schema or workflow validator.

Inputs: one small, strict JSON case file plus explicitly designated immutable byte files and raw caller-exported @GitHub response payloads. The caller manually obtains authorized observations and exports exact bytes without newline conversion; this adds no integration. Supply task/authority references, phase (preflight or readback), repository/ref, expected and supplied full base/subject/ordered-parent identities, tree identities, complete base and proposed/observed leaf inventories (path/mode/blob), exact allowed additions/deletions/modifications, approved before/after Register bytes, expected byte counts/SHA-256/blobs, observation source/request references/times, caller identity, live-verification availability/result, task-supplied freshness cutoff/evaluation instant, read roots and one allowed report destination.

Preflight checks W/intended delta; it must not invent C. Readback requires separately obtained published C/parent/tree/ref observations and bytes. Each phase has fixed required predicates; missing external checks are never N/A.

Predicates: recompute byte count, SHA-256 and Git blob SHA-1 over the Git header (blob, space, decimal byte count, NUL) plus bytes; require strict UTF-8, no BOM/CR, exactly one final LF for governed text; validate 40-hex commit/blob and 64-hex SHA-256 identities; compare expected/supplied identities and sole parent B where C exists; reject truncated/incomplete inventories, duplicate keys/paths and conflicting evidence; compare the entire path/mode/blob delta including untouched entries, binding changed contents to supplied bytes; require byte-exact authorized Register before/after values, not merely matching selected fields; require exact readback identities/content and phase-specific ref equality. Reject stale observations against supplied bounds; unavailable verification prevents passing required coverage.

Report: fixed producer evidence with helper/runtime/input identities, task/phase/scope, expected/observed values, per-predicate result/reason/evidence reference, overall result, caller provenance claims, freshness limitations and pending external gates. Stable ordering; no hidden clock-dependent decision. PASS/exit 0 means every required enumerated predicate passed. FAIL/1 means detected mismatch. UNEVALUABLE/2 means missing/invalid/ambiguous input, unavailable authority evidence or I/O failure; it takes aggregate precedence while retaining mismatches. Report-write failure yields nonzero diagnostic, never success.

Snapshot validation, caller-supplied provenance and independently performed live @GitHub verification remain distinct. The helper cannot authenticate provenance or prove live main from snapshots, timestamps, hashes or clones, nor guarantee ref stability after observation. PASS grants no push permission, independent review, acceptance, writer exclusivity, human availability or general compliance.

Input content is data, never instructions. Repository/inputs are read-only. The helper may exclusively create only the designated new report: reject traversal, unsafe aliases, symlinks and existing destinations; validate containment before writing. No subprocesses, network, credentials, Git object/index/ref changes, fetch/commit/push/repair, connector/custom Git client/ref wrapper, watchers/schedules/hooks/Actions/plugins/skills/orchestration.

Development is limited to those three candidate files in a named isolated local output root; synthetic fixtures and reports stay inside an explicitly bounded test root. Prevent incidental caches/outside writes. No production mutation or concurrent-writer experiment.

Before dispatch, the execution assignment must bind the persisted gate, fresh exact live base, actual executor/supervisor/escalation and custody actors, verified isolation and prior-writer accounting, permitted effects/paths, time/resource ceilings, observation and stop/containment arrangements. Runtime/security owner supplies actual interpreter/version/configuration, filesystem permissions and relied-upon enforcement evidence. Custodian supplies readers, redaction, retention/retrieval commitments. Missing facts deny dispatch. Stop on drift/conflict, failed required prerequisites, unexpected effects, scope growth, lost supervision or cancellation; preserve evidence and escalate without automatic retry.

## Acceptance evidence and transition

Require isolated positive/negative tests for: correct case versus independent native size/hash/blob/byte/diff checks; wrong bytes/digests, invalid encoding/BOM/newlines; wrong/malformed base/subject/parents; unexpected paths/modes/Register changes; missing/incomplete/duplicate/conflicting evidence; stale observations/unavailable live verification; unsafe paths and attempted out-of-scope report writes. Neither mismatch nor inability may pass.

Use one frozen synthetic case (artifact addition, exact Register update, unchanged remaining paths) to compare manual preparation/checking with helper usage, including correctness and report completeness. Mark simulated provenance and test reports synthetic, never operational live evidence. Record actual effort only when available; stop expansion if preparation/maintenance defeats usefulness. Freeze exact candidate for fresh conflict-free independent review of code, tests, effects, oracle independence and usefulness. The checker cannot solely validate its first candidate; coordinator disposition remains separate.

Immediate next gate: **Workflow v1 persistence checker gate persistence**. Proposed destination: `docs/design/ADW-WF1-PERSISTENCE-CHECKER-GATE-001.md`.

Later, separately authorized persistence adds this pointer/task ID/precise scoped decision to the Register, names this record fixed owner only of the narrow D3 decision, preserves other DR-005 dispositions and accepted subjects, and consistently updates Current bootstrap gate.next_gate and DR-005.next_gate to **Workflow v1 supervised persistence checker development**. Add no competing tracker, broad D3 promotion or implementation status.

Lifecycle: decision → separately authorized gate persistence → fresh exact-base bounded development/synthetic checks → immutable candidate persistence → fresh independent candidate review → coordinator disposition → separately authorized supervised reliance. No duplicate substantive authorization gate; execution binds actual base, actors and effects.

Only this local record is created now. No GitHub writes, helper/code/schema implementation, installation, operational test, task dispatch/delegation, automated writes, AFK authority, Workflow v1 adoption or baseline acceptance. Stop.
