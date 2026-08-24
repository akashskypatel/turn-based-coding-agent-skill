# Example Project Configuration

## Repository

- Repository: `owner/example-project`
- Repository access mode: `github_connector`
- GitHub connector name: `@GitHub`
- Base branch: `main`
- Working branch prefix: `agent/example-project`
- Root TODO file: `TODO.md`
- Live handoff file: `.agents/HANDOFF.md`
- Agent entry-point documents: `AGENTS.md`, `.agents/README.md`

## Objective and Scope

- Objective: Make the parser recover from malformed records without losing subsequent valid records.
- In scope: parser state, diagnostics, focused fixtures, performance regression coverage.
- Out of scope: public syntax changes and serializer behavior.
- Supported platforms/configurations: Linux and Windows release builds.

## Authoritative Sources

Store paths first; open contents only when the current state needs them.

- Design documents: `docs/design/*.md`
- Milestone tracker: `docs/MILESTONE_3.md`
- Remediation plan: `docs/parser-remediation.md`
- Project notes: `notes/parser/*.md`
- Architecture/contracts: `docs/file-format.md`
- Failure diagnostics: `results/failed-recovery.md`
- Existing results: `results/latest/`

## Turn Execution Policy

- Execution mode: `per_turn`
- Default Code + Build mode: `granular`
- Default Test + Benchmark mode: `granular`
- Temporary CB-DRAFT patch storage: agent artifact
- Temporary patch persistence permitted: yes
- Temporary patch cleanup: remove after CB-APPLY verifies committed source
- Mandatory Test + Benchmark plan: `.agents/parser/TB_PLAN.md`

Example granular sequence:

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE
    ^                         |
    |------ compile FAIL -----|
CB-COMPILE PASS -> CB-CLOSEOUT -> TB-EXEC -> TB-REVIEW -> TB-PLAN
```

## Context Loading Policy

- Policy: `strict_on_demand`
- Live handoff `load_next`: required, exactly one primary turn/subturn file
- Preload sibling turn/subturn files: no
- Preload capability-module reference directories: no
- Preload templates: no
- Research/provenance/examples during normal execution: no
- Historical reports/results: only when cited by the handoff or current turn file

Example successor load plan after a successful CB-COMPILE:

```yaml
load_next:
  - references/turns/CB-CLOSEOUT.md
conditional_modules: []
deep_references: []
templates_when_producing:
  - templates/CODE_BUILD_REPORT.md
  - templates/TEST_PLAN.md
do_not_preload:
  - sibling turn/subturn files
  - module reference directories
  - research/provenance/examples
  - uncited historical reports
```

## Commands and Workflows

- Build workflow: `.github/workflows/agent-parser-build.yml`
- Test commands: packaged `parser_tests` filters followed by the full suite
- Benchmark commands: packaged recovery corpus benchmark, four independent runs

## Test-Plan Policy

- Plan owner: CB-CLOSEOUT
- Evidence identity: exact successfully compiled source SHA and artifact digest
- Order: defect reproduction -> focused parser regressions -> full parser suite -> corpus benchmark
- Benchmark baseline: latest accepted parser baseline, four runs
- Stop conditions: artifact mismatch, checksum failure, missing corpus, or invalid runner dependency
- Evidence retention: raw test logs, machine-readable results, benchmark outputs, and artifact metadata

## GitHub Workflow Policy

- Detailed logging: required for success and failure.
- Log initialization: before checkout.
- Log artifact: separate, uploaded under `if: always()` with `if-no-files-found: error`.
- Result artifact: uploaded only after successful verification.
- Failure diagnosis: use the downloaded detailed log artifact.
- Compile-only workflow: execute no test or benchmark binary.
- Workflow self-modification: forbidden.
- Trigger: `workflow_dispatch` or one exact marker path.

## Review Policy

- Policy: optional
- Review required when: the recovery contract or test fixtures change.
- Review may be skipped when: a localized implementation defect has direct reproduction and regression evidence.
