---
id: ADW-D13-PET-EXECUTION-PREREQUISITE-DISPOSITION-001
artifact: coordinator-execution-prerequisite-disposition
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-decision
repository: ahtoxaandy999/agentic-development-workflow
subject_main: d1f30a3c362459fe3a59cbba725a77be3f571f97
subject_tree: d76f1258150c4bb64295927ea44bad030c7cd6f2
subject_register_blob: 45357fa9259584ab7bd40cb7d1872e254fb04672
authorization_ref: docs/design/ADW-D13-BOUNDED-POC-AUTHORIZATION-001.md
authorization_blob: 72fd838f807d565517ce4668700f2e2a02fed8a3
profile_amendment_ref: docs/design/ADW-D13-BOUNDED-POC-PET-PROFILE-AMENDMENT-001.md
profile_amendment_blob: e4860562ff7764d548e17814de5eddaa494ddb3b
scoping_ref: docs/design/ADW-D13-CONFORMANCE-EVIDENCE-ACQUISITION-SCOPING-001.md
scoping_blob: 25615d21d28ef74bf0a6fede1bf9cc1609a54319
selected_profile_repository: ahtoxaandy999/pet-project
observed_profile_main: 28f84fe4324925adae0f17163d578ed2e1f9bc19
observed_profile_tree: 34a4b5ce54a1608d37305a8a4fecc4c29ce83689
preflight_candidate_root: /Users/antony/Work/Projects/adw-d13-poc-preflight-003
preflight_candidate_identity: e06eee1bbb0083adc35a965c8768f1516d97bae1d017908dffe1c0e05d7b32e8
preflight_subject_sha256: 7ca638b99e7d3025347f0969d9decbda5aaed2a596ccf37f468d30bb7e3c0ff7
preflight_report_sha256: ac80f130eb8ed7d6c6f9df332afd1160a6cf1213a355f3292023be7f3bfaefbe
preflight_review_result: PASS
preflight_review_findings: 0-blocker-0-major-2-minor-4-note
decided_on: 2026-09-25
decision_basis: user/coordinator decisions persisted by task ADW-D13-PET-EXECUTION-PREREQUISITE-DISPOSITION-001
decision: accept-preflight-003-as-execution-preparation-input-accept-one-poc-main-write-residual-risk-and-select-two-separate-fine-grained-pat-credential-products
d13_status: CONDITIONALLY SELECT FOR ONE BOUNDED POC
d5_status: CONFIRM DEFER
x3_status: CONFIRM REJECT
selected_mechanism_changed: false
main_write_residual_risk_disposition: accepted-for-one-bounded-pet-poc-only
main_write_residual_risk_eliminated: false
publisher_credential_product: github-fine-grained-personal-access-token
reviewer_live_reader_credential_product: github-fine-grained-personal-access-token
credential_separation: two-separate-credentials
live_provider_reader_required_before_execution: true
credential_creation_authorized: false
pet_project_mutation_authorized: false
pilot_execution_authorized: false
conformance_result: not-established
normative_effect: none
supersedes: null
---

# D13 Pet execution-prerequisite disposition

## Decision

`accept-preflight-003-as-execution-preparation-input-accept-one-poc-main-write-residual-risk-and-select-two-separate-fine-grained-pat-credential-products`

This record persists decisions already made by the user/coordinator before any
D13 Pet credential creation or execution authorization. It records exactly:

1. acceptance of the exact reviewed preflight-003 package as the
   implementation/preflight input for subsequent D13 execution-preparation
   decisions;
2. a narrowly scoped acceptance of the known `main`-write residual risk for the
   one bounded D13 Pet PoC;
3. selection of GitHub fine-grained personal access tokens as the credential
   product, as two separate credentials with separate roles;
4. the requirement for a separately reviewed live provider reader before
   execution authorization can become effective;
5. the preflight review MINOR-2 editorial discrepancy as historical evidence.

This record is a prerequisite disposition only. It does not:

- create, store or configure any credential or token;
- authorize credential creation;
- mutate Pet Project, create the pilot branch, marker or draft PR;
- execute GraphQL mutations or trigger workflows;
- run the PoC or authorize pilot execution;
- implement or review the live provider reader;
- select any mechanism beyond the credential product and role separation stated
  here;
- establish D13 conformance.

