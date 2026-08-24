# Test + Benchmark Turn

## Purpose

Validate the exact successfully built source commit using the Test + Benchmark plan produced by Code + Build, review the evidence, classify findings, and produce the proposed next Code + Build action plan. Do not edit implementation or validation logic.

A Test + Benchmark turn may run canonically as one turn or use the optional granular decomposition in `references/11-granular-subturns.md`:

```text
TB-EXEC -> TB-REVIEW -> TB-PLAN
```

Canonical mode must still satisfy the responsibilities represented by all three subturns.

## Entry checks

- Confirm the designated canonical turn is Test + Benchmark.
- Record execution mode: canonical | granular.
- If granular, confirm the exact active subturn.
- Confirm the implementation commit built successfully.
- Identify the exact built evidence commit and latest handoff commit.
- Verify the evidence commit is reachable from the handoff commit and only allowed documentation changed between them.
- Obtain artifacts built from the exact evidence commit.
- Read the live handoff and locate the authoritative Test + Benchmark plan drafted during Code + Build.
- Refuse to invent a replacement validation plan silently when the required plan is missing; record the process defect and recover the intended plan from authoritative project evidence when possible.
- When artifacts or workflow evidence come from GitHub Actions, read `references/10-github-connector-workflows.md`.
- When unit-test failures require fixture, expectation, assertion, isolation, or scope diagnosis, load `modules/unit-testing/MODULE.md` for analysis only.

## Test-plan authority

The Code + Build closeout plan is the runtime execution authority for this turn.

- Execute the plan in its declared order unless an explicit stop condition is reached.
- Record every deviation and its reason.
- Do not broaden validation scope ad hoc merely because additional tests are convenient.
- Plan-defined repetitions, seeds, and nondeterminism checks are allowed.
- If the plan is materially defective, preserve that finding for TB-REVIEW/TB-PLAN rather than editing test logic or compiling replacement code.

Use `templates/TEST_PLAN.md` as the standard plan shape.

## Artifact integrity gate

Before executing a packaged binary:

1. Download the exact declared artifact through the connector.
2. Verify the outer digest when supplied.
3. Verify the recursive checksum manifest.
4. Verify source commit, clean source status, dependency/submodule revisions, required binaries/libraries, and fixture/input closure.
5. Extract into an arbitrary directory.
6. Do not configure, compile, relink, patch, or regenerate code.

If integrity fails, classify infrastructure status separately and do not claim product pass or fail.

## Allowed work

- Retrieve compiled artifacts and detailed workflow logs.
- Execute the approved focused, regression, integration, full-suite, platform tests, and benchmarks.
- Run correctness, quality, performance, memory, and determinism benchmarks included in the plan.
- Collect logs, reports, traces, crash dumps, seeds, and outputs.
- Compare results with accepted baselines.
- Analyze unit-test design using `modules/unit-testing/MODULE.md` without editing test code.
- Update TODO, handoff, validation-result, and planning documents.
- Propose the next Code + Build action plan.

Granular mode narrows these permissions by TB-EXEC, TB-REVIEW, and TB-PLAN; follow `references/11-granular-subturns.md`.

## Forbidden work

- Modifying production behavior.
- Editing test or benchmark logic.
- Fixing build configuration.
- Weakening assertions or thresholds.
- Compiling a replacement source revision.
- Combining diagnosis with an implementation fix.

## Execution order

Follow the Code + Build test plan. The standard progression is:

1. Direct defect reproduction or focused behavior validation.
2. Focused subsystem tests.
3. Related regressions.
4. Integration tests.
5. Full suite.
6. Required platform validation.
7. Required benchmarks.

Record exact commit, artifact, commands, environment, filters, counts, duration, exit type, and evidence locations.

## Granular TB responsibilities

### TB-EXEC

Execute the approved plan and preserve raw evidence. Do not change code or convert findings into corrective implementation work. Exit with complete evidence or an explicit execution/infrastructure blocker.

### TB-REVIEW

Interpret TB-EXEC evidence against every acceptance criterion. Classify failures, identify evidence gaps, compare benchmark results, and document findings/confidence. Do not execute additional unplanned validation or edit code.

### TB-PLAN

Convert reviewed findings into phase status and a proposed next Code + Build plan. Each task must state required change, build verification, and future validation. Decide whether optional independent Review is skipped or requested.

## Unit-test diagnosis

For a failing unit test, use `modules/unit-testing/MODULE.md` to check whether:

- the asserted behavior is supported by an authoritative contract,
- the fixture actually creates the claimed scenario,
- the test belongs at unit scope,
- expected values are independently justified,
- mocks or test doubles distort production semantics,
- ordering, time, randomness, environment, or shared state can change the result,
- the assertion is too broad, too weak, or coupled to implementation details.

This analysis may change the proposed next-turn plan, but all source/test edits remain deferred to the next Code + Build turn.

## Benchmark execution

Compare against last known good, previous phase, quality thresholds, runtime/memory budgets, and determinism requirements from the test plan. Record inputs, repetition count, timing, memory, quality, variance, structural digests, and baseline differences.

Faster execution is not success when correctness or quality regresses.

## Remote evidence requirements

- Preserve every raw log and machine-readable result.
- Use the detailed workflow log artifact when diagnosing build or packaging failures.
- Record result and log artifact IDs, names, digests, source SHA, and retention when relevant.
- A green workflow summary does not prove artifact integrity or runtime correctness.
- Do not trigger a compile workflow from a Test + Benchmark turn to replace an invalid artifact.

## Failure classifications

Classify each failure as production implementation, structurally invalid fixture, incorrect expectation, infrastructure, performance regression, or nondeterminism. Preserve evidence and avoid over-claiming certainty.

## Exit requirements

- Every Test + Benchmark plan item has a result or explicit blocker.
- All requested validation results and deviations are recorded.
- Every failure is classified with evidence.
- Phase status is explicit: complete, incomplete, blocked, or regressed.
- A proposed next Code + Build plan exists or phase closure/next phase is explicitly recommended when all criteria pass.
- TODO records whether optional review is requested.
- The live handoff records the exact next canonical turn/subturn, evidence commit/artifact, authoritative or pending plan, missing procedure, and lessons.
- Every agent entry-point document still links to the handoff.

If review is skipped, TB-PLAN becomes authoritative. If requested, label it `proposed_pending_review`.

Use `templates/TEST_BENCHMARK_REPORT.md`. Use `templates/SUBTURN_REPORT.md` for granular subturn reports.
