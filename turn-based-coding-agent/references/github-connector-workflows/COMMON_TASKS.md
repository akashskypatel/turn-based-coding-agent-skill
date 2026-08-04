# Common Task Recipes

## 1. Orient to an existing PR

1. `get_pr_info(repository_full_name, pr_number)`.
2. Record base/head branches and SHAs, draft state, merge state, and title.
3. `list_pr_changed_filenames` for scope.
4. Fetch only the files or patches needed for the task.
5. Re-fetch PR metadata before final mutation to detect head movement.

## 2. Update multiple files atomically

Pseudo-call sequence:

```text
parent = fetch_commit(branch_head)
blobA = create_blob(contentA)
blobB = create_blob(contentB)
tree = create_tree(
  base_tree_sha = parent.tree.sha,
  entries = [
    {path: pathA, mode: "100644", type: "blob", sha: blobA},
    {path: pathB, mode: "100644", type: "blob", sha: blobB}
  ])
commit = create_commit(message, tree.sha, parent.sha)
update_ref(branch, commit.sha, force=false)
```

Before `update_ref`, verify the branch still points to `parent.sha`. If it moved, rebuild on the new parent.

## 3. Modify a workflow safely

1. Fetch the existing workflow and repository policy.
2. Validate event triggers, path filters, permissions, and concurrency.
3. Ensure no workflow step writes `.github/workflows/**`.
4. Put persistent logs under `/tmp` or create them from `$RUNNER_TEMP` inside a shell step.
5. Do not use `${{ runner.temp }}` in root-level workflow `env`; context availability is key-specific and this form can make the workflow invalid.
6. Upload logs under `if: always()`.
7. Commit workflow changes through the connector.
8. Trigger only after GitHub accepts the workflow syntax.

## 4. Trigger through a marker commit

Use when no connector action dispatches `workflow_dispatch`.

Workflow trigger:

```yaml
on:
  push:
    branches: [agent/example]
    paths:
      - .agents/connector-triggers/task-123.txt
```

Then create that exact marker file through the connector. The workflow's result commit must not modify the marker.

Avoid:

```yaml
paths:
  - .agents/**
  - src/**
```

when the workflow itself commits under those patterns; that can cause repeated runs.

## 5. Troubleshoot a failed workflow

1. Resolve run and job IDs.
2. Fetch job steps to identify where it failed.
3. Fetch complete job logs.
4. Download the dedicated log artifact.
5. Compare console logs and artifact logs; artifact logs should contain task traps and final state omitted from summaries.
6. Classify the failure before editing anything.
7. Fix syntax or deterministic workflow defects in a new connector commit.
8. Re-run only after the workflow file is valid.

## 6. Troubleshoot a patch that does not apply

Failure:

```text
error: patch failed: path:line
error: path: patch does not apply
```

Do not immediately regenerate or force the patch.

1. Compare current blob hashes with expected final blob hashes.
2. If all match, the patch was already applied; return success/no-op.
3. If none match, run `git apply --check` against the intended base.
4. If reverse-check succeeds, inspect whether the branch contains a semantically equivalent change.
5. If only some match, stop: the branch is partially applied or divergent.
6. Never use three-way or reject-file application without a subsequent exact-output verification.

## 7. Package a compile-only artifact

The workflow must:

1. Record exact checked-out SHA and remote/ref relationship.
2. Verify a clean source status before configure/build.
3. Configure once.
4. Compile only the explicitly permitted targets.
5. Execute no produced binary.
6. Package:
   - binaries/libraries;
   - exact source archive;
   - source commit and source status;
   - submodule revisions;
   - required fixtures;
   - configure/build logs;
   - recursive checksum manifest.
7. Upload the package only on success.
8. Upload detailed workflow logs regardless of outcome.

## 8. Run an artifact-only test turn

1. Download the exact artifact.
2. Verify outer digest and recursive checksum manifest.
3. Verify exact source commit, clean source status, dependency revisions, and fixture closure.
4. Extract to an arbitrary directory.
5. Run packaged binaries directly without configuring or rebuilding.
6. Preserve every raw log and machine-readable result.
7. Upload or commit only reports and summaries; do not modify implementation during a test-only turn.

## 9. Close a stale trigger PR

1. Fetch PR metadata and changed filenames.
2. Confirm its intended source result already exists on the authoritative branch.
3. Confirm the PR contains only temporary marker/trigger files or no required source state.
4. Comment with commit/blob evidence.
5. Close without merging.

## 10. Recover from a stale `update_file` SHA

1. Re-fetch the same path on the same branch.
2. Compare the new content to the intended edit.
3. Rebase the replacement content manually if needed.
4. Call `update_file` with the new blob SHA.
5. Do not reuse an old SHA after another write to the same path.
