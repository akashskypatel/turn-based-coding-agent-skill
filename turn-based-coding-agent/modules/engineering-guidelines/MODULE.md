# Engineering Guidelines Module

**Context class:** `conditional-capability`

Load for implementation design/corrective planning (`CB-DRAFT`, canonical CB planning, `TB-PLAN`, independent Review). Do not load for routine `CB-APPLY`, `CB-COMPILE`, `CB-CLOSEOUT`, `TB-EXEC`, or evidence-only `TB-REVIEW`.

This module distills the integrated Karpathy-derived engineering guidance while preserving this skill's separated runtime-validation cadence.

## Working rules

1. Surface material assumptions; resolve from repository evidence before asking when possible.
2. Prefer the simplest sufficient implementation; no speculative abstractions/features/configurability.
3. Keep changes surgical and style-consistent; every changed line must trace to the objective, validation support, diagnostics, or build integration.
4. Define observable success criteria, build verification, and future TB validation before approving the implementation plan.

## Reference router

Load only what the current design question requires:

- General implementation/planning decision rules: `references/01-principles.md`.
- Suspected overengineering, drive-by refactor, hidden assumption, style drift, or vague-goal pattern: `references/02-practical-patterns.md`.
- Source/license/provenance audit of this module itself: `references/03-source-attribution.md` **only**. This is cold storage and must not be loaded during normal project work.

Do not preload the reference directory.

## Turn adaptation

For defects, author or preserve reproduction/regression source during Code + Build, compile it there, and execute it only during Test + Benchmark. The source material's immediate test-first loop is adapted to the parent skill's stricter turn separation.
