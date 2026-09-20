# General-Purpose AI Harness

A progressively disclosed problem-solving harness for general-purpose AI assistants and agents.

The repository packages the **Model-First Adaptive Harness** as a machine-readable, versioned knowledge system instead of forcing the full methodology into every context window.

## Start here

### AI agents

1. Read [AGENTS.md](AGENTS.md).
2. Identify the current dominant gap.
3. Load only the relevant skill from [`.agents/skills/`](.agents/skills/).
4. Read [HARNESS.md](HARNESS.md) only when the compact runtime layer is insufficient or the user explicitly asks for the canonical methodology.

### Humans

- [HARNESS.md](HARNESS.md) — canonical Model-First Adaptive Harness v2.6. This is the source text and is intentionally preserved.
- [AGENTS.md](AGENTS.md) — compact runtime kernel and router.
- [`.agents/skills/`](.agents/skills/) — progressively disclosed methods.
- [docs/architecture.md](docs/architecture.md) — repository architecture and maintenance rules.
- [docs/coverage-map.md](docs/coverage-map.md) — semantic coverage from the canonical Harness to the runtime layer.
- [evals/routing-cases.md](evals/routing-cases.md) — routing regression cases.

## Design

```text
HARNESS.md
Canonical methodology
        |
        v
AGENTS.md
Always-on kernel + router
        |
        v
.agents/skills/*
Load only when relevant
        |
        v
Task-specific work
        |
        v
Evidence -> Update -> Reroute
```

The repository follows two complementary principles:

> Preserve the complexity necessary to make good decisions.

> Remove the complexity unnecessary to understand or execute those decisions.

## Canonical vs derived content

`HARNESS.md` is canonical.

`AGENTS.md`, skills, docs, and evals are **derived runtime representations**. They may compress or reorganize the canonical methodology for progressive disclosure, but they must not silently change its meaning.

When derived files and `HARNESS.md` disagree, treat `HARNESS.md` as authoritative unless the task explicitly updates the canonical Harness.

See [docs/coverage-map.md](docs/coverage-map.md) before changing routing or skill boundaries.

## Compatibility

The skills use the open Agent Skills `SKILL.md` format and are stored under `.agents/skills/`, which Codex discovers as repository-local skills.

Other general-purpose AI systems can still use the repository by starting from `AGENTS.md` and reading the referenced skills as ordinary Markdown.

## Design references

- OpenAI — Harness engineering: repository knowledge as the system of record, short `AGENTS.md`, progressive disclosure.
- OpenAI — Codex customization and repository-local skills.
- Agent Skills specification — `SKILL.md` metadata, on-demand loading, optional resources.

This repository is intentionally small at the entry layer. Do not turn `AGENTS.md` into a second copy of `HARNESS.md`.
