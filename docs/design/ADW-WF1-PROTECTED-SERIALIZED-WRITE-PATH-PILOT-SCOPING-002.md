---
id: ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-SCOPING-002
artifact: enforcement-pilot-scoping
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-decision
decision: propose-protected-serialized-write-path-pilot
repository: ahtoxaandy999/agentic-development-workflow
gate_subject_main: c231ee8fcef48d32a30c9db54c57e860043b282c
gate_subject_tree: 9c993ec5370ceeff7f3efcd9b60be0d8807b71f9
research_register_ref: docs/research/research-register.md
research_register_blob: 76c9d4992c012f3a9f1fc76e34616e5232fdfbeb
repository_visibility_observed: public
supersedes: ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-SCOPING-001-local-unpersisted
decided_on: 2026-09-06
normative_effect: none
---

# ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-SCOPING-002

Task: `ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-SCOPING-002`.
Mode: read-only coordinator enforcement-pilot scoping.
Repository: `ahtoxaandy999/agentic-development-workflow`.

## Result

Decision: `propose-protected-serialized-write-path-pilot`.

The repository's transition from private to public removes the capability gap that controlled the local, unpersisted `ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-SCOPING-001` result. A repository-level GitHub branch ruleset is now available for this repository and can be scoped as a bounded enforcement pilot. No ruleset or classic branch protection is currently configured.

This decision authorizes only later persistence of this scoping record and later consideration of an exact, separately authorized configuration task. It does not configure protection, authorize a repository write, resolve RG1-RG4, establish operational readiness, or adopt Workflow v1.

Proposed next gate after exact persistence of this record:

`Workflow v1 protected serialized write-path enforcement pilot configuration authorization gate`

## Exact live basis

Connected `@GitHub` was used read-only for the repository-dependent claims in this decision.

At the point of reliance:

- live default branch: `main`;
- live `main`: `c231ee8fcef48d32a30c9db54c57e860043b282c`;
- live main tree: `9c993ec5370ceeff7f3efcd9b60be0d8807b71f9`;
- Research Register blob: `76c9d4992c012f3a9f1fc76e34616e5232fdfbeb`;
- repository visibility: `public`;
- connected-user repository permissions: admin, maintain, push, triage, and pull available;
- branch `protected`: `false`;
- classic branch protection: disabled;
- required status-check enforcement: off;
- repository-level rulesets: available and empty;
- branches: only `main`;
- open pull requests: none;
- workflow directory: absent;
- workflow runs for the live commit: none;
- combined commit statuses for the live commit: none.

Both mutable current-gate owners in the Research Register are exactly:

`Workflow v1 protected serialized write-path enforcement pilot scoping gate`

No competing current enforcement pilot decision was found in the inspected authoritative repository state. The Register's existing private-repository branch-protection capability wording is stale after the separately authorized visibility change. It must be corrected only through an explicit bounded Register transition; it is not silently treated as current evidence here.

## Prerequisite assessment

| Prerequisite | Result | Basis |
| --- | --- | --- |
| Exact live main and Register | PASS | Exact identities above matched the expected gate basis. |
| Current gate | PASS | Both mutable owners match the scoping gate. |
| Public-repository ruleset capability | PASS | Ruleset read surface is available; the current collection is empty. |
| Administrative configuration capability | PASS | Connected user has repository administration permission. |
| Existing-protection conflict | PASS | No classic protection or ruleset is configured. |
| Existing branch/PR/workflow conflict | PASS | Only `main`; no open PR or workflow/status dependency. |
| Accepted design compatibility | PASS | A supervised serialized PR path can preserve accepted Workflow v1 boundaries. |
| Competing current decision | PASS | None found in current owners or live repository collections. |
| Configuration authority | NOT GRANTED | Requires a later exact, explicit configuration authorization. |

## Selected enforcement mechanism

Select one repository-level GitHub branch ruleset for the pilot. Do not combine it with classic branch protection.

Proposed identity and target:

- name: `adw-protect-main-pilot`;
- target: branch;
- enforcement: active;
- include: `refs/heads/main`;
- exclude: none;
- standing bypass actors: none.

Proposed rules:

1. Require changes to `main` to enter through a pull request.
2. Required approving reviews: `0` for this pilot. Independent review remains a separate Workflow v1 evidence obligation bound to the exact candidate SHA; this pilot does not falsely claim GitHub-enforced reviewer independence.
3. Block force pushes through the non-fast-forward rule.
4. Restrict deletion of `main`.

Do not configure:

- required status checks, because no qualifying check currently exists;
- GitHub Actions or any workflow;
- hooks, checker integration, auto-review, deployment gates, code-scanning gates, or unattended automation;
- signed-commit, linear-history, file-path, file-size, creation, or generic update restrictions unless a later separately authorized decision supplies evidence and intent;
- any standing administrator, integration, application, team, role, or user bypass.

The pull-request rule is the direct-write denial mechanism for normal operation. The repository owner retains administrative ability to edit or disable the ruleset, but that capability is not a standing publication bypass. Any emergency use requires a separate explicit authorization, a stated reason, exact before/after configuration evidence, and immediate readback.

## Pilot branch and pull-request lifecycle

The later pilot must use one natural, independently authorized repository change. It must not manufacture a repository write merely to exercise the reference or the ruleset.

For that one pilot:

1. A later selection gate identifies one exact natural task and immutable base `B`.
2. A separately authorized executor creates one bounded candidate branch named for the selected task.
3. One serialized writer owns that branch for the complete candidate episode. Parallel, background, automated, and AFK writers remain denied.
4. The executor produces candidate `C`, verifies its exact tree and allowed path delta, then stops.
5. A fresh independent reviewer binds the review to exact full candidate SHA `C`. Branch name, PR number, checks, or a moving head are insufficient identity.
6. A coordinator disposition decides whether that exact `C` may proceed to publication. Neither the producer nor reviewer self-accepts it.
7. Before merge, the publication actor rereads live `main`, the PR base, and the PR head. If the base or head differs from the accepted identities, publication stops; no automatic update, rebase, replay, or adaptation is allowed.
8. Publication uses the GitHub pull-request merge path. The pilot should use a merge commit so reviewed candidate `C` remains directly represented in the published ancestry. Squash or rebase merge is outside this pilot.
9. Record integration subject `I`, publication commit `Ppub`, its ordered parents, resulting tree, exact changed paths, and post-publication live-main readback.
10. Delete the candidate branch only after accepted publication evidence and only through a separately authorized cleanup step. Deletion of `main` remains denied.

The candidate branch itself is not technically fenced by the main-targeted ruleset. Its one-writer constraint remains procedural in this pilot and RG2 remains unresolved.

## Actor and state ownership

- Research Register: current repository gate and current pilot-decision pointer until an explicit owner migration.
- Command Center coordinator: task selection, gate decisions, exact authority grants, disposition, and stop/continue decisions.
- Human repository owner: supervision, serialization confirmation, emergency configuration authority, evidence custody, and escalation ownership.
- Configuration executor: exactly one bounded ruleset configuration attempt when separately authorized; no policy discretion.
- Candidate executor: one bounded branch writer for the selected natural task; no review or acceptance authority.
- Independent reviewer: review evidence bound to exact candidate SHA; no candidate mutation or coordinator acceptance authority.
- Publication executor: exact authorized PR merge and readback only; no candidate revision or authority adaptation.
- GitHub: enforcement surface and derived live view, not owner of Workflow v1 semantic state or coordinator disposition.

No Issue, PR, branch, chat, runner, local clone, or ruleset may become a competing owner of the Research Register's current gate or coordinator decisions.

## RG1-RG4 boundary

### RG1 — effective protection

The mechanism is now available, but RG1 remains unresolved until an authorized configuration exists, exact live readback proves it applies to `main`, and authorized negative tests demonstrate that direct push, force update, and branch deletion are denied. A displayed `protected` flag alone is insufficient.

### RG2 — writer fencing

The pilot requires one declared writer and serialized task authority, but the selected ruleset does not technically fence the candidate branch. Competing writers, stale grants, revocation, and branch-owner identity remain external controls. The pilot must not claim RG2 resolved.

### RG3 — exact integration publication

The design requires explicit `B`, working candidate, verified candidate, reviewed candidate `C`, integration subject `I`, and final publication `Ppub` identities. Moved base/head, wrong parent, tree drift, or path drift fail closed. The pilot tests this mapping but does not resolve RG3 in general.

### RG4 — reviewer identity

The ruleset intentionally requires zero GitHub approvals. Independent review remains a separate exact-SHA artifact and procedural conflict check. Platform-enforced reviewer identity, stale approval dismissal, last-pusher separation, and bypass resistance remain unresolved.

RG1-RG4 therefore remain explicit validation subjects, not satisfied prerequisites or accepted outcomes.

## Failure, containment, and recovery

