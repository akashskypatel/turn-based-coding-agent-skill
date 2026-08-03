# Repository and Branch Workflow

## Remote operations

Use the configured repository connector for remote branch inspection, workflow dispatch, artifact retrieval, pull requests, merges, and push verification when available. Use local Git for working-tree operations.

## Active branch tracking

Before implementation:

1. Update the base branch TODO with the active working branch and phase.
2. Commit and push that tracking update.
3. Create the working branch from the updated base commit.
4. Confirm the working branch contains the same recovery state.

During a phase, keep the working-branch TODO and live handoff current. Mirror essential recovery state to the base branch without merging unfinished implementation.

## Existing patch artifacts

When the user identifies existing unapplied patches as authoritative:

1. Create the working branch first.
2. Apply patches to the working tree.
3. Review all resulting source changes.
4. Resolve conflicts normally.
5. Commit ordinary source files.
6. Push normal commits.

Do not use encoded patches, patch blobs, or archives as a substitute for committing source changes. Do not stage or push new WIP as encoded patches.

## Commit discipline

- Commit coherent, reviewable progress regularly.
- Commit and push WIP directly to the remote working branch when recoverability requires it.
- Do not mix unrelated changes.
- Record the reason for each change, not merely the files touched.

## Pre-build synchronization gate

Before every authoritative build:

1. Review the diff.
2. Remove accidental and unrelated changes.
3. Update the TODO and live handoff when the build changes the resume state.
4. Commit all intended changes.
5. Push the working branch.
6. Verify local and remote heads match.
7. Verify the working tree is clean.
8. Build the exact pushed commit.


## End-of-turn handoff commit

At the end of every turn, update the live handoff as necessary and commit it with the turn report or planning records. The handoff must be part of ordinary version control on the active branch.

When the build, tests, or benchmarks already produced evidence for an earlier exact commit, use a documentation-only transition commit rather than claiming the evidence applies to the later handoff commit. Record both:

- `evidence_commit`: exact revision compiled or validated.
- `handoff_commit`: later documentation-only revision containing the current resume state.

The next turn starts from the handoff commit but retrieves or validates artifacts from the recorded evidence commit. It must verify that no production, test, benchmark, or build-configuration files changed between those commits.

Do not create a new historical handoff file per turn. Maintain one concise live document and rely on Git history and linked turn reports for chronology.

If the turn produces no change to resume context, verify the handoff is still accurate and record that verification in the turn report; do not add filler.

## Planning-only review commits

An optional Review turn may update TODO or planning documents only.

When such a commit is created, record both:

- `validated_source_commit`: the source revision whose build, tests, and benchmarks were reviewed.
- `planning_commit`: the later documentation-only revision containing the authoritative next plan.

The next Code + Build turn begins from the planning commit but must preserve the validated source identity in its handoff.

## Merge gate

Merge a phase branch into the base branch only when:

- The phase implementation is complete.
- Required build targets succeed.
- Required tests and benchmarks meet phase criteria.
- The optional Review turn, when used, has no unresolved blocking findings.
- Remaining failures are explicitly outside phase scope.
- TODO and documentation match the resulting behavior.

After merge, record the merge commit, close the phase, and define the next phase.
