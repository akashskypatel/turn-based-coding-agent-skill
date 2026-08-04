# GitHub Connector and Actions Workflow

Use this module whenever the active repository is available through `@GitHub` but the agent does not have a trusted local checkout, authenticated shell, or direct repository filesystem. It is part of the turn-based workflow: it does not relax Code + Build, Test + Benchmark, or Review boundaries.

For turn-specific execution:

- **Code + Build:** the connector manages source authority and GitHub Actions compiles the exact pushed commit. The workflow must not execute tests or benchmarks.
- **Test + Benchmark:** download and execute the exact build artifact without rebuilding. Preserve raw logs and results.
- **Review:** inspect repository, PR, evidence, logs, and plans without modifying implementation or validation logic.


## Purpose

Use the connected `@GitHub` app as the primary control plane for a remote repository. When the connector cannot directly perform computation, apply a large change, or run repository tools, use a narrowly scoped GitHub Actions workflow as the remote execution plane and use Actions artifacts as the evidence plane.

This skill is designed for agents that can call connector actions but may not have a local clone, an authenticated shell, or direct filesystem access to the remote repository.

## Core operating model

1. **Connector control plane**
   - Resolve repositories, branches, commits, pull requests, issues, files, and workflow results.
   - Create branches, blobs, trees, commits, files, PRs, comments, and labels.
   - Download job logs and workflow artifacts when the installed connector exposes those actions.
2. **Actions execution plane**
   - Run compilers, tests, benchmarks, patch application, repository scripts, and content verification inside GitHub-hosted runners.
   - Keep each workflow bounded to one declared purpose.
3. **Artifact evidence plane**
   - Upload detailed activity logs on success and failure.
   - Upload build, test, benchmark, patch, and verification outputs separately from logs.
   - Diagnose failed workflows from the uploaded detailed log artifact, not only from abbreviated step summaries.

## Mandatory workflow policy

Every workflow created or modified under this skill must:

1. Initialize a persistent activity log before checkout or other fallible work.
2. Capture tool versions, exact event/ref/source metadata, command output, exit codes, final repository status, and relevant resource usage.
3. Redirect task output to both the Actions console and the persistent activity log.
4. Use an `EXIT` trap or equivalent so failure context is recorded.
5. Upload a dedicated log artifact under `if: always()` with `if-no-files-found: error`.
6. Keep the log artifact separate from successful build or result artifacts.
7. Avoid printing tokens, secrets, credentials, authenticated URLs, or secret-bearing arguments.
8. Never modify `.github/workflows/**` from inside a workflow. Workflow files are changed only through the connector or another explicitly authenticated client outside Actions.
9. Preserve execution boundaries. A compile-only workflow must not execute tests, benchmarks, custom inputs, help/list commands, discovery commands, or compiled project binaries.

Use `templates/logged-remote-task.yml` as the baseline.

## Start every task by resolving authority

Before reading or writing:

1. Identify `repository_full_name` as `owner/repo`.
2. Resolve the authoritative branch, tag, commit, PR, or issue.
3. For a PR, call `get_pr_info` or `fetch_pr` and record:
   - base branch and SHA;
   - head branch and SHA;
   - state, draft status, and merge status.
4. For branch work, resolve the current head commit before creating dependent commits.
5. Treat branch heads as moving. Re-read the head before a final `update_ref` or other compare-and-swap mutation.
6. Do not infer that a file exists in a local sandbox because the connector returned a file reference.

## Route by task type

| Task | Preferred connector path | Remote workflow needed? |
|---|---|---:|
| Read repository/file/commit/PR state | `get_repo`, `fetch_file`, `fetch_commit`, `get_pr_info` | No |
| Update one small text file | `fetch_file` → `update_file` | No |
| Create one small text file | `create_file` | No |
| Atomic multi-file text update | `create_blob` → `create_tree` → `create_commit` → `update_ref` | No |
| Create branch | `create_branch` | No |
| Open or update draft PR | `create_pull_request`, `update_pull_request`, `convert_pull_request_to_draft` | No |
| Inspect workflow runs/jobs/logs/artifacts | `fetch_commit_workflow_runs`, `fetch_workflow_run_jobs`, `fetch_workflow_job_logs`, `fetch_workflow_run_artifacts` | No |
| Re-run failed jobs | `rerun_failed_workflow_run_jobs` or `rerun_workflow_job` | No |
| Compile, test, benchmark, execute repo tools | Create/trigger bounded workflow | Yes |
| Apply a large unified patch | Commit patch parts + trigger patch workflow | Usually |
| Transfer large binary/generated outputs | Workflow artifact | Usually |
| Verify an already-applied patch | Blob/hash comparison first; workflow only if computation is needed | Sometimes |

