---
id: ADW-D13-BOUNDED-POC-PET-PROFILE-AMENDMENT-001
artifact: coordinator-pilot-profile-amendment
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-decision
repository: ahtoxaandy999/agentic-development-workflow
subject_main: 1256727d511ac973fae4501ce2c4181dda0fee9d
subject_tree: f12ceebde7601ccd729e594390c0949bb05b8705
subject_register_blob: e369b20500d6f762d96dbf7943f6001d5216f0f2
amends: docs/design/ADW-D13-BOUNDED-POC-AUTHORIZATION-001.md
amends_blob: 72fd838f807d565517ce4668700f2e2a02fed8a3
amended_scope: current-selected-profile-only
scoping_ref: docs/design/ADW-D13-CONFORMANCE-EVIDENCE-ACQUISITION-SCOPING-001.md
scoping_blob: 25615d21d28ef74bf0a6fede1bf9cc1609a54319
prior_selected_profile_repository: ahtoxaandy999/housing-recovery
prior_observed_profile_main: 01b3ae5288069660a12c6b35254e4fa59867429e
selected_profile_repository: ahtoxaandy999/pet-project
observed_profile_main: 28f84fe4324925adae0f17163d578ed2e1f9bc19
observed_profile_tree: 34a4b5ce54a1608d37305a8a4fecc4c29ce83689
decided_on: 2026-09-23
decision_basis: user profile-selection correction; the intended bounded test run is in Pet Project
decision: correct-d13-bounded-poc-selected-profile-from-housing-to-pet-project
d13_status: CONDITIONALLY SELECT FOR ONE BOUNDED POC
d5_status: CONFIRM DEFER
x3_status: CONFIRM REJECT
selected_mechanism_changed: false
implementation_preflight_authorized: true
pilot_execution_authorized: false
pet_project_mutation_authorized: false
credential_creation_authorized: false
conformance_result: not-established
normative_effect: none
supersedes: null
---

# D13 bounded PoC profile amendment: Pet Project

## Decision

`correct-d13-bounded-poc-selected-profile-from-housing-to-pet-project`

Correct the selected repository profile of the one bounded D13 proof of concept
from:

`ahtoxaandy999/housing-recovery`

to:

`ahtoxaandy999/pet-project`

This is a profile-selection correction only. The intended bounded test run is in
Pet Project, not Housing.

This record:

- supersedes only the **current profile-selection portion** of
  [ADW-D13-BOUNDED-POC-AUTHORIZATION-001](ADW-D13-BOUNDED-POC-AUTHORIZATION-001.md)
  for the one bounded PoC;
- leaves the already accepted runtime, generation fence, commit primitive,
  credential-separation architecture, evidence/recovery surface and every
  authorization boundary of that record unchanged;
- is not a new D13 mechanism selection;
- does not execute the PoC, mutate Pet Project, create credentials, reopen D5,
  change X3 or establish D13 conformance.

## Historical integrity

Housing was the previously accepted profile. It was selected by
[ADW-D13-CONFORMANCE-EVIDENCE-ACQUISITION-SCOPING-001](ADW-D13-CONFORMANCE-EVIDENCE-ACQUISITION-SCOPING-001.md)
and bound by
[ADW-D13-BOUNDED-POC-AUTHORIZATION-001](ADW-D13-BOUNDED-POC-AUTHORIZATION-001.md)
at observed Housing `main` `01b3ae5288069660a12c6b35254e4fa59867429e`.

Those records are not rewritten. Their review, acceptance and merge evidence
remains historical evidence of what was decided at their subjects. Their
Housing-specific statements, including `housing_mutation_authorized: false`,
remain historical statements and do not carry forward as current profile
authority.

This amendment does not claim Housing was technically invalid. Housing remains a
plausible control-loop pilot profile; it is simply not the profile the bounded
test run is intended to exercise.

## Exact amendment basis

At amendment time:

| Item | Identity |
| --- | --- |
| ADW `main` | `1256727d511ac973fae4501ce2c4181dda0fee9d` |
| ADW tree | `f12ceebde7601ccd729e594390c0949bb05b8705` |
| ADW Research Register blob | `e369b20500d6f762d96dbf7943f6001d5216f0f2` |
| Amended authorization blob | `72fd838f807d565517ce4668700f2e2a02fed8a3` |
| Scoping record blob | `25615d21d28ef74bf0a6fede1bf9cc1609a54319` |
| Pet `main` | `28f84fe4324925adae0f17163d578ed2e1f9bc19` |
| Pet tree | `34a4b5ce54a1608d37305a8a4fecc4c29ce83689` |

Pet observations, read live on 2026-09-23 through the GitHub API:

- repository visibility: private; default branch `main`;
- `pilot/d13-runtime-control-evidence-001`: absent (branch read returned 404;
  no branch name containing `d13` exists);
- pull requests using that branch, any state: none;
- open pull requests: exactly one, draft PR #99
  `docs/exp-003-termination-without-result-001`, head
  `9e599e3ae65dc0dfa9ba4a5d20be9d98e3ce7df6`, unrelated to this PoC;
- active workflows: exactly one, `Exact candidate verification`
  (`.github/workflows/exact-candidate-verification.yml`, workflow id
  `362615264`);
- branch listing reports `main` as `protected: false`;
- classic branch-protection, repository-ruleset and branch-rules reads returned
  a plan-related 403 (`Upgrade to GitHub Pro or make this repository public`).

The 403 is an evidence gap, not proof that GitHub lacks a capability. As with the
prior profile, this pilot may not rely on branch protection or a ruleset as
writer fencing or as a `main` guard.

Pet blobs inspected at the observed `main`:

| Path | Blob |
| --- | --- |
| `AGENTS.md` | `6c5b07ec5e7b6fb36062be3a772d282cba3d238a` |
| `.agents/repository-map.md` | `56654a9532b72904b8001945263801ba144b2da3` |
| `docs/development/current-work.md` | `210c35f40cdffd93605941c68e0d56c545f7c201` |
| `docs/development/codex-workflow.md` | `67928196e7c48f680457082462ab0fd2b7578946` |
| `.github/workflows/exact-candidate-verification.yml` | `f1f69cf51feae8d11df4ac63d54cf7d770511955` |
| `scripts/run-task-checks.sh` | `260bcab75f1fea796a0456b56ae48d8ba4d570e4` |
| `scripts/chat-conveyor-transport.py` | `d48c14197ec82412574aa22c18b0bd794f26df84` |
| `scripts/test-chat-conveyor-transport.py` | `95d42134d3ef8c550e04ac2309f9af56459ec7f3` |
| `.agents/skills/chat-conveyor-transport/SKILL.md` | `0f6825e21b87db284069b27f64de16871eb54c3b` |
| `docs/reviews/PP-WF-CONVEYOR-001-closure.md` | `dcf172529ce24c0468fd0bcf12eae171c3be3cb6` |
| `docs/development/exp-003-execution-routing-plan.md` | `35700cb39dcd7f4523df2916b24ef5fc9db2bf03` |

These are observations for this amendment candidate only. The later
implementation/preflight gate and any execution gate must re-read live Pet state.

## Why Pet is the current profile

Pet is now the selected profile because:

- it is the intended real conveyor test target;
- it already owns the accepted Supervised Conveyor routing profile;
- it already owns repository-owned Chat conveyor operation/journal controls;
- it already has exact-SHA verification of every non-`main` push;
- the future D13 run can exercise the control contract against the repository
  where the conveyor mechanics already exist.

### Reusable prior evidence in Pet

Pet already contains bounded evidence surfaces relevant to this PoC:

1. **Exact non-`main` candidate SHA verification on every push.**
   `exact-candidate-verification.yml` runs on `push` to every branch except
   `main`, checks out `${{ github.sha }}` with `persist-credentials: false`, and
   asserts `git rev-parse HEAD` equals `GITHUB_SHA`.
