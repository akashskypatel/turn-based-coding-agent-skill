# CB-APPLY

**Context class:** `conditional-turn`

## Load contract

Load only when `canonical_turn=Code + Build` and `subturn=CB-APPLY`.

Required dependencies:
- `references/core/turn-boundaries.md`
- `references/core/evidence.md`
- `references/03-repository-workflow.md`

Conditional dependencies:
- `modules/github-connector/MODULE.md` only for connector/hybrid remote mutation.

Do not load engineering/unit-testing modules merely because they were used in CB-DRAFT. If patch application requires semantic redesign, stop and return to CB-DRAFT.

## Goal

Apply the approved draft patch, verify the resulting diff, and establish committed/pushed ordinary source state for compilation.

## Procedure

1. Verify the patch base and current branch authority.
2. Apply the patch without semantic redesign.
3. Inspect the resulting diff for intended files/semantics, unrelated changes, and style drift.
4. Remove or archive temporary patch transport according to project policy.
5. Commit and push ordinary source/test/build files.
6. Record the resulting branch head.

## Forbidden

- compiling;
- runtime tests/benchmarks;
- broad manual edits outside patch intent;
- silently redesigning the implementation;
- treating temporary patch material as final authority.

## Exit

Source is committed/pushed and matches patch intent. Update handoff to `CB-COMPILE` with `load_next: references/turns/CB-COMPILE.md`.
