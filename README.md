# General-Purpose AI Operating Protocol

A progressively disclosed operating protocol for general-purpose AI assistants and agents.

The repository packages the **Model-First Adaptive Protocol** as a small router plus on-demand skills. It is designed to guide judgment inside existing AI runtimes rather than replace them.

## What this is

This project provides:

- a compact operating protocol for non-trivial problem solving;
- a small `AGENTS.md` router;
- progressively disclosed `SKILL.md` methods;
- explicit evidence, capability, decision, and validation discipline;
- examples of expected routing behavior.

It is **not**:

- an agent runtime or SDK;
- an executor or tool orchestration framework;
- a formal decision procedure;
- a claim that every routing decision can be mechanically proven;
- a CI or benchmark suite.

The Protocol supports model judgment. It does not replace judgment.

## Start here

### AI systems

1. Read [AGENTS.md](AGENTS.md).
2. Diagnose the current blocker.
3. Load only the relevant skill from [`.agents/skills/`](.agents/skills/).
4. Read [PROTOCOL.md](PROTOCOL.md) only when canonical wording, unusual edge cases, or Protocol maintenance require it.

Codex can discover repository `AGENTS.md` instructions and repository-local skills automatically. Other AI systems that can read repository files can use the same structure by starting from `AGENTS.md`.

### Humans

- [PROTOCOL.md](PROTOCOL.md) — canonical **Model-First Adaptive Protocol v2.7**.
- [AGENTS.md](AGENTS.md) — compact router and always-on guards.
- [`.agents/skills/`](.agents/skills/) — conditional methods and task modes.
- [docs/architecture.md](docs/architecture.md) — repository architecture and maintenance policy.
- [docs/runtime-map.md](docs/runtime-map.md) — descriptive mapping from canonical concepts to runtime files.
- [examples/routing-cases.md](examples/routing-cases.md) — expected routing examples, not an automated benchmark.

## Conceptual model

```text
Purpose
  ↓
Diagnosis
  ↓
Dominant Gap
  ↓
Conditional Method
  ↓
Action / Evidence
  ↓
Verification / Validation
  ↓
Update
```

The important distinction is that **Gaps are diagnostic dimensions, not mutually exclusive states**. Several may coexist. The Dominant Gap is simply the one whose reduction is most likely to change the next useful decision, action, or proof.

Methods such as first-principles reasoning, inversion, experiments, trade studies, planning, and workflow hardening are conditional tools. They are not mandatory stages.

## Design

```text
PROTOCOL.md
Canonical operational doctrine
        │
        ▼
AGENTS.md
Small router + guards
        │
        ▼
.agents/skills/*
Load only when relevant
        │
        ▼
Task-specific work
        │
        ▼
Evidence → Update → Reroute
```

This follows two constraints:

> Preserve distinctions that can change the current decision, action, constraint, capability source, or proof.

> Remove structure that cannot.

## Why progressive disclosure

Frontier models already possess substantial general reasoning ability. The Protocol should therefore add only the guidance that materially improves behavior for the current task.

OpenAI's current guidance similarly favors concise, outcome-oriented instructions for capable models, and its Agent Skills design loads skill metadata first and full instructions only when the skill is selected.

The repository therefore keeps `AGENTS.md` small and moves conditional procedures into skills.

## Canonical vs derived content

`PROTOCOL.md` is canonical.

`AGENTS.md`, skills, docs, and examples are derived representations. They may compress or reorganize the canonical Protocol for progressive disclosure, but should not silently change its meaning.

[docs/runtime-map.md](docs/runtime-map.md) is a maintenance aid, not proof that semantic coverage is complete.

[examples/routing-cases.md](examples/routing-cases.md) records expected behavior, not measured model performance.

## Development principle

Do not add a new concept, rule, skill, script, validator, or automation merely to make the system look more complete.

Add structure when repeated real tasks show that the current Protocol is insufficient.

Prefer:

```text
real failure
→ diagnose
→ smallest useful correction
→ use again
```

over speculative framework growth.

## Design references

- OpenAI — Harness engineering: short repository maps, structured knowledge, progressive disclosure, and mechanical enforcement only where useful.
- OpenAI — Codex customization: concise `AGENTS.md`, repository-local skills, and task-specific instructions.
- OpenAI — reasoning and model guidance: capable models often benefit from simple, direct, outcome-oriented prompts.

The Protocol is intended to work **inside** existing agent harnesses and chat interfaces rather than reimplement their runtime infrastructure.
