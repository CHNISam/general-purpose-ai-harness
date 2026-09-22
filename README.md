# General-Purpose AI Operating Protocol

A progressively disclosed operating protocol for general-purpose AI assistants and agents.

The repository packages the **Model-First Adaptive Protocol** as a versioned canonical methodology, a small router, and on-demand skills. It is designed to guide judgment inside existing AI runtimes rather than replace them.

## What this is

This project provides:

- a preserved canonical operating protocol for non-trivial problem solving;
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

- [PROTOCOL.md](PROTOCOL.md) — canonical **Model-First Adaptive Protocol v2.9.0**.
- [AGENTS.md](AGENTS.md) — compact router and always-on guards.
- [`.agents/skills/`](.agents/skills/) — conditional methods and task modes.
- [docs/architecture.md](docs/architecture.md) — repository architecture and maintenance policy.
- [docs/runtime-map.md](docs/runtime-map.md) — descriptive mapping from canonical concepts to runtime files.
- [docs/method-registry.md](docs/method-registry.md) — non-canonical pointers to mature external methods and standards that can be sourced when useful.
- [examples/routing-cases.md](examples/routing-cases.md) — expected routing examples, not an automated benchmark.

## Recommended operating pattern

The primary reader is normally a **general-purpose AI assistant** such as a chat-oriented frontier model.

```text
User problem
    ↓
General-purpose AI reads AGENTS.md + relevant skills
    ↓
understand / research / model / decide
    ↓
compile minimum sufficient execution contract
    ↓
Coding Agent reads the TARGET code repository
    ↓
implement + verify
```

Do **not** make the Coding Agent read this Protocol repository by default.

The Coding Agent should normally receive the task-specific prompt and follow the target repository's own `AGENTS.md`, code, tests, documentation, constraints, and acceptance criteria.

Pass Protocol material downstream only when the Protocol itself is being maintained, the user explicitly requests it, or methodology-level reasoning is intentionally delegated.

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

This follows three constraints:

> Preserve distinctions that can change the current decision, action, constraint, capability source, reroute, or proof.

> Compress language, not decision-relevant semantics.

> Remove structure that cannot.

v2.9.0 builds on v2.8 model integrity with intended-use / schema selection,
model-use envelopes, explicit separation of representative scenarios from evidence,
claim–evidence fit, sufficient alternative / solution-space coverage, and sourcing
of mature external methods before inventing custom methodology.

## Why progressive disclosure

Frontier models already possess substantial general reasoning ability. The Protocol should therefore add only the guidance that materially improves behavior for the current task.

OpenAI's current guidance similarly favors concise, outcome-oriented instructions for capable models, and its Agent Skills design loads skill metadata first and full instructions only when the skill is selected.

The repository therefore keeps `AGENTS.md` small and moves conditional procedures into skills.

## Preservation policy

Progressive disclosure means **move detail out of always-on context**, not delete accumulated methodology.

Named methods, tests, distinctions, and decision rules that have been deliberately retained should not be silently collapsed into "equivalent" prose merely to shorten the repository.

When a concept is too detailed for `AGENTS.md`:
- keep it in the relevant Skill or canonical Protocol;
- move supporting detail into a reference if needed;
- preserve historical versions under `docs/history/` when making major conceptual changes.

When semantic equivalence is uncertain, prefer restoring the known version from Git history and applying a minimal diff over regenerating it from memory.

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

See [docs/method-registry.md](docs/method-registry.md) for non-canonical external
methods and standards that may be sourced when relevant.

- OpenAI — Harness engineering: short repository maps, structured knowledge, progressive disclosure, and mechanical enforcement only where useful.
- OpenAI — Codex customization: concise `AGENTS.md`, repository-local skills, and task-specific instructions.
- OpenAI — reasoning and model guidance: capable models often benefit from simple, direct, outcome-oriented prompts.

The Protocol is intended to work **inside** existing agent harnesses and chat interfaces rather than reimplement their runtime infrastructure.
