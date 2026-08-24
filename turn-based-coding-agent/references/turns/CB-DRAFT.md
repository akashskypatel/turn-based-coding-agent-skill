# CB-DRAFT

**Context class:** `conditional-turn`

## Load contract

Load only when `canonical_turn=Code + Build` and `subturn=CB-DRAFT`.

Required dependencies:
- `references/core/turn-boundaries.md`
- `references/core/evidence.md`
- `modules/engineering-guidelines/MODULE.md`

Conditional dependencies:
- `modules/unit-testing/MODULE.md` only when unit-test source is part of the patch.
- project architecture/contracts cited by the authoritative plan.

Do not load CB-APPLY/CB-COMPILE/CB-CLOSEOUT or TB files.

## Goal

Draft the actual implementation change as a plain reviewable patch against an exact base commit without mutating authoritative source.

## Procedure

1. Confirm exact branch/base commit and authoritative plan.
2. Surface material assumptions and unresolved contract questions.
3. Choose the simplest sufficient, generalized approach.
4. Draft only changes traceable to the objective, validation support, diagnostics, or build integration.
5. Include justified test-source changes when needed, but do not execute them.
6. Record intended files, invariant/behavior addressed, base commit, and expected diff scope.

## Forbidden

- applying the patch to authoritative source;
- compiling;
- runtime tests/benchmarks;
- encoded patch/archive as authoritative implementation;
- speculative features, unrelated refactors, or style drift.

## Exit

The patch is reviewable and tied to an exact base. Update handoff state to `CB-APPLY` with `load_next: references/turns/CB-APPLY.md` and only the conditional modules that state actually needs.
