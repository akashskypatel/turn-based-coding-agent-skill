# Source Attribution and Integration Notes

This module incorporates and adapts ideas from the public repository:

- `multica-ai/andrej-karpathy-skills/skills/karpathy-guidelines/SKILL.md`
  - https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md
- `multica-ai/andrej-karpathy-skills/EXAMPLES.md`
  - https://github.com/multica-ai/andrej-karpathy-skills/blob/main/EXAMPLES.md

The source skill identifies its license as MIT. The material here is a distilled and workflow-adapted formulation rather than a verbatim copy of the example implementations.

## Concepts incorporated

- Surface material assumptions before coding.
- Present materially different interpretations rather than choosing silently.
- Prefer the simplest sufficient implementation.
- Avoid speculative abstractions and features.
- Keep changes surgical and consistent with surrounding style.
- Remove only artifacts made unused by the active change.
- Convert vague tasks into measurable success criteria.
- Tie implementation steps to explicit verification.
- Reproduce defects with targeted tests before claiming a fix when trustworthy reproduction evidence is not already available.
- Split large work into independently verifiable increments when practical.

## Adaptation to this skill

The source examples commonly describe an immediate test-first loop. `turn-based-coding-agent` intentionally separates source modification from runtime validation, so that pattern is adapted as follows:

- test/reproduction **design and source changes** occur in Code + Build;
- those test targets are **compiled** during Code + Build;
- runtime **execution** occurs only in Test + Benchmark;
- observed failures drive the next Code + Build plan;
- optional independent Review may challenge the diagnosis or plan without editing code.

This preserves the source guidance's goal-driven verification principle without weakening the canonical turn boundary.
