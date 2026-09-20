---
name: modeling
description: Build or challenge a minimum sufficient model when an Understanding Gap prevents reliable prediction, decision, action, or verification. Use for ambiguous goals, unclear boundaries/states/relations, hidden assumptions, or missing causal structure. Do not use merely because a task is complex when the decisive evidence or action is already known.
---

# Modeling

Use this skill for an **Understanding Gap**.

## Orient first

Determine only what can change the current work:

- Goal — intended real-world state.
- Current Question — what must be understood, chosen, changed, or verified now.
- Success — observable resolution.
- Constraints — only those capable of changing action or acceptance.

Ownership, authority, or trade-off policy matters only when it can change a real decision or risk boundary.

Do not treat the user's proposed feature, task, implementation, tool, architecture, or terminology as the Goal by default.

## Build only the model you need

Preserve distinctions capable of changing a relevant:

- prediction;
- decision;
- action;
- capability source;
- constraint;
- proof or acceptance result.

Possible dimensions include boundary, entities, state, relations, dynamics, causality, dependencies, capabilities, constraints, time, actions, authority, observations, and uncertainty.

These are prompts for thought, not mandatory fields.

## Optional methods

Use only when triggered.

- **First principles** — when a convention or inherited solution may be mistaken for the requirement.
- **Inversion / fault analysis** — when hidden failure modes, regressions, reliability, or safety matter.
- **Stress / boundary analysis** — when extremes, scale, concurrency, missing data, or resource pressure may expose weakness.
- **Causal analysis** — when the decision depends on why something happens.
- **Experiment / simulation / spike** — when a controlled observation can resolve uncertainty more cheaply than more argument.

Use another established method when it is better suited.

## Challenge important models

Do not run a fixed checklist. Ask only the checks that can expose a decision-relevant weakness:

- Can the model distinguish cases that should produce different outcomes?
- Does it make useful counterfactual predictions?
- Are important claims grounded in reality, and what would falsify them?
- Have relevant boundaries, exceptions, or failure modes been omitted?
- Can important elements trace to the current purpose, and can irrelevant ones be removed?

Increase rigor with consequence, uncertainty, novelty, irreversibility, and cost.

## Exit

Stop when remaining uncertainty is unlikely to change the next decision, action, capability source, constraint, or proof.

If the decisive missing observation becomes known → `evidence-acquisition` or `observability-coverage`.

If materially different viable actions remain → `decision-analysis`.

If the intervention is understood but a capability is missing → `capability-sourcing`.