2. **Repository-owned deterministic candidate verification.** The workflow
   delegates semantics to `scripts/run-task-checks.sh --verification-id
   GITHUB-ACTIONS-EXACT-CANDIDATE-<sha> --candidate-sha <sha>` rather than
   owning test semantics in YAML.
3. **Immutable candidate evidence artifact production.** It uploads
   `candidate-verification-${{ github.sha }}` (candidate JSON and log) with
   `retention-days: 90` and publishes the artifact digest in the job summary.
   A prior observed push run (`35508252700`, head
   `1cb6e3100c6f54ef01bc8bf23534317c2391c8df`, conclusion `success`) shows the
   workflow producing that evidence on a non-`main` branch.
4. **Accepted Supervised Conveyor routing.**
   `docs/reviews/PP-WF-CONVEYOR-001-closure.md` records Product acceptance of
   the Supervised Conveyor profile (accepted candidate
   `a041d1d4657d2ed514e0c41a287e3c187349445f`), described in
   `docs/development/codex-workflow.md` as a composition of existing owners,
   not a state machine, daemon, controller or unattended executor.
5. **Repository-owned Chat conveyor transport.**
   `scripts/chat-conveyor-transport.py` and its Skill provide operation
   identity (`operation_id` bound to the step ID), a durable run journal with
   readback, no-blind-resend guarding (`guard_no_blind_resend` blocks any new
   step while an unresolved post-send operation exists), and a fresh-reviewer
   procedure (a corrected candidate always receives a fresh reviewer
   conversation). `docs/development/exp-003-execution-routing-plan.md` §6
   records a local `CHAT-CONVEYOR-PILOT-001` roundtrip; that plan is itself a
   proposed, non-adopted Pet document and is cited here as evidence only.

These are reusable prior evidence only. They do not establish D13 conformance,
do not satisfy any mandatory D13 scenario, and do not become the selected D13
runtime by implication.

## Selected mechanism remains unchanged

The mechanism accepted by ADW-D13-BOUNDED-POC-AUTHORIZATION-001 is preserved
exactly:

- supervised task-local deterministic Python runtime;
- exactly one credential-bearing publisher process per pilot evidence root;
- canonical `publisher.lock` outside all repository worktrees;
- Python stdlib `fcntl.flock(..., LOCK_EX | LOCK_NB)` lifetime lock;
- canonical generation record beside that lock;
- prior-publisher cessation before generation advancement;
- GitHub GraphQL `createCommitOnBranch`;
- required `expectedHeadOid` provider-side exact-head CAS;
- local append-only evidence/recovery state outside the governed repositories;
- a separate future publisher credential;
- an isolated read-only reviewer credential.

Every requirement of that record for generation activation, stale
credential-holding publisher exclusion, provider head fencing, recovery and
replacement, local evidence contents, implementation/preflight deliverables and
the execution authorization boundary applies unchanged, with the target
repository read as `ahtoxaandy999/pet-project`.

This mechanism is not replaced by, and does not delegate its control authority
to:

- Pet `scripts/chat-conveyor-transport.py`;
- `gh-aw`;
- GitHub Actions orchestration;
- Codex App Server or SDK;
- Codex GitHub Action;
- Claude Code Action;
- Symphony;
- another daemon or controller.

Pet's existing conveyor implementation and exact-candidate workflow are evidence
and inputs only. The existing Pet workflow is an observed indirect effect of the
pilot's branch updates; it is not the D13 runtime, publisher or recorder.

## Pet-specific effect model

The scoping semantics (roles, runtime subject manifest, writer-generation
contract, stable operation identity, effect receipt, reconciliation, mandatory
scenario matrix, supplemental F1/F2 scenarios, fault-injection boundary,
reviewer isolation evidence, evidence package, attempt/retry ceiling, stop
conditions and pilot acceptance bar) apply to Pet with the following
profile-specific effect model. Where the scoping record names Housing, its
`pull_request`-triggered Candidate verification workflow or Merge closeout
verification, read this section instead.

### Effect domain

The future pilot effect domain is limited to:

