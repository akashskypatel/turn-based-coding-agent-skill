# Common Pitfalls and Avoidance

## Connector and repository state

### Assuming a connector file is a local file

A connector reference is not automatically available in a local sandbox. Use connector reads or an explicit download/copy action.

### Exceeding the observed connector write ceiling

Historical agent work has observed individual content writes around/above 20 KB being silently truncated without an error. Treat 19 KB UTF-8 as a hard ceiling for each `create_file`, `update_file`, and `create_blob` content payload.

Preflight sizes and use `PATCH_APPLICATION.md` when one write would exceed the ceiling.

### Assuming an atomic tree removes the write limit

Atomic Git-data commits are useful for coherence, but each `create_blob` is still an individual connector content write and must remain <=19 KB.

### Updating related files one by one

Sequential commits can expose inconsistent intermediate branch state and trigger workflows repeatedly. Use atomic Git-data commits when each individual blob is safely sized.

### Blindly retrying `409` writes

`409` means expected state changed. Re-fetch file/branch authority and rebuild the mutation.

### Force-updating a moving branch

A forced ref update can discard other work. Prefer non-force compare-and-swap behavior.

### Creating unnecessary control branches

Work on the configured working branch. Create a temporary/control/staging branch only for a documented procedural blocker that cannot safely be resolved otherwise.

## Workflow syntax, reuse, and permissions

### Guessing reusable workflow inputs

Fetch the current reusable workflow and pass only inputs declared by `workflow_call.inputs`.

### Under-provisioning caller permissions because a nested job is skipped

Reusable workflow permission ceilings can be validated before runtime `if:` conditions. Compute the union required by every called reusable workflow/job, even conditionally skipped nested jobs.

### Using `runner.temp` in an unsupported context

Use a static `/tmp` path, `$RUNNER_TEMP` inside shell, or `${{ runner.temp }}` only where GitHub permits it.

### Creating logs inside the worktree

This dirties source status and can enter commits/artifacts. Store logs in runner temporary storage.

### Initializing logs after checkout

Checkout failure then leaves no durable diagnostics. Initialize logging first.

### Uploading logs only on success

Use `if: always()` and keep diagnostic logs separate from successful results.

### Broad push triggers

A workflow that commits a path matching its own broad trigger can retrigger. Use one exact unique marker path.

### Publishing malformed workflow YAML

Draft outside `.github/workflows/**` when practical and validate against a current GitHub workflow schema before publication.

### Workflow self-modification

Do not modify `.github/workflows/**` from inside Actions. Publish workflow changes externally through the connector.

## Run observability and triggering

### Treating empty commit-run lookup as proof no push run exists

Some connector run lookup surfaces can filter by event. For push-triggered workflows, use a run-ID observer or repository-wide run inventory before deciding a run is absent.

### Combining caller installation and first marker creation

The workflow may not be active early enough for the same commit's path trigger. Install/verify caller first; modify the marker in a separate later commit.

### Retrying the marker because no run ID appeared immediately

Delayed observability is not proof of missing execution. Query observer/repository-wide run inventory before retrying.

### Cleaning marker before workflow

Deleting a marker while the temporary caller is still active can trigger another run. Remove/disable the workflow caller first, then delete the marker.

## Patch transport

### Base64 line wrapping or fragment newlines

Compressed payload fragments must reconstruct the Base64 stream byte-for-byte. Do not add line wrapping, fragment newlines, whitespace, delimiters, or headers.

### Skipping the encoded-payload checksum

Verify the reconstructed encoded stream before Base64 decoding, then verify the decoded/decompressed patch checksum separately.

### Treating `git apply` failure as proof of a missing change

The patch may already be applied or the base may have moved. Compare expected final blobs and base authority first.

### Applying partial/fuzzy patches

Require checksum verification, `git apply --check`, transactional application, `git diff --check`, exact changed-path verification, and expected output checks. Do not accept partial, reject-file, or unverified three-way results.

### Including workflow paths in implementation patches

A workflow must not modify itself. Separate `.github/workflows/**` changes from patches applied inside Actions.

### Nondeterministic fragment order

Use zero-padded ordinal suffixes and a stable lexical order.

## Caching

### Per-run cache keys masquerading as compatibility keys

Do not append run IDs, source SHAs, timestamps, turn names, or retry numbers when a reusable compile workflow owns a stable compiler-cache compatibility key.

### Letting temporary callers own cache lineage

Reusable compile workflow policy owns cache schema/compatibility/versioning. Temporary callers provide task/source inputs only.

## Test execution

### Timing out a required full-suite acceptance run

Do not add a repository timeout whose purpose is to terminate the required full-suite semantic gate. A platform limit or explicit human cancellation is infrastructure/orchestration evidence, not pass/skip.

### Zero selected tests counted as success

A filter selecting zero tests is orchestration failure.

## Permissions and security

### Logging secrets with `set -x`

Do not trace token expansion, authenticated URLs, or secret-bearing arguments.

### Using `pull_request_target` with untrusted code

Never execute untrusted fork head code under elevated base-repository permissions.

### Expecting default `GITHUB_TOKEN` pushes to trigger follow-up workflows

GitHub normally suppresses recursive workflow creation from default-token pushes. Use an authorized token only when follow-up trigger semantics are intentionally required.

## Evidence and closure

### Closing from a green step summary

Verify exact source SHA, source status, artifact checksums, required contents, and execution boundary.

### Evidence upload failed after successful workload

Acceptance is incomplete. Required evidence must be retrievable.

### Leaving temporary workflow/marker/payload debris

Inspect configured temporary-state directories at start/end. Preserve durable workflows; clean temporary caller first, marker second, then payload/observation state.
