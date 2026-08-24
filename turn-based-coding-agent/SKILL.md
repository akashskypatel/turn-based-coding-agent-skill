---
name: turn-based-coding-agent
description: Production-harden software through separated code-and-build, test-and-benchmark, and optional independent-review turns with optional granular subturn control, recoverable Git workflow, evidence-based planning, and integrated engineering and unit-test guidance.
---

# Turn-Based Coding Agent

Use this skill for multi-turn implementation, remediation, or production-hardening work where code changes and runtime validation must remain separate and recoverable.

## Authoritative canonical cadence

```text
Code + Build -> Test + Benchmark -> [Optional Review] -> Code + Build
```

The Review turn is optional:

- If skipped, the Test + Benchmark turn's next-action plan is authoritative.
- If used, the independent Review turn may approve, amend, reorder, narrow, expand, or replace that plan.
- A Review turn does not modify production code, test logic, benchmark logic, or build configuration.

Never combine canonical turn types.

## Optional granular execution

Code + Build and Test + Benchmark may each be decomposed into smaller resumable subturns without changing their canonical authority:

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

TB-EXEC -> TB-REVIEW -> TB-PLAN -> [Optional Review]
```

- `CB-COMPILE` PASS is required before `CB-CLOSEOUT`.
- On compile failure, return to `CB-DRAFT`, produce the smallest corrective patch, re-apply, and recompile.
- Every Code + Build turn, canonical or granular, must close with an explicit Test + Benchmark plan.
- When granular mode is used, each subturn is a valid handoff/resume boundary and must leave TODO/handoff state sufficient for a context-free successor.

Read `references/11-granular-subturns.md` whenever granular execution is enabled.

## Non-negotiable rules

1. Implement domain-correct, generalized behavior. Never special-case one fixture, file, dataset, platform, or benchmark input.
2. A Code + Build turn may edit and compile, but may not run tests or benchmarks.
3. A Test + Benchmark turn may execute validation, but may not edit implementation, test, benchmark, or build logic.
4. An optional Review turn must be performed by an independent agent or fresh review context and may change only the next-turn plan and planning records.
5. Build and validate exact pushed commits. Record commit identities with all evidence.
6. Keep the root TODO, live handoff, canonical turn, and granular subturn state current.
7. Maintain a concise, version-controlled handoff that lets a new agent resume without chat context.
8. Never weaken validation to conceal a product defect.
9. When the repository is available only through `@GitHub`, use the connector as the control plane and a narrowly scoped GitHub Actions workflow only as the remote execution plane.
10. Every created or modified GitHub Actions workflow must retain detailed activity on success and failure and always upload a separate diagnostic log artifact.
11. Load `modules/engineering-guidelines/MODULE.md` before drafting/applying implementation changes and when reviewing implementation plans.
12. When unit-test design, repair, diagnosis, or review is in scope, load `modules/unit-testing/MODULE.md`. Its rules supplement this skill but never override the active turn boundary or `references/07-testing-integrity.md`.
13. A Code + Build turn is incomplete until a concrete Test + Benchmark plan exists for the exact compiled evidence commit/artifact.

## Progressive task index

Read only the modules needed for the current operation.

### First use or project reset

Read:

- `references/01-project-configuration.md`
- `references/02-initialization.md`
- `references/03-repository-workflow.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `modules/engineering-guidelines/MODULE.md`
- `references/10-github-connector-workflows.md` when remote work uses `@GitHub` or GitHub Actions
- `references/11-granular-subturns.md` when granular/per-turn decomposition is configured

### Code + Build turn

Read:

- `references/03-repository-workflow.md`
- `references/04-code-build-turn.md`
- `references/07-testing-integrity.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `modules/engineering-guidelines/MODULE.md`
- `references/11-granular-subturns.md` when this CB turn is decomposed
- `references/10-github-connector-workflows.md` when the build or source changes are remote
- `modules/unit-testing/MODULE.md` when adding, changing, or repairing unit tests

### Test + Benchmark turn

Read:

- `references/05-test-benchmark-turn.md`
- `references/07-testing-integrity.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `references/11-granular-subturns.md` when this TB turn is decomposed
- `references/10-github-connector-workflows.md` when retrieving Actions artifacts or diagnosing remote runs
- `modules/unit-testing/MODULE.md` when classifying unit-test fixture, expectation, isolation, scope, or assertion validity

### Optional independent Review turn

Read:

- `references/06-optional-review-turn.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `modules/engineering-guidelines/MODULE.md`
- `references/10-github-connector-workflows.md` when remote PR, workflow, or artifact evidence is reviewed
- `modules/unit-testing/MODULE.md` when unit-test design is part of the reviewed next-turn plan

## Integrated engineering-guidelines module

`modules/engineering-guidelines/MODULE.md` is an internal module distilled from the Karpathy-guidelines skill and examples referenced in its attribution file. It makes these behaviors part of implementation planning and review:

- surface material assumptions before coding;
- prefer the simplest sufficient solution;
- make surgical, style-consistent changes;
- define observable success criteria and verification before implementation;
- avoid speculative abstractions, drive-by refactors, style drift, and vague all-at-once changes.

The module adapts test-first examples to this skill's strict turn separation: reproduction/regression test source may be authored and compiled in Code + Build, but runtime execution waits for Test + Benchmark.

## Integrated unit-testing module

`modules/unit-testing/MODULE.md` supplies research-backed guidance for contract-first unit-test design, scenario selection, dependency isolation, test-double choice, assertion quality, regression-test design, and test review.

The separation of responsibilities is strict:

- the turn workflow controls **when** test code may change or execute;
- the unit-testing module controls **how** unit tests should be designed and reviewed;
- `references/07-testing-integrity.md` controls test-versus-implementation diagnosis and prohibits synthetic validation.

## Remote GitHub routing

When no trusted local checkout is available:

1. Resolve repository, branch, commit, PR, and file authority with `@GitHub`.
2. Prefer direct connector reads and writes for repository metadata, small text changes, branches, commits, PRs, comments, labels, logs, and artifacts.
3. Use Git blobs, trees, commits, and non-forced ref updates for coherent multi-file changes when available.
4. Use GitHub Actions only for computation or repository operations the connector cannot perform directly.
5. Load `references/10-github-connector-workflows.md`, then the focused task or pitfall reference it identifies.
6. Never let a remote workflow blur the active turn/subturn boundary.

## Included templates

- `templates/PROJECT_CONFIG.md` - project-specific values, execution mode, commands, connector mode, and workflow policy.
- `templates/TODO.md` - authoritative progress and recovery tracker.
- `templates/HANDOFF.md` - concise live context for a context-free successor agent.
- `templates/CODE_BUILD_REPORT.md` - canonical Code + Build report.
- `templates/TEST_PLAN.md` - mandatory Code + Build closeout plan for the next Test + Benchmark turn.
- `templates/TEST_BENCHMARK_REPORT.md` - canonical validation report.
- `templates/SUBTURN_REPORT.md` - granular subturn state/report template.
- `templates/REVIEW_REPORT.md` - optional independent review decision.
- `modules/unit-testing/templates/UNIT_TEST_PLAN.md` - unit-test design plan when the test surface is non-trivial.
- `modules/unit-testing/templates/UNIT_TEST_REVIEW.md` - structured unit-test quality review.
- `templates/github-actions/logged-remote-task.yml` - mandatory logging baseline for bounded remote work.
- `templates/github-actions/apply-unified-patch.yml` - idempotent large-patch application with output verification.
- `templates/github-actions/PR_BODY.md` - remote workflow and artifact evidence template.

## Start rule

Before implementation begins:

1. Resolve project configuration, including repository access, canonical/granular execution policy, and GitHub workflow policy.
2. Inspect repository and historical evidence.
3. Create or normalize root TODO and live handoff.
4. Link the handoff from every agent entry-point document.
5. Report current status and phase boundaries.
6. Create a dedicated working branch.
7. Begin with Code + Build; when granular mode is active, begin with CB-DRAFT.
