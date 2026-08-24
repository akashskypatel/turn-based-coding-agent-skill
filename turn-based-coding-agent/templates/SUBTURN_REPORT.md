# Granular Subturn Report

- Canonical turn: Code + Build | Test + Benchmark
- Subturn: CB-DRAFT | CB-APPLY | CB-COMPILE | CB-CLOSEOUT | TB-EXEC | TB-REVIEW | TB-PLAN
- Phase:
- Working branch:
- Starting source commit:
- Evidence commit, when applicable:
- Handoff/planning commit, when applicable:
- Result: PASS | FAIL | COMPLETE | BLOCKED

## Work Performed

-

## Evidence / Artifact References

-

## Scope Integrity

- Engineering-guidelines module loaded when required:
- Unit-testing module loaded when required:
- Unrelated changes introduced: no | explain
- Turn-boundary violations: none | explain

## Subturn-Specific State

### CB-DRAFT

- Patch base commit:
- Patch artifact/reference:
- Assumptions surfaced:
- Simpler alternatives considered:
- Intended files:
- Source mutated: no

### CB-APPLY

- Draft patch reference:
- Resulting commit:
- Resulting diff verified:
- Temporary patch disposition:
- Compile/test executed: none

### CB-COMPILE

- Exact pushed commit compiled:
- Build targets:
- Commands/workflows:
- Result:
- First actionable error on FAIL:
- Tests/benchmarks executed: none
- Next on PASS: CB-CLOSEOUT
- Next on FAIL: CB-DRAFT

### CB-CLOSEOUT

- Change documentation:
- Test plan: `templates/TEST_PLAN.md` or project equivalent
- Test plan evidence commit:
- Acceptance criteria recorded:
- Implementation/build/test logic changed: no
- Next: TB-EXEC or canonical Test + Benchmark

### TB-EXEC

- Test plan reference:
- Artifact identity verified:
- Commands executed:
- Deviations from plan:
- Raw evidence:
- Source/build/test logic changed: no

### TB-REVIEW

- Test plan criteria reviewed:
- Findings:
- Failure classifications:
- Evidence gaps:
- Source/test execution performed: none

### TB-PLAN

- Phase status:
- Proposed next Code + Build plan:
- Plan status: authoritative | proposed_pending_review
- Optional Review: skip | request
- Source/test execution performed: none

## Live Handoff

- Path:
- Updated next canonical turn:
- Updated next subturn:
- Exact resume instruction:
- New lesson recorded, if any:
