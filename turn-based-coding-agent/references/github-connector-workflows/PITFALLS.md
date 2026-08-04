# Common Pitfalls and Avoidance

## Connector and repository state

### Assuming a connector file is a local file

A connector reference is not automatically available at `/mnt/data` or in a local checkout. Use connector reads, or explicitly download/copy through a supported action.

### Updating related files one by one

Sequential file commits can expose an inconsistent intermediate branch and generate many workflow runs. Use blobs/trees/commits for atomic multi-file changes.

### Blindly retrying `409` writes

`409` means the expected state changed. Re-fetch the file or branch head and rebuild the mutation.

### Force-updating a moving branch

A forced `update_ref` can discard other work. Prefer non-force compare-and-swap behavior.

## Workflow syntax and contexts

### Using `runner.temp` in root-level `env`

This can be rejected as an unrecognized named value. Use a static path such as `/tmp/task-logs`, use `$RUNNER_TEMP` inside `run`, or reference `${{ runner.temp }}` only in a context where GitHub permits it, such as an individual step input.

### Creating logs inside the worktree

This dirties source status and can accidentally enter commits or artifacts. Store activity logs under `/tmp` or the runner temp directory.

### Initializing logs after checkout

A checkout failure then leaves no diagnostic artifact. Create the log directory and metadata in the first step, before checkout.

### Uploading logs only on success

Use `if: always()`. A failure without a log artifact violates the evidence contract.

### Combining logs and result artifacts

A failed run may have no result package, but it must still have logs. Keep them separate.

### Broad push triggers

A workflow that commits files matching its own `paths` filter may retrigger repeatedly. Use exact unique marker paths or `workflow_dispatch`.

### Workflow self-modification

Do not apply patches touching `.github/workflows/**` from inside Actions. Update workflow files externally through the connector.

## Patch transport

### Treating `git apply` failure as proof of a missing change

The patch may already be applied. Compare final blob hashes first.

### Applying partial patches

A partial application can leave a branch that is neither old nor intended. Require digest verification, preflight, exact post-apply blob checks, and transactional commit behavior.

### Including workflow paths in implementation patches

This can fail due to token scope and creates a self-modifying workflow hazard. Separate workflow changes from source patches.

### Reconstructing chunks in nondeterministic order

Name parts with zero-padded numeric suffixes and sort using a stable locale before concatenation.

## Permissions and security

### Missing `contents: write`

A workflow that commits cannot push with a read-only token. Grant only the needed permission.

### Logging secrets with `set -x`

Do not trace authentication setup, secret expansion, signed URLs, or token-bearing commands. Disable tracing around sensitive operations.

### Using `pull_request_target` with untrusted code

Never execute a fork's head code under elevated base-repository permissions.

### Expecting fork PR workflows to push

Fork-triggered workflows commonly receive read-only tokens and no secrets.

## Evidence and closure

### Closing a turn from a green step summary

Verify exact source SHA, source status, artifact checksums, required contents, and the declared execution boundary.

### Claiming tests ran during compile-only work

Report exactly what ran and what did not. Build success is not runtime correctness.

### Leaving trigger-only PRs open

They can continue to produce noise or repeated workflows. Close them after the authoritative source result lands.

### Merging a stale trigger PR

A marker-only PR should not be merged merely because its workflow once performed useful work elsewhere.