It does not rewrite
[ADW-D13-BOUNDED-POC-AUTHORIZATION-001](ADW-D13-BOUNDED-POC-AUTHORIZATION-001.md),
[ADW-D13-BOUNDED-POC-PET-PROFILE-AMENDMENT-001](ADW-D13-BOUNDED-POC-PET-PROFILE-AMENDMENT-001.md),
the accepted prerequisite/scoping records or any immutable local preflight
package. Every requirement of the authorization as amended for Pet remains in
force unless this record narrows an open choice that those records explicitly
left to a later decision.

## Exact basis

At disposition time:

| Item | Identity |
| --- | --- |
| ADW `main` | `d1f30a3c362459fe3a59cbba725a77be3f571f97` |
| ADW tree | `d76f1258150c4bb64295927ea44bad030c7cd6f2` |
| ADW Research Register blob | `45357fa9259584ab7bd40cb7d1872e254fb04672` |
| Authorization blob | `72fd838f807d565517ce4668700f2e2a02fed8a3` |
| Pet profile amendment blob | `e4860562ff7764d548e17814de5eddaa494ddb3b` |
| Scoping record blob | `25615d21d28ef74bf0a6fede1bf9cc1609a54319` |
| Pet `main` | `28f84fe4324925adae0f17163d578ed2e1f9bc19` |
| Pet tree | `34a4b5ce54a1608d37305a8a4fecc4c29ce83689` |

Pet observations, read live and read-only on 2026-09-25 through Git and the
GitHub API:

- `main` is `28f84fe4324925adae0f17163d578ed2e1f9bc19`, tree
  `34a4b5ce54a1608d37305a8a4fecc4c29ce83689`, unchanged from the preflight-003
  subject;
- branch read reports `main` as `protected: false`;
- no branch named `pilot/*` or containing `d13` exists;
- pull requests with head `pilot/d13-runtime-control-evidence-001`, any state:
  none;
- open pull requests: exactly one, draft PR #99
  `docs/exp-003-termination-without-result-001`, unrelated to this PoC.

These are observations for this disposition candidate only. The credential
gate and any execution gate must re-read live Pet state.

## Accepted preflight input: preflight-003

The exact reviewed implementation/preflight package is:

| Item | Identity |
| --- | --- |
| Local root | `/Users/antony/Work/Projects/adw-d13-poc-preflight-003` |
| Candidate identity (SHA-256 of the exact bytes of `MANIFEST.sha256`) | `e06eee1bbb0083adc35a965c8768f1516d97bae1d017908dffe1c0e05d7b32e8` |
| `subject.json` SHA-256 | `7ca638b99e7d3025347f0969d9decbda5aaed2a596ccf37f468d30bb7e3c0ff7` |
| `preflight-report.md` SHA-256 | `ac80f130eb8ed7d6c6f9df332afd1160a6cf1213a355f3292023be7f3bfaefbe` |

Fresh independent affected review result: **PASS**, with findings
BLOCKER 0, MAJOR 0, MINOR 2, NOTE 4.

The PASS means only that the implementation/preflight package is technically
suitable evidence for the next execution-authorization process. It does not
authorize execution or credential creation, does not establish D13 conformance
and does not accept Product behavior beyond the explicit decisions in this
record.

Decision: preflight-003, at exactly the identities above, is accepted as the
reviewed implementation/preflight input for subsequent D13
execution-preparation decisions. Every later authority record must cite these
exact identities. A package whose manifest bytes, subject or report differ is a
different candidate and is not covered.

The preflight-003 subject remains an implementation/preflight subject only; it
refuses execution authority by construction. An execution subject must still be
a new, separately reviewed subject.

The two MINOR findings are carried forward below. The four NOTEs are recorded by
count only; this record neither restates nor dispositions them.

## Decision 1: `main`-write residual-risk disposition

### Known residual risk

For the selected Pet profile, all of the following hold at disposition time:

- Pet `main` reports `protected: false`;
- classic branch-protection, repository-ruleset and branch-rules evidence is
  incomplete and plan-limited (plan-related 403, as recorded by the profile
  amendment and reread by preflight-003); this is an evidence gap, not proof of
  absence of capability;
- the publisher's software ref/path allowlist constrains only that code path;
  it is **not** a GitHub provider-side fence;
- the selected publisher credential may technically possess repository-level
  contents-write capability beyond the intended pilot branch, including the
  capability to write `main`.

