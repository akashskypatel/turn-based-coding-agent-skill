# Live Handoff Document

## Purpose

Maintain one concise, version-controlled handoff under the project's agent-documentation directory. Use `.agents/HANDOFF.md` when the repository has no existing convention. It is the first document a new coding agent reads when resuming with no chat or prior-session context.

The handoff complements the root TODO and reports:

- TODO tracks task inventory and status.
- Turn/subturn reports preserve detailed evidence.
- The live handoff explains exactly how to resume the next canonical turn or granular subturn expertly.

Use `templates/HANDOFF.md`.

## Required content

The handoff must contain only the context needed to resume safely:

1. Exact repository, branch, phase, execution mode, canonical turn, next subturn when granular, and relevant source/planning commits.
2. A direct reference to the authoritative next-step document when it contains explicit executable next steps.
3. Explicit next steps in the handoff when no referenced document contains them clearly enough.
4. The exact first actions, commands, workflows, evidence, or files the successor must inspect.
5. The active CB-DRAFT patch reference when resuming at CB-APPLY, or the authoritative Test + Benchmark plan when resuming at TB-EXEC.
6. Procedural information needed to execute the next turn/subturn that is not already stated by this skill, the next-step plan, test plan, or other agent documentation.
7. Current blockers, unresolved decisions, and assumptions that must not be made silently.
8. Concise lessons learned from failed attempts, errors, invalid fixtures, misleading diagnostics, environment problems, or process mistakes that could otherwise be repeated.

## Concision and anti-bloat rules

Do not copy information already available in authoritative documents. Link to the exact file, section, report, workflow run, result directory, issue, artifact, or commit instead.

Include a fact directly only when at least one condition holds:

- It changes how the next turn/subturn must be executed.
- It prevents a known mistake from recurring.
- It is not documented elsewhere.
- The external reference would be ambiguous without one sentence of context.

Remove stale instructions when the next-turn state changes. Consolidate repeated lessons into one durable statement. Prefer stable rules over chronological diaries.

Do not include:

- Full diffs or long log excerpts.
- Full CB-DRAFT patches when a durable artifact/reference already exists.
- A duplicate TODO list.
- Complete test or benchmark results already stored in a report.
- Generic skill procedures already defined by this package.
- Chat transcripts.
- Every action taken during prior turns.

## Update timing

At the end of every Code + Build, Test + Benchmark, optional Review turn, and every separately resumable granular subturn:

1. Re-read the handoff as a context-free successor.
2. Update it when the exact next turn/subturn, plan authority, commits, patch/test-plan/artifact reference, evidence, blockers, procedure, or lessons changed.
3. Remove superseded guidance.
4. Verify every reference exists and points to the intended revision or result.
5. Commit and push the handoff with documentation changes when repository policy requires durable recovery.
6. Record both the evidence commit and later handoff/planning commit; never relabel evidence as coming from the documentation-only commit.

When nothing material changed, leave the document unchanged after verifying it remains accurate. State that verification in the relevant report.

## Granular resume rules

When granular execution is active, the handoff must distinguish canonical turn from subturn.

Examples:

- `Code + Build / CB-APPLY` — successor retrieves the exact CB-DRAFT patch/reference and applies only that patch intent.
- `Code + Build / CB-COMPILE` — successor compiles the exact pushed source commit and must not edit code.
- `Code + Build / CB-CLOSEOUT` — successor drafts documentation and the TB plan; no source/build/test mutation.
- `Test + Benchmark / TB-EXEC` — successor executes the linked test plan against the exact evidence artifact.
- `Test + Benchmark / TB-REVIEW` — successor reads raw evidence and classifies findings; no new runtime execution.
- `Test + Benchmark / TB-PLAN` — successor produces the next CB plan and review decision; no source/runtime work.

Do not collapse these permissions merely because the same agent performs consecutive subturns.

## Agent entry-point links

Every agent-facing entry document must prominently reference the configured handoff path. Typical entry points include:

- `AGENTS.md`
- `.agents/README.md`
- `CLAUDE.md`
- `CODEX.md`
- repository-specific agent instructions

Use a compact pointer such as:

```markdown
## Resume Current Work

Read [the live agent handoff](.agents/HANDOFF.md) before making changes. It identifies the exact canonical turn/subturn, authoritative plan, required evidence, and known pitfalls.
```

Adapt the relative path to the entry document. Do not duplicate handoff contents in entry points.

## Authority rules

- The handoff must identify which implementation plan and Test + Benchmark plan are authoritative.
- After Code + Build compile success, TB-EXEC must use the closeout test plan tied to the evidence commit/artifact.
- After Test + Benchmark/TB-PLAN with review skipped, reference that authoritative next Code + Build plan.
- While optional Review is pending, mark the plan pending and direct the successor to perform Review, not Code + Build.
- After Review, reference the review-approved or replacement plan and mark the earlier proposal superseded.
- If the handoff conflicts with a newer committed authoritative plan, the newer plan wins and the handoff must be corrected before other work proceeds.

## Quality check

A valid handoff lets a new agent answer, without chat context:

- What exact canonical turn and subturn do I perform next?
- Which commit produced build/validation evidence, and which later commit contains the current handoff?
- On which branch and commit do I start?
- Which implementation plan is authoritative?
- Which patch, build artifact, or Test + Benchmark plan must I retrieve?
- What must I read or retrieve first?
- What actions are allowed and forbidden in this subturn?
- What must I not repeat from prior failed attempts?
- What evidence will establish success?
