# Optional Independent Review Turn

## Purpose

Independently review the validated source revision, evidence, diagnosis, and proposed next Code + Build plan. The reviewer may change the plan but may not change source or validation logic.

This turn is optional.

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

The reviewer must not rely only on prior summaries. It must inspect the relevant diff, authoritative documents, exact build evidence, test results, benchmark results, and failure artifacts.

## Entry checks

- Record the exact `validated_source_commit`.
- Confirm the Test + Benchmark report is complete enough to review.
- Confirm the proposed plan is marked `proposed_pending_review`.
- Confirm reviewer independence.
- Read the live handoff first and verify its resume state against primary evidence.
- Verify repository and evidence references are accessible.

## Allowed work

- Inspect source and validation diffs read-only.
- Inspect build, test, benchmark, and diagnostic evidence.
- Challenge root-cause claims and classifications.
- Identify missing invariants, regressions, or scope errors.
- Approve the proposed plan unchanged.
- Amend, reorder, narrow, expand, or replace next-turn tasks.
- Add explicit build and next-validation acceptance criteria.
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
3. Is any task tailored to one fixture or artifact?
4. Are simpler, safer, or more surgical changes available?
5. Are relevant contracts or historical decisions missing?
6. Are test changes justified without weakening intended validation?
7. Are acceptance criteria observable and reproducible?
8. Are phase scope and merge criteria appropriate?
9. Does the plan preserve diagnostics, determinism, and supported behavior?
10. What should the next Test + Benchmark turn validate?

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

- `validated_source_commit` - the source revision reviewed.
- `planning_commit` - the documentation-only commit containing the authoritative plan.

## Exit requirements

- Review decision and evidence are recorded.
- One authoritative next Code + Build plan is identified.
- Superseded plans are clearly marked.
- Tasks include build checks and future validation criteria.
- No implementation or validation logic changed.
- The live handoff is updated to point to the review-approved authoritative plan and any new review lessons.
- It records the validated source commit separately from the documentation-only review/handoff commit.
- Every agent entry-point document still links to the handoff.

Use `templates/REVIEW_REPORT.md`.