If an action is not loaded, discover the current connector schema before claiming it is unavailable. Use `gh` only when the connector lacks the required capability and an authenticated CLI environment actually exists.

## Common task procedures

### Read a file safely

1. Call `fetch_file` with explicit repository, path, and ref.
2. Record the returned blob SHA.
3. Use line ranges for large files when only a section is needed.
4. Re-fetch before a write if another actor may have changed the same path.

### Update one file

1. `fetch_file` on the target branch.
2. Prepare the complete replacement content.
3. `update_file` with the returned blob SHA and explicit branch.
4. Verify the resulting commit and re-fetch the file when correctness matters.

A `409` usually means the supplied blob SHA is stale or the same path was changed after it was fetched. Re-fetch that path and retry intentionally. Do not blindly repeat the same request.

### Create an atomic multi-file commit

Use Git data objects instead of sequential `update_file` calls when all files must land together.

1. Resolve the parent commit and its tree.
2. Create one blob per new file content using `create_blob`.
3. Create a new tree using `create_tree` with the parent tree as `base_tree_sha`.
4. Create a commit with `create_commit` and the resolved parent SHA.
5. Move the branch with non-forced `update_ref`.
6. If the ref moved, stop, re-read the head, reconstruct the tree on the new parent, and retry. Never force-update a shared branch merely to bypass a race.

Use this method for related source, test, and documentation edits that must remain coherent.

### Create a branch and draft PR

1. Resolve the exact base branch or commit.
2. `create_branch` from the explicit base.
3. Apply changes to that branch.
4. Verify the branch head.
5. `create_pull_request` with explicit head, base, title, body, and `draft: true` unless the user requests otherwise.
6. Re-fetch PR metadata and report the final head SHA and state.

Do not open a second PR when an existing PR already tracks the work branch. Update the existing PR instead.

### Create or modify a workflow

1. Read repository workflow policy and existing related workflows.
2. Create or update the workflow only through the connector or an authenticated external client.
3. Use least-privilege `permissions`.
4. Use a narrow trigger:
   - `workflow_dispatch` when a human or API dispatch is available; or
   - an exact unique push-marker path when connector dispatch is unavailable.
5. Add `concurrency` to prevent overlapping runs for the same branch/task.
6. Initialize `/tmp` or `$RUNNER_TEMP` logging before checkout.
7. Upload logs with `if: always()`.
8. Ensure task outputs are uploaded separately and only when valid.
9. Avoid broad `paths` patterns that allow unrelated documentation commits to retrigger the workflow.
10. Do not let a workflow commit changes to its own workflow file.

### Trigger a workflow when dispatch is unavailable

Use a unique marker file such as:

```text
.agents/connector-triggers/apply-patch-<unique-id>.txt
```

Configure the workflow `push.paths` to match only that exact marker or a tightly scoped marker directory. Create the marker once through the connector. The workflow's output commit must not change the marker path, preventing a loop.

Prefer one marker per intended run. Do not keep adding trigger files to a temporary PR after the task is complete. Close stale trigger-only PRs rather than merging them.

### Monitor a workflow

1. Record the event commit SHA when triggering.
2. Use `fetch_commit_workflow_runs` or the most specific available run lookup.
3. Fetch jobs with `fetch_workflow_run_jobs`.
4. Fetch detailed job logs with `fetch_workflow_job_logs`.
5. Fetch artifact metadata with `fetch_workflow_run_artifacts`.
6. Download both:
   - the dedicated log artifact;
   - the successful result/build artifact, when present.
7. Verify artifact digests, internal checksums, exact source commit, source status, and fixture/input closure before executing packaged binaries.

A successful workflow step summary is not enough to close a gate. Verify the artifacts and exact source authority.

