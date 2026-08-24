# CB-COMPILE

**Context class:** `conditional-turn`

## Load contract

Load only when `canonical_turn=Code + Build` and `subturn=CB-COMPILE`.

Required dependencies:
- `references/core/turn-boundaries.md`
- `references/core/evidence.md`
- `references/03-repository-workflow.md`

Conditional dependencies:
- `modules/github-connector/MODULE.md` only for remote compilation/Actions/artifact work.

Do not load engineering-guidelines, unit-testing, CB-DRAFT, or TB files during a normal compile pass.

## Goal

Compile the exact pushed source commit and collect build evidence. This subturn is read-only with respect to implementation/test/benchmark/build logic.

## Procedure

1. Verify the exact pushed commit to compile.
2. Inspect build scripts/workflows only as needed to ensure no runtime validation is hidden inside the compile step.
3. Compile all required affected targets and permitted compile-time/static checks.
4. Preserve build logs/artifacts and the first actionable error on failure.

## PASS

Record exact evidence commit/artifact and advance to `CB-CLOSEOUT` with `load_next: references/turns/CB-CLOSEOUT.md`.

## FAIL

Do not fix code here. Record the actionable failure, then return to `CB-DRAFT` with:

```yaml
load_next:
  - references/turns/CB-DRAFT.md
conditional_modules:
  - trigger: corrective implementation design
    path: modules/engineering-guidelines/MODULE.md
```

Draft the smallest corrective patch against the latest committed branch head, then repeat `CB-DRAFT -> CB-APPLY -> CB-COMPILE`.

## Forbidden

- source/test/benchmark/build-logic edits;
- runtime tests/benchmarks or produced-binary discovery/help execution;
- continuing to closeout after a failed required compile.
