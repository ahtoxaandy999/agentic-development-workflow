---
id: ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-OPERATIONAL-USE-SCOPING-001
artifact: coordinator-operational-use-decision
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-decision
repository: ahtoxaandy999/agentic-development-workflow
subject_main: 5abf774919ecafb1c3a051206d603a7f9f1f516d
subject_tree: aa39393a665f892da7ea1f2905d1f41501980be6
subject_register_blob: 21bafdfeb1df1d7cfeb6789c1e5c560689217c21
pilot_disposition_ref: docs/design/ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-FINAL-DISPOSITION-001.md
pilot_disposition_blob: c1b1455df9b7dca4f6b5a7d30ba9c4cf176ab2df
ruleset_id: 22392483
ruleset_name: adw-protect-main-pilot
decided_on: 2026-09-07
decision: authorize-protected-serialized-write-path-as-default-for-separately-authorized-supervised-publications
normative_effect: none
supersedes: null
---

# Protected serialized write-path operational-use scoping

## Decision

`authorize-protected-serialized-write-path-as-default-for-separately-authorized-supervised-publications`

After exact protected persistence of this decision, use the validated GitHub branch-ruleset path as the default publication mechanism for every later, separately authorized supervised repository write in `ahtoxaandy999/agentic-development-workflow`.

This decision standardizes the publication mechanism. It does not itself authorize any repository change, implementation, routine write, parallel writer, automation, unattended execution, AFK execution or Workflow v1 adoption. Each substantive task remains separately authorized and bounded by its owning gate or accepted contract.

## Live basis

Connected GitHub read-only verification established:

- live `main`: `5abf774919ecafb1c3a051206d603a7f9f1f516d`;
- live tree: `aa39393a665f892da7ea1f2905d1f41501980be6`;
- ordered publication parents:
  1. `e5ebca200e0131868ce21367954e61498b0ba2a2`;
  2. `1f0b8d45289010847981c65bbe961f5941ca1143`;
- publication verification: `verified`, reason `valid`;
- PR `#5`: closed, merged and non-draft, with exact merge commit equal to live `main`;
- published Research Register: blob `21bafdfeb1df1d7cfeb6789c1e5c560689217c21`, 109492 bytes, SHA-256 `d1cd74780b91532244ca76c08b91113f0691632346b230b91cb0faf680987f4d`;
- both current mutable Register gates: `Workflow v1 supervised protected serialized write-path operational-use scoping gate`;
- branch response: `protected: true`; classic protection and required-status-check enforcement remain disabled;
- repository ruleset `22392483` / `adw-protect-main-pilot`: active, targets only `refs/heads/main`, has no bypass actors, reports `current_user_can_bypass: never`, and retains deletion, non-fast-forward and pull-request rules;
- allowed merge method: `merge`;
- required approving reviews and status checks: zero.

The final pilot disposition at blob `c1b1455df9b7dca4f6b5a7d30ba9c4cf176ab2df` accepts the exact pilot as a validated bounded enforcement basis. Positive protected publication and the three bounded negative cases passed. No competing current operational-use decision was found in the authoritative Register.

## Authorized operating pattern

For a later repository write to use this mechanism, all of the following must be true:

1. The substantive work is already authorized by its owning gate, accepted design contract or explicit user decision.
2. The task names the exact live base commit and allowed changed paths or another equally bounded write scope.
3. One identified executor is the sole writer for one candidate branch during the task.
4. The executor rereads live `main`, the Research Register and ruleset `22392483` immediately before the first write-producing step.
5. Candidate production occurs off `main` on one bounded branch.
6. The candidate is bound by full commit SHA, tree, parent topology, complete changed-path inventory and relevant artifact identities.
7. The branch is pushed non-force with explicit expected state and no silent retry or adaptation.
8. One draft pull request targets `main`; auto-merge and maintainer modification remain disabled unless a later explicit decision changes them.
9. A fresh independent reviewer reads the exact immutable candidate and controlling sources. The producer does not self-review or self-accept.
10. Any correction creates a new candidate identity; the reviewed candidate is not amended or rewritten.
11. Coordinator acceptance binds the exact reviewed candidate before publication.
12. Ready transition and merge remain explicit external mutation boundaries. Merge uses the exact accepted head SHA and method `merge`.
13. Post-merge readback binds the publication commit, ordered parents, resulting tree, complete delta, published identities, Register transition, PR state and unchanged ruleset.
14. Any drift, ambiguous mutation result, unexpected success or inability to establish exact identity fails closed.

The default initial shape is one candidate commit. A multi-commit candidate requires explicit task-level justification and must still bind the complete ordered candidate range and terminal head.

## Process compression

This decision removes redundant process without removing authority boundaries:

- A separately authorized substantive task may include candidate creation, one candidate-branch push and one draft PR in the same execution contract. It does not need an additional repository artifact whose sole purpose is to authorize those mechanical steps.
- Candidate review remains a fresh independent task but its local immutable review record does not have to be inserted into the already reviewed candidate. Doing so would change the candidate and create a recursive review loop.
- Coordinator acceptance may authorize the exact ready transition and merge contract in one decision. The user or controlling authority must still explicitly permit the external mutation when required by the execution environment.
- A failed transport or blocked local command remains an execution episode. It requires fresh recovery authority but does not require a repository record unless it materially affects repository state, accepted evidence or a current decision.
- Historical prompts, routine preflight logs and duplicated narrative are not repository state owners. Persist only durable decisions, accepted evidence required for rehydration and material exceptions.
- The Research Register remains the sole owner of the mutable current gate. Pull requests, branches, chats, runners and local records are subjects or evidence, not competing current-state trackers.

