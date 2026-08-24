# Core Evidence Rules

**Context class:** `core-conditional`

Load only for states that create, consume, or reason about build/test/benchmark evidence.

## Exact provenance

- Record the exact source commit for every authoritative build.
- Test and benchmark evidence must identify the exact compiled source commit/artifact being executed.
- A later documentation-only handoff/planning commit does not change evidence provenance.
- Record `evidence_commit` separately from `handoff_commit` or `planning_commit`.

## Source synchronization

Before an authoritative build, ensure intended source is committed/pushed and the authoritative local/connector/remote head is known. Build the exact pushed revision.

Before runtime validation, verify the artifact belongs to that exact evidence commit. Do not rebuild inside Test + Benchmark merely to obtain a convenient artifact.

## Evidence quality

Preserve enough information to reproduce a claim:

- exact commit/artifact identity;
- command/workflow and filters;
- environment/platform/tool versions when material;
- input, fixture, seed, or dataset identity;
- pass/fail/skip/exit state;
- logs, traces, dumps, metrics, or benchmark outputs;
- baseline identity for comparisons.

Focused success does not prove production readiness. Performance improvement does not excuse correctness or quality regression.

## Failure evidence

Preserve the first actionable failure and raw evidence before planning a fix. Do not rewrite history by attributing evidence to a later source or documentation commit.