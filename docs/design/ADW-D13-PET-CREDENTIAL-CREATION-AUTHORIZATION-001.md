---
id: ADW-D13-PET-CREDENTIAL-CREATION-AUTHORIZATION-001
artifact: coordinator-credential-creation-authorization
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-decision
repository: ahtoxaandy999/agentic-development-workflow
subject_main: 7ae30eee82b71b5f06a84b1aa428721fd3766e76
subject_tree: afd3cc70d4c9e5bca3a6a75651b8f8f4fe6840c0
subject_register_blob: baecfbc3757b78e59e8e73183b2ee64f18f74d55
authorization_ref: docs/design/ADW-D13-BOUNDED-POC-AUTHORIZATION-001.md
authorization_blob: 72fd838f807d565517ce4668700f2e2a02fed8a3
profile_amendment_ref: docs/design/ADW-D13-BOUNDED-POC-PET-PROFILE-AMENDMENT-001.md
profile_amendment_blob: e4860562ff7764d548e17814de5eddaa494ddb3b
execution_prerequisite_disposition_ref: docs/design/ADW-D13-PET-EXECUTION-PREREQUISITE-DISPOSITION-001.md
execution_prerequisite_disposition_blob: 5cf8ac218c0227adbc53e09b4d175595541c8615
selected_profile_repository: ahtoxaandy999/pet-project
preflight_candidate_identity: e06eee1bbb0083adc35a965c8768f1516d97bae1d017908dffe1c0e05d7b32e8
preflight_subject_sha256: 7ca638b99e7d3025347f0969d9decbda5aaed2a596ccf37f468d30bb7e3c0ff7
preflight_report_sha256: ac80f130eb8ed7d6c6f9df332afd1160a6cf1213a355f3292023be7f3bfaefbe
decided_on: 2026-09-25
human_signal: "++"
decision: authorize-bounded-d13-pet-fine-grained-pat-creation-effective-permission-proof-and-live-provider-reader-implementation
d13_status: CONDITIONALLY SELECT FOR ONE BOUNDED POC
d5_status: CONFIRM DEFER
x3_status: CONFIRM REJECT
selected_mechanism_changed: false
credential_products_changed: false
effective_condition: independent-review-coordinator-acceptance-protected-publication-verified-readback
credential_creation_authorized_after_effective_condition: true
credential_effective_permission_proof_authorized_after_effective_condition: true
live_provider_reader_implementation_authorized_after_effective_condition: true
live_provider_reader_review_required: true
pet_project_mutation_authorized: false
pilot_execution_authorized: false
main_write_residual_risk_disposition: accepted-for-one-bounded-pet-poc-only
main_write_residual_risk_eliminated: false
conformance_result: not-established
normative_effect: none
supersedes: null
---

# D13 Pet credential creation and effective-permission proof authorization

## Decision

`authorize-bounded-d13-pet-fine-grained-pat-creation-effective-permission-proof-and-live-provider-reader-implementation`

The user has explicitly authorized, with signal `++`, progression through the
**D13 Pet credential creation and effective-permission proof authorization
gate** for the one bounded D13 Pet PoC already selected.

This record fixes, exactly:

1. the two credential profiles (A publisher, B reviewer/live provider reader);
2. the manual, user-mediated creation procedure;
3. the macOS Keychain storage contract;
4. the non-secret effective-permission proof;
5. the live-provider-reader implementation and review plan;
6. stop conditions and the next gate.

It does not create any token, mutate Pet Project, implement the reader, execute
the pilot or establish D13 conformance.

## Effective condition

The authorizations in this record become effective only after all of the
following hold for this exact record:

1. fresh independent review of the exact candidate commit;
2. explicit coordinator/human acceptance of that exact candidate;
3. separately authorized protected merge publication;
4. verified remote readback.

Until then, `credential_creation_authorized`,
`credential_effective_permission_proof_authorized` and
`live_provider_reader_implementation_authorized` are not in effect. A local
file, commit, branch, draft PR or passing check does not satisfy this condition.

After the effective condition, the authorizations apply only to the exact
procedures and scopes below. Anything not stated here remains unauthorized.

## Exact basis

| Item | Identity |
| --- | --- |
| ADW `main` | `7ae30eee82b71b5f06a84b1aa428721fd3766e76` |
| ADW tree | `afd3cc70d4c9e5bca3a6a75651b8f8f4fe6840c0` |
| ADW Research Register blob | `baecfbc3757b78e59e8e73183b2ee64f18f74d55` |
| Authorization blob | `72fd838f807d565517ce4668700f2e2a02fed8a3` |
| Pet profile amendment blob | `e4860562ff7764d548e17814de5eddaa494ddb3b` |
| Execution-prerequisite disposition blob | `5cf8ac218c0227adbc53e09b4d175595541c8615` |
| Accepted preflight-003 candidate identity | `e06eee1bbb0083adc35a965c8768f1516d97bae1d017908dffe1c0e05d7b32e8` |
| preflight-003 `subject.json` SHA-256 | `7ca638b99e7d3025347f0969d9decbda5aaed2a596ccf37f468d30bb7e3c0ff7` |
| preflight-003 `preflight-report.md` SHA-256 | `ac80f130eb8ed7d6c6f9df332afd1160a6cf1213a355f3292023be7f3bfaefbe` |

The credential products and role separation selected by
[ADW-D13-PET-EXECUTION-PREREQUISITE-DISPOSITION-001](ADW-D13-PET-EXECUTION-PREREQUISITE-DISPOSITION-001.md)
are unchanged. This record fixes their exact configuration.

## Credential A — publisher

| Field | Value |
| --- | --- |
| Product | GitHub fine-grained personal access token |
| Resource owner | `ahtoxaandy999` |
| Repository access | Only select repositories |
| Selected repository | `ahtoxaandy999/pet-project` only |
| Expiration | 7 days from token generation |
| Metadata | read (provider-required/implicit) |
| Contents | read and write |
| Actions | read |
| Pull requests | read and write |
| Any other repository, organization or account permission | not intentionally selected |
| Keychain service | `adw-d13-pet-publisher` |
| Keychain account label | `ahtoxaandy999` |

Intended use, only when later separately authorized:

- bounded pilot branch setup and publisher effects;
- draft pilot PR creation, only if the later exact execution authorization
  assigns that effect to this credential;
- Actions readback and reconciliation.

Forbidden authority remains:

- direct `main` mutation;
- merge;
- ready-for-review;
- Actions dispatch/write;
- workflow-definition mutation;
- administration;
- ruleset/protection mutation;
- secret management;
- unrelated repository activity;
- general-purpose GitHub use.

Contents write is repository-scoped, **not** branch-scoped. Credential A
therefore carries the main-write residual risk already accepted, for one bounded
Pet PoC only, by the execution-prerequisite disposition. The risk is **not
eliminated**.

Pull requests write is likewise not provider-fenced to the pilot PR. Any
platform capability it confers to change PR state outside the pilot, mark ready
or merge remains forbidden by authority and by the publisher allowlist only.
A merge would be a `main` write covered by the accepted residual risk and remains
forbidden. This record does not broaden the accepted residual risk.

No regeneration, replacement or extension of credential A beyond its exact
7-day lifetime is authorized. Any later regeneration, replacement or extension
requires separately established authority or an explicitly applicable
replacement rule. Automatic renewal authority is not assumed.

## Credential B — reviewer / live provider reader

| Field | Value |
| --- | --- |
| Product | GitHub fine-grained personal access token (second, distinct) |
| Resource owner | `ahtoxaandy999` |
| Repository access | Only select repositories |
| Selected repository | `ahtoxaandy999/pet-project` only |
| Expiration | 7 days from token generation |
| Metadata | read (provider-required/implicit) |
| Contents | read |
| Actions | read |
| Pull requests | read |
| Any write permission | not intentionally selected |
| Keychain service | `adw-d13-pet-reviewer-reader` |
| Keychain account label | `ahtoxaandy999` |

Credential B must be a distinct token value and a distinct credential record
from A. It must not intentionally possess:

