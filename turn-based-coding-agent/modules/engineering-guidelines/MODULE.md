# Engineering Guidelines Module

Internal progressive-disclosure module for `turn-based-coding-agent`. Load this module before drafting or applying implementation changes and when independently reviewing a proposed implementation plan.

The module distills the coding principles and examples from `multica-ai/andrej-karpathy-skills` into rules compatible with this skill's separated Code + Build and Test + Benchmark cadence.

## Core principles

1. **Think before coding**
   - State material assumptions instead of silently choosing them.
   - When multiple interpretations materially change the implementation, identify them before editing.
   - Prefer repository evidence and authoritative project documents over guesses.
   - Identify a simpler viable approach when one exists.
   - Ask only when a material ambiguity cannot be resolved safely from available evidence.

2. **Simplicity first**
   - Implement the minimum behavior required by the active plan.
   - Do not add speculative abstraction, configurability, features, or defensive machinery without a demonstrated requirement.
   - Avoid infrastructure or patterns whose complexity exceeds the problem being solved.
   - If a substantially smaller implementation satisfies the same contract, prefer it.

3. **Surgical changes**
   - Every changed line must trace to the active objective, required validation support, diagnostics, or build integration.
   - Match existing project style and conventions.
   - Do not perform drive-by refactors, formatting changes, renames, comment rewrites, or dead-code cleanup.
   - Remove only code made unused by the active change.
   - Record unrelated issues instead of silently expanding scope.

4. **Goal-driven execution**
   - Convert vague tasks into observable success criteria before implementation.
   - Connect every planned change to a build check and future runtime validation.
   - For defects, preserve or create a reproduction-oriented test scenario during Code + Build, then execute it only during Test + Benchmark.
   - Use evidence from compile/test/benchmark results to decide whether another implementation loop is justified.

## Turn-workflow adaptation

The source guidance often describes writing and immediately running a test before fixing a defect. This skill preserves the intent while maintaining stricter turn separation:

```text
Code + Build: design or author reproduction/regression coverage -> compile it
Test + Benchmark: execute the reproduction/regression coverage
Next Code + Build: correct remaining implementation defects when evidence requires it
```

When granular subturns are enabled:

- **CB-DRAFT**: surface assumptions, choose the simplest sufficient approach, and draft only the necessary patch.
- **CB-APPLY**: verify the applied diff remains surgical and matches project style.
- **CB-COMPILE**: use compile evidence as the only implementation-loop gate; do not edit code here.
- **CB-CLOSEOUT**: define verifiable TB acceptance criteria and an explicit test plan.
- **TB-REVIEW / TB-PLAN**: challenge whether the evidence actually proves the intended behavior before proposing further code.

## Progressive references

Read only what is needed:

- `references/01-principles.md` — detailed decision rules.
- `references/02-practical-patterns.md` — adapted anti-patterns and preferred behaviors drawn from the source examples.
- `references/03-source-attribution.md` — source links, license note, and integration rationale.

## Non-negotiable checks before implementation

Before approving a code patch, answer:

- What exact contract or failure is being addressed?
- Which assumptions are evidence-backed and which remain uncertain?
- Is there a materially simpler implementation?
- Does every changed line belong to this objective?
- What build evidence will prove structural validity?
- What later Test + Benchmark evidence will prove behavioral validity?

If those questions do not have concrete answers, the implementation plan is not ready.
