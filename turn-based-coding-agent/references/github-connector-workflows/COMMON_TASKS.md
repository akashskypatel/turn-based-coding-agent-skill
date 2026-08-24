# Common Task Recipes

Load `PATCH_APPLICATION.md` before any content write whose size is not clearly below 19 KB. Load `WORKFLOW_POLICY.md` for any GitHub Actions mutation/execution.

## 1. Orient to an existing PR

1. `get_pr_info(repository_full_name, pr_number)`.
2. Record base/head branches and SHAs, draft state, merge state, and title.
3. `list_pr_changed_filenames` for scope.
4. Fetch only the files or patches needed for the task.
5. Re-fetch PR metadata before final mutation to detect head movement.

## 2. Update multiple files atomically

Before creating blobs, compute UTF-8 size of each file content. Every individual `create_blob` payload must be `<=19 KB`.

Pseudo-call sequence:

```text
parent = fetch_commit(branch_head)
blobA = create_blob(contentA)  # <=19 KB
blobB = create_blob(contentB)  # <=19 KB
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

If one desired blob exceeds 19 KB, do not send it as one connector content write. Use the patch strategy or another project-approved transfer path.

## 3. Modify a workflow safely

1. Fetch repository workflow policy and all reusable workflows the caller will use.
2. Draft outside `.github/workflows/**` when practical.
3. Validate triggers, exact marker path, permissions, reusable inputs, concurrency, and source identity.
4. Compute caller permissions as the union required by all called reusable workflows/jobs.
5. Ensure no workflow step writes `.github/workflows/**`.
6. Put persistent logs outside the worktree and initialize them before checkout.
7. Upload logs under `if: always()`.
8. Validate the exact YAML against a current GitHub-workflow schema/configured validator.
9. Publish through the connector only after validation.
10. Trigger only after the active caller is re-fetched and verified.

## 4. Trigger through a marker commit

Use `TEMP_WORKFLOW_LIFECYCLE.md`.

Critical ordering:

1. publish and verify the temporary caller **without touching the marker**;
2. create/modify the exact marker in a separate later commit;
3. record that marker commit as the expected event SHA;
4. do not trigger repeatedly while waiting for run observability;
5. remove the workflow before deleting the marker during cleanup.

## 5. Troubleshoot a failed workflow

1. Resolve the exact run ID; do not infer push-run absence from an event-filtered commit lookup.
2. Fetch jobs/steps and complete workload logs.
3. Download the dedicated diagnostic log artifact.
4. Compare console logs and artifact logs.
5. Classify syntax/configuration, reusable permission/input, checkout/ref race, auth, environment, deterministic product, or transient infrastructure failure.
6. Fix deterministic workflow defects before retrying.
7. For temporary marker callers, commit the correction without touching the marker, verify it, then update the marker in a separate retry commit.
8. Never rerun an unchanged deterministic failure merely to see whether it passes.

## 6. Prepare and apply a connector patch

Use `PATCH_APPLICATION.md`, `scripts/split_patch.py`, and `templates/github-actions/apply-unified-patch.yml`.

Decision:

- all direct writes <=19 KB → direct connector writes;
- compressed Base64 patch <=19 KB → one payload write;
- larger encoded stream → deterministic <=19 KB fragments.

The application must verify encoded checksum, decoded patch checksum, base authority, `git apply --check`, `git diff --check`, exact intended changed paths, and expected output blobs when supplied.

## 7. Troubleshoot a patch that does not apply

1. Compare current blob hashes with expected final blob hashes.
2. If all match, classify already applied/no-op.
3. Verify payload/encoded and patch checksums before blaming `git apply`.
4. Verify current base/source authority.
5. Run `git apply --check`.
6. If only some expected outputs match, stop: branch is partial/divergent.
7. Never use three-way/reject-file application without exact final-scope/output verification.

## 8. Package a compile-only artifact

When a reusable compile workflow is configured, call it rather than duplicating its compile/cache/package implementation.

The workload must:

1. record exact checked-out SHA and ref relationship;
2. preserve clean source authority;
3. compile only approved targets;
4. execute no produced project binary;
5. package required binaries/libraries, source identity/archive, dependency revisions, configure/build logs, cache metadata, and checksum manifest;
6. upload result only when valid;
7. upload diagnostic logs regardless of outcome.

## 9. Run an artifact-only test turn

1. Download exact artifact.
2. Verify outer digest and recursive checksum manifest.
3. Verify source commit, clean status, dependency revisions, and fixture/input closure.
4. Extract without repairing content/permissions.
5. Execute packaged binaries directly without configuring/rebuilding.
6. Preserve raw logs and machine-readable results.
7. Treat zero-selected filters/timeouts as orchestration outcomes, not passes.
8. Do not impose a repository timeout on a required full-suite acceptance gate solely to cap elapsed runtime.

## 10. Cleanup a temporary workflow

Follow workflow-first order:

1. preserve run/log/artifact/source evidence;
2. delete/disable temporary workflow caller;
3. verify it is inactive/absent;
4. delete marker;
5. delete retained temporary patch/payload/observation files when allowed;
6. verify no temporary debris remains.

## 11. Recover from a stale `update_file` SHA

1. Re-fetch the same path on the same branch.
2. Compare new content to intended edit.
3. Rebase the replacement content deliberately.
4. Confirm replacement UTF-8 content is <=19 KB.
5. Call `update_file` with the new blob SHA.
6. Re-fetch and verify.
