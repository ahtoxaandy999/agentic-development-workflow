---
id: ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-NEGATIVE-VALIDATION-GATE-001
artifact: coordinator-validation-gate
artifact_status: active
owner: chatgpt-coordinator
repository: ahtoxaandy999/agentic-development-workflow
gate_subject_main: 03ad4ae1525851dd9afb3c15e754f5452889b63b
gate_subject_tree: b07126495d74b41370e71cf483d5d4a98af41ef1
gate_subject_register_blob: 21978f8552453dcf6ad64fe7d8843f51f6cf28ff
ruleset_id: 22392483
decided_on: 2026-09-06
decision: authorize-bounded-negative-enforcement-validation
normative_effect: none
supersedes: null
---

# Workflow v1 protected serialized write-path pilot negative validation gate

## Decision

`authorize-bounded-negative-enforcement-validation`

Authorize one later, separately dispatched, supervised and serialized negative-enforcement validation episode against the exact live basis in this record. The episode covers exactly three attempted changes to `refs/heads/main`: a direct fast-forward update, a forced non-fast-forward update, and deletion. Each case receives one invocation and no retry.

This gate is authorization and framing only. It performs no test, ref update, commit-object creation, default-branch change, ruleset change, repository write, or GitHub mutation.

## Exact live basis

Connected `@GitHub` read-only observations at gate evaluation established:

- live `main`: `03ad4ae1525851dd9afb3c15e754f5452889b63b` (`P`);
- live tree: `b07126495d74b41370e71cf483d5d4a98af41ef1` (`T`);
- ordered parents of `P`:
  1. `d2c055f1b9c33b52c18cf3dfcbe9034d2cf0d40e`;
  2. `ec1c350327e0a0c8e464fdc12d3474195c9be2a9`;
- `docs/research/research-register.md`: Git blob `21978f8552453dcf6ad64fe7d8843f51f6cf28ff`, 104200 bytes, SHA-256 `856fc69c6a8d3af3ad350bfb7d62de5a951e4918e421a1ff0ca83f2e19516124`;
- both authoritative mutable next-gate fields: `Workflow v1 protected serialized write-path enforcement pilot negative enforcement validation scoping gate`;
- repository: public, not archived, default branch `main`;
- connected user: `ahtoxaandy999`, repository permission `admin`;
- branch response: `main` is covered by rules while classic protection is disabled and required-status-check enforcement is off;
- active repository rulesets: exactly one;
- ruleset `22392483`, `adw-protect-main-pilot`: active, repository branch ruleset, target only `refs/heads/main`, no exclusions, no bypass actors, `current_user_can_bypass: never`, and exactly the deletion, non-fast-forward, and pull-request rules; the pull-request rule allows only merge commits and requires zero approvals/checks;
- open pull requests: none;
- existing branches: `main`, `adw/wf1-protected-write-path-pilot-001`, and `adw/wf1-protected-write-path-pilot-evidence-001`;
- no competing current negative-validation gate, decision, or persisted record was found in the inspected authoritative repository owners.

The ruleset rule-suite endpoint returned `403 Resource not accessible by integration`. The execution evidence contract therefore does not rely on rule-suite history. Raw push rejection evidence plus authoritative before/after ref, repository, and ruleset readback is required.

## Controlling design boundaries

The accepted tooling design and its disposition remain controlling. For this episode:

- RG1 remains unresolved until effective rejection evidence is separately assessed and dispositioned; this gate does not resolve it.
- RG2 remains unresolved because serialization and the declared writer are procedural, not a global credential/process fence.
- RG3 remains unresolved; exact `B/C/I/Ppub` publication mapping is not generalized by these negative cases.
- RG4 remains unresolved; the configured pull-request rule requires zero platform approvals and independent review remains separately bound evidence.
- post-operation readback detects state but cannot retroactively authorize or undo a wrong mutation;
- ambiguous completion denies blind retry;
- recovery is a distinct, bounded, evidence-bearing episode and cannot erase the failed test episode;
- no emergency write power or standing bypass is created.

DI-1 and DI-2 remain preserved. Workflow v1 remains non-normative, unadopted, and not generally implemented.

## Why the episode is recoverable

