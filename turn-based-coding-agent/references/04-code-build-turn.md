# Code + Build Turn

## Purpose

Implement the active phase and prove that all affected targets compile. Runtime tests and benchmarks are forbidden in this turn.

## Entry checks

- Confirm the designated turn type is Code + Build.
- Read the authoritative next-action plan.
- If an optional Review turn occurred, use its plan instead of the earlier Test + Benchmark proposal.
- Confirm active branch, source commit, and clean starting state.
- Synchronize local and remote state.
- Read the live handoff first, then follow its referenced authoritative plan and evidence.
- Review relevant project documents and this turn protocol.

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
- Continuing into validation after the build succeeds.

Inspect build scripts and workflows before invoking them. Disable or separate embedded runtime test steps when necessary.

## Implementation rules

The change must:

- Enforce documented domain invariants.
- Apply to the supported input domain.
- Preserve valid behavior outside the failing scenario.
- Fail explicitly when safe completion is impossible.
- Preserve useful diagnostics.
- Match existing architecture and conventions.

Do not introduce:

- Filename, fixture, or dataset recognition.
- Test-only success paths.
- Hard-coded golden output.
- Unsupported tolerance inflation.
- Environment-dependent bypasses.
- Success without satisfying required invariants.

Make surgical changes. Do not refactor or reformat unrelated code.

## Test changes in this turn

Test code may be changed only to:

- Add coverage for intended behavior.
- Correct a fixture that cannot create its claimed scenario.
- Remove synthetic assumptions that contradict the contract.
- Update expectations after an intentional, documented contract change.

For a fixture correction, document:

1. Intended behavior.
2. Why the old fixture was structurally invalid.
3. How the new fixture creates the required condition.
4. Which assertion proves the intended behavior.
5. Why production code should not accommodate the invalid fixture.

Do not run the changed tests in this turn.

## Build loop

Build every affected target. When compilation fails:

1. Diagnose the first actionable error.
2. Determine whether active changes caused it.
3. Apply the smallest correct fix.
4. Update the TODO when diagnosis changes.
5. Commit and push.
6. Verify synchronization.
7. Rebuild the exact pushed commit.

Continue until required builds succeed or a genuine external blocker is evidenced.

## Exit requirements

- Intended changes are committed and pushed.
- Required targets compile from the exact remote commit.
- Working tree is clean.
- No tests or benchmarks were run.
- The next Test + Benchmark commands and acceptance criteria are recorded.
- The live handoff is updated with exact resume guidance, references, missing procedure, and newly learned failure-avoidance lessons.
- If updated after the authoritative build, it is committed as documentation-only and records both the built evidence commit and handoff commit.
- Every agent entry-point document still links to the handoff.

Use `templates/CODE_BUILD_REPORT.md` for the handoff.
