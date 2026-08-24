# Core Turn Boundaries

**Context class:** `core-conditional`

Load only when the active turn/subturn file declares this dependency. Do not preload it merely because the skill is active.

## Canonical authority

```text
Code + Build -> Test + Benchmark -> [Optional Review] -> Code + Build
```

Granular subturns narrow permissions inside a canonical turn; they never broaden them.

## Code + Build boundary

May change implementation, test/benchmark definitions when justified, build configuration, diagnostics, and documentation. May compile and perform compile-time/static checks.

Must not execute runtime tests, benchmarks, produced binaries for discovery/help, or runtime validation hidden inside build scripts.

## Test + Benchmark boundary

May execute the pre-authored validation plan, collect evidence, review results, classify failures, and plan the next Code + Build turn.

Must not edit production, test, benchmark, or build logic and must not compile a replacement source revision.

## Optional Review boundary

May inspect evidence and revise planning records only. It must be independent of the implementation/primary validation context when used.

Must not edit implementation or validation logic, compile, execute tests/benchmarks, or claim a fix was implemented.

## Granular narrowing

- `CB-DRAFT`: draft patch only; no authoritative source mutation, compile, or runtime execution.
- `CB-APPLY`: apply/verify/commit patch only; no compile or runtime execution.
- `CB-COMPILE`: compile exact pushed commit only; no source/test/build-logic edits or runtime execution.
- `CB-CLOSEOUT`: documentation and TB planning only.
- `TB-EXEC`: execute approved TB plan and preserve raw evidence only.
- `TB-REVIEW`: interpret existing evidence only; no new unplanned runtime work.
- `TB-PLAN`: planning/documentation only.

If any requested action exceeds the active boundary, defer it to the correct next state and record that transition in the handoff.