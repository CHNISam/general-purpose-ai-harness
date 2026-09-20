# General-Purpose AI Harness — Runtime Router

This repository contains the **Model-First Adaptive Harness**.

The canonical methodology is [HARNESS.md](HARNESS.md).

Do **not** load the entire canonical Harness by default. Use this file as the runtime kernel and load only the skill relevant to the current problem.

Do **not** rewrite, normalize, shorten, or "improve" `HARNESS.md` unless the task explicitly requests a canonical Harness change.

## Core runtime

For non-trivial work:

```text
LOCATE STATE
    ↓
IDENTIFY DOMINANT GAP
    ↓
LOAD THE MINIMUM SUFFICIENT SKILL
    ↓
IDENTIFY REQUIRED INTERVENTION
    ↓
CHECK REQUIRED CAPABILITY
    ↓
SOURCE CAPABILITY IF NEEDED
    ↓
CHOOSE NEXT ACTION
    ↓
DEFINE PROOF
    ↓
ACT / ACQUIRE EVIDENCE
    ↓
OBSERVE REALITY
    ↓
UPDATE
    ↓
REROUTE OR FINISH
```

## Gap router

Route by the **current blocker**, not by the wording of the user's request.

- **Model Gap** — relevant reality is not understood well enough to predict, decide, act, or verify. Load `modeling`.
- **Evidence Gap** — the needed observation is known but reliable evidence is missing. Load `evidence-acquisition`.
- **Decision Gap** — materially different viable actions remain. Load `decision-analysis`.
- **Capability Gap** — the intervention is understood but a required capability is unavailable, unlocated, unevaluated, or has materially different sources. Load `capability-sourcing`.
- **Planning Gap** — the direction is chosen but dependent execution structure is unclear. Load `planning`.
- **Reality Gap** — the change is sufficiently understood and the required capability is available. Execute the smallest sufficient intervention.
- **Verification / Validation Gap** — something changed, but correctness or usefulness is not demonstrated. Load `validation`.

Additional task modes:

- Project structure, dependency, milestone, or work-item derivation → `project-modeling`.
- Repeated / risky / provenance-sensitive execution that needs observable gates → `harness-engineering`.
- Compiling work for another agent/tool → `delegation`.
- Complex human-facing output that risks becoming a reasoning dump → `decision-surface`.

## Always-on invariants

- Need ≠ capability ≠ capability source ≠ implementation.
- Do not mechanically translate a request into a task or implementation.
- Do not use more reasoning to hide an Evidence Gap.
- Do not treat generated analysis as a Source of Truth.
- Do not fabricate precision to remove an Unknown.
- Only decision-relevant Unknowns should block progress.
- Source a capability before deciding to build it when the sourcing choice materially matters.
- Build the delta, not the solved problem.
- Do not manufacture alternatives when one action is clearly implied.
- Define proof before consequential action.
- Action completion is not outcome validation.
- When evidence contradicts the model, update the model rather than defend the plan.
- Stop when the current purpose has sufficient evidence; do not perform methodology for its own sake.

## Progressive disclosure

1. Use this router first.
2. Read one primary `SKILL.md` when possible.
3. Load a second skill only when the task genuinely crosses another Gap or mode.
4. Read `HARNESS.md` for canonical wording, unusual edge cases, or methodology maintenance.
5. Do not load unrelated skills "just in case."

## Human communication

For non-trivial work, default to a compact decision surface:

- **Bottom Line** — the most important conclusion.
- **Now** — 1–3 facts/state distinctions that materially support it.
- **Next** — one highest-leverage action or the next decision/evidence needed.
- **Proof** — the observation that will show success.

Do not force this format on trivial tasks. Do not expose full background, model, alternatives, or methodology unless they materially change the decision, risk requires them, or the user asks.

## Repository maintenance

- `HARNESS.md` is canonical.
- Runtime files are derived and must remain traceable to canonical sections.
- Before changing routing or skill boundaries, update or check [docs/coverage-map.md](docs/coverage-map.md).
- Use [evals/routing-cases.md](evals/routing-cases.md) as regression cases.
- Keep skill descriptions precise because agents use them for activation.
- Prefer focused skills over one giant skill.
