# GitHub Connector Module

**Context class:** `conditional-capability`

Load only when `repository_access_mode` is `github_connector` or `hybrid`, or when the active state must inspect/operate GitHub Actions runs, artifacts, PRs, branches, or remote repository state.

Do not load for purely local repository work.

## Minimal routing

Load only the deepest reference required by the current operation:

- Simple connector reads/writes, branch/PR/Git-data operations: `../../references/github-connector-workflows/TOOL_MAP.md` and, only if procedure is needed, `../../references/github-connector-workflows/COMMON_TASKS.md`.
- GitHub Actions execution, artifact provenance, compile/test workflow boundaries, patch workflows, or remote evidence handling: `../../references/10-github-connector-workflows.md`.
- Known connector/workflow failure mode or race: `../../references/github-connector-workflows/PITFALLS.md`.

Do not open all three references automatically.

## Core rules

- Connector is the control plane; GitHub Actions is a bounded execution plane; artifacts/logs are the evidence plane.
- Prefer direct connector mutations over Actions when computation is unnecessary.
- Use atomic Git-data commits for coherent multi-file changes when available.
- Never force-update a shared branch merely to bypass a race.
- Every created/modified workflow preserves the active turn/subturn boundary, uses least privilege, logs detailed activity on success/failure, and uploads a separate diagnostic log artifact.
- Connector file references are not local filesystem paths.

Return to the active turn file after the required remote operation; do not continue traversing GitHub references for completeness.
