# Practical Patterns and Anti-Patterns

These examples adapt the source repository's scenarios to the stricter turn-based workflow. They are conceptual examples, not copied source implementations.

## Hidden assumptions

**Anti-pattern:** A request says "export user data" and the implementation silently chooses all users, JSON, a filesystem destination, and a field set.

**Preferred behavior:** Surface the decisions that materially affect behavior or privacy, resolve them from project contracts where possible, and implement only the confirmed scope.

## Over-abstraction

**Anti-pattern:** A simple calculation or local transformation introduces strategy interfaces, configuration objects, plugin points, factories, or dependency injection that current requirements do not need.

**Preferred behavior:** Implement the direct operation first. Generalize only after the project has multiple real variants or an explicit extensibility requirement.

## Speculative features

**Anti-pattern:** A request to persist one value also adds caching, merging, notification, validation layers, retry systems, or configurability without evidence they are required.

**Preferred behavior:** Add only persistence behavior required by the contract. Record plausible future work separately.

## Drive-by refactoring

**Anti-pattern:** A bug fix also rewrites nearby validation, renames variables, adds unrelated rules, modernizes syntax, and changes comments.

**Preferred behavior:** Correct the defect with the smallest coherent diff. Leave unrelated cleanup untouched.

## Style drift

**Anti-pattern:** While adding logging or one branch, the patch changes quote style, formatting, type annotations, return structure, or naming conventions across the function.

**Preferred behavior:** Match the surrounding file and change only what the requested behavior requires.

## Vague execution

**Anti-pattern:** "Review the system, improve it, and test it."

**Preferred behavior:** Define specific observable goals, compile targets, runtime validation, and acceptance criteria before implementation.

## Fixing before reproducing

**Anti-pattern:** Change an algorithm immediately because a bug report sounds plausible.

**Preferred behavior under this skill:**

1. During Code + Build, define or author a reproduction/regression test and compile it without executing it.
2. During Test + Benchmark, execute that test and preserve the result.
3. If evidence still shows a defect, the next Code + Build plan targets the evidenced root cause.

When the defect is already supported by trustworthy existing runtime evidence, do not manufacture a redundant failing run solely for ritual.

## All-at-once implementation

**Anti-pattern:** Solve a bounded feature by simultaneously adding middleware, distributed storage, configuration, metrics, caching, and migration machinery.

**Preferred behavior:** Split work into independently useful, verifiable phases unless the components are contractually inseparable.

## Review prompts

Before accepting a patch or next-turn plan, ask:

- Which assumption could make this patch wrong?
- What is the simplest implementation that satisfies the same contract?
- Which changed lines are unrelated to the requested behavior?
- What plausible broken implementation would still satisfy the proposed test plan?
- Is complexity being added because it is required now or because it might be useful later?
