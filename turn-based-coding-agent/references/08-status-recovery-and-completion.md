# Status, Recovery, Evidence, and Completion

## Authoritative TODO and live handoff

The root TODO tracks scope and task state. The live handoff is the concise first-read document for a new coding agent with no chat context. Keep both synchronized with branch state, canonical turn, granular subturn when used, and turn/subturn reports.

Use `templates/TODO.md`, `templates/HANDOFF.md`, and `references/09-live-handoff.md`.

## Evidence rules

Every completion claim requires evidence:

- Build success: exact pushed commit and successful target results.
- Test success: exact command, commit, environment, and counts.
- Fixed regression: trustworthy failing reproduction before the change and passing validation afterward, unless authoritative prior evidence already establishes the failure.
- Performance improvement: comparable benchmark measurements and variance.
- Generalized implementation: invariant-based explanation and representative coverage.
- Completed phase: all phase criteria satisfied.

Focused tests alone do not establish production readiness.

## Blockers

A blocker is valid only when progress cannot continue without external information, access, or an unavailable required environment.

Before declaring a blocker:

1. Search repository documentation and notes.
2. Inspect CI and build definitions.
3. Review previous evidence.
4. Attempt the safest non-destructive path.
5. Record exact failure evidence.

Report what is blocked, why, what was attempted, what is required, and the exact resume step/subturn.

## Phase completion

A phase is complete only when:

- Intended behavior is implemented.
- Required targets compile.
- Focused and related regression tests pass.
- Required integration and platform tests pass.
- Benchmarks meet accepted correctness and performance criteria.
- No fixture-specific workaround exists.
- Diagnostics remain accurate.
- TODO, live handoff, and documentation reflect final behavior.
- Changes are committed and pushed.
- Optional review findings, when review was used, are resolved.
- Branch policy permits merge.

## Project production readiness

The complete project additionally requires:

- Full-suite success.
- Representative benchmark coverage.
- Supported-platform validation.
- Failure-path validation.
- Required determinism.
- Acceptable memory and performance characteristics.
- No unresolved critical TODO items.
- Recoverable repository state with an accurate linked handoff.

## Execution-mode state

Project configuration chooses `canonical`, `granular`, or `per_turn` execution. When granular mode is active, TODO/handoff must record:

- canonical turn,
- current/last completed subturn,
- exact next subturn,
- source/evidence/handoff commits,
- required patch/test-plan/artifact reference.

Use `references/11-granular-subturns.md`.

## Turn transition rules

### Canonical Code + Build

Code + Build may close only after required compilation succeeds **and an explicit Test + Benchmark plan has been drafted** for the exact compiled evidence commit/artifact.

The next canonical turn is Test + Benchmark.

### Granular Code + Build

- CB-DRAFT -> CB-APPLY
- CB-APPLY -> CB-COMPILE
- CB-COMPILE PASS -> CB-CLOSEOUT
- CB-COMPILE FAIL -> CB-DRAFT
- CB-CLOSEOUT -> TB-EXEC

CB-CLOSEOUT requires change documentation and the mandatory TB plan.

### Canonical Test + Benchmark

- Execute the Code + Build test plan.
- Review/classify evidence.
- Produce the proposed next Code + Build plan.
- If review is skipped, that plan becomes authoritative.
- If review is requested, next canonical turn is Review and the plan remains pending.

### Granular Test + Benchmark

- TB-EXEC -> TB-REVIEW
- TB-REVIEW -> TB-PLAN
- TB-PLAN -> Code + Build when review is skipped
- TB-PLAN -> Optional Review when review is requested

### After optional Review

The next turn is Code + Build using the review-approved or review-replaced authoritative plan. If execution policy is granular, resume at CB-DRAFT.

## Minimal per-turn checklist

### Common

- Confirm phase, branch, canonical turn, granular subturn when applicable, and exact commit.
- Verify synchronization.
- Read the live handoff, then the relevant modules and referenced evidence.
- Keep changes scoped and TODO/handoff recovery state current.

### Code + Build

- Load `modules/engineering-guidelines/MODULE.md` before implementation.
- Do not execute tests or benchmarks.
- Commit and push before authoritative builds.
- Build exact pushed commits.
- Produce a Test + Benchmark plan before closeout.

### Test + Benchmark

- Do not edit implementation or validation logic.
- Validate the exact built commit/artifact using the authored test plan.
- Preserve and classify failures.
- Produce a proposed next plan and review decision.

### Optional Review

- Confirm independence.
- Load `modules/engineering-guidelines/MODULE.md`.
- Do not edit source or validation logic.
- Inspect primary evidence and test plan.
- Publish exactly one authoritative next plan.
