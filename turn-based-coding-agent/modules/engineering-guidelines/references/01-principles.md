# Engineering Principles

## Think before coding

Before changing code:

1. Read the authoritative plan, live handoff, relevant contracts, and nearby implementation.
2. State assumptions that materially affect behavior, scope, data handling, compatibility, performance, or security.
3. If the request has multiple plausible interpretations, resolve them from evidence when possible; otherwise surface the alternatives instead of silently choosing one.
4. Identify the simplest approach that satisfies the contract.
5. Define observable success criteria and future validation before implementation begins.

Do not use clarification as a substitute for repository investigation. Ask only when available evidence cannot resolve a material ambiguity safely.

## Simplicity first

Prefer the smallest design that meets current requirements.

Avoid:

- abstractions used only once,
- generalized strategy/plugin/configuration layers without a present requirement,
- speculative caching, validation, notification, retry, or fallback behavior,
- broad defensive branches for states the contract excludes,
- framework introduction for a local problem,
- large rewrites when a local correction is sufficient.

Complexity is justified when existing requirements, measured constraints, or repeated patterns demand it—not because it might be useful later.

## Surgical changes

Preserve existing project shape unless the task explicitly requires changing it.

- Match local naming, formatting, error handling, ownership, and API conventions.
- Do not reformat unrelated lines.
- Do not add type annotations, comments, documentation, logging, or validation outside scope unless required by the change.
- Do not refactor neighboring code simply because a cleaner design is imaginable.
- Remove imports, variables, helpers, or branches only when the active change made them unused.
- Mention unrelated defects separately.

A useful review test is: **Can every changed line be explained by the active objective or its required build/test support?** If not, shrink the diff.

## Goal-driven execution

Translate each task into verifiable outcomes.

Weak:

- "improve parsing"
- "fix authentication"
- "make search faster"

Strong:

- "malformed record X no longer prevents the next valid record from being parsed"
- "password change invalidates all pre-change sessions"
- "p95 query latency for corpus Y falls below Z without reducing result correctness"

For each implementation step specify:

1. required change,
2. compile/build verification,
3. deferred runtime validation,
4. acceptance criterion.

When a defect is involved, prefer a focused reproduction or regression test whose failure would distinguish the defect from nearby valid behavior. Under this skill, author/compile that coverage in Code + Build and execute it only in Test + Benchmark.

## Avoid premature all-at-once changes

When a task naturally decomposes into independently verifiable behavior, prefer bounded phases. Do not introduce several architectural layers, migrations, performance optimizations, and configuration systems in one implementation unit unless they are inseparable requirements.

Granular CB subturns exist specifically to make the implementation proposal, application, compilation, and closeout independently inspectable.
