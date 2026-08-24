# Optional Granular Subturn Workflow

## Purpose

Code + Build and Test + Benchmark remain the canonical turn types. Either may optionally be decomposed into smaller resumable subturns when the user, project policy, or task risk benefits from finer control.

Canonical mode is still valid. Granular mode adds stop points; it does not weaken any canonical boundary.

```text
Canonical:
Code + Build -> Test + Benchmark -> [Optional Review] -> Code + Build

Granular Code + Build:
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

Granular Test + Benchmark:
TB-EXEC -> TB-REVIEW -> TB-PLAN -> [Optional Review]
```

The optional independent Review turn remains a canonical planning-only turn.

## Choosing execution mode

Record the execution mode in project configuration, TODO, and handoff:

- `canonical` — perform all responsibilities of a canonical turn in one turn.
- `granular` — expose each applicable subturn as a separate resumable boundary.
- `per_turn` — choose canonical or granular at the start of each canonical turn and record the choice before work begins.

Do not silently change modes mid-turn. A user instruction may override the configured mode.

Every completed subturn updates the live handoff as necessary. The handoff records both the canonical turn and exact next subturn.

# Code + Build decomposition

A canonical Code + Build turn still owns all implementation and compile work and must finish with a Test + Benchmark test plan. Granular mode separates those responsibilities.

## CB-DRAFT

### Purpose

Design the actual source changes and express them as a reviewable patch before mutating authoritative source state.

### Required inputs

- authoritative next Code + Build plan,
- exact branch/base commit,
- relevant contracts and implementation,
- `modules/engineering-guidelines/MODULE.md`,
- `modules/unit-testing/MODULE.md` when unit-test code is in scope.

### Allowed

- repository/document inspection,
- assumption and tradeoff analysis,
- patch design,
- drafting a plain unified diff against the exact base commit,
- drafting or updating implementation notes associated with the patch.

### Forbidden

- applying the patch to authoritative source,
- compiling,
- executing tests or benchmarks,
- using an encoded patch/archive as a substitute for committed source.

### Patch contract

The draft patch must identify:

- base commit,
- intended files,
- behavior/invariant addressed,
- assumptions that materially affect the change,
- expected resulting diff scope.

The patch is a temporary implementation artifact. When durable storage is needed between agents, store it only through a project-approved temporary artifact mechanism. Do not make encoded patch blobs the authoritative implementation. After CB-APPLY, committed ordinary source files become authority and temporary patch transport should be removed or archived according to policy.

### Exit

- patch is reviewable and tied to an exact base,
- no source mutation occurred,
- next subturn is CB-APPLY.

## CB-APPLY

### Purpose

Apply the CB-DRAFT patch and establish exact committed source state for compilation.

### Allowed

- apply the drafted patch,
- resolve only mechanical application context needed to produce the intended patch result,
- inspect the resulting diff,
- remove temporary patch transport when appropriate,
- commit and push ordinary source/test/build files.

### Forbidden

- redesigning the implementation silently,
- broad manual edits not represented by the patch intent,
- compiling,
- executing tests or benchmarks.

If the patch cannot be applied without semantic redesign, stop and return to CB-DRAFT.

### Exit gate

Before advancing:

1. resulting diff matches intended patch semantics,
2. no unrelated files or style drift were introduced,
3. source changes are committed and pushed,
4. remote branch head is recorded,
5. next subturn is CB-COMPILE.

## CB-COMPILE

### Purpose

Compile the exact pushed source commit. This subturn is evidence-only with respect to implementation code.

### Allowed

- configure/build steps that do not execute runtime tests,
- compilation of production, test, benchmark, plugin, or packaging targets,
- compile-time/static analysis permitted by project policy,
- build log and artifact collection.

### Forbidden

- editing production, test, benchmark, or build logic,
- executing test/benchmark binaries,
- hiding runtime execution inside build scripts.

### PASS

If all required compile targets pass:

- record exact evidence commit and artifacts,
- advance to CB-CLOSEOUT.

### FAIL

If compilation fails:

1. record the first actionable compile error and evidence,
2. do not fix it inside CB-COMPILE,
3. transition back to CB-DRAFT,
4. draft the smallest corrective patch against the latest committed branch head,
5. repeat `CB-DRAFT -> CB-APPLY -> CB-COMPILE` until compilation passes or a genuine blocker is established.

Every correction loop must remain surgical and evidence-driven.

## CB-CLOSEOUT

### Purpose

Close the canonical Code + Build turn after compile success and prepare authoritative runtime validation.

### Allowed

- change documentation,
- TODO and live handoff updates,
- Code + Build report,
- mandatory Test + Benchmark test plan,
- documentation-only closeout commit.

### Forbidden

- changing implementation/test/benchmark/build logic,
- compiling a new source revision,
- executing tests or benchmarks.

### Mandatory Test + Benchmark plan

A Code + Build turn cannot close without a concrete TB plan. Use `templates/TEST_PLAN.md` or an equivalent project document containing at minimum:

- exact evidence commit/artifact to validate,
- validation objective and behavior/invariants under test,
- ordered commands/tests/benchmarks,
- required fixtures/inputs/seeds/environment,
- focused regression and broader regression scope,
- benchmark baselines and repetition requirements when applicable,
- expected results and explicit acceptance criteria,
- evidence to preserve,
- stop/blocker conditions,
- any plan-defined rerun rules.

When unit tests are part of the plan, use `modules/unit-testing/MODULE.md` to ensure the cases and assertions are meaningful.

The closeout may create a later documentation-only handoff commit. Record the compiled `evidence_commit` separately from the `handoff_commit`.

### Exit

- required compilation passed,
- change documentation is current,
- TB test plan is explicit and executable,
- TODO/handoff identify the evidence commit and plan,
- next canonical turn is Test + Benchmark,
- granular next subturn, when enabled, is TB-EXEC.

# Test + Benchmark decomposition

## TB-EXEC

### Purpose

Execute the pre-authored Test + Benchmark plan against the exact compiled evidence commit/artifact.

### Allowed

- artifact retrieval and integrity verification,
- execution of the approved test/benchmark commands,
- collection of raw logs/results/traces/dumps/metrics,
- plan-defined repetitions or seeds.

### Forbidden

- changing production/test/benchmark/build logic,
- compiling replacement code,
- expanding validation scope ad hoc without recording the deviation,
- converting findings into corrective code changes.

Follow the test plan in order unless an explicit stop condition is met. Record any deviation and why it was necessary.

Exit to TB-REVIEW with complete raw evidence or an explicit execution/infrastructure blocker.

## TB-REVIEW

### Purpose

Interpret TB-EXEC evidence without changing code or planning implementation details prematurely.

### Review duties

- compare actual results with each test-plan acceptance criterion,
- classify every failure,
- identify whether evidence is complete and trustworthy,
- distinguish product defects, invalid fixtures, incorrect expectations, infrastructure issues, performance regressions, and nondeterminism,
- use `modules/unit-testing/MODULE.md` when unit-test quality is relevant,
- document findings and confidence level.

Do not edit source or execute additional unplanned validation in this subturn. If evidence is missing, record the gap for TB-PLAN rather than fabricating certainty.

Exit to TB-PLAN.

## TB-PLAN

### Purpose

Turn reviewed evidence into the next authoritative workflow decision.

### Required outcomes

- explicit phase status,
- corrective measures when failures exist,
- proposed next Code + Build plan with verifiable tasks,
- build verification for each proposed task,
- future TB validation expectations,
- decision to skip or request optional independent Review.

If all acceptance criteria pass, plan the next implementation phase or phase closure rather than inventing corrective work.

If optional Review is skipped, the TB-PLAN output becomes authoritative. If Review is requested, mark it `proposed_pending_review`; the independent reviewer may revise it.

# Canonical-mode equivalence

When subturn decomposition is not used:

- one Code + Build turn must internally satisfy CB-DRAFT, CB-APPLY, CB-COMPILE, and CB-CLOSEOUT responsibilities, including the mandatory TB test plan;
- one Test + Benchmark turn must internally satisfy TB-EXEC, TB-REVIEW, and TB-PLAN responsibilities;
- the same prohibitions and evidence requirements apply.

Granular mode changes workflow control and resumability, not acceptance standards.