- Contents write;
- Pull requests write;
- Actions write;
- Administration;
- Workflows write;
- Secrets write;
- ruleset/protection mutation.

Roles:

- independent reviewer GitHub read surface;
- live `ProviderSnapshot` reader.

Credential B must never receive or have access to credential A.

The same regeneration/replacement/extension restriction applies to B as to A.

## Token creation procedure

Creation is manual and user-mediated through the GitHub fine-grained PAT UI.
Token generation is not automated.

For each token, separately:

1. open GitHub fine-grained PAT creation;
2. select resource owner `ahtoxaandy999`;
3. select **Only select repositories**;
4. select `pet-project` only;
5. set the exact 7-day expiration;
6. configure only the exact permissions defined for that credential above;
7. verify the complete form before generation;
8. generate;
9. immediately store the secret in macOS Keychain under that credential's
   service name;
10. clear any transient clipboard copy as soon as storage and readback are
    complete.

Token values must never be:

- pasted into ChatGPT;
- pasted into Codex or other agent prompts;
- committed;
- written to repository files;
- written to evidence;
- written to logs;
- written to `.env` files;
- written to shell history;
- passed as ordinary command-line arguments.

Consequently, the storage step must not place the token value in argv or shell
history; the exact storage method used is recorded, without the value, in the
evidence package.

If secure creation or storage cannot be completed without exposing token bytes
to the execution or chat surface, stop.

## macOS Keychain storage contract

Canonical secret store: macOS Keychain on the authorized Mac.

Two separate generic-password records:

| Credential | Service | Account |
| --- | --- | --- |
| A publisher | `adw-d13-pet-publisher` | `ahtoxaandy999` |
| B reviewer/live reader | `adw-d13-pet-reviewer-reader` | `ahtoxaandy999` |

At authorization-candidate time, a metadata-only lookup found no existing
generic-password record for either service. The setup must reconfirm absence
before storage; an unexpected pre-existing record is a stop condition, not
something to overwrite.

The token value is not stored anywhere else as canonical state.

Evidence may record only:

- service name;
- account label;
- creation timestamp;
- expiration timestamp;
- non-secret token identifier, if GitHub exposes one safely;
- SHA-256 token fingerprint, only if computed locally in memory with no token
  bytes retained.

Evidence must never contain the token itself.

The two stored credentials must be proven distinct without revealing values.

## Effective-permission proof

The later credential-setup execution produces a non-secret evidence package in a
local evidence root outside all repository worktrees. Its exact path and
custodian are recorded in that package.

For each credential record, the package must contain:

1. provider-authoritative creation/configuration evidence proving resource
   owner, selected repository, expiration and selected permissions;
2. a successful read-only repository identity read for
   `ahtoxaandy999/pet-project`;
3. successful allowed read probes for every required read capability of that
   credential;
4. confirmation that no Pet mutation occurred as part of the permission proof;
5. proof that A and B are different credentials;
6. proof that B has no intentionally selected write permission;
7. an explicit note that A's Contents write capability is not branch-scoped and
   remains the accepted residual risk.

Write capability is **not** proven by performing an otherwise unauthorized Pet
write. Provider UI/configuration evidence is required for any permission that
cannot be proved safely by a read-only API operation. Absence of write
capability is not inferred merely because no write was tried.

## Live provider reader plan

A new, separately reviewed local reader implementation is required before exact
execution authorization. Suggested local candidate root:

`/Users/antony/Work/Projects/adw-d13-pet-live-reader-001`

The reader is separate from the mutation publisher surface.

Implementation constraints:

- Python standard library unless live evidence proves a dependency is necessary;
- network read capability only;
- GitHub REST/GraphQL queries only where required;
- no mutation documents;
- no POST/PATCH/PUT/DELETE provider effects, except that a GraphQL read query
  sent over HTTP POST is permitted only if the document is a fixed query with no
  mutation operation;
- no `git push`;
- no `gh` mutation fallback;
- no generic arbitrary URL or request interface;
- repository hard-bound to `ahtoxaandy999/pet-project`.

Credential: B only, never A.

The reader constructs `ProviderSnapshot` from live provider state itself and
internally derives:

- observation evidence;
- observation digest;
- semantic provider-state fingerprint.

Caller-provided digest or fingerprint values are never authoritative.

Preflight review MINOR-1 is addressed explicitly. The reader candidate must:

- require the actual reviewed `ProviderSnapshot`/reader result type at every
  advancing transition, not a caller-supplied `fresh_snapshot`;
- compute the observation digest from actual reader evidence inside the trusted
  reader/gate boundary;
- not trust a caller-supplied digest;
- define and verify freshness and provenance semantics suitable for each
  advancing transition;
- preserve the distinction between observation identity and semantic
  provider-state identity;
- have its implementation digest bound into the later execution subject.

Reader output must cover every GitHub fact required by preflight-003
reconciliation and freshness semantics, including:

- pilot branch presence and head;
- pilot commits and commit readback;
- `Exact candidate verification` workflow runs;
- workflow and run identity;
- event, status and conclusion;
- artifacts and artifact digests;
- pilot PR state;
- attribution needed to exclude unrelated PR #99 effects.

The live-reader candidate must receive fresh independent review before execution
authorization. Implementation authorization does not accept the reader.

## Stop conditions for credential setup

Stop before accepting a created credential if:

- the resource owner differs;
- repository selection is not exactly `pet-project`;
- expiration differs materially from the authorized value;
- an unexpected permission is enabled;
- tokens A and B cannot be proven distinct;
- the reviewer token has write capability intentionally selected;
- token bytes enter logs, evidence, the repository or prompt history;
- secure Keychain storage cannot be established;
- the provider UI requires materially broader access;
- the account or policy blocks fine-grained PAT creation or requires an
  unplanned approval path.

A failed or aborted token creation grants no fallback authority to use the
existing broad local GitHub authentication.

## Authority after the effective condition

After independent review, explicit coordinator/human acceptance and protected
publication with verified readback of this exact record:

- `credential_creation_authorized: true`
- `credential_effective_permission_proof_authorized: true`
- `live_provider_reader_implementation_authorized: true`

only for the exact procedures and scopes in this record.

The following remain:

- `pet_project_mutation_authorized: false`
- `pilot_execution_authorized: false`
- `d13_conformance_result: not-established`

Credential creation is not Pet repository mutation. No first Pet effect is
authorized by this record.

## States that remain unchanged

- `d13_status`: `CONDITIONALLY SELECT FOR ONE BOUNDED POC`;
- `d5_status`: `CONFIRM DEFER`;
- `x3_status`: `CONFIRM REJECT`;
- selected profile: `ahtoxaandy999/pet-project`;
- selected mechanism, accepted preflight-003 identity and credential products;
- main-write residual risk: accepted for one bounded Pet PoC only, not
  eliminated;
- repository-wide current gate.

## Next gate

**D13 Pet credential proof and live-provider-reader evidence acquisition gate**

This gate does not advance directly to pilot execution. It comprises:

1. actual bounded credential creation and effective-permission proof;
2. the live-reader implementation candidate;
3. independent review of the credential evidence and the live reader;
4. exact execution subject preparation;
5. a separate exact execution authorization before the first Pet effect.

## Intended Register transition

After the effective condition, the Research Register DR-006/D13 block records
this artifact, task, decision and subject main; the exact credential profiles,
two-token separation, repository scope, expiration, Keychain storage contract;
the three authorizations as `true`; live-reader review required; Pet mutation
and pilot execution `false`; conformance `not-established`; the residual risk
still accepted and not eliminated; and the next gate above. The repository-wide
current gate is unchanged.

## Explicit non-actions

This record does not:

- create, store or configure any token;
- request or expose token values;
- mutate Pet Project, create the pilot branch, marker or PR, or touch PR #99;
- implement or accept the live reader;
- execute GraphQL mutations or trigger workflows;
- run the PoC or authorize pilot execution;
- change the selected mechanism, preflight identity or credential products;
- establish D13 conformance;
- reopen D5 or change X3;
- amend Workflow v1 or accept a repository baseline;
- change the repository-wide current gate;
- authorize merge, unattended or AFK operation.
