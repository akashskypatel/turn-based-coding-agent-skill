---
name: turn-based-coding-agent
description: Production-harden software through separated code-and-build, test-and-benchmark, and optional independent-review turns with recoverable Git workflow, connector-first remote operations, and evidence-based planning.
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
3. A Test + Benchmark turn may execute validation, but may not edit implementation, test, benchmark, or build logic.
4. An optional Review turn must be performed by an independent agent or fresh review context and may change only the next-turn plan and planning records.
5. Build and validate exact pushed commits. Record commit identities with all evidence.
6. Keep the root TODO, live handoff, and recovery state current.
7. Maintain a concise, version-controlled handoff that lets a new agent resume the next turn without chat context.
8. Never weaken validation to conceal a product defect.
9. When the repository is available only through `@GitHub`, use the connector as the control plane and a narrowly scoped GitHub Actions workflow only as the remote execution plane.
10. Every created or modified GitHub Actions workflow must retain detailed activity on success and failure and must always upload a separate diagnostic log artifact.

## Progressive task index

Read only the modules needed for the current operation.

### First use or project reset

Read:

- `references/01-project-configuration.md`
- `references/02-initialization.md`
- `references/03-repository-workflow.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `references/10-github-connector-workflows.md` when remote work uses `@GitHub` or GitHub Actions

### Code + Build turn

Read:

- `references/03-repository-workflow.md`
- `references/04-code-build-turn.md`
- `references/07-testing-integrity.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `references/10-github-connector-workflows.md` when the build or source changes are remote

### Test + Benchmark turn

Read:

- `references/05-test-benchmark-turn.md`
- `references/07-testing-integrity.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `references/10-github-connector-workflows.md` when retrieving Actions artifacts or diagnosing remote runs

### Optional independent Review turn

Read:

- `references/06-optional-review-turn.md`
- `references/08-status-recovery-and-completion.md`
- `references/09-live-handoff.md`
- `references/10-github-connector-workflows.md` when remote PR, workflow, or artifact evidence is reviewed

## Remote GitHub routing

When no trusted local checkout is available:

1. Resolve repository, branch, commit, PR, and file authority with `@GitHub`.
2. Prefer direct connector reads and writes for repository metadata, small text changes, branches, commits, PRs, comments, labels, logs, and artifacts.
3. Use Git blobs, trees, commits, and non-forced ref updates for coherent multi-file changes when those actions are available.
4. Use GitHub Actions only for computation or repository operations the connector cannot directly perform.
5. Load `references/10-github-connector-workflows.md`, then the focused task or pitfall reference it identifies.
6. Never let a remote workflow blur the active turn boundary.

## Included templates

- `templates/PROJECT_CONFIG.md` - project-specific values, commands, connector mode, and workflow policy.
- `templates/TODO.md` - authoritative progress and recovery tracker.
- `templates/HANDOFF.md` - concise live context for a context-free successor agent.
- `templates/CODE_BUILD_REPORT.md` - Code + Build handoff.
- `templates/TEST_BENCHMARK_REPORT.md` - validation handoff.
- `templates/REVIEW_REPORT.md` - optional independent review decision.
- `templates/github-actions/logged-remote-task.yml` - mandatory logging baseline for bounded remote work.
- `templates/github-actions/apply-unified-patch.yml` - idempotent large-patch application with output verification.
- `templates/github-actions/PR_BODY.md` - remote workflow and artifact evidence template.

## Start rule

Before implementation begins:

1. Resolve the project configuration, including connector availability and GitHub workflow policy.
2. Inspect the repository and historical evidence.
3. Create or normalize the root TODO and live handoff.
4. Link the handoff from every agent entry-point document.
5. Report current status and phase boundaries.
6. Create a dedicated working branch.
7. Begin with a Code + Build turn.
