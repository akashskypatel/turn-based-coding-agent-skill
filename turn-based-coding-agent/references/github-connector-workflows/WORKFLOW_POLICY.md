# GitHub Actions Workflow Policy

**Context class:** `conditional-deep-reference`

Load when an agent creates, modifies, validates, triggers, observes, or cleans up GitHub Actions workflows.

## Operating authority

GitHub connector is the control plane. GitHub Actions is a bounded remote execution plane for computation or repository operations that the connector cannot safely perform directly. Actions never relax the active Code + Build, Test + Benchmark, granular subturn, or Review boundary.

Respect project-configured retention and cleanup policies.

## Working-branch policy

Perform agent work directly on the configured working branch. Do not create temporary, control, side, or staging branches unless a concrete procedural blocker cannot safely be solved on the working branch.

If an exception is necessary:

- record the blocker and why a branch is required;
- keep the branch narrowly scoped;
- remove/reset it as soon as the blocker is cleared.

## Allowed workflow uses

A project may define a stricter allowlist. By default, agent-created workflows are appropriate only for:

- long-running/resource-heavy compile or build work;
- patch application that cannot be safely represented by direct <=19 KB connector writes;
- source/repository snapshot generation for artifact transfer;
- repository-wide Actions-run inventory when connector run discovery is insufficient;
- validation of GitHub Actions YAML before publication;
- bounded computation or repository tooling not exposed by the connector.

Do not use Actions for small connector-native mutations merely for convenience.

## Durable reusable workflow roles

When the project supplies durable reusable workflows, prefer them over reproducing logic in turn-specific callers. Project configuration may identify:

- reusable compile/build workflow;
- reusable run-ID observer;
- reusable recent-runs inventory;
- reusable workflow-schema validator.

A temporary caller may provide only declared inputs and exact source/task parameters. It must not invent implementation details owned by a reusable workflow, such as cache lineage or compatibility keys.

## Mandatory workflow contract

Every new or modified agent workflow must:

1. initialize persistent diagnostic logging before checkout or other fallible work;
2. record event/ref/source identity, tool versions, commands/output, exit context, final source status, and relevant resource/cache state;
3. stream task output to console and the persistent log;
4. upload a dedicated diagnostic log under `if: always()` with `if-no-files-found: error`;
5. keep diagnostic logs separate from successful result artifacts;
6. use narrow triggers, concurrency where applicable, least privilege, and exact source/hash checks;
7. keep logs/evidence outside the source worktree;
8. never print secrets, credentials, authenticated URLs, or secret-bearing arguments;
9. never modify `.github/workflows/**` from inside a workflow;
10. use indentation-safe YAML/shell construction;
11. validate new/modified workflow YAML against a current GitHub-workflow schema or the configured reusable schema validator before treating it as publishable authority.

Schema validation complements but does not replace declared reusable-input checks or caller permission-ceiling checks.

## Reusable-workflow permissions

Compute caller permissions as the **union of permissions required by every called reusable workflow/job**, including nested jobs that may be skipped by runtime conditions. GitHub can validate reusable permission ceilings before `if:` conditions are evaluated.

Therefore:

- fetch current reusable workflow definitions before drafting the caller;
- pass only declared `workflow_call.inputs`;
- use `secrets: inherit` for same-repository calls when repository secrets are required;
- never assume a skipped nested job makes its requested permission irrelevant;
- do not grant more permissions than the static reusable graph actually requires.

## Workflow-originated pushes and authentication

When a workflow push must trigger a later push workflow, do not assume the default `GITHUB_TOKEN` will create that follow-up run. GitHub intentionally suppresses most recursive workflow creation from default-token pushes.

Use a project-authorized fine-grained token/PAT only when the intended control flow requires a workflow-originated repository write to remain trigger-eligible. Never copy the token value into workflow YAML or logs.

## Run-ID observability

Do not treat commit-associated workflow lookup as authoritative for push-triggered runs when the connector surface is known to filter by event. In particular, an empty commit-to-workflow result must not be interpreted as proof that a push workflow did not run.

For temporary push-triggered callers:

- prefer an early run-ID observer that reports the per-execution `github.run_id`;
- PR conversation comments are preferred because they do not advance branch state;
- an optional branch-file observer is a fallback and creates additional race/cleanup surface;
- verify observer `event_sha` against the exact trigger commit;
- if the observer is absent, query repository-wide Actions runs using the connector or a configured recent-runs reusable before retrying;
- never retrigger merely because a run ID was not immediately visible.

Load `TEMP_WORKFLOW_LIFECYCLE.md` for the exact caller/marker procedure.

## Compile/build boundary

Compile-only workflows may checkout exact pushed source, initialize required dependencies, configure in a compile-only mode, compile/link approved targets, and package compile evidence.

They must not execute produced project binaries, including tests, benchmarks, discovery/list/help/version commands, CLI/GUI entry points, fuzzers, or custom runtime inputs.

When a project provides a reusable compile workflow, all compile/build execution must call it rather than duplicate its implementation in temporary callers.

## Compiler-cache policy

When a durable reusable compile workflow owns compiler caching:

- prefer compiler-object caching (for example `ccache`) over opaque build-tree caching;
- derive compatibility keys only from stable compatibility facts such as runner OS, compiler/toolchain, build/configuration family, and a workflow-owned schema version;
- do not append run ID, turn name, source SHA, timestamp, retry number, or other per-run lineage;
- source SHA remains build/evidence authority, not cache compatibility authority;
- serialize destructive cache refreshes when overlapping runs could race;
- restrict cache writes to trusted events/tokens;
- cache compiler objects only, not immutable evidence or packaged outputs;
- log exact cache key, scope, restore status, statistics, size cap, refresh/delete operations, and whether save was allowed.

Temporary callers must not invent or override durable cache compatibility/versioning owned by the reusable workflow.

## Test + Benchmark boundary

Artifact-only Test + Benchmark workflows must verify the immutable package before execution and run packaged binaries/inputs without configure, compile, relink, regeneration, patching, or fixture mutation.

A zero-selected filter is orchestration failure, never a pass.

### Full-suite timeout rule

A complete acceptance/full semantic suite should run uninterrupted to an organic process result. Do not impose a repository workflow/job timeout whose purpose is to terminate the required full-suite run, and do not partition/retry/stitch continuations merely to evade elapsed runtime.

Platform service limits remain external infrastructure constraints. Focused diagnostic commands may use justified bounded timeouts; a timeout is orchestration/infrastructure failure, never semantic pass/skip.

## Evidence and failure rules

- Diagnose from detailed logs, not only Actions summaries.
- Record run/job IDs, exact source SHA, result/log artifact IDs/digests, checks executed, and checks deliberately not executed.
- Evidence-upload failure prevents acceptance even when the workload command succeeded.
- Do not rerun deterministic malformed orchestration unchanged.
- Never synthesize success or weaken validation.
- Never force-push to bypass a race.
- Clean temporary workflow state only after required evidence/source authority is preserved.

## End-of-turn hygiene

At the start and end of workflow-driven work, inspect configured workflow, trigger-marker, observation, and payload locations. Preserve durable reusable workflows and remove stale temporary state in workflow-first order.

When a project requires a final PR summary/comment, perform it only after repository mutations and cleanup are complete so the summary reflects final authority.
