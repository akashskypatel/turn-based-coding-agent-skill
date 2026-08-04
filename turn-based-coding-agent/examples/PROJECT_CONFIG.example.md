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

- Milestone tracker: `docs/MILESTONE_3.md`
- Remediation plan: `docs/parser-remediation.md`
- Project notes: `notes/parser/*.md`
- Architecture/contracts: `docs/file-format.md`
- Failure diagnostics: `results/failed-recovery.md`
- Existing results: `results/latest/`

## Commands and Workflows

- Build workflow: `.github/workflows/agent-parser-build.yml`
- Test commands: packaged `parser_tests` filters followed by the full suite
- Benchmark commands: packaged recovery corpus benchmark, four independent runs

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