No currently evidenced GitHub provider-side control prevents a repository
contents-write credential from targeting `main`.

### Disposition

For exactly one bounded D13 PoC targeting `ahtoxaandy999/pet-project`, this
known residual risk is **accepted**.

The acceptance is scoped to:

- one bounded D13 Pet pilot only;
- the selected D13 mechanism only;
- the dedicated pilot branch/effect domain only, as defined by the Pet profile
  amendment.

It confers:

- no general workflow authority;
- no production authority;
- no multi-project authority;
- no merge authority;
- no unattended/AFK authority.

The risk is **not eliminated**. Accepting it does not make the software
allowlist a provider-side control, does not make repository-scoped contents
write branch-scoped, and does not relax any forbidden Pet effect, including the
prohibition on writing `main`. The allowlist and the minimal effective
permission of the publisher credential remain load-bearing. A later
out-of-domain write, or evidence that the effective publisher permission is
broader than the proven profile, remains a stop condition.

## Decision 2: credential products and role separation

### Selected products

GitHub fine-grained personal access tokens are selected as the credential
product for the one bounded pilot.

Exactly **two separate credentials** are selected:

- **A. publisher credential**;
- **B. reviewer/live-provider-reader credential**.

They must never be the same token. Existing broad local GitHub authentication
is not either selected credential.

No token is created, stored or configured by this record.

### A. Publisher credential profile

Product: GitHub fine-grained personal access token.

Repository scope: `ahtoxaandy999/pet-project` only.

Intended minimum effective capabilities, to be proven later:

- repository metadata/read access required by GitHub;
- Contents read/write, only because the bounded publisher must eventually update
  the dedicated pilot branch;
- Actions read for workflow-run and artifact reconciliation;
- Pull requests read/write only if the later exact execution authorization
  assigns draft-pilot-PR creation to this credential.

Forbidden intended capabilities:

- repository administration;
- ruleset/protection mutation;
- secrets mutation, or secrets read beyond unavoidable platform metadata;
- workflow-definition mutation;
- Actions write/dispatch, unless later separately authorized;
- merge;
- ready-for-review;
- unrelated repository access;
- general-purpose user GitHub activity.

Repository-scoped Contents write is **not** branch-scoped. The exact effective
permission proof for this credential is a later prerequisite.

The publisher credential remains subject to every constraint of the amended
authorization: it is available only to the lock-owning publisher process, and
possession without the canonical lifetime lock and current canonical generation
is never authorization. It must never enter logs, evidence, prompts, repository
files, or executor or reviewer contexts.

### B. Reviewer/live-provider-reader credential profile

Product: a **second** GitHub fine-grained personal access token.

Repository scope: `ahtoxaandy999/pet-project` only.

Intended capabilities:

- Contents read;
- Pull requests read;
- Actions/workflow-run/artifact read;
- additional read-only metadata/check visibility only if proven necessary.

Must not have:

- Contents write;
- pull request mutation;
- ready-for-review or merge;
- Actions mutation;
- ruleset/protection mutation;
- administration;
- secret mutation;
- access to the publisher token.

This credential owns both:

- the independent reviewer GitHub read surface; and
- the reviewed live provider-reader observations used by the runtime freshness
  gates.

The reader implementation has not been produced or reviewed. The exact
effective read-only permission proof for this credential is a later
prerequisite, including its suitability for S9 reviewer isolation.

## Preflight review MINOR-1: live provider reader required

The reviewed preflight-003 package relies on a caller-supplied `fresh_snapshot`
at its advancing transitions. The execution candidate must **not** inherit that
caller-supplied snapshot as sufficient authority.

Before an execution authorization can become effective, a separately reviewed
live provider reader must:

- construct the actual `ProviderSnapshot` from live GitHub;
- use the selected read-only reviewer/live-reader credential (B);
- be repository-bound to `ahtoxaandy999/pet-project`;
- compute its observation digest internally from the actual evidence
  bytes/state;
- compute the semantic provider-state fingerprint internally;
- not allow a caller to substitute arbitrary digest or fingerprint values;
- provide an observation whose freshness and provenance are suitable for each
  advancing transition;
- preserve the reviewed distinction between observation identity and semantic
  provider-state identity.

The eventual runtime gate must bind this reviewed reader implementation and its
digest.

This record does not implement, select or review the reader.

