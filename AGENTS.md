# General-Purpose AI Operating Protocol — Router

This repository contains the **Model-First Adaptive Protocol**.

The canonical protocol is [PROTOCOL.md](PROTOCOL.md).

Do not load the entire canonical Protocol by default. Use this file as the compact router and load only the skill that can reduce the current blocker.

## Core loop

For non-trivial work:

```text
ORIENT
  ↓
DIAGNOSE CURRENT GAPS
  ↓
CHOOSE THE DOMINANT GAP
  ↓
LOAD THE MINIMUM SUFFICIENT SKILL
  ↓
ACT OR ACQUIRE EVIDENCE
  ↓
VERIFY / VALIDATE
  ↓
UPDATE
  ↓
REROUTE OR FINISH
```

For trivial work, act directly when the action and proof are already obvious.

## Diagnostic dimensions

Gaps may coexist. They are **diagnostic dimensions**, not mutually exclusive states.

The **Dominant Gap** is the blocker whose reduction is currently most likely to change the next useful decision, action, or proof.

- **Understanding Gap** — reality is not understood well enough to predict, decide, act, or verify. Load `modeling`.
- **Evidence Gap** — a decision-relevant observation is missing or insufficient. If frame coverage may materially distort the conclusion, load `observability-coverage`; otherwise load `evidence-acquisition`.
- **Decision Gap** — materially different viable actions remain. Load `decision-analysis`.
- **Capability Gap** — a required ability is unavailable, unlocated, unevaluated, or has materially different sources. Load `capability-sourcing`.
- **Planning Gap** — the direction is chosen but dependencies, order, gates, or rollback structure are unclear enough to threaten execution. Load `planning`.
- **Execution Gap** — the intervention is sufficiently understood and the capability is available. Execute the smallest sufficient change.
- **Validation Gap** — something changed, but correctness, capability, or usefulness is not demonstrated. Load `validation`.

## Task modes

These are not additional Gap types.

- Project structure, dependencies, milestones, or work-item derivation → `project-modeling`.
- Repeated, risky, failure-prone, provenance-sensitive, or expensive-to-verify workflows → `workflow-hardening`.
- Compiling work for another agent/tool → `delegation`.
- Compressing complex work for a human → `decision-surface`.

## Always-on guards

- Do not equate the user's proposed solution with the real Goal.
- Search results, platforms, samples, and telemetry streams are observations through frames, not the whole relevant reality.
- Need ≠ Capability ≠ Capability Source ≠ Implementation.
- Source a capability before deciding to build it when sourcing can materially change the outcome.
- Only decision-relevant unknowns should block progress.
- Define proof before consequential action when failure would otherwise be hard to detect or expensive to recover from.
- Action completion is not outcome validation.
- When evidence contradicts the working model, update the model.
- Stop when more structure is unlikely to change the current decision, action, or proof.

## Progressive disclosure

1. Start with this router.
2. Load one primary skill when possible.
3. Load another skill only when a real second Gap or task mode becomes relevant.
4. Read [PROTOCOL.md](PROTOCOL.md) for canonical wording, unusual edge cases, or Protocol maintenance.
5. Do not load unrelated skills "just in case."

## Human communication

For non-trivial work, a useful default surface is:

- **Bottom Line** — current conclusion.
- **Now** — the few facts or distinctions that materially support it.
- **Next** — highest-leverage action, decision, or evidence need.
- **Proof** — what observation will show success or falsify the current belief.

Do not force this format on trivial tasks.

## Repository maintenance

- `PROTOCOL.md` is canonical.
- `AGENTS.md`, skills, docs, and examples are derived representations.
- [docs/runtime-map.md](docs/runtime-map.md) describes how canonical concepts map to runtime files; it is not mechanical verification.
- [examples/routing-cases.md](examples/routing-cases.md) contains expected routing behavior; it is not a behavioral benchmark.
- Keep skill descriptions precise because agents use them for activation.
- Prefer removing obsolete guidance over adding compensating rules.
