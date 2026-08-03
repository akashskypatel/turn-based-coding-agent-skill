# Live Handoff Document

## Purpose

Maintain one concise, version-controlled handoff under the project's agent-documentation directory. Use `.agents/HANDOFF.md` when the repository has no existing convention. It is the first document a new coding agent reads when resuming with no chat or prior-session context.

The handoff complements the root TODO and turn reports:

- TODO tracks task inventory and status.
- Turn reports preserve detailed evidence from a completed turn.
- The live handoff explains exactly how to resume the next turn expertly.

Use `templates/HANDOFF.md`.

## Required content

The handoff must contain only the context needed to resume safely:

1. Exact repository, branch, phase, next turn type, and relevant source/planning commits.
2. A direct reference to the authoritative next-step document when it contains explicit executable next steps.
3. Explicit next steps in the handoff when no referenced document contains them clearly enough.
4. The exact first actions, commands, workflows, evidence, or files the successor must inspect.
5. Procedural information needed to execute the next turn that is not already stated by this skill, the next-step plan, or other agent documentation.
6. Current blockers, unresolved decisions, and assumptions that must not be made silently.
7. Concise lessons learned from failed attempts, errors, invalid fixtures, misleading diagnostics, environment problems, or process mistakes that could otherwise be repeated.

## Concision and anti-bloat rules

Do not copy information already available in authoritative documents. Link to the exact file, section, report, workflow run, result directory, issue, or commit instead.

Include a fact directly only when at least one condition holds:

- It changes how the next turn must be executed.
- It prevents a known mistake from recurring.
- It is not documented elsewhere.
- The external reference would be ambiguous without one sentence of context.

Remove stale instructions when the next-turn state changes. Consolidate repeated lessons into one durable statement. Prefer stable rules over chronological diaries.

Do not include:

- Full diffs or long log excerpts.
- A duplicate TODO list.
- Complete test or benchmark results already stored in a report.
- Generic skill procedures already defined by this package.
- Chat transcripts.
- Every action taken during prior turns.

## Update timing

At the end of every Code + Build, Test + Benchmark, and optional Review turn:

1. Re-read the handoff as a context-free successor.
2. Update it when the exact next turn, plan authority, commits, evidence, blockers, procedure, or lessons changed.
3. Remove superseded guidance.
4. Verify every reference exists and points to the intended revision or result.
5. Commit and push the handoff with the turn's documentation changes as a documentation-only transition commit when the evidence commit has already been built or validated.
6. Record both the evidence commit and the later handoff commit; never relabel evidence as coming from the handoff commit.

When nothing material changed, leave the document unchanged after verifying it remains accurate. State that verification in the turn report.

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

Read [the live agent handoff](.agents/HANDOFF.md) before making changes. It identifies the exact next turn, authoritative plan, required evidence, and known pitfalls.
```

Adapt the relative path to the entry document. Do not duplicate handoff contents in entry points.

## Authority rules

- The handoff must identify which plan is authoritative.
- After Test + Benchmark with review skipped, reference that turn report's authoritative plan.
- While optional Review is pending, mark the plan as pending and direct the successor to perform Review, not Code + Build.
- After Review, reference the review-approved or replacement plan and mark the earlier proposal superseded.
- If the handoff conflicts with a newer committed authoritative plan, the newer plan wins and the handoff must be corrected before other work proceeds.

## Quality check

A valid handoff lets a new agent answer, without chat context:

- What exact turn do I perform next?
- Which commit produced the build or validation evidence, and which later commit contains the current handoff?
- On which branch and commit do I start?
- Which plan is authoritative?
- What must I read or retrieve first?
- What commands or workflows are expected?
- What must I not repeat from prior failed attempts?
- What evidence will establish success?
