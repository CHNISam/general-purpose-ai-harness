---
name: modeling
description: Build or attack a minimum sufficient model when the relevant reality is not understood well enough to predict, decide, act, or verify. Use for ambiguous goals, missing causal structure, unclear boundaries/states/relations, hidden assumptions, or model-quality testing. Do not use merely because a task is complex if the missing evidence or action is already known.
---

# Modeling

Use this skill for a **Model Gap**.

## Purpose first

When not already clear, determine only what can change the current work:

- Goal — intended real-world state.
- Current Question — what must be understood, chosen, changed, or verified now.
- Success — observable resolution.

When materially relevant, also distinguish Outcome Owner, Decision Owner, Risk Owner, and Priority / Trade-off Policy.

Do not automatically treat the user's proposed feature, task, implementation, workflow, technology, library, service, or terminology as the real Goal.

## Build the minimum sufficient model

Preserve distinctions capable of changing a relevant prediction, decision, action, capability source, constraint, or acceptance result.

Possible dimensions:

- Boundary
- Entities
- State
- Relations
- Dynamics
- Causality
- Dependencies
- Capabilities
- Constraints / Invariants
- Time
- Actions / Inputs
- Authority / Agency
- Observations / Outputs
- Uncertainty

These are tools, not mandatory headings.

Preserve any materially different layer or relation that can change a prediction,
decision, action, reroute, capability-source choice, risk, or acceptance result.
Simplify wording, not semantics.

When relation meaning matters, type it explicitly enough to avoid collapse.
Useful generic meanings include derives-from, requires, provided-by, depends-on,
closes, verifies, and validates. These labels are illustrative rather than a
mandatory ontology.

Do not create information merely because a schema contains a field.

## Optional operators

Use only when triggered.

### First Principles

Use when a convention, inherited solution, or terminology may be mistaken for the requirement.

Ask what fundamentally must be true, what outcome matters, which constraints are conventions, and what requirement would remain if the current implementation disappeared.

### Inversion

Use when failure, reliability, regressions, omissions, or hidden failure modes matter.

Ask: **What would make this definitely fail?**

Work backward to causes, missing states, violated invariants, unsafe assumptions, guards, and required evidence.

### Stress Thinking

Use when scale, boundaries, resources, missing data, concurrency, accuracy, or failure cost may hide structural weakness.

Ask: **What breaks first?**

Use another established method when it is better suited.

## Attack important models

Apply rigor proportional to consequence, uncertainty, novelty, irreversibility, cost, and complexity.

- **Scenario / Run Test** — instantiate a representative concrete case, run it to a concrete result, then trace the important result back to the abstract model. For important cross-layer models distinguish Abstract Pass, Scenario Pass, and Reverse Pass.
- **Separation Test** — can the model distinguish cases that should differ?
- **Counterfactual Test** — if one important condition changes, what should change and remain unchanged?
- **Coverage Test** — check decision-relevant boundaries, exceptions, and failure modes.
- **Grounding Test** — connect important claims to code, data, documents, logs, measurements, behavior, tests, observations, or authoritative sources.
- **Falsification Test** — what evidence would make the model wrong?
- **Generalization Test** — test a materially different or off-nominal case where practical.
- **Bidirectional Traceability Test** — why does each important element exist, and what downstream realization/evidence closes or proves it?
- **Ablation Test** — if an element were removed, could any relevant result change?
- **Typed-Relation / Layer-Preservation Test** — do not flatten materially different meanings such as requirement, capability, solution, implementation, verification, or validation into one arrow.
- **Compilation Integrity Test** — when the model becomes a milestone, plan, task, prompt, or contract, does the downstream form preserve upstream semantics and separable failure modes?
- **Proof-Type Test** — distinguish model structure coherence, implementation verification, real-world validation, and unknown/untested evidence where materially relevant.
- **Change-Impact / Revalidation Test** — after a decision-relevant upstream change, identify affected dependents and revalidate only the affected scope before relying on prior PASS.

## Exit

Stop modeling when the current model is sufficiently trustworthy for the current purpose.

If the exact missing observation is now known, reroute to **evidence-acquisition**.

If several materially different interventions remain, reroute to **decision-analysis**.

If the intervention is known but a capability is missing, reroute to **capability-sourcing**.
