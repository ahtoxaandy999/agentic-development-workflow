---
id: ADW-WF1-PERSISTENCE-CHECKER-OPVAL-DISPOSITION-RECORD-001
artifact: coordinator-disposition-record
artifact_status: active
owner: chatgpt-coordinator
decision: accept-bounded-operational-validation-evidence-for-limited-supervised-secondary-helper-use-only
checker_subject_commit: d17af996803ae91253f11308e92f1b3601e04aa8
decided_on: 2026-09-05
normative_effect: none
operational_authority: none
supersedes: null
---

# Workflow v1 persistence checker bounded operational-validation disposition

## Decision

`accept-bounded-operational-validation-evidence-for-limited-supervised-secondary-helper-use-only`

The completed bounded operational-validation evidence is accepted only as support for possible future, separately authorized, limited supervised use of the persistence checker as a secondary helper.

This decision accepts evidence. It does not authorize checker execution or operational use.

## Exact checker subject

This disposition concerns the exact three-file checker candidate at commit `d17af996803ae91253f11308e92f1b3601e04aa8`:

| Path | Git blob | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `tools/persistence_checker.py` | `655cf2e8c2809b299e53f6e585a5d9bce0dc9c34` | 62875 | `c0ad28a8e59d3e4d161c74b0f832682ed590836229b35f45527c645d9030d723` |
| `tests/test_persistence_checker.py` | `f975ced081a736e9b156411a303bb8675deb8bb3` | 62065 | `f58273a337019da436af1d65d4f590e008773c72bf00566ebb9011a5c0d7a970` |
| `docs/tooling/persistence-checker.md` | `405f8222b4d6f7b48b9332a758ab6d1c3c945f0f` | 14173 | `cec48b49f7496c3869b5a10eefd43db266e384d9aa3f816b22f1cda1da0c3814` |

The checker remains a manually invoked, deterministic, offline, input-read-only helper whose only permitted output effect, when separately authorized, is exclusive creation of one designated report.

## Accepted positive evidence

The positive retrospective readback case produced:

- result `PASS/0`;
- `105/105` predicates with result `PASS`;
- agreement with an independent native Git/byte oracle.

Positive report identity:

- SHA-256: `dbdb2d2afdd6f72a44d7544435b2d5e9c5e83974fa30c9037b44cc1c7e0b05e6`.

No Git blob identity for this report is asserted by this record because none was established in the accepted evidence supplied to the coordinator.

## Accepted negative evidence

### Incorrect parent

- preserved case-level evidence: the successful incorrect-parent case from `OPVAL-005`;
- expected and observed result: `FAIL/1`;
- report SHA-256: `01ae0fd303d1fbee808124862f8d3bc6d143eb6daf88188250717a36321038d9`;
- report Git blob: `e836e03691705202d631349502d6bf3e65f45b69`.

### Unauthorized extra path

- accepted continuation evidence: `OPVAL-007`;
- expected and observed result: `FAIL/1`;
- report SHA-256: `0fadb5edd3879d59c76d1cfb511004b42888aa0f0631a20e0e46ebf8d57f72ff`;
- report Git blob: `e49ad588d53a5ff4491b0950ee5c8fb60f7548ef`.

### Corrupted Research Register bytes

- accepted continuation evidence: `OPVAL-007`;
- expected and observed aggregate result: `FAIL/1`;
- report SHA-256: `da123d3458f2dd6530ebc6773e0fdcd36e7ca590698fad959de85cd23ebc222b`;
- report Git blob: `05a66101cc571eb74ab9a127bca10db1b12cb49c`.

The frozen case oracle incorrectly expected `register.after_binding=FAIL`. That individual expectation was not satisfied. The actual corrupted bytes were nevertheless exposed fail-closed by five definite `FAIL` predicates:

- `file.register-after-observed.sha256`;
- `file.register-after-observed.git_blob`;
- `binding.docs/research/research-register.md.blob`;
- `register.after_exact`;
- `register.after_blob`.

The case is accepted as valid negative evidence because the material corruption was correctly detected and the aggregate result was `FAIL/1`. The incorrect frozen expectation remains preserved as oracle-preparation error evidence and is not rewritten as agreement.

### Incomplete required evidence

- accepted continuation evidence: `OPVAL-007`;
- expected and observed result: `UNEVALUABLE/2`;
- report SHA-256: `22429933544381c36fe3772b31da94cecb535dcc1db0fc21d78c18499db3d73f`;
- report Git blob: `ae50bb5eb3e8fd8bcd8f48bbeadb85b29af7313f`;
- exact non-PASS evidence:
  - `file.github-tree-response.read=UNEVALUABLE`;
  - `authority.raw_response_files=UNEVALUABLE`;
  - `authority.raw_tree_schema` was absent as expected because the required raw evidence could not be evaluated.

## Execution-episode preservation

All validation execution episodes remain separate evidence and must not be rewritten, collapsed, or deleted.

In particular:

- Attempts `001` and `002` remain distinct failed execution episodes;
- the accidental `--help` invocation remains a failed execution episode and is not checker introspection evidence;
- frozen `OPVAL-004`, `OPVAL-005`, `OPVAL-006`, and `OPVAL-007` evidence remains unchanged;
- the successful incorrect-parent case from `OPVAL-005` remains case-level evidence;
- failed fixture and oracle preparation remains evidence of preparation risk and cost;
- later successful or corrected cases do not overwrite earlier failed episodes.

The preparation history supports the fail-closed behavior observed, but it is evidence against routine, low-supervision, automated, or unattended use.

## Permitted interpretation

The accepted evidence supports only a future possibility of limited supervised secondary-helper use inside a separately authorized bounded operation.

For any such future authorization:

- the checker may produce supporting evidence only;
- active human supervision is mandatory;
- the exact subject, base, inputs, evidence sources, report destination, effects, and stop boundary must be bound in advance;
- authoritative and native verification required by the owning gate remains mandatory;
- coordinator acceptance remains separate from checker output;
- a checker result cannot independently advance a gate, authorize persistence, or establish acceptance.

## Mandatory fail-closed conditions

A future bounded operation must stop on any of the following:

- `FAIL/1`;
- `UNEVALUABLE/2`;
- checker/oracle disagreement;
- contradiction with authoritative or native evidence;
- stale, unavailable, incomplete, unauthenticated, or unverifiable evidence;
- fixture, case, report, or oracle preparation error;
- failure of an authoritative state reread required by the owning gate;
- ambiguity concerning subject, parent, tree, path set, Register bytes, evidence identity, permissions, custody, or writer exclusivity;
- unexpected repository state;
- attempted scope expansion.

No positive checker result overrides a stop condition. Missing enforcement or evidence fails closed.

## Authoritative rereads and ownership

The checker is not an authoritative mutable state owner.

This record owns only the immutable coordinator disposition stated here. It does not own current repository state, current Register state, task state, execution state, operational authorization, checker acceptance state, or Workflow v1 adoption state.

The Research Register or another explicitly designated existing owner continues to own mutable current gate and decision status where applicable. Chats, fixtures, reports, runners, and this record may point to authoritative state but do not replace it.

At every state-dependent gate, the required authoritative repository and native Git evidence must be reread independently of checker output. A branch name, green result, report, commit, or `PASS/0` is not sufficient identity by itself.

## RG and design-impact boundaries

`RG1` through `RG12` remain unresolved. This disposition resolves none of them and creates no missing protection, writer fencing, publication guarantee, reviewer-identity enforcement, permission proof, containment, recovery, retention, capability verification, optional integration assurance, documentation clarity, or AFK control.

`DI-1` remains preserved: orthogonal state planes and legitimate `N/A` remain distinct from required pass.

`DI-2` remains preserved: freshness, operation-aware retry, containment/recovery separation, durable episode history, reopening, explicit reset, and independent terminal guards are not weakened to fit the checker.

## Explicit non-authorities

This disposition does not authorize:

- checker execution;
- any operational trial or operational reliance;
- standing, routine, primary, or sole-authority use;
- automated acceptance or automated execution;
- parallel execution;
- unattended or AFK execution;
- repository, Research Register, Git, or GitHub mutation;
- a commit, push, branch, tag, pull request, Issue, comment, review, check, release, hook, Action, installation, or configuration;
- replacement of independent review, native verification, or coordinator disposition;
- expansion to another repository, workflow, task class, case type, or operating mode;
- Workflow v1 normative adoption;
- resolution of any `RG1` through `RG12`;
- establishment of a new baseline.

Availability of the checker is not authority to use it. Acceptance of bounded validation evidence is not operational authorization.

## Unresolved limitations

The accepted validation does not establish:

- completeness against untested failure modes;
- authenticated provenance of supplied snapshots or fixtures;
- current live-state truth or future ref stability;
- technical writer exclusivity or cross-surface permission enforcement;
- safety under concurrency, stale-state races, unusual Git states, filesystem check/use races, or different environments;
- reliable or low-cost preparation of fixtures and independent oracles;
- suitability for repeated, routine, automated, parallel, unattended, or AFK use;
- suitability as primary or sole acceptance authority;
- measured operational usefulness or maintenance economy.

Any broader use requires a new explicit gate, evidence matched to that expansion, independent validation, deterministic stop semantics, preserved state ownership, and a separate coordinator decision.

## Lifecycle

This local record materializes the coordinator disposition only. It does not change repository or Research Register state.

The next repository-facing step, if desired, is a separately authorized exact-base persistence gate that independently rereads live GitHub state, verifies all controlling owners and identities, defines the exact changed paths and Register transition, and stops on drift or conflict.

No repository persistence is required automatically merely because this local disposition record exists.

## Materialization statement

This record was materialized locally under explicit user authorization. The materialization did not run the checker and did not modify the repository, Research Register, or GitHub. Exact serialization identity is reported separately after byte-level verification.