### Re-run a failed workflow

1. Read the detailed log artifact first.
2. Classify the failure as:
   - workflow syntax/configuration;
   - checkout/ref race;
   - permissions/authentication;
   - environment/dependency;
   - deterministic implementation failure;
   - transient infrastructure failure.
3. Fix deterministic workflow defects before retrying.
4. Use `rerun_workflow_job` for one isolated failed job or `rerun_failed_workflow_run_jobs` for all failed jobs.
5. Do not retry a malformed workflow; it must be committed in a valid form first.

### Apply a large unified patch through Actions

Use `templates/apply-unified-patch.yml`.

1. Ensure the patch contains no `.github/workflows/**` changes.
2. Split the patch into connector-sized parts if necessary.
3. Commit:
   - ordered patch parts;
   - full patch SHA-256;
   - expected output blob manifest;
   - one unique trigger marker.
4. The workflow must:
   - concatenate parts in deterministic order;
   - verify the full patch digest;
   - reject workflow-file paths;
   - compare current output blob hashes with the expected manifest;
   - return success without applying when every output already matches;
   - run `git apply --check` before applying;
   - verify every output blob after applying;
   - commit and push only the intended result;
   - upload detailed logs unconditionally.
5. After success, compare the remote target blobs to the expected manifest through the connector.

A normal `git apply` failure does not prove the patch is missing. It may mean the patch was already applied or the base changed. Check expected output blobs first. `git apply --reverse --check` can support an already-applied diagnosis, but exact output hashes are authoritative.

### Verify whether a patch was already applied

1. Obtain the expected final Git blob SHA for every target path.
2. Fetch each current target file/blob from the branch.
3. Compare all current blob SHAs to expected values.
4. If every path matches, classify the patch as already present and do not apply it again.
5. If only some match, classify it as a partial or divergent state and investigate; do not force-apply.
6. Record the commit that first introduced the matching blobs when provenance matters.

### Close a stale workflow-trigger PR

A trigger PR is stale when:

- the intended source patch already landed elsewhere;
- its diff contains only markers, temporary workflow triggers, or no-op files;
- merging would add no required implementation state;
- leaving it open can continue to trigger workflows.

Procedure:

1. Fetch PR metadata and changed filenames.
2. Verify the intended output exists on the authoritative work branch.
3. Update the PR body/comment with the evidence.
4. Close without merging.
5. Leave the implementation PR open when it still owns active work.

## Failure and safety rules

- Never treat positional proximity as proof that two remote files, patches, or outputs are equivalent; compare hashes or canonical content.
- Never synthesize a successful workflow result when a command failed.
- Never weaken tests or validation merely to produce a green workflow.
- Never expose secrets through `set -x`, environment dumps, command arguments, URLs, or uploaded logs.
- Never use `pull_request_target` to check out and execute untrusted PR code under elevated permissions.
- Workflows from forks may receive read-only tokens and no secrets. Plan write operations accordingly.
- `GITHUB_TOKEN` permissions are explicit. Set `contents: write` only for workflows that must commit.
- Do not use broad force pushes. Prefer compare-and-swap ref updates and explicit branch authority.
- Keep generated logs outside the repository worktree so clean-source checks are meaningful.
- Keep successful result artifacts and unconditional diagnostic logs separate.

## Required completion report

End each task with:

- repository and authoritative ref;
- exact starting and ending commit SHAs;
- files, branches, PRs, comments, or labels changed;
- workflow run/job IDs when used;
- result and log artifact IDs, names, digests, and retention when available;
- checks actually executed and checks deliberately not executed;
- remaining risks or open gates;
- confirmation that temporary trigger PRs/workflows are closed or intentionally retained.

## Supporting material

- `references/COMMON_TASKS.md` — connector call sequences and detailed recipes.
- `references/PITFALLS.md` — failure modes learned from remote workflow operation.
- `references/TOOL_MAP.md` — action selection guide.
- `templates/logged-remote-task.yml` — mandatory logging baseline.
- `templates/apply-unified-patch.yml` — idempotent patch application workflow.
- `templates/PR_BODY.md` — remote-work PR evidence template.
- `scripts/split_patch.py` — deterministic patch chunking and digest generation.
