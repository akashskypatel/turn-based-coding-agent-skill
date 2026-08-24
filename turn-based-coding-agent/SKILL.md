---
name: turn-based-coding-agent
description: Production-harden software through separated Code + Build, Test + Benchmark, and optional independent Review turns with optional granular subturns, strict on-demand context loading, recoverable Git workflow, and integrated engineering/unit-test guidance.
---

# Turn-Based Coding Agent

Use this skill for multi-turn implementation, remediation, refactoring, or production-hardening where implementation and runtime validation must remain separate and recoverable.

## Context-loading policy

Use strict progressive disclosure. `SKILL.md` is a dispatcher, not a complete operating manual.

1. Read this file.
2. Read the project live handoff.
3. Load exactly the current turn/subturn file listed by the handoff's `load_next` field.
4. Load a capability `MODULE.md` only when the current turn file or handoff trigger requires it.
5. Load module references only when that `MODULE.md` routes to them for the current question.
6. Load templates only when producing that artifact.
7. Load historical plans/results only when the handoff or current turn file cites them.
8. Treat research, attribution, examples, and provenance files as cold storage; do not load them during normal execution.
9. Do not read sibling turn files, sibling module references, or all project documentation "for completeness."
10. If an old document points to a compatibility reference, follow its redirect to the focused current file and stop there.

The live handoff should precompute the minimum context set for the successor in `Context Load Plan`.

## Canonical cadence

```text
Code + Build -> Test + Benchmark -> [Optional Review] -> Code + Build
```

Optional granular execution:

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

TB-EXEC -> TB-REVIEW -> TB-PLAN -> [Optional Review]
```

Granular states narrow permissions inside a canonical turn; they never broaden canonical boundaries.

## State router

Load exactly one primary turn file for the current state:

| State | Primary file |
|---|---|
| Initialize/reset | `references/02-initialization.md` |
| Canonical Code + Build | `references/turns/CB.md` |
| CB-DRAFT | `references/turns/CB-DRAFT.md` |
| CB-APPLY | `references/turns/CB-APPLY.md` |
| CB-COMPILE | `references/turns/CB-COMPILE.md` |
| CB-CLOSEOUT | `references/turns/CB-CLOSEOUT.md` |
| Canonical Test + Benchmark | `references/turns/TB.md` |
| TB-EXEC | `references/turns/TB-EXEC.md` |
| TB-REVIEW | `references/turns/TB-REVIEW.md` |
| TB-PLAN | `references/turns/TB-PLAN.md` |
| Optional independent Review | `references/turns/REVIEW.md` |

Do not preload the other rows.

## Capability router

Load capability modules only when their trigger is present:

| Trigger | Module |
|---|---|
| Implementation design or corrective planning | `modules/engineering-guidelines/MODULE.md` |
| Unit-test design, repair, diagnosis, or review | `modules/unit-testing/MODULE.md` |
| `github_connector`/`hybrid` access or GitHub Actions/artifact work | `modules/github-connector/MODULE.md` |

A module may route to deeper references. Do not open all references in that module automatically.

## Non-negotiable boundaries

- Code + Build may change source and compile, but may not execute runtime tests or benchmarks.
- Test + Benchmark may execute validation and plan corrective work, but may not edit implementation/test/benchmark/build logic or compile a replacement revision.
- Optional Review is planning-only and may revise the next Code + Build plan without editing or executing implementation/validation logic.
- Build and validate exact pushed commits; keep evidence commit separate from later documentation-only commits.
- Never weaken validation, special-case fixtures, synthesize success, or hide a product defect.
- Every Code + Build turn must close with an executable Test + Benchmark plan tied to the exact successfully compiled evidence commit/artifact.
- Keep TODO and the live handoff current at every separately resumable turn/subturn boundary.

Detailed permission rules are in `references/core/turn-boundaries.md`; load them only when the current turn file requires them.

## Handoff-first resume rule

A context-free successor should normally need only:

```text
SKILL.md
-> project HANDOFF.md
-> HANDOFF load_next primary turn file
-> explicitly triggered capability MODULE.md files
-> specifically routed deep references/evidence/templates
```

If the handoff lacks an exact `load_next` path, repair the handoff before implementation proceeds.
