# Code + Build Turn

## Purpose

Implement the active phase, prove that all affected targets compile, document the change, and produce the executable Test + Benchmark plan for the exact compiled evidence commit. Runtime tests and benchmarks are forbidden in this turn.

A Code + Build turn may run canonically as one turn or use the optional granular decomposition in `references/11-granular-subturns.md`:

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|
```

Canonical mode must still satisfy the responsibilities represented by all four subturns.

## Entry checks

- Confirm the designated canonical turn is Code + Build.
- Record execution mode: canonical | granular.
- If granular, confirm the exact active subturn.
- Read the authoritative next-action plan.
- If an optional Review turn occurred, use its plan instead of the earlier Test + Benchmark proposal.
- Confirm active branch, source commit, and clean starting state.
- Synchronize local, connector, and remote state as applicable.
- Read the live handoff first, then its referenced plan and evidence.
- Load `modules/engineering-guidelines/MODULE.md` before drafting implementation changes.
- When remote work uses `@GitHub` or Actions, read `references/10-github-connector-workflows.md` and the repository workflow policy.
- When adding, repairing, or materially changing unit tests, load `modules/unit-testing/MODULE.md` before editing test logic.

## Allowed work

- Edit production code.
- Edit tests and benchmark definitions when the plan requires valid coverage changes.
- Edit build configuration.
- Edit diagnostics, TODO, handoff, reports, and documentation.
- Compile libraries, applications, tests, benchmarks, plugins, and packaging targets.
- Run compile-time checks and static analysis.
- Use remote workflows to compile exact pushed commits.
- Commit and push changes.
- Draft the mandatory next-turn Test + Benchmark plan.

Granular mode narrows these permissions further by subturn; follow `references/11-granular-subturns.md`.

## Forbidden work

- Running test binaries.
- Running benchmarks.
- Executing runtime validation hidden inside another script.
- Treating application smoke execution as a build step.
- Running produced binaries for help, list, discovery, fixture inspection, or version output when the turn forbids binary execution.
- Continuing into runtime validation after the build succeeds.

Inspect build scripts and workflows before invoking them. Disable or separate embedded runtime test steps when necessary.

## Engineering discipline

Use `modules/engineering-guidelines/MODULE.md` as the implementation standard:

- surface material assumptions,
- prefer the simplest sufficient design,
- keep the diff surgical,
- match existing style,
- avoid speculative behavior and unrelated cleanup,
- define build and future runtime success criteria before implementation.

Every changed line should trace to the active objective, required validation support, diagnostics, or build integration.

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

Do not refactor or reformat unrelated code.

## Unit-test design integration

When unit tests are in scope, `modules/unit-testing/MODULE.md` supplies the design standard for:

- defining the unit and observable contract,
- selecting focused scenarios and robust values,
- controlling external dependencies and nondeterminism,
- choosing real collaborators, fakes, stubs, or mocks,
- writing narrow actionable assertions,
- designing regression coverage that protects behavior rather than the fix implementation.

The module does not authorize test execution in this turn.

## Test changes in this turn

Test code may change only to add intended coverage, correct a structurally invalid fixture, remove synthetic assumptions, or update expectations after an intentional documented contract change.

For a fixture correction, document the intended behavior, structural invalidity, corrected construction, proving assertion, and why production code should not accommodate the invalid fixture.

For a defect, prefer authoring or preserving focused reproduction/regression coverage during this turn. Compile it with the required test targets, but do not execute it until Test + Benchmark.

## Build loop

### Canonical mode

When compilation fails:

1. Diagnose the first actionable error from the full build or workflow log artifact.
2. Determine whether active changes caused it.
3. Apply the smallest correct fix.
4. Update TODO when diagnosis changes.
5. Commit and push.
6. Verify synchronization.
7. Rebuild the exact pushed commit.

Continue until required builds succeed or a genuine external blocker is evidenced.

### Granular mode

`CB-COMPILE` never edits implementation code. On FAIL it records evidence and returns to `CB-DRAFT`, which produces a corrective patch against the latest committed branch head. Then repeat `CB-DRAFT -> CB-APPLY -> CB-COMPILE` until PASS or a genuine blocker.

## Mandatory Test + Benchmark plan

A Code + Build turn is incomplete until it produces an executable validation plan for the exact successfully compiled evidence commit/artifact.

Use `templates/TEST_PLAN.md` or an equivalent project-local plan. At minimum record:

- exact evidence commit and artifacts,
- validation objectives and intended behaviors/invariants,
- ordered tests/benchmarks/commands,
- fixtures, inputs, seeds, environment, and required dependencies,
- focused and broader regression scope,
- expected outcomes and explicit acceptance criteria,
- benchmark baselines/repetitions where applicable,
- evidence to preserve,
- stop/blocker conditions,
- plan-defined rerun or nondeterminism rules.

This plan is drafted in CB-CLOSEOUT when granular mode is used. In canonical mode it is still a required closeout responsibility.

## Exit requirements

- Intended changes are committed and pushed.
- Required targets compile from the exact remote commit.
- Source status is clean.
- No tests or benchmarks ran.
- Required result and detailed-log artifacts are verified.
- Change documentation is current.
- A concrete Test + Benchmark plan exists and references the exact evidence commit/artifact.
- The live handoff identifies the plan and exact next turn/subturn.
- The live handoff contains exact resume guidance, references, missing procedure, and new failure-avoidance lessons.
- Every agent entry-point document still links to the handoff.

Next canonical turn: Test + Benchmark.

When granular mode is enabled, the completed Code + Build sequence ends at CB-CLOSEOUT and the next subturn is TB-EXEC.

Use `templates/CODE_BUILD_REPORT.md`. Use `templates/SUBTURN_REPORT.md` for granular subturn reports.