## Preflight review MINOR-2: editorial discrepancy

Nonblocking editorial discrepancy: the immutable preflight-003
`preflight-report.md` §5.7 contains stale prose referencing the previous
candidate root (`…/adw-d13-poc-preflight-002`) and an older observation.

The actual reviewed `subject.json` and the candidate identity are correct.

preflight-003 is **not** modified to repair the prose. The discrepancy is
preserved as historical review evidence. All future authority records must use
the exact preflight-003 identities recorded above, not the §5.7 prose.

## States that remain unchanged

- `d13_status`: `CONDITIONALLY SELECT FOR ONE BOUNDED POC`;
- `d5_status`: `CONFIRM DEFER`;
- `x3_status`: `CONFIRM REJECT`;
- `d13_conformance_result`: `not-established`;
- current selected profile: `ahtoxaandy999/pet-project`.

The selected mechanism is unchanged:

- supervised task-local deterministic Python;
- one credential-bearing publisher process;
- publisher lifetime POSIX `flock`;
- canonical generation record;
- canonical local control/evidence lock;
- GitHub GraphQL `createCommitOnBranch(expectedHeadOid)`;
- local durable evidence/recovery state;
- separate publisher and reviewer/live-reader credentials.

## Authority after this record

After independent review, coordinator acceptance and protected publication with
verified readback, this record establishes only:

- preflight-003, at the exact identities above, is accepted as the reviewed
  implementation/preflight input for subsequent D13 execution-preparation
  decisions;
- the one-PoC `main`-write residual-risk disposition above;
- selected credential products: two separate GitHub fine-grained personal access
  tokens;
- the selected role separation: publisher (A) and reviewer/live-provider-reader
  (B);
- the requirement for a separately reviewed live provider reader before
  execution authorization can become effective.

It does **not** establish:

- `credential_creation_authorized: true`;
- `pilot_execution_authorized: true`;
- `pet_project_mutation_authorized: true`;
- D13 conformance.

All three authorization flags remain `false`:

- `credential_creation_authorized: false`
- `pet_project_mutation_authorized: false`
- `pilot_execution_authorized: false`

## Next gate

**D13 Pet credential creation and effective-permission proof authorization gate**

Its purpose is to obtain a new, explicit user/coordinator authorization before
any token is created. That later gate must bind:

- the exact selected credential products from this record;
- how the credentials will be created;
- where they are stored;
- evidence that they are separate;
- exact effective GitHub permissions of each;
- exact repository scope of each;
- secret-handling constraints;
- the live-reader implementation and review plan.

Only after credential creation and effective-permission proof may an exact
execution-authorization candidate be produced. That execution authorization
remains mandatory before the first Pet effect and must still bind every item
required by the amended authorization's execution-authorization boundary,
including the reviewed live reader and its digest.

## Intended Register transition

After exact candidate review, coordinator/human acceptance and protected
publication of this record, the Research Register should, in the DR-006/D13
block only:

- add this record, its task and decision;
- record the preflight-003 candidate identity, subject digest, report digest,
  PASS review result and findings count;
- record preflight-003 as accepted execution-preparation input;
- record the `main`-write residual-risk disposition, its one-bounded-Pet-PoC
  scope and that the risk is not eliminated;
- record the selected publisher and reviewer/live-reader credential products and
  the two-credential separation;
- record the live-provider-reader prerequisite and the MINOR-2 editorial
  discrepancy;
- retain `credential_creation_authorized: false`,
  `pet_project_mutation_authorized: false`, `pilot_execution_authorized: false`
  and `d13_conformance_result: not-established`;
- retain D13/D5/X3 and the repository-wide current gate;
- set the D13-specific next gate to
  `D13 Pet credential creation and effective-permission proof authorization gate`.

## Explicit non-actions

This record does not:

- create, store, select beyond product/role, or configure credentials or tokens;
- mutate Pet Project;
- create the Pet pilot branch, marker or PR;
- touch PR #99;
- execute GraphQL mutations or trigger workflows;
- run the PoC or authorize pilot execution;
- implement or review the live provider reader;
- modify any immutable local preflight package;
- change the selected runtime, generation fence or commit primitive;
- establish D13 conformance;
- reopen D5 or change X3;
- amend Workflow v1 or accept a repository baseline;
- change the repository-wide current gate;
- authorize merge, unattended or AFK operation.
