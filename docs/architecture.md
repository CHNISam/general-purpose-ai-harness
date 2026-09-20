# Architecture

## Goal

Make the Model-First Adaptive Harness usable by general-purpose AI without loading the entire methodology into every context window.

## Layers

```text
Layer 0 — Canonical methodology
HARNESS.md

Layer 1 — Always-on runtime
AGENTS.md

Layer 2 — Progressive methods
.agents/skills/*/SKILL.md

Layer 3 — Verification
docs/coverage-map.md
evals/routing-cases.md
```

### Layer 0 — Canonical methodology

`HARNESS.md` preserves the complete methodology and wording supplied by the project owner.

It is the semantic source of truth for this repository.

Do not silently rewrite it as part of runtime refactoring.

### Layer 1 — Runtime router

`AGENTS.md` should stay small and stable.

Its job is to:

- preserve the non-negotiable invariants;
- identify the dominant Gap;
- point to the relevant skill;
- prevent premature implementation;
- define the default communication surface.

It is a map, not an encyclopedia.

### Layer 2 — Skills

Each skill should:

- have a narrow trigger;
- state when it should and should not be used;
- contain enough procedure to operate without loading unrelated methods;
- preserve the relevant canonical semantics;
- route back to evidence and rerouting rather than pretending to be a terminal workflow.

Skill metadata matters. Agents often see `name` and `description` before the body.

### Layer 3 — Verification

`docs/coverage-map.md` protects against semantic loss during decomposition.

`evals/routing-cases.md` protects against behavioral regression: the router should load the right skill for representative tasks and avoid loading irrelevant ones.

## Change policy

### Canonical changes

When intentionally changing `HARNESS.md`:

1. make the canonical change explicitly;
2. identify affected runtime concepts;
3. update the relevant skill(s) and router only as needed;
4. update the coverage map;
5. add or update routing regression cases when behavior changes.

### Runtime-only changes

Runtime files may be reorganized for clarity, progressive disclosure, or better activation without changing canonical semantics.

When doing so:

1. do not edit `HARNESS.md`;
2. preserve coverage;
3. prefer moving detail out of always-on context;
4. verify routing cases.

## Skill authoring rules

- Use Agent Skills YAML frontmatter with `name` and `description`.
- Keep names kebab-case.
- Make descriptions explicit about trigger conditions.
- Keep the body focused; do not restate the whole Harness.
- Prefer references/resources only when the skill would otherwise become large.
- Do not create a skill for a method that is cheap enough to remain an inline invariant.
- Avoid overlapping skills unless the overlap represents a real multi-gap task.

## Repository principle

The Harness should obey its own principle:

> Use the minimum sufficient context for the current problem.
