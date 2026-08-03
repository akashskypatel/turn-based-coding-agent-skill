---
name: turn-based-coding-agent
description: Production-harden software through separated code-and-build, test-and-benchmark, and optional independent-review turns with recoverable Git workflow and evidence-based planning.
---

# Turn-Based Coding Agent

Use this skill for multi-turn implementation, remediation, or production-hardening work where code changes and runtime validation must remain separate.

## Authoritative cadence

```text
Code + Build -> Test + Benchmark -> [Optional Review] -> Code + Build
```

The Review turn is optional:

- If skipped, the Test + Benchmark turn's next-action plan is authoritative.
- If used, the independent Review turn may approve, amend, reorder, narrow, expand, or replace that plan.
- A Review turn does not modify production code, test logic, benchmark logic, or build configuration.

Never combine turn types.

## Non-negotiable rules

1. Implement domain-correct, generalized behavior. Never special-case one fixture, file, dataset, platform, or benchmark input.
2. A Code + Build turn may edit and compile, but may not run tests or benchmarks.
3. A Test + Benchmark turn may execute validation, but may not edit implementation, test, or benchmark logic.
4. An optional Review turn must be performed by an independent agent or fresh review context and may change only the next-turn plan and planning records.
5. Build and validate exact pushed commits. Record commit identities with all evidence.
6. Keep the root TODO, live handoff, and recovery state current.
7. Maintain a concise, version-controlled handoff that lets a new agent resume the next turn without chat context.
8. Never weaken validation to conceal a product defect.

## Progressive task index

Read only the modules needed for the current operation.

### First use or project reset

Read:

- `references/01-project-configuration.md`
- `references/02-initialization.md`
- `references/03-repository-workflow.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`

### Code + Build turn

Read:

- `references/03-repository-workflow.md`
- `references/04-code-build-turn.md`
- `references/07-testing-integrity.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`

### Test + Benchmark turn

Read:

- `references/05-test-benchmark-turn.md`
- `references/07-testing-integrity.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`

### Optional independent Review turn

Read:

- `references/06-optional-review-turn.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`

## Included templates

- `templates/PROJECT_CONFIG.md` - project-specific values and commands.
- `templates/TODO.md` - authoritative progress and recovery tracker.
- `templates/HANDOFF.md` - concise live context for a context-free successor agent.
- `templates/CODE_BUILD_REPORT.md` - Code + Build handoff.
- `templates/TEST_BENCHMARK_REPORT.md` - validation handoff.
- `templates/REVIEW_REPORT.md` - optional independent review decision.

## Start rule

Before implementation begins:

1. Resolve the project configuration.
2. Inspect the repository and historical evidence.
3. Create or normalize the root TODO and live handoff.
4. Link the handoff from every agent entry-point document.
5. Report current status and phase boundaries.
6. Create a dedicated working branch.
7. Begin with a Code + Build turn.
