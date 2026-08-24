# Temporary GitHub Workflow Lifecycle

**Context class:** `conditional-deep-reference`

Load only when an agent must create a temporary GitHub Actions caller/trigger to execute or observe remote work.

This procedure generalizes the proven caller-install → marker-trigger pattern.

## Phase 0 — preflight

Before writing a workflow:

1. Read `WORKFLOW_POLICY.md` and the repository-specific workflow policy.
2. Fetch current versions of every reusable workflow the caller will invoke, including configured schema validator, observer, compile workflow, or recent-runs inventory as applicable.
3. Inspect configured temporary workflow, trigger-marker, observation, and payload locations. Do not reuse stale state from an earlier run.
4. Choose and record:
   - unique temporary caller path;
   - unique marker path;
   - stable observer label;
   - exact working branch;
   - PR number if one exists;
   - whether branch-file observation is disabled (default) or justified;
   - required payload/patch paths.
5. Default to a narrow `push` trigger on the exact working branch and exact marker path when connector dispatch is unavailable.
6. Compute caller permissions as the union required by all called reusable workflows/jobs.
7. Decide the exact source identity consumed by the workload. Any source, fixture, patch, or payload required by the workload must exist before the marker-trigger commit.

## Phase 1 — draft without triggering

Draft the caller outside `.github/workflows/**` when practical, validate it, then publish the exact validated content.

Default shape:

```yaml
name: <unique-name>

on:
  push:
    branches:
      - <working-branch>
    paths:
      - <exact-marker-path>

permissions:
  <union required by all reusable calls>

concurrency:
  group: <stable-unique-group>
  cancel-in-progress: false

jobs:
  observe:
    uses: <configured-run-observer>
    with:
      <declared inputs only>
    secrets: inherit

  workload:
    # inline job OR reusable-workflow call
```

Rules:

- reusable-call jobs use `uses:` syntax and must not also define `runs-on:`/`steps:`;
- pass only inputs declared by `workflow_call`;
- keep observer independent of workload so run ID can surface even if workload fails;
- default branch-file observation off;
- compare permissions/inputs against current reusable definitions immediately before publication;
- validate YAML before it becomes active workflow authority.

## Phase 2 — install caller

1. Commit the caller and any payload/source files that must exist before execution.
2. **Do not create or modify the marker in this commit.**
3. Record caller-install commit SHA.
4. Re-fetch the active caller and verify:
   - exact branch filter;
   - exact unique marker path;
   - observer placement/path/inputs;
   - `secrets: inherit` when required;
   - permission union;
   - workload reusable path/inputs;
   - no unintended broad trigger.
5. Re-fetch required payload/source and verify branch authority.

The caller-install commit is not the execution trigger.

## Phase 3 — trigger exactly once

1. Create or modify the exact marker in a separate later commit.
2. Record marker-trigger commit SHA.
3. For normal push callers, this is the expected `github.sha`.
4. After the trigger commit, avoid additional repository writes until the observer reports the run ID.
5. If branch-file observation is enabled, do not advance the branch until that observer job completes/fails.
6. Trigger once. Do not repeatedly edit the marker because observability is delayed.

## Phase 4 — obtain run ID

1. Read the configured observer channel.
2. Verify observer event/source SHA equals the marker-trigger commit.
3. Record numeric workflow **run ID**; distinguish it from workflow-definition, job, artifact, and commit IDs.
4. Do not use an event-filtered commit-run lookup as proof of absence for push runs.
5. If observer output is missing, query repository-wide workflow runs through the connector or configured recent-runs inventory before considering a retry.

## Phase 5 — observe and collect evidence

1. Fetch jobs for the exact run ID.
2. Confirm expected observer/workload jobs exist; startup failure/no runnable jobs is orchestration failure.
3. Wait for workload terminal conclusion; observer completion is not workload completion.
4. Fetch exact workload job logs.
5. Fetch expected result and diagnostic artifacts.
6. Verify source identity from observer and workload/package metadata.
7. Record run ID, workload job ID, source SHA, artifact IDs/digests, terminal conclusion, and turn-boundary metadata.

## Phase 6 — deterministic retry

Do not trial-and-error retry.

- Invalid workflow/startup failure: diagnose YAML, reusable inputs, and caller permission ceiling first.
- Commit caller correction without touching the marker.
- Re-fetch and verify corrected caller.
- Modify marker in a separate later commit for one diagnosed retry.
- If workload started and failed, inspect exact logs first and change only the diagnosed workflow/payload/source defect.
- Never combine caller correction and marker triggering.
- Never rerun an unchanged deterministic failure just to see if it passes.

## Phase 7 — cleanup in workflow-first order

Cleanup starts only after run/log/artifact/source evidence is preserved.

1. Re-read current branch head.
2. Fetch temporary caller/marker/payload/observation files and current blob SHAs.
3. **Delete/disable the temporary workflow caller first.**
4. Verify caller is no longer active.
5. Delete marker only after caller removal is branch authority.
6. Delete temporary payload/patch fragments when retention permits.
7. Delete temporary branch-observation files.
8. Re-inspect temporary-state locations and verify no debris remains.
9. Do not delete remote result/log artifacts that remain authoritative evidence.

Deleting the marker before the caller can retrigger the workflow; workflow-first cleanup is mandatory.

## Phase 8 — closeout

1. Verify final working-branch head.
2. Verify temporary caller, marker, and observation files are absent.
3. Verify durable reusable workflows remain present and unchanged except for authorized durable edits.
4. Update handoff/TODO/report state.
5. If a final PR summary/comment is required by project policy, make it after all repository mutations are complete.