- dedicated branch: `pilot/d13-runtime-control-evidence-001`;
- one draft pull request targeting `main`;
- inert marker path on that branch:
  `docs/research/d13-runtime-control-evidence-pilot-marker.md`;
- indirect `Exact candidate verification` GitHub Actions runs, their job
  summaries and their `candidate-verification-<sha>` artifacts, caused by pushes
  to the dedicated branch.

The pilot may create successive immutable commits changing only that marker
path.

### Marker

The marker must state explicitly that it is non-authoritative pilot evidence
scaffolding. It is not Product state, a contract, a decision, policy, a task
tracker, a research note or repository authority, and it must never be merged.
Its placement under Pet `docs/research/` does not make it Pet research evidence.

### Forbidden Pet effects

The pilot may not:

- write `main` directly, merge, force-push or mark the draft PR ready;
- modify `docs/development/current-work.md`;
- modify Product contracts, decisions or architecture records;
- modify game code (`packages/game-core/`), simulation tooling or Playtest code
  (`tools/playtest/`);
- modify the existing conveyor transport, its tests or its Skill;
- modify existing workflows, verifier scripts or `scripts/run-task-checks.sh`;
- change rulesets, protection, Actions settings or secrets;
- touch PR #99 or any other non-pilot branch or PR;
- delete branches, PRs, runs or artifacts;
- use production or user data, or persist secrets.

Cleanup is not part of the pilot.

Because Pet `main` is reported unprotected and protection/ruleset state is not
readable on the current plan, no platform control is evidenced to deny a `main`
write by a credential holding repository contents write. The publisher's exact
ref/path allowlist and the minimal effective permission of the future publisher
credential are therefore load-bearing. The implementation/preflight candidate
must state this gap explicitly, and the later execution authorization must
decide whether the residual risk is acceptable. This amendment neither accepts
nor resolves it.

### Known indirect effect: push-triggered exact-candidate verification

Pet `Exact candidate verification` runs on `push` to non-`main` branches, not on
`pull_request` events. Therefore every future pilot ref update to the dedicated
branch can create an indirect external effect: one `Exact candidate
verification` run for that pushed SHA, including a job summary and a
`candidate-verification-<sha>` artifact retained for 90 days.

The workflow declares `permissions: contents: read` and performs no repository
write. Its effect is the run, summary and artifact, not a repository mutation.

This differs from the previous Housing profile:

- the run may begin before any draft PR exists;
- branch creation, if it produces a push event, can itself trigger a run against
  the branch's initial SHA;
- each `createCommitOnBranch` commit on the dedicated branch can trigger a run
  against the new head SHA;
- draft PR creation is not the trigger owner for this workflow and is not
  expected to trigger it;
- no merge-closeout workflow exists in Pet and none is required, because merge
  remains forbidden.

Whether a provider mutation made with the future publisher credential actually
produces a workflow-triggering push event is a live fact the implementation/
preflight candidate must list for readback and the execution run must observe.
It is not assumed either way.

Consequently:

- the push-triggered run identity (run ID, workflow ID, `head_sha`, `event`,
  `status`, `conclusion`), its artifact name and artifact digest belong in the
  publisher receipt's indirect-effect fields and in the residual/queued-effect
  inventory;
- queued, in-progress, completed and cancelled workflow states must each be
  observed and recorded, not inferred;
- a successful branch update is not fully reconciled while its triggered
  candidate-verification effect remains unaccounted for, including when an
  expected run is absent or not yet observed;
- any workflow run, event or artifact other than the expected push-triggered
  `Exact candidate verification` effect for a pilot-branch SHA is a stop-and-
  reconcile condition;
- a green candidate-verification run is machine evidence only; under S8 it
  cannot advance review, disposition, Product/coordinator acceptance, merge
  authority or terminal task state.

Scenario mapping follows directly: S1 binds the push-triggered run and artifact
for the exact pilot candidate SHA; S6 and the corresponding fault-injection case
use a queued or in-progress push-triggered `Exact candidate verification` run
remaining after the primary branch mutation.

## Open PR #99 isolation

PR #99 (`docs/exp-003-termination-without-result-001`, draft) is unrelated
existing Pet repository state. It is not part of this PoC.