- If live `main`, visibility, permissions, current Register, or ruleset collection changes before configuration, stop and return to the coordinator.
- If the configuration request fails or its outcome is ambiguous, do not retry. Read back rulesets and branch state, preserve the execution episode, and escalate.
- If the resulting configuration differs from the authorized object, treat the pilot as failed and do not begin candidate work.
- If direct push, force update, or deletion unexpectedly succeeds, stop all publication activity, preserve exact evidence, and escalate. Do not repair by improvisation.
- If the intended PR path is unusable, do not weaken the rule automatically.
- Emergency recovery, if required, is a separately authorized owner action to disable or correct the ruleset. It requires exact before/after evidence and does not authorize a direct-main content write.
- After recovery, no work resumes until the coordinator issues a new exact authority grant.

A temporary recovery path is necessary because a first enforcement configuration can accidentally deny the intended supervised merge path. The recovery path is administrative ruleset disablement or correction by the human repository owner, not a standing actor bypass and not an emergency direct-main push path.

## Observable acceptance tests

Configuration acceptance requires all of the following read-only observations:

1. The exact ruleset exists once, targets only `refs/heads/main`, and is active.
2. It contains exactly the authorized pull-request, non-fast-forward, and deletion rules.
3. It contains no bypass actor and no required status check.
4. `main` is reported as covered by effective rules.
5. Repository visibility, default branch, and unrelated repository settings remain unchanged.

Enforcement validation requires separately authorized, bounded attempts:

6. A normal direct update to `main` is rejected without changing live `main`.
7. A non-fast-forward update to `main` is rejected without changing live `main`.
8. Deletion of `main` is rejected.
9. One natural candidate can be proposed through a PR without a nonexistent status check.
10. Review binds exact candidate `C`; after the review, any head movement invalidates the review and blocks merge.
11. The authorized merge publishes the expected `Ppub` with the expected relation to `B` and `C`.
12. Post-publication readback reproduces live ref, commit, tree, path delta, and required evidence identities.

Negative tests 6-8 and positive test 9-12 require their own explicit execution authorities. This scoping decision does not authorize them.

## Implementation non-goals

The pilot does not authorize or select:

- GitHub Actions, hooks, apps, MCPs, skills, bots, auto-review, or orchestration;
- a mandatory status check that does not exist;
- routine, parallel, automated, unattended, or AFK execution;
- broad branch policy beyond `main`;
- technical candidate-branch writer fencing;
- general reviewer-identity enforcement;
- production repository migration or product-project dogfooding;
- schema, validator, tracker, Issue workflow, or task database creation;
- Workflow v1 normative adoption;
- resolution of RG1-RG12 or modification of DI-1/DI-2;
- permission, visibility, merge-strategy, or repository-setting changes other than the exact future ruleset configuration.

## Later authority required

Before any GitHub configuration, a separate coordinator configuration-authorization gate must bind:

- the then-live exact `main` and Research Register;
- exact repository visibility and connected-user administrative permission;
- absence of a competing ruleset/protection decision;
- the complete proposed ruleset request object;
- named configuration executor, human supervisor, evidence custodian, and escalation owner;
- exactly one configuration attempt and no retry;
- permitted mutation limited to creation of the one ruleset;
- readback method and expected effective rules;
- rollback authority boundary;
- stop conditions and explicit non-goals.

Persistence of this record must happen before that gate and is itself a separate exact-base repository write.

## Intended minimal Research Register transition

Later exact persistence of this record should:

- add a durable pointer to `docs/design/ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-SCOPING-002.md`;
- add task ID `ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-PILOT-SCOPING-002`;
- add decision `propose-protected-serialized-write-path-pilot`;
- record `github-repository-branch-ruleset` as the selected pilot mechanism;
- update the mutable branch-protection capability observation from the stale private-repository value to a public-repository, available-but-not-configured value without claiming protection is active;
- preserve accepted Workflow v1 design, DR-005 disposition, all RG/DI boundaries, and all current execution restrictions;
- set both current `next_gate` owners to `Workflow v1 protected serialized write-path enforcement pilot configuration authorization gate`.

No ruleset implementation, validation result, protection claim, operational authority, or RG resolution may be added by the persistence task.

## Stop boundary and explicit non-actions

This task stops after the local coordinator record.

It did not modify GitHub, the repository, Research Register, branch protection, rulesets, permissions, branches, pull requests, checks, workflows, or candidate files. It did not create a commit or push. It did not configure or validate the pilot, create a test write, select a natural candidate, authorize routine publication, resolve RG1-RG4, or adopt Workflow v1.
