# GitHub Connector Module

**Context class:** `conditional-capability`

Load only when `repository_access_mode` is `github_connector` or `hybrid`, or when the active state must inspect or operate GitHub Actions, artifacts, PRs, branches, or remote repository state.

Do not load for purely local repository work.

## Minimal routing

Load only the reference required by the current operation:

- Simple connector reads/writes, branch/PR/Git-data operations: `../../references/github-connector-workflows/TOOL_MAP.md`; add `COMMON_TASKS.md` only when a procedure is needed.
- Any connector content write or patch transport decision: `../../references/github-connector-workflows/PATCH_APPLICATION.md`.
- Creating, modifying, validating, triggering, observing, or cleaning up GitHub Actions workflows: `../../references/github-connector-workflows/WORKFLOW_POLICY.md`.
- Temporary push-marker workflow lifecycle: additionally load `../../references/github-connector-workflows/TEMP_WORKFLOW_LIFECYCLE.md`.
- Known connector/workflow failure mode or race: `../../references/github-connector-workflows/PITFALLS.md`.

`../../references/10-github-connector-workflows.md` is a compatibility/overview router. Do not load it when the focused reference above is already known.

## Core rules

- GitHub connector is the control plane; GitHub Actions is a bounded execution plane; artifacts/logs are the evidence plane.
- Work directly on the configured working branch. Do not create temporary/control/staging branches unless a concrete blocker makes one necessary.
- Prefer direct connector mutations over Actions when computation is unnecessary.
- Before every connector content write, estimate the UTF-8 size of that individual write. Keep it at or below **19 KB** because larger writes have been observed to truncate silently.
- Use the patch-transport decision tree in `PATCH_APPLICATION.md` when a source change cannot be safely persisted as direct <=19 KB writes.
- Use atomic Git-data commits for coherent multi-file changes when available, but the 19 KB ceiling still applies to each individual content-bearing connector write such as each blob creation.
- Never force-update a shared branch merely to bypass a race.
- Every created or modified workflow must follow `WORKFLOW_POLICY.md`, preserve the active turn/subturn boundary, fail closed, and retain detailed success/failure evidence.
- Connector file references are not local filesystem paths.

Return to the active turn file after the required remote operation. Do not continue traversing GitHub references for completeness.