The future pilot must:

- not modify its branch;
- not use its candidate SHA as a pilot base, head or subject;
- not close, update, comment on, ready or merge it;
- not infer repository-wide writer exclusivity, or its absence, from its
  existence;
- operate only within the dedicated D13 branch/effect domain.

Its presence is not itself a blocker, because the D13 publisher effect domain is
branch-scoped and `main` mutation and merge remain forbidden. Its own
push-triggered workflow runs are outside the pilot effect inventory and must not
be attributed to pilot operations.

If any other actor begins writing the exact D13 pilot branch, or the branch
exists unexpectedly before authorized setup, the pilot stops.

## Credential boundary for Pet

The credential architecture of the amended authorization applies with the target
repository read as Pet:

- the future publisher credential must be limited to
  `ahtoxaandy999/pet-project` and to the permissions strictly required for the
  dedicated pilot branch, draft PR setup/observation and Actions readback;
- the future reviewer credential must be effectively read-only for Pet
  repository state and pilot evidence; because Pet is private, it must hold
  repository read access without contents write, PR mutation, ready/merge,
  ruleset/protection mutation or secret access.

Existing broad local GitHub authentication is not the selected publisher or
reviewer credential. No credential is created, selected or reconfigured by this
amendment.

## D13 / D5 / X3 state

- `d13_status`: `CONDITIONALLY SELECT FOR ONE BOUNDED POC` — unchanged, now for
  the same exact mechanism with the Pet profile;
- `d5_status`: `CONFIRM DEFER` — unchanged;
- `x3_status`: `CONFIRM REJECT` — unchanged;
- `d13_conformance_result`: `not-established` — unchanged.

## Authority state

- `implementation_preflight_authorized: true`
- `pilot_execution_authorized: false`
- `pet_project_mutation_authorized: false`
- `credential_creation_authorized: false`

The implementation/preflight candidate is local-only. It may use read-only live
Pet inspection. It authorizes no Pet branch creation, commit, draft PR, GraphQL
mutation, workflow trigger, credential or token creation, secret configuration,
reviewer mutation test, fault injection against GitHub, unattended execution,
automatic retry, merge or cleanup.

A later exact execution authorization remains mandatory before the first Pet
effect. It must bind exact live Pet base and tree, and every item already listed
by the amended authorization's execution-authorization boundary.

## Intended Register transition

After exact candidate review, coordinator/human acceptance and protected
publication of this amendment, the Research Register should:

- add this amendment artifact, task and decision;
- record the prior selected profile `ahtoxaandy999/housing-recovery` as
  historical;
- record the current selected profile `ahtoxaandy999/pet-project` with observed
  Pet `main` `28f84fe4324925adae0f17163d578ed2e1f9bc19`;
- retain the selected runtime, generation fence and commit primitive unchanged;
- retain `implementation_preflight_authorized: true`,
  `pilot_execution_authorized: false` and `credential_creation_authorized: false`;
- replace the current Housing mutation flag with
  `pet_project_mutation_authorized: false`;
- preserve `d13_conformance_result: not-established`, D13/D5/X3 and the
  repository-wide current gate;
- keep the D13-specific next gate unchanged.

## Next gate

**D13 bounded PoC implementation/preflight candidate production gate**

unchanged, now targeting Pet Project. That gate is local-only and read-only with
respect to Pet. It does not advance to execution authorization.

## Explicit non-actions

This amendment does not:

- mutate Pet Project or Housing;
- create a branch, commit, PR or marker;
- touch PR #99;
- create, select or reconfigure credentials;
- execute GraphQL mutations or trigger workflows;
- change the selected runtime, generation fence or commit primitive;
- select Pet's conveyor transport, Actions, `gh-aw`, App Server, Symphony or any
  other mechanism;
- run the PoC or begin implementation/preflight;
- establish D13 conformance;
- reopen D5 or change X3;
- amend Workflow v1 or accept a repository baseline;
- change the repository-wide current gate;
- authorize unattended/AFK operation.
