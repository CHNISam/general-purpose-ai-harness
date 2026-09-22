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

It should remain understandable as one coherent protocol without sacrificing deliberately preserved methods or tests.

Canonical changes are justified when they alter:
- the conceptual layers;
- diagnostic dimensions;
- core guards;
- action / proof discipline;
- communication contract.

Do not promote every useful technique into an always-on primitive. Preserve useful detail in the appropriate progressive layer.

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
2. identify affected router / skill / example behavior through change-impact analysis;
3. treat affected derived representations as requiring revalidation until synchronized;
4. update only those derived files that need to change;
5. update `docs/runtime-map.md` if the mapping changes;
6. update examples when expected routing or model-integrity behavior changes;
7. re-check that the derived runtime preserves the canonical distinction and proof type rather than only matching terminology.

### Runtime-only changes

Runtime files may be reorganized for activation quality or progressive disclosure without changing canonical semantics.

When doing so:
- do not change the canonical Protocol silently;
- keep `AGENTS.md` small;
- prefer relocation or deduplication only when semantic coverage is preserved;
- do not call examples "evals" unless model behavior is actually measured.

## Preservation policy

Progressive disclosure is a **loading strategy**, not permission to erase semantics.

- Do not delete or rewrite a deliberately preserved named test, method, distinction, or rule solely to make the Protocol shorter.
- If material is too detailed for the router, move it to a Skill or reference.
- If a refactor changes terminology, preserve the old semantics first and apply the smallest explicit transformation.
- When unsure whether a rewrite is equivalent, restore the known version from Git history and patch it rather than regenerating it.
- Major conceptual revisions should preserve a historical snapshot under `docs/history/`.

## Responsibility boundary

This repository is normally consumed by the upstream general-purpose AI.

A downstream Coding Agent should normally receive a compiled execution contract and operate on the target code repository. It should not be required to read this Protocol repository unless methodology-level reasoning is explicitly part of its task.

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

> Compress language, not decision-relevant semantics.

A derived artifact that copies mutable canonical facts should either be regenerated
from the authoritative source or carry explicit staleness/revalidation semantics.
Do not maintain a silent second live truth.
