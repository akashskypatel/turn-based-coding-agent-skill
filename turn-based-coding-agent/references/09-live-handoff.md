# Live Handoff Contract

**Context class:** `deep-reference`

Load only when creating, repairing, or auditing the project live handoff. Normal resume reads the project handoff itself, not this reference.

## Purpose

Maintain one concise version-controlled first-read document under project agent documentation. It tells a context-free successor exactly what state to resume, what is authoritative, and what minimum context to load.

## Required content

- repository/base/work branch/phase;
- execution mode, canonical turn, exact next subturn/state;
- current source, evidence, planning, and handoff commits as applicable;
- authoritative plan reference and explicit next steps when the referenced plan lacks them;
- blockers/decisions and only procedural details not already covered elsewhere;
- concise lessons that prevent repeated mistakes;
- evidence/report references;
- `Context Load Plan`.

## Context Load Plan

Precompute the successor's minimum context:

```yaml
load_next:
  - references/turns/<STATE>.md
conditional_modules:
  - trigger: <specific condition>
    path: modules/<capability>/MODULE.md
deep_references:
  - <only if already known necessary>
templates_when_producing:
  - <only artifacts the successor must create>
do_not_preload:
  - sibling turn files
  - module reference directories
  - research/provenance/examples
  - uncited historical reports
```

Rules:

- `load_next` normally contains exactly one primary turn/subturn file.
- Capability modules are conditional unless the next state certainly requires them.
- Do not list whole directories.
- Do not tell the successor to "read all references" or "review all documentation."
- Templates are not loaded until their artifact is produced.

## Anti-bloat

Link rather than copy full plans, logs, diffs, TODO inventories, test/benchmark reports, generic skill procedures, or chat history. Remove stale instructions when state changes. Consolidate repeated lessons into one durable statement.

## Update timing

At every separately resumable turn/subturn boundary, update or verify the handoff. When evidence belongs to an earlier source commit, record `evidence_commit` separately from later documentation-only `handoff_commit`.

Every agent entry-point document should link prominently to the handoff, but must not duplicate its contents.
