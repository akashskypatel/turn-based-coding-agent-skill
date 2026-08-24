# CB-CLOSEOUT

**Context class:** `conditional-turn`

## Load contract

Load only after required `CB-COMPILE` passes.

Required dependencies:
- `references/core/evidence.md`
- `references/core/recovery.md`

Conditional dependencies:
- `modules/unit-testing/MODULE.md` only if the TB plan itself requires resolving unit-test design/acceptance ambiguity.

Templates: load `templates/CODE_BUILD_REPORT.md` and `templates/TEST_PLAN.md` only now, because this state produces them.

Do not load CB-DRAFT/CB-APPLY/CB-COMPILE or TB execution/review procedures.

## Goal

Perform documentation-only Code + Build closeout and author the executable TB plan for the exact successfully compiled evidence commit/artifact.

## Required TB plan

Record:
- exact evidence commit/artifact;
- validation objectives and invariants;
- ordered tests/benchmarks/commands;
- fixtures, inputs, seeds, environment/dependencies;
- focused and broader regression scope;
- expected results and explicit acceptance criteria;
- benchmark baselines/repetitions where applicable;
- evidence to preserve;
- stop/blocker conditions;
- plan-defined rerun/nondeterminism rules.

## Forbidden

- implementation/test/benchmark/build-logic edits;
- new compilation;
- runtime tests/benchmarks.

## Exit

Update change docs, TODO, and handoff. Record evidence commit separately from any documentation-only handoff commit. Set the successor context to:

```yaml
load_next:
  - references/turns/TB-EXEC.md
conditional_modules:
  - trigger: GitHub artifact/workflow retrieval required
    path: modules/github-connector/MODULE.md
```

Do not preload TB-REVIEW or TB-PLAN.