## Applicable work

The protected path becomes the default publication mechanism for:

- bounded documentation persistence;
- accepted design and disposition artifacts;
- separately authorized implementation or materialization changes;
- focused corrections to previously reviewed candidates;
- bounded Register transitions accompanying the same authorized outcome.

Using the mechanism does not supply missing semantic, implementation, review or adoption authority. The work must already be justified independently of the publication path.

## Denied modes

The following remain denied:

- direct agent push to `main`;
- force push or deletion of `main`;
- ruleset bypass or an undocumented emergency owner path;
- more than one active writer for the same candidate;
- parallel publication to `main` without a later explicit concurrency design;
- candidate mutation after independent review;
- producer self-review or self-acceptance;
- automatic ready transition, merge or branch deletion;
- Actions, hooks, bots, required checks or orchestration introduced by implication;
- unattended or AFK repository mutation;
- treating a branch, PR, green state or successful merge as semantic acceptance;
- changing ruleset `22392483` without a separate configuration decision and exact mutation authority.

## Minimum durable evidence

Each protected publication must make the following reconstructable from GitHub and the controlling records:

- authorized base SHA and tree;
- task authority and bounded changed-path scope;
- candidate branch, commit SHA, tree and parent topology;
- complete candidate delta and relevant bytes/blob/digest identities;
- independent-review subject SHA, verdict and material findings;
- coordinator acceptance bound to the exact candidate;
- ready and merge mutation counts, including any separately authorized recovery episode;
- publication commit, ordered parents, tree and verification state;
- final PR state and merge SHA;
- post-publication Register identity and current gate when the Register changes;
- ruleset identity and observed state at reliance points.

Evidence may remain local when it is transient execution detail and the repository contains the durable decision needed for rehydration. Evidence essential to a durable claim must have an explicit custodian and exact identity.

## Failure and recovery boundary

- A stale base, moved candidate ref, changed ruleset, unexpected path, dirty checkout, competing writer or conflicting current decision stops the task.
- A rejected push is not silently retried. A new recovery grant must specify the transport, exact existing commit and remaining allowed effects.
- An ambiguous ready or merge response is followed only by read-only state inspection. The mutation is not repeated without proof that it did not occur and fresh authority.
- An unexpected successful forbidden mutation triggers the task-specific recovery contract; no generic bypass or ruleset disablement is authorized here.
- Branch cleanup is not implicit. Retained candidate branches may be deleted only by a later bounded cleanup decision.

## RG and design-impact boundary

No RG item is declared globally resolved.

- RG1: the active ruleset supplies evidenced protection for the tested repository and state, but future drift and other credentials remain outside the proof.
- RG2: direct tested mutations to `main` are fenced, while candidate-branch writer exclusivity remains procedural.
- RG3: exact merge publication identity is required and was demonstrated, but no generalized automated verifier is selected.
- RG4: platform-enforced reviewer identity remains absent because the ruleset requires zero approvals; independent review remains procedural and evidence-bound.
- RG5 through RG12 remain unresolved and unchanged.

DI-1 remains preserved: GitHub branch, PR and merge states do not replace Workflow v1's orthogonal state planes.

DI-2 remains preserved: exact freshness, stale-authority denial, operation-aware retry, containment, recovery history and terminal guards are not weakened.

## Acceptance test for operational use

This decision is successful when a competent coordinator and executor can take a separately authorized repository change and derive the same protected publication sequence without inventing intent about:

- whether direct `main` writes are permitted;
- who owns the candidate branch;
- which exact identity is reviewed and accepted;
- when correction creates a new candidate;
- what evidence binds publication;
- whether ready/merge may run automatically;
- whether a failed mutation may be retried;
- whether successful publication implies semantic acceptance or Workflow v1 adoption.

## Intended Register transition

After separate exact protected persistence of this decision, the Research Register should:

- add the decision path, task ID, exact subject publication commit, ruleset ID and decision;
- set protected write-path operational-use status to `default-for-separately-authorized-supervised-publications`;
- preserve the final pilot disposition and all positive, negative, failed and recovery evidence already recorded;
- preserve RG1 through RG12 as unresolved and DI-1/DI-2 as unchanged;
- preserve Workflow v1 as non-normative, unadopted and unimplemented;
- preserve all prohibitions on routine, parallel, automated, unattended and AFK execution;
- update both current mutable `next_gate` values to `Workflow v1 supervised end-to-end workflow dry-run scoping gate`.

## Next gate

Immediate next gate:

`Workflow v1 protected serialized write-path operational-use decision persistence candidate production gate`

After exact protected publication of this decision:

`Workflow v1 supervised end-to-end workflow dry-run scoping gate`

## Explicit non-actions

This decision did not modify GitHub, the repository, Research Register, ruleset, branches, pull requests, permissions, checks or workflows. It did not authorize or execute a repository change, implementation, dry run, automation, parallel writer, unattended operation, AFK operation, RG resolution, Workflow v1 adoption or baseline establishment.
