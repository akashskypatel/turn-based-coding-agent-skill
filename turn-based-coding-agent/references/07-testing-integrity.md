# Testing Integrity and Generalization

## Organic validation

Tests must pass because implementation satisfies intended behavior. Never:

- Bypass assertions.
- Disable a failing test without an approved reason.
- Convert failures into warnings.
- Return synthetic success.
- Detect the test environment and skip production behavior.
- Skip difficult fixtures only in CI.
- Lower quality thresholds without evidence.
- Replace semantic checks with existence checks.
- Regenerate golden outputs without reviewing semantic differences.
- Change benchmark inputs solely to hide a regression.

## Test-versus-implementation diagnosis

When a test fails, separately establish:

1. The documented behavior.
2. The actual fixture state.
3. Whether the fixture creates the intended scenario.
4. The implementation result.
5. The assertion's relationship to the contract.

Do not assume production code is wrong merely because an assertion failed. Do not assume the test is wrong merely because fixing production code is difficult.

## Valid fixture correction

A test fixture may be corrected only when evidence shows that the original input cannot structurally exercise the claimed behavior.

A valid correction must:

- Preserve the test's stated purpose.
- Create the missing precondition naturally.
- Preserve or strengthen semantic assertions.
- Avoid embedding expected implementation output in the fixture.
- Include a regression explanation.

## Generalization review

For every proposed fix, ask:

- Which invariant does this enforce?
- Which class of valid inputs benefits?
- Which valid inputs could regress?
- Is behavior dependent on a name, index, ordering accident, seed, or fixture constant?
- Does the fix preserve deterministic behavior where required?
- Does failure remain explicit and diagnosable?

## Performance integrity

Do not trade correctness for benchmark success. Report correctness, output quality, runtime, memory, and variance separately.

## Evidence preservation

Retain sufficient evidence to reproduce failures:

- Exact source commit.
- Exact command and environment.
- Input or seed identity.
- Logs and stack traces.
- Output artifacts.
- Baseline revision and metrics.
