# Architecture

## Goal

Make the Model-First Adaptive Protocol usable by general-purpose AI without loading the full canonical document into every context window.

The repository is a **knowledge and instruction layer**, not an agent runtime.

## Layers

```text
Layer 0 — Canonical protocol
PROTOCOL.md

Layer 1 — Compact router
AGENTS.md

Layer 2 — Progressive methods
.agents/skills/*/SKILL.md

Layer 3 — Maintenance aids
docs/runtime-map.md
examples/routing-cases.md
```

### Layer 0 — Canonical protocol

`PROTOCOL.md` defines the conceptual model, core guards, and operating doctrine.

It should remain compact enough to be understandable as one coherent protocol.

Canonical changes are justified when they alter:
- the conceptual layers;
- diagnostic dimensions;
- core guards;
- action / proof discipline;
- communication contract.

Do not add detail merely because a useful technique exists.

### Layer 1 — Router

`AGENTS.md` is the always-on map.

Its job is to:
- orient the agent;
- define Gap semantics;
- select a relevant skill;
- preserve a small set of guards;
- point to deeper material.

It should not become a second copy of `PROTOCOL.md`.

### Layer 2 — Skills

Skills contain conditional methods and task modes.

Each skill should:
- have a narrow trigger;
- state when it should and should not be used;
- contain only procedure that benefits from being loaded on demand;
- route back to evidence, action, verification, or another real Gap;
- avoid re-declaring the whole Protocol.

Skills are not the canonical ontology.

A skill may package a method, domain procedure, or reusable workflow without making it a core Protocol concept.

### Layer 3 — Maintenance aids

`docs/runtime-map.md` is a descriptive map from canonical concepts to runtime files.

It helps maintain traceability, but it is **not mechanical verification**.

`examples/routing-cases.md` contains representative routing examples and expected behavior.

It is **not an automated eval or regression test** until an actual runner measures model behavior.

## Concept classes

When editing the Protocol, keep these classes separate:

| Class | Question |
|---|---|
| Purpose | What outcome matters? |
| Diagnosis | What insufficiency blocks progress? |
| Method | What technique may reduce it? |
| Guard | What must not be violated? |
| Action / Proof | What changes next, and how do we know? |
| Communication | What does the human or downstream executor need? |

Avoid placing concepts from different classes into one flat taxonomy.

## Gap semantics

A Gap is a diagnostic dimension, not a state.

Several Gaps may coexist.

The Dominant Gap is a prioritization decision: which insufficiency should be reduced first because it is most likely to change the next useful decision, action, or proof?

Do not attempt to force the Gap set into a mutually exclusive state machine.

## Change policy

### Canonical changes

When intentionally changing `PROTOCOL.md`:

1. make the conceptual change explicitly;
2. identify affected router / skill behavior;
3. update only those derived files that need to change;
4. update `docs/runtime-map.md` if the mapping changes;
5. update examples when expected routing changes.

### Runtime-only changes

Runtime files may be reorganized for activation quality or progressive disclosure without changing canonical semantics.

When doing so:
- do not change the canonical Protocol silently;
- keep `AGENTS.md` small;
- prefer deletion or consolidation over compensating rules;
- do not call examples "evals" unless model behavior is actually measured.

## Skill authoring

- Use Agent Skills YAML frontmatter with `name` and `description`.
- Keep names concrete and kebab-case.
- Make triggers explicit.
- Prefer one clear purpose per skill.
- Put optional detail in the skill body, not the router.
- Do not create a skill solely to preserve a named concept.
- If a method is cheap and universal enough to remain a guard, keep it inline.

## Automation policy

Scripts, tests, CI, validators, or mechanical enforcement are optional capability sources.

Add them when repeated failure, scale, risk, or verification cost justifies ownership.

Do not add automation merely to make the repository look more engineered.

## Repository principle

> Use the least structure that reliably improves the current decision, action, or proof.
