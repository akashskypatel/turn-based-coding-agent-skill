# Status, Recovery, Evidence, and Completion

## Authoritative TODO and live handoff

The root TODO tracks scope and task state. The live handoff is the concise first-read document for a new coding agent with no chat context. Keep both synchronized with branch state and turn reports.

Use `templates/TODO.md`, `templates/HANDOFF.md`, and `references/09-live-handoff.md`.

## Evidence rules

Every completion claim requires evidence:

- Build success: exact pushed commit and successful target results.
- Test success: exact command, commit, environment, and counts.
- Fixed regression: failing reproduction before the change and passing validation after it.
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

Report what is blocked, why, what was attempted, what is required, and the exact resume step.

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

## Turn transition rules

### After Code + Build

The next turn is always Test + Benchmark.

### After Test + Benchmark

- If review is skipped, its proposed plan becomes the authoritative Code + Build plan.
- If review is requested, the next turn is Review and its plan remains pending.

### After optional Review

The next turn is Code + Build using the review-approved or review-replaced authoritative plan.

## Minimal per-turn checklist

### Common

- Confirm phase, branch, turn type, and exact commit.
- Verify synchronization.
- Read the live handoff, then the relevant modules and referenced evidence.
- Keep changes scoped and TODO/handoff recovery state current.

### Code + Build

- Do not execute tests or benchmarks.
- Commit and push before authoritative builds.
- Build exact pushed commits.
- Record next validation commands.

### Test + Benchmark

- Do not edit implementation or validation logic.
- Validate the exact built commit.
- Preserve and classify failures.
- Produce a proposed next plan and review decision.

### Optional Review

- Confirm independence.
- Do not edit source or validation logic.
- Inspect primary evidence.
- Publish exactly one authoritative next plan.
