# General-Purpose AI Operating Protocol

[![Protocol Conformance](https://github.com/CHNISam/general-purpose-ai-operating-protocol/actions/workflows/conformance.yml/badge.svg)](https://github.com/CHNISam/general-purpose-ai-operating-protocol/actions/workflows/conformance.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/CHNISam/general-purpose-ai-operating-protocol/badge)](https://securityscorecards.dev/viewer/?uri=github.com/CHNISam/general-purpose-ai-operating-protocol)

A **model-agnostic behavioral engineering protocol** for general-purpose AI assistants and agents: diagnose the real blocker, source capabilities before building, preserve evidence/proof semantics, and mechanically enforce the subset that can be checked deterministically.

The repository packages the **Model-First Adaptive Protocol** as a versioned canonical methodology, a small router, on-demand skills, real-world failure evals, and executable conformance policy. It is designed to improve behavior inside existing AI runtimes rather than replace them.

## 60-second example

A real historical failure pattern:

> **Task:** obtain reliable structured information from a web source.

**Without the Protocol discipline**, the assistant jumped directly from the need to a custom implementation: browser automation → DOM extraction → OCR/model choice → bespoke pipeline.

**With the Protocol model**, the task routes differently:

```text
Need
↓
Required capability
↓
Capability Gap
↓
inspect existing/internal/standard/library/API/workflow sources
↓
fit-gap + cheap representative spike
↓
select the source
↓
define proof
↓
build only the unresolved delta
```

The important change is not more prompting. It is preventing **Need → Implementation** collapse before the capability source and proof are known.

This failure is recorded as [R001](evals/real-world-retrospective-pilot-v0.1.md). The same failure class is now represented in the runtime skills and executable policy where deterministic checks are possible.

## Evidence at a glance

| Evidence layer | Current public state |
|---|---|
| Real historical failure patterns | **12** sanitized retrospective cases |
| Deterministic conformance | **8/8** public fixtures passing |
| Mechanical policy | JSON Schema + OPA/Rego |
| Portable enforcement | CI-built OPA WebAssembly bundle |
| Repository engineering signal | Protocol Conformance CI + OpenSSF Scorecard |
| Controlled Protocol OFF vs ON behavioral eval | **Specified, not yet run** |

This table deliberately separates what is already demonstrated from what remains unproven.

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
- a claim that every routing decision can be mechanically proven.

The repository now also includes a **reference executable enforcement layer** for the subset of Protocol invariants that can be checked deterministically. That layer complements model judgment; it does not replace it.

The Protocol supports model judgment. It does not replace judgment.

## Quick start

### AI systems — minimal path

1. Read [AGENTS.md](AGENTS.md).
2. Load only the skill it routes you to.
3. Use [PROTOCOL.md](PROTOCOL.md) only for canonical wording, edge cases, or methodology maintenance.
4. When the task produces a supported machine-readable decision envelope, run the [executable enforcement](enforcement/) as an additional gate.

For precise canonical navigation without loading the whole document, use [docs/protocol-index.md](docs/protocol-index.md).

### AI systems

1. Read [AGENTS.md](AGENTS.md).
2. Diagnose the current blocker.
3. Load only the relevant skill from [`.agents/skills/`](.agents/skills/).
4. Read [PROTOCOL.md](PROTOCOL.md) only when canonical wording, unusual edge cases, or Protocol maintenance require it.

Codex can discover repository `AGENTS.md` instructions and repository-local skills automatically. Other AI systems that can read repository files can use the same structure by starting from `AGENTS.md`.

### Humans

- [PROTOCOL.md](PROTOCOL.md) — canonical **Model-First Adaptive Protocol v2.9.1**.
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

v2.9.1 builds on v2.9.0 model integrity with a staged-audit rule for existing
layered models: downstream material may be inspected to test consistency, but
layers are accepted and derived in order rather than being prematurely treated
as validated.

## Executable enforcement

The repository contains a real mechanical policy layer in [`enforcement/`](enforcement/) and a public conformance suite in [`conformance/`](conformance/).

The current reference implementation uses:

- **JSON Schema** for the versioned machine-readable decision envelope;
- **Open Policy Agent / Rego** for deterministic Protocol invariants;
- **public fixtures** for allow/deny regression behavior;
- **GitHub Actions** for automatic conformance checks;
- **OPA WebAssembly builds** for portable embedding without an always-on server.

Examples of mechanically blocked states include VERIFIED evidence without provenance, generated output promoted directly to VERIFIED evidence, reality-changing action without proof defined first, unresolved decision-relevant evidence conflicts at completion, and a claimed VALIDATION PASS without observed validation evidence.

A mechanical PASS is deliberately weaker than a real-world VALIDATION PASS. The executable layer proves only the invariants it actually encodes.

## Evidence and behavioral evals

This Protocol is iterated from real task failures, not only speculative framework design.

The first public retrospective pilot records **12 sanitized historical failure patterns**
from real AI-assisted work. Eleven were already directly covered by v2.9.0; one exposed
a missing staged-audit rule and produced the v2.9.1 correction.

See:

- [evals/real-world-retrospective-pilot-v0.1.md](evals/real-world-retrospective-pilot-v0.1.md) — real historical failures, user corrections, expected Protocol behavior, and coverage results.
- [evals/controlled-pilot-spec.md](evals/controlled-pilot-spec.md) — a frozen Protocol OFF vs ON behavioral pilot design.
- [evals/README.md](evals/README.md) — evidence policy and scoring rules.

The retrospective pilot demonstrates **coverage of real observed failure modes**.
It does not by itself prove causal effectiveness; controlled behavioral and
real-world outcome validation remain separate evidence stages.

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
