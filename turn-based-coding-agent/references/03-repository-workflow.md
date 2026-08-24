# Repository and Branch Workflow

## Access-mode routing

Determine the configured `repository_access_mode` first.

- `local`: use local Git for working-tree operations and the configured connector for remote state when helpful.
- `github_connector`: use `@GitHub` as the repository control plane; do not pretend connector file references are local files.
- `hybrid`: keep connector state and the local checkout aligned and record which side is authoritative for each operation.

For connector-only or hybrid work, load `references/10-github-connector-workflows.md`.

## Remote operations

Use the configured repository connector for repository orientation, branch inspection, file reads and writes, Git-data commits, workflow runs, artifacts, pull requests, issues, comments, labels, merges, and push verification when available.

Use a narrowly scoped GitHub Actions workflow only when computation or repository tooling cannot be performed directly through the connector. A workflow is an execution plane, not the source-of-truth control plane.

## Active branch tracking

Before implementation:

1. Update the base branch TODO with the active working branch and phase when project policy requires it.
2. Commit and push that tracking update.
3. Create the working branch from the exact resolved base commit.
4. Confirm the working branch contains the same recovery state.

During a phase, keep the working-branch TODO and live handoff current. Mirror essential recovery state to the base branch only when project policy requires it; do not merge unfinished implementation.

When granular subturns are enabled, TODO and handoff must record both the canonical turn and exact subturn.

## Connector-safe writes

- For one small text file, fetch the current blob SHA and use a compare-and-swap update.
- A `409` means state changed; re-fetch and intentionally rebase the edit.
- For coherent multi-file changes, prefer blobs, a base tree, one commit, and a non-forced ref update when available.
- If the branch moves before `update_ref`, reconstruct on the new parent. Never force a shared branch merely to bypass a race.
- Verify the resulting branch head and critical file contents after mutation.

## Draft patch artifacts

Granular `CB-DRAFT` intentionally produces the proposed source change as a plain reviewable patch before source mutation.

A draft patch:

- is tied to an exact base commit,
- is temporary implementation transport/review material,
- may be persisted only through a project-approved temporary artifact or agent-document mechanism when a separate agent must resume at CB-APPLY,
- must not become the permanent authority for implementation state,
- must not be encoded merely to bypass normal source commits,
- must be superseded by ordinary committed source files after CB-APPLY.

If project policy forbids persisting patch artifacts at all, CB-DRAFT may still be used for review but should proceed directly to CB-APPLY in the same agent context rather than creating an unrecoverable stop point.

When a patch is applied, verify the resulting ordinary source diff against the draft intent and remove/archive temporary patch transport according to project policy.

## Existing patch artifacts

When the user identifies existing unapplied patches as authoritative:

1. Create the working branch first.
2. Verify patch digest and target base.
3. Ensure the patch does not modify `.github/workflows/**` when it will be applied inside Actions.
4. Compare expected final blob hashes before application; an apply failure may mean the patch is already present.
5. Apply transactionally and verify every expected output blob.
6. Commit ordinary source files, not encoded patch parts, as final authority.
7. Remove or archive temporary trigger and patch transport files according to project policy.

Do not use encoded patches or archives as a permanent substitute for committed source changes.

## GitHub Actions requirements

Every created or modified workflow must follow the configured `github_workflow_policy` and, at minimum:

- initialize persistent logs before checkout;
- log exact run/ref/source metadata, tool versions, commands, exit codes, final source status, and relevant resource usage;
- upload detailed logs under `if: always()`;
- keep logs separate from successful result artifacts;
- use least-privilege permissions and narrow triggers;
- avoid secret-bearing command traces;
- never modify its own workflow files;
- preserve Code + Build versus Test + Benchmark boundaries and active granular subturn restrictions.

Use `templates/github-actions/logged-remote-task.yml` as the baseline.

## Commit discipline

- Commit coherent, reviewable progress regularly.
- Commit and push WIP ordinary source changes directly to the remote working branch when recoverability requires it.
- Do not mix unrelated changes.
- Record the reason for each change, not merely the files touched.
- Do not open a second PR when an existing PR already tracks the work branch.
- In granular mode, CB-APPLY establishes committed source authority before CB-COMPILE.

## Pre-build synchronization gate

Before every authoritative build:

1. Review the diff.
2. Remove accidental and unrelated changes.
3. Update the TODO and live handoff when the build changes resume state.
4. Commit all intended changes.
5. Push the working branch.
6. Verify local/connector and remote heads match.
7. Verify source status is clean.
8. Build the exact pushed commit.

Granular CB-COMPILE may not compile an uncommitted CB-DRAFT/CB-APPLY state.

## End-of-turn and end-of-subturn handoff commit

At the end of every canonical turn, update the live handoff as necessary and commit it with the turn report or planning records.

When granular mode creates a separate resumable subturn, update the live handoff at the end of that subturn as necessary so a context-free successor knows the exact next subturn and required artifact/reference.

When evidence applies to an earlier exact commit, record both:

- `evidence_commit`: exact revision compiled or validated.
- `handoff_commit`: later documentation-only revision containing current resume state.

The next turn/subturn starts from the handoff commit but retrieves or validates artifacts from the evidence commit. Verify no production, test, benchmark, or build-configuration files changed between them when the subturn forbids such changes.

Do not create a new historical handoff file per turn. Maintain one concise live document and rely on Git history and linked reports.

## Planning-only review commits

An optional Review turn or TB-PLAN documentation closeout may update TODO or planning documents only. Record `validated_source_commit` separately from later `planning_commit`.

## Merge gate

Merge a phase branch only when:

- The phase implementation is complete.
- Required build targets succeed.
- Required tests and benchmarks meet phase criteria.
- The optional Review turn, when used, has no unresolved blocking findings.
- Remaining failures are explicitly outside phase scope.
- TODO and documentation match resulting behavior.
- Temporary trigger workflows, marker files, and patch transport artifacts have an explicit final disposition.

After merge, record the merge commit, close the phase, and define the next phase.
