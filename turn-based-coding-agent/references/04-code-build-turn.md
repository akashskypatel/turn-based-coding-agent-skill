# Code + Build Turn

## Purpose

Implement the active phase and prove that all affected targets compile. Runtime tests and benchmarks are forbidden in this turn.

## Entry checks

- Confirm the designated turn type is Code + Build.
- Read the authoritative next-action plan.
- If an optional Review turn occurred, use its plan instead of the earlier Test + Benchmark proposal.
- Confirm active branch, source commit, and clean starting state.
- Synchronize local, connector, and remote state as applicable.
- Read the live handoff first, then its referenced plan and evidence.
- When remote work uses `@GitHub` or Actions, read `references/10-github-connector-workflows.md` and the repository workflow policy.
- When adding, repairing, or materially changing unit tests, load the companion `unit-testing` skill before editing test logic.

## Allowed work

- Edit production code.
- Edit tests and benchmark definitions when the plan requires valid coverage changes.
- Edit build configuration.
- Edit diagnostics, TODO, and documentation.
- Compile libraries, applications, tests, benchmarks, plugins, and packaging targets.
- Run compile-time checks and static analysis.
- Use remote workflows to compile exact pushed commits.
- Commit and push changes.

## Forbidden work

- Running test binaries.
- Running benchmarks.
- Executing runtime validation hidden inside another script.
- Treating application smoke execution as a build step.
- Running produced binaries for help, list, discovery, fixture inspection, or version output when the turn forbids binary execution.
- Continuing into validation after the build succeeds.

Inspect build scripts and workflows before invoking them. Disable or separate embedded runtime test steps when necessary.

## Remote compile workflow contract

When compilation occurs through GitHub Actions:

1. Compile the exact pushed commit and verify checked-out SHA against the authoritative branch/ref.
2. Initialize detailed logs before checkout and always upload the dedicated log artifact.
3. Compile only the explicitly permitted targets.
4. Do not execute produced binaries.
5. Package binaries/libraries, exact source archive, source commit/status, dependency revisions, fixtures, configure/build logs, and recursive checksums.
6. Upload the result artifact only on success and separately from logs.
7. Record run, job, source SHA, artifact IDs, digests, and what did not run.

Use `templates/github-actions/logged-remote-task.yml` as the logging baseline.

## Implementation rules

The change must enforce documented domain invariants, apply to the supported input domain, preserve valid behavior, fail explicitly when safe completion is impossible, preserve useful diagnostics, and match existing architecture.

Do not introduce fixture recognition, test-only success paths, hard-coded golden output, unsupported tolerance inflation, environment-dependent bypasses, or success without required invariants.

Make surgical changes. Do not refactor or reformat unrelated code.

## Unit-test design integration

When unit tests are in scope, the companion `unit-testing` skill supplies the design standard for:

- defining the unit and observable contract,
- selecting focused scenarios and robust values,
- controlling external dependencies and nondeterminism,
- choosing real collaborators, fakes, stubs, or mocks,
- writing narrow actionable assertions,
- designing regression coverage that protects behavior rather than the fix implementation.

The companion skill does not authorize test execution in this turn.

## Test changes in this turn

Test code may change only to add intended coverage, correct a structurally invalid fixture, remove synthetic assumptions, or update expectations after an intentional documented contract change.

For a fixture correction, document the intended behavior, structural invalidity, corrected construction, proving assertion, and why production code should not accommodate the invalid fixture.

Do not run the changed tests in this turn.

## Build loop

When compilation fails:

1. Diagnose the first actionable error from the full build or workflow log artifact.
2. Determine whether active changes caused it.
3. Apply the smallest correct fix.
4. Update TODO when diagnosis changes.
5. Commit and push.
6. Verify synchronization.
7. Rebuild the exact pushed commit.

Continue until required builds succeed or a genuine external blocker is evidenced.

## Exit requirements

- Intended changes are committed and pushed.
- Required targets compile from the exact remote commit.
- Source status is clean.
- No tests or benchmarks ran.
- Required result and detailed-log artifacts are verified.
- The next Test + Benchmark commands and acceptance criteria are recorded.
- The live handoff contains exact resume guidance, references, missing procedure, and new failure-avoidance lessons.
- Every agent entry-point document still links to the handoff.

Use `templates/CODE_BUILD_REPORT.md`.