Every proposed subject has tree `T`. An unexpected successful fast-forward or forced non-fast-forward update changes commit identity but not repository content, including the Research Register bytes. Before any negative case, a dedicated recovery branch must be created at exact `P` and read back. The connected repository owner has current `admin` permission and GitHub supports disabling/restoring a repository ruleset, updating a repository default branch, and creating/updating branch references.

Deletion of the default branch is independently rejected by GitHub and would not prove the ruleset deletion rule. Therefore the deletion case is eligible only after the repository default branch is temporarily changed to the verified recovery branch. If deletion unexpectedly succeeds, `P` remains reachable through that recovery branch, so `main` can be recreated exactly at `P` before restoring the default branch. The active ruleset contains no creation restriction.

These properties prevent content loss and retain an immutable recovery identity. Any mismatch in permissions, API availability, recovery-branch identity, ruleset identity, or default-branch transitions blocks the affected test before its invocation.

## Actors and state ownership

- Coordinator and serialization controller: the current Agentic Development Command Center.
- Supervisor, evidence custodian, escalation owner, and emergency recovery owner: the current user, GitHub owner `ahtoxaandy999`.
- Execution environment: one new projectless Codex task, task ID `ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-NEGATIVE-VALIDATION-EXEC-001`.
- Repository mutation actor: the single credential/session verified immediately before execution as `ahtoxaandy999` with `admin` permission and no ruleset bypass.
- Evidence owner: the user as custodian; the executor may create only the isolated local evidence package named by the later execution prompt.
- Research Register: remains the sole repository owner of current gate/status. It is not changed by the validation episode.

No second executor, background writer, delegation, parallel case execution, automation, scheduler, hook, Action, or retry is allowed.

## Frozen identifiers and test subjects

The later execution starts from:

- expected old `main` for every case: `P = 03ad4ae1525851dd9afb3c15e754f5452889b63b`;
- required unchanged content tree: `T = b07126495d74b41370e71cf483d5d4a98af41ef1`;
- required unchanged Register blob: `21978f8552453dcf6ad64fe7d8843f51f6cf28ff`;
- recovery branch: `adw/wf1-protected-write-path-pilot-negative-recovery-001`, created only at `P`;
- ruleset: exact ID `22392483` and the exact active configuration stated above.

Two harmless commit subjects may be created in an isolated temporary Git object store during execution:

1. `F`: one new commit whose sole parent is `P` and whose tree is exactly `T`. It is the direct fast-forward subject.
2. `N`: one new commit whose sole parent is `d2c055f1b9c33b52c18cf3dfcbe9034d2cf0d40e` and whose tree is exactly `T`. It is a sibling-side subject and is not a descendant of `P`; it is the forced non-fast-forward subject.

Before any remote test invocation, the executor must record the complete raw commit framing, full SHA, tree, ordered parent list, message, author/committer fields, and independent ancestry result for each subject. Neither subject may alter file bytes. No commit may be added to `main` except by an unexpected enforcement failure.

## Execution preconditions

The future execution must stop before any mutation unless all of the following are freshly true:

1. Connected `@GitHub` shows live `main = P`, tree `T`, Register blob as bound above, default branch `main`, ruleset `22392483` exact and active, no bypass, and no competing current decision or writer.
2. A native remote read independently shows `main = P`.
3. The named user explicitly confirms supervisor availability, custody availability, and no other active repository writer for the complete episode and possible recovery.
4. The execution credential is verified to be the same named repository owner with admin authority and can read the ruleset and repository settings needed for recovery.
5. The isolated local evidence root and temporary object store are absent or empty as specified by the execution grant; repository checkout/index/Git metadata are not used as an output area.
6. The recovery branch name is absent. Its creation at `P` succeeds once, is read back as exactly `P`, and remains unchanged before every case.
7. The exact recovery API/commands for ruleset disable/restore, ref restore/recreation, and default-branch update have been resolved without invoking the checker or a test mutation.
8. `F` and `N` satisfy the frozen subject constraints and their tree bytes independently reproduce `T`.

Failure or uncertainty in any prerequisite blocks the episode. Do not adapt names, identities, rules, actors, case count, order, or recovery mechanics.

## Authorized order and exact case semantics

