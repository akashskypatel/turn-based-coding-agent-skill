# Optional Independent Review Turn

## Purpose

Independently review the validated source revision, evidence, diagnosis, and proposed next Code + Build plan. The reviewer may change the plan but may not change source or validation logic.

This turn is optional and remains canonical; it is not decomposed into CB/TB subturns.

## When to use it

Use an independent Review turn when requested by the user or when it provides meaningful risk reduction, such as:

- A high-impact or security-sensitive change.
- Broad architectural changes.
- Ambiguous or disputed failure diagnosis.
- Multiple interacting regressions.
- A phase merge or production-readiness gate.
- A proposed test-fixture or contract change.
- Significant performance or determinism regressions.

Skip it for low-risk, well-evidenced changes when the configured review policy does not require it.

## Independence requirement

The reviewer should be a separate agent, fresh session, or context that did not author the implementation or primary validation report.

The reviewer must not rely only on prior summaries. It must inspect the relevant diff, authoritative documents, exact build evidence, Test + Benchmark plan, test results, benchmark results, and failure artifacts.

## Entry checks

- Record the exact `validated_source_commit`.
- Confirm the Test + Benchmark report/TB-REVIEW findings and TB-PLAN are complete enough to review.
- Confirm the proposed plan is marked `proposed_pending_review`.
- Confirm reviewer independence.
- Read the live handoff first and verify its resume state against primary evidence.
- Verify repository and evidence references are accessible.
- Load `modules/engineering-guidelines/MODULE.md` to challenge assumptions, complexity, scope, and verifiability.
- When unit-test design, fixture validity, expectation correctness, isolation, or mocking strategy is under review, load `modules/unit-testing/MODULE.md`.

## Allowed work

- Inspect source and validation diffs read-only.
- Inspect build, test-plan, test, benchmark, and diagnostic evidence.
- Challenge root-cause claims and classifications.
- Review whether the proposed implementation is simple, surgical, assumption-aware, and verifiable.
- Review unit-test quality with `modules/unit-testing/MODULE.md` without editing tests.
- Identify missing invariants, regressions, or scope errors.
- Approve the proposed plan unchanged.
- Amend, reorder, narrow, expand, or replace next-turn tasks.
- Add explicit build and next-validation acceptance criteria.
- Decide whether the next Code + Build turn should run canonically or granularly when project policy is `per_turn`.
- Update TODO and planning documents only.
- Commit and push a documentation-only planning commit when repository tracking requires it.

## Forbidden work

- Editing production code.
- Editing tests, fixtures, assertions, or benchmarks.
- Editing build configuration.
- Compiling code.
- Running tests or benchmarks.
- Claiming a defect is fixed.
- Merging the phase.

## Review questions

1. Does the evidence support each failure classification?
2. Does the proposed correction address root cause rather than symptoms?
3. Which assumptions does the plan make, and are they supported by evidence?
4. Is there a materially simpler or more surgical correction?
5. Is any task tailored to one fixture or artifact?
6. Are unrelated refactors, style changes, abstractions, or speculative features being introduced?
7. Are relevant contracts or historical decisions missing?
8. Are test changes justified without weakening intended validation?
9. For unit tests, is the scenario focused, deterministic, behavior-oriented, and using the right collaborator fidelity/test level?
10. Does every proposed task have observable build and future validation criteria?
11. Are phase scope and merge criteria appropriate?
12. Does the plan preserve diagnostics, determinism, and supported behavior?
13. What should the next Test + Benchmark plan validate?

## Decision states

### Approved

The proposed plan becomes authoritative unchanged.

### Approved with amendments

The reviewer publishes a revised authoritative plan. The earlier proposal is retained as historical evidence but must not be followed.

### Rejected and replaced

The reviewer explains why the proposed diagnosis or plan is unsound and publishes a replacement plan.

### Insufficient evidence

The reviewer cannot approve a code plan. It may define evidence-preservation or instrumentation work for the next Code + Build turn, followed by explicit validation requirements.

## Planning commits

A review planning commit may modify only TODO and planning documents. Record:

- `validated_source_commit` — source revision reviewed.
- `planning_commit` — documentation-only commit containing the authoritative plan.

## Exit requirements

- Review decision and evidence are recorded.
- One authoritative next Code + Build plan is identified.
- Superseded plans are clearly marked.
- Tasks include build checks and future validation criteria.
- The selected next Code + Build execution mode/subturn is explicit when granular/per-turn control is used.
- No implementation or validation logic changed.
- The live handoff points to the review-approved authoritative plan and any new review lessons.
- It records validated source commit separately from the documentation-only review/handoff commit.
- Every agent entry-point document still links to the handoff.

Use `templates/REVIEW_REPORT.md`.
