# Method Registry

This is a **non-canonical reference map**.

It points to mature external methods, standards, and harness patterns that may be
sourced when they fit the current problem. It does not make those methods
mandatory, copy their requirements into the Protocol, or replace `PROTOCOL.md`.

Use the Protocol first to identify the current Gap and intended use. Then load or
consult only the external method capable of changing the current model,
decision, action, or proof.

## Selection rule

Prefer:

```text
current intended use
    ↓
mature relevant method / standard
    ↓
tailor only the useful capability
    ↓
build only the unresolved delta
```

Do not cargo-cult a complete framework.

When version or wording matters, verify the current official source before
relying on it.

## Reference methods

| Need | External reference | Useful capability |
|---|---|---|
| Model intended use, credibility, permissible use, provenance, uncertainty | NASA Standard for Models and Simulations (NASA-STD-7009B) — https://standards.nasa.gov/node/263 | Scope a model to its intended use; distinguish verification, validation, input/data pedigree, uncertainty, and credibility. |
| Operational scenarios / nominal and off-nominal cases | NASA Systems Engineering Handbook, ConOps Appendix — https://www.nasa.gov/reference/appendix-s-concept-of-operations-annotated-outline/ | Exercise a model through concrete operational scenarios and expose missing capabilities or safeguards. |
| Requirements engineering and operational scenarios | ISO/IEC/IEEE 29148:2018 — https://www.iso.org/standard/72089.html | Requirements lifecycle discipline; operational scenarios for evaluating requirements and design. |
| Architecture descriptions, viewpoints, model kinds | ISO/IEC/IEEE 42010:2022 — https://www.iso.org/standard/74393.html | Select viewpoints / model kinds based on stakeholder concerns instead of forcing one universal architecture representation. |
| Alternatives, trade studies, uncertainty-aware decisions | NASA Systems Engineering Handbook, Decision Analysis — https://www.nasa.gov/reference/6-8-decision-analysis/ | Define decision need and criteria, cover alternative space, evaluate uncertainty, and document pruning / recommendation rationale. |
| Alternative design solution generation and trade studies | NASA Systems Engineering Handbook, Design Solution Definition — https://www.nasa.gov/reference/4-4-design-solution-definition/ | Translate requirements / logical decomposition into alternative solutions before selecting a design. |
| Specification-driven software delivery | GitHub Spec Kit — https://github.github.com/spec-kit/ | Keep intent and evidence ahead of implementation; use independent processes for specification, bug fixing, and idea assessment rather than one mandatory workflow. |
| Agent-first repository harness / structured knowledge | OpenAI Harness Engineering — https://openai.com/index/harness-engineering/ | Keep repository knowledge as system of record, use small maps and progressive disclosure, and mechanize high-value invariants with linters, structural tests, CI, and feedback loops rather than relying on documentation alone. |
| Repeatable operational mechanisms | AWS Well-Architected, Building mechanisms — https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/building-mechanisms.html | Replace human best-effort with repeatable/scalable tools and processes, drive adoption, inspect results, and iterate; useful when a recurring rule must become an operating mechanism rather than a reminder. |
| Repository harness authoring / workflow iteration | OpenAI Cookbook, Iterating development workflows with Codex — https://github.com/openai/openai-cookbook/blob/main/examples/codex/iterating-development-workflows-with-codex.md | Inspect the live repository first, right-size the harness, preserve local ownership/conventions, separate planning from implementation, use explicit acceptance/verification, and iteratively improve the harness from observed failures. Its file layout is an example, not a mandatory schema. |
| Reusable agent Skill authoring | OpenAI Skills, `skill-creator` — https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md | Match degrees of freedom to task fragility, use progressive disclosure, package deterministic repeated work as scripts, validate the Skill, and iterate from real usage. |
| Agent instruction placement / skills / deterministic hooks | Anthropic, Steering Claude Code — https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more | Put persistent context, conditional procedures, isolated subagents, and deterministic hooks in the layer that matches loading, authority, context cost, and reliability. |
| Repository / path-scoped agent instructions | GitHub Copilot custom instructions — https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions | Separate repository-wide, path-specific, and agent instructions; keep reusable prompt files distinct from always-on repository context where the runtime supports them. |

## Boundary

These references are capability sources, not authorities over the user's Goal.

If an external method:

- assumes a different problem;
- requires unjustified ceremony;
- collapses a decision-relevant distinction;
- conflicts with stronger evidence;
- or costs more than the uncertainty it removes;

tailor it or do not use it.