The cases are strictly sequential. Each case has one Git push invocation, an exact expected-old-SHA lease for `refs/heads/main = P`, no retry, and immediate read-only evidence capture. A case may begin only after the prior case was rejected and authoritative readback still shows exact `P`, `T`, the Register blob, and the unchanged active ruleset.

### Case 1 — direct fast-forward rejection

- Subject: `F`, sole parent `P`, tree `T`.
- Invocation: one non-force fast-forward push of `F` to `refs/heads/main`, guarded by expected-old SHA `P`.
- Expected result: nonzero rejection attributable to the pull-request rule; remote `main` remains exactly `P`.
- PASS evidence: raw invocation/exit/stdout/stderr plus post-case @GitHub and native ref readback proving `main = P`, tree `T`, Register unchanged, and ruleset exact/active.
- Any success, ambiguous completion, moved ref, or rejection not attributable to the intended protection stops later cases and enters the recovery boundary.

### Case 2 — forced non-fast-forward rejection

- Subject: `N`, verified not to be a descendant of `P`, tree `T`.
- Invocation: one forced push of `N` to `refs/heads/main`, guarded by expected-old SHA `P`.
- Expected result: nonzero rejection attributable to the non-fast-forward rule, with the pull-request rule allowed to be additionally reported; remote `main` remains exactly `P`.
- PASS evidence: raw invocation/exit/stdout/stderr, independent ancestry evidence, and post-case @GitHub/native readback proving unchanged `P`, `T`, Register, and ruleset.
- Any success, ambiguity, or unexpected ref/configuration state stops later cases and enters recovery.

### Case 3 — deletion rejection

Before the single deletion invocation:

1. Reverify recovery branch `= P`, main `= P`, tree `T`, Register, and exact active ruleset.
2. Change the repository default branch once from `main` to `adw/wf1-protected-write-path-pilot-negative-recovery-001`.
3. Read back the new default branch and both ref identities. If the change or readback is uncertain, restore if necessary and stop without deletion invocation.

Then:

- Invocation: one deletion push for `refs/heads/main`, guarded by expected-old SHA `P`.
- Expected result: nonzero rejection attributable to the ruleset deletion rule; `main` remains exactly `P`.
- PASS evidence: raw invocation/exit/stdout/stderr plus readback proving the deletion rule was the applicable denial, `main = P`, and recovery branch `= P`.
- After confirmed rejection, change the default branch once back to `main` and verify exact repository/default-branch/ref/ruleset state.
- Any success, ambiguity, wrong rejection source, or restoration mismatch enters recovery and makes the validation episode non-PASS.

The default-branch changes are test setup/restoration, not additional negative cases. They grant no standing authority to alter repository settings.

## Permitted effects in the future execution

Only the following effects may be separately dispatched under this gate:

- local creation of the isolated evidence directory and temporary Git object store;
- local creation of exactly `F` and `N` with tree `T` and the parents defined above;
- one remote recovery branch creation at exact `P`;
- exactly the three ordered main-ref push invocations described above, at most one per case and never retried;
- exactly one temporary default-branch change to the recovery branch and one restoration to `main`, only around case 3;
- exclusive creation of immutable local evidence files;
- conditional recovery effects stated below, only after a confirmed or ambiguous unexpected mutation.

No repository file, Research Register byte, ruleset setting, permission, PR, workflow, check, issue, tag, release, existing candidate branch, or existing artifact may otherwise change. Test and recovery branches are retained after the episode for later separately authorized cleanup; this gate does not authorize their deletion.

## Expected rejection evidence and episode result

For each case, evidence must retain:

- exact task/gate identity, actor, time window, command/API framing, expected-old SHA, subject SHA, subject tree and parent/ancestry facts;
- raw stdout, stderr, exit status, and any GitHub request/correlation identifiers available;
- raw @GitHub branch, repository, ruleset, and relevant ref readbacks before and after;
- byte identity of the Register at the read commit;
- hashes and byte counts of every retained evidence payload;
- an immutable manifest relating raw evidence to the case and observation time;
- whether the denial is attributable to the intended rule or is inconclusive.

