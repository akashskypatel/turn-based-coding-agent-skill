# Core Recovery and Context Loading

**Context class:** `core-conditional`

Load only for states that update TODO/handoff, establish the next state, or recover interrupted work.

## Recovery authority

The live handoff is the first-read runtime state pointer. TODO is the task/state inventory. Detailed plans, reports, and evidence stay external and are linked rather than copied.

At every separately resumable turn/subturn boundary, ensure the handoff records:

- repository, branch, active phase;
- execution mode;
- canonical turn and exact next subturn/state;
- source/evidence/planning/handoff commits as applicable;
- authoritative next-step plan;
- blockers/decisions and concise lessons not documented elsewhere;
- exact `Context Load Plan` for the successor.

## Context Load Plan contract

The handoff must precompute the smallest sufficient context set:

```yaml
load_next:
  - references/turns/<CURRENT_STATE>.md
conditional_modules:
  - trigger: <condition>
    path: modules/<capability>/MODULE.md
deep_references:
  - <only when already known to be required>
templates_when_producing:
  - <artifact template path>
do_not_preload:
  - sibling turn files
  - module reference directories
  - research/provenance/examples
  - uncited historical reports
```

`load_next` should normally contain exactly one primary turn/subturn file. Capability modules belong under `conditional_modules`, not unconditional `load_next`, unless the next state certainly requires them.

## Anti-bloat rules

- Do not duplicate procedures already defined by this skill.
- Do not copy full plans, logs, diffs, or test reports into the handoff.
- Link exact file/section/commit/artifact instead.
- Remove stale context instructions when state changes.
- Do not preserve chronological diaries; retain only reusable lessons that prevent repeated mistakes.

## Documentation-only transitions

When build/test evidence applies to an earlier source commit, later handoff/planning commits must remain documentation-only. Record `evidence_commit` separately and verify no implementation/test/benchmark/build-configuration changes occurred between evidence and handoff commits.
