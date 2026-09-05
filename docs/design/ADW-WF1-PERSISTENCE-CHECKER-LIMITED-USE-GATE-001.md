---
id: ADW-WF1-PERSISTENCE-CHECKER-LIMITED-USE-GATE-001
artifact: checker-limited-use-gate
artifact_status: active
owner: chatgpt-coordinator
decision: authorize-one-bounded-supervised-retrospective-readback-secondary-helper-use
repository: ahtoxaandy999/agentic-development-workflow
decision_basis_main: 79b9c2d2dbd9cedf674b8a1569a03cd3bd8da491
authorized_base_commit: 729e5d1ba3a8d06c976c58b12493c4c2c95eeb34
authorized_candidate_commit: 79b9c2d2dbd9cedf674b8a1569a03cd3bd8da491
checker_subject_commit: d17af996803ae91253f11308e92f1b3601e04aa8
operational_validation_disposition_ref: docs/design/ADW-WF1-PERSISTENCE-CHECKER-OPVAL-DISPOSITION-RECORD-001.md
operational_validation_disposition_blob: b53c22e6a2e76ce75a7af4fd56a6b2adfda68454
register_ref: docs/research/research-register.md
register_blob: 0f87311cea47a68cfa4841c53666941d74ab36bf
decided_on: 2026-09-05
normative_effect: none
execution_authority: none
supersedes: null
---

# Workflow v1 persistence checker limited supervised secondary-helper use gate

## Result

**LIMITED SUPERVISED SECONDARY-HELPER USE GATE READY**

Decision:

`authorize-one-bounded-supervised-retrospective-readback-secondary-helper-use`

The coordinator authorizes the eligibility of exactly one future supervised retrospective readback case using the accepted persistence checker only as a secondary helper. This gate record does not authorize the checker invocation itself. Fixture preparation, exact invocation and any report creation remain subject to later bounded authorization and fresh prerequisite verification.

## Live decision basis

Connected `@GitHub` read-only verification established at the decision point:

- live `main`: `79b9c2d2dbd9cedf674b8a1569a03cd3bd8da491`;
- Research Register blob: `0f87311cea47a68cfa4841c53666941d74ab36bf`;
- both current Register next-gate fields: `Workflow v1 supervised persistence checker limited supervised secondary-helper use authorization gate`;
- operational-validation disposition blob: `b53c22e6a2e76ce75a7af4fd56a6b2adfda68454`;
- accepted checker usage blob: `405f8222b4d6f7b48b9332a758ab6d1c3c945f0f`;
- no competing limited-use authorization artifact was found in the inspected current repository surfaces.

The parent-to-candidate comparison is exactly one commit ahead and zero behind, with only these changed paths:

- `docs/design/ADW-WF1-PERSISTENCE-CHECKER-OPVAL-DISPOSITION-RECORD-001.md`;
- `docs/research/research-register.md`.

No fresh branch-protection state is asserted by this record. Branch protection is not relied upon to authorize this read-only retrospective case, and no broader write or operating authority follows from its state.

## Exact authorized case subject

The only eligible case is a readback evaluation of:

- base `B`: `729e5d1ba3a8d06c976c58b12493c4c2c95eeb34`;
- published candidate `C`: `79b9c2d2dbd9cedf674b8a1569a03cd3bd8da491`;
- sole ordered parent relationship: `C` has only parent `B`;
- exact changed-path set:
  - `docs/design/ADW-WF1-PERSISTENCE-CHECKER-OPVAL-DISPOSITION-RECORD-001.md` added;
  - `docs/research/research-register.md` modified.

The governed disposition file at `C` is bound to:

- Git blob: `b53c22e6a2e76ce75a7af4fd56a6b2adfda68454`;
- bytes: `10746`;
- SHA-256: `265343dfd01f9d8c2697ac6edcbab951c93f9053f3d48d88110de898fbdea0d3`;
- mode: `100644`;
- UTF-8 without BOM, LF-only, exactly one final LF.

The Research Register transition is bound to:

- before blob at `B`: `222661d38db71f20b396f16a4ca16199dabbc4aa`;
- before bytes: `51947`;
- before SHA-256: `318ead97e0774a87cb4f30cc1aa8173b67fcac28d549c4e04b81abf91cb78c19`;
- after blob at `C`: `0f87311cea47a68cfa4841c53666941d74ab36bf`;
- after bytes: `53037`;
- after SHA-256: `8d58f7a05c96cb783bf806daecb99f194a7ca33f08ac688a04ba25903fb3d546`.

The case must not be retargeted to another base, candidate, parent, path set or Register transition. A moved live ref, changed subject or incompatible evidence requires a new coordinator decision rather than adaptation.

## Exact checker basis

The only eligible helper is the accepted checker candidate at commit `d17af996803ae91253f11308e92f1b3601e04aa8`:

| Path | Git blob | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `tools/persistence_checker.py` | `655cf2e8c2809b299e53f6e585a5d9bce0dc9c34` | 62875 | `c0ad28a8e59d3e4d161c74b0f832682ed590836229b35f45527c645d9030d723` |
| `tests/test_persistence_checker.py` | `f975ced081a736e9b156411a303bb8675deb8bb3` | 62065 | `f58273a337019da436af1d65d4f590e008773c72bf00566ebb9011a5c0d7a970` |
| `docs/tooling/persistence-checker.md` | `405f8222b4d6f7b48b9332a758ab6d1c3c945f0f` | 14173 | `cec48b49f7496c3869b5a10eefd43db266e384d9aa3f816b22f1cda1da0c3814` |

Any material checker change creates a new identity and is outside this gate.

## Permitted role and authority ordering

The checker is secondary evidence only.

Native Git and connected `@GitHub` verification remain the primary evidence and acceptance oracle. They must independently establish the exact base, candidate, parent, tree and changed paths; byte-level checks must independently establish the governed file and Register identities.

A checker result cannot:

- establish current live repository truth by itself;
- replace authoritative or native rereads;
- grant persistence, push, acceptance or lifecycle-transition authority;
- resolve a discrepancy with the primary evidence;
- become an authoritative mutable state owner.

The coordinator remains responsible for any later acceptance or disposition. The Research Register remains the current repository owner of mutable gate and decision status.

## Future fixture requirements

A later fixture-preparation authorization must create one isolated, readback-phase case without running the checker. It must bind:

- the exact `B + C` subject above;
- complete base and candidate leaf inventories;
- exact allowed additions, deletions and modifications;
- exact before and after Register bytes and identities;
- exact disposition-record bytes and identity;
- raw, complete, non-truncated GitHub branch and recursive-tree response bytes;
- independently checked directory/tree relationships;
- caller-supplied observation, evaluation and freshness times;
- one absolute canonical read root;
- one separate absolute canonical report root;
- one new report destination that does not exist;
- named executor, supervisor, evidence custodian and escalation owner;
- explicit limitations and pending gates.

All fixture and oracle identities must be frozen and reviewed before any invocation authorization. Manual fixture or oracle preparation is not trusted merely because it completed successfully.

If live `main` no longer equals `C` when live-ref evidence is captured or relied upon, preparation stops. The fixture must not substitute historical or synthetic evidence for a required live claim without a new explicit decision.

## Future invocation ceiling

Subject to later exact authorization, this gate permits at most:

- exactly one checker invocation;
- phase `readback` only;
- the frozen case described here only;
- one new local report as the sole allowed effect;
- no invocation for `--help`, introspection, probing, correction, retry or a second case.

This record does not itself activate that ceiling or authorize the invocation.

## Mandatory stop conditions

The fixture-preparation or invocation lifecycle must stop on:

- live `main` differing from `C` at a required state-dependent check;
- stale, unavailable, incomplete, unauthenticated or unverifiable authority evidence;
- subject, parent, tree, inventory, path, byte, mode, hash or blob mismatch;
- fixture, oracle, report-path or case-preparation error;
- ambiguity or contradictory evidence;
- inability to establish supervision, custody, permissions, path containment or writer exclusivity required by the later task;
- checker/native-oracle disagreement;
- checker result `FAIL/1`;
- checker result `UNEVALUABLE/2`;
- report creation failure or partial report;
- attempted scope expansion.

No stop condition is permission to repair, retry, regenerate, retarget or continue. Any correction or renewed attempt requires a new explicit authorization and a new execution episode.

## Expected interpretation of a future result

If a separately authorized invocation returns `PASS/0`, that is supporting evidence for this exact case only. It does not accept the publication commit, establish general operational readiness or authorize another use.

`FAIL/1` or `UNEVALUABLE/2` is non-acceptance for the case and stops the lifecycle. Detected failures remain visible even when `UNEVALUABLE` has aggregate precedence.

All preparation and invocation attempts, including failed episodes, must remain distinct and preserved.

## Explicit non-authorities

This gate does not authorize:

- checker execution now;
- fixture, case, oracle or report creation now;
- preflight-phase checker use;
- a second invocation, retry or corrected run;
- standing, routine, primary or sole-authority checker use;
- automated acceptance or execution;
- parallel execution;
- unattended or AFK execution;
- repository, Research Register, Git or GitHub mutation;
- installation, configuration, hooks, Actions, workflows or orchestration;
- replacement of independent review, native verification or coordinator disposition;
- another repository, workflow, base, candidate, path set or task class;
- Workflow v1 normative adoption;
- resolution of RG1 through RG12;
- modification of DI-1 or DI-2;
- establishment of a new baseline.

## RG and design-impact boundaries

RG1 through RG12 remain unresolved. This gate creates none of the missing controls and relies on none of them as resolved.

DI-1 remains preserved: orthogonal state planes and legitimate `N/A` remain distinct from required pass.

DI-2 remains preserved: freshness, operation-aware retry, containment/recovery separation, durable episode history, reopening, explicit reset and independent terminal guards are not weakened.

## Acceptance test for this gate

This gate is correctly interpreted only if two competent operators independently conclude that:

1. exactly one retrospective `readback` case is eligible;
2. `B`, `C`, their parent relationship and their two-path delta are immutable and exact;
3. checker output is secondary to native Git and connected `@GitHub` evidence;
4. no fixture, invocation or report creation is authorized by this record alone;
5. a later invocation, if separately authorized, has a ceiling of one and one local report effect;
6. every mismatch, preparation error, stale state, disagreement, `FAIL/1` or `UNEVALUABLE/2` stops the lifecycle;
7. preflight, retry, routine, automated, parallel, unattended and AFK use remain unauthorized;
8. RG1 through RG12 remain unresolved and DI-1/DI-2 remain preserved.

## Lifecycle

Immediate next gate:

`Workflow v1 supervised persistence checker limited-use gate persistence`

After verified gate persistence, the intended next gate is:

`Workflow v1 supervised persistence checker single retrospective readback fixture preparation gate`

Fixture preparation, fixture verification, exact invocation authorization, invocation, result assessment and any later Register transition remain separate. No later step follows automatically.

## Materialization statement

This gate record was materialized locally under explicit user authorization. Its creation did not prepare a fixture, run the checker, create a checker report, modify the repository or Research Register, or write to GitHub. Exact serialization identity is reported separately after verification.