The complete episode is PASS only when all three invocations are rejected for the intended enforcement reason, `main` remains `P` after each, default branch is restored to `main`, ruleset `22392483` remains exact/active, Register bytes remain unchanged, and recovery was not needed. An unexpected successful mutation, ambiguous response, unrelated denial, missing evidence, or any recovery use makes the episode FAIL or UNEVALUABLE, never PASS.

## Pre-authorized recovery boundary

Recovery is authorized only to restore the exact pre-episode state after an unexpected success or ambiguous mutation. It is not a retry and it ends the validation episode.

### If case 1 or case 2 unexpectedly changes `main`

1. Stop all later cases and preserve raw evidence.
2. Read both `main` and the recovery branch. Require the recovery branch to remain exactly `P`.
3. If ruleset enforcement blocks exact restoration, change only ruleset `22392483` from active to disabled; record/read back the complete before/disabled object.
4. Perform one forced ref restoration of `refs/heads/main` to exact `P`, with the observed unexpected current SHA as expected-old guard.
5. Verify `main = P`, tree `T`, and Register blob exact.
6. Restore ruleset `22392483` to its exact pre-episode active object and verify it.
7. Verify default branch `main`, record the failed episode and completed recovery, and stop.

### If case 3 unexpectedly deletes `main`

1. Stop and preserve raw evidence. Keep the recovery branch as the repository default and require it to remain exactly `P`.
2. Recreate `refs/heads/main` once at exact `P`. The current ruleset has no creation restriction.
3. If recreation is blocked, disable only ruleset `22392483`, recreate `main` once at `P`, verify it, then restore the exact active ruleset.
4. Change the default branch back to `main` once and verify default branch, `main = P`, tree `T`, Register blob, recovery branch `= P`, and exact active ruleset.
5. Record the failed episode and completed recovery, then stop.

### If state is ambiguous

Do not repeat the test invocation. Read current refs/settings first. Apply only the recovery branch above that matches observed effects. If exact restoration cannot be proved, leave the repository on the intact recovery branch, keep all evidence, mark intervention required, and escalate to the named human owner. No subsequent case or repository work may start.

The owner’s current admin permission and the preserved `P` recovery ref make content and authority restoration feasible. Recovery success does not turn the failed validation into PASS and does not resolve an RG gap.

## Stop conditions

Stop before or during execution on:

- live `main`, tree, Register, default branch, ruleset, bypass, permission, branch inventory, or current gate drift;
- a competing writer, credential, worktree, ref update, task, or authority claim;
- missing supervisor/custodian/recovery-owner availability;
- inability to create or read back the recovery branch at `P`;
- inability to demonstrate the required recovery commands and permissions before case 1;
- subject tree/parent/ancestry mismatch;
- any case success, ambiguity, wrong denial source, missing raw evidence, or main/configuration change;
- evidence destination collision, unsafe path, incomplete manifest, or custody failure;
- any need to retry, broaden scope, edit the ruleset outside conditional recovery, change content, or improvise restoration.

## Non-goals and non-authority limits

This gate and the later episode do not authorize:

- routine, parallel, multi-writer, automated, unattended, scheduled, or AFK operation;
- a standing bypass, emergency direct-main publication path, or general ruleset administration;
- content changes, Register transition, implementation, hooks, Actions, required checks, or checker invocation;
- PR review or merge, candidate acceptance, coordinator acceptance, or Workflow v1 adoption;
- deletion of recovery/test branches or local evidence;
- claims that RG1, RG2, RG3, RG4, or any other RG gap is resolved;
- treating a displayed protected flag, a generic GitHub rejection, default-branch deletion denial, or successful recovery as proof of the intended rules.

The later evidence is validation input only. A separate coordinator assessment and disposition must decide what it supports.

## Acceptance boundary and next gate

This gate authorizes framing only. The next task requires a fresh exact-base execution grant that repeats the three case invocations, actors, paths, evidence destination, recovery permissions, and zero-retry boundary without broadening them.

Next gate:

`Workflow v1 protected serialized write-path enforcement pilot negative enforcement validation execution`

## Explicit non-actions

No negative test, ref update, commit-object creation, branch creation/deletion, default-branch change, ruleset change, repository write, Research Register update, GitHub mutation, checker invocation, automation, recovery, RG disposition, or Workflow v1 adoption occurred in this gate.
