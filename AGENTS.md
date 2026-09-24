# General-Purpose AI Operating Protocol — Router

This repository contains the **Model-First Adaptive Protocol**.

The canonical methodology is [PROTOCOL.md](PROTOCOL.md).

Do **not** load the entire canonical Protocol by default. Use this file as the runtime kernel and load only the skill relevant to the current problem.

Do **not** rewrite, normalize, shorten, or "improve" `PROTOCOL.md` unless the task explicitly requests a canonical Protocol change.

## Intended use

The primary consumer is a **general-purpose AI assistant** doing upstream understanding,
research, modeling, decision-making, capability sourcing, planning, and prompt compilation.

When work is delegated to a Coding Agent, compile the minimum sufficient execution contract.
Do **not** tell the Coding Agent to read this Protocol repository by default.

The Coding Agent should normally read the **target code repository's** own instructions,
code, tests, documentation, and other Sources of Truth.

## Core runtime

For non-trivial work:

```text
LOCATE STATE
    ↓
CHECK RELEVANT EXISTING CLOSURE
    ↓
IDENTIFY DOMINANT GAP
    ↓
LOAD THE MINIMUM SUFFICIENT SKILL
    ↓
IDENTIFY REQUIRED CHANGE / OUTCOME
    ↓
INSPECT RELEVANT CAPABILITY SURFACE WHEN MATERIAL
    ↓
SOURCE / SELECT CAPABILITY IF NEEDED
    ↓
ESTABLISH / REUSE A PROVEN BASELINE WHEN MATERIAL
    ↓
CHOOSE INTERVENTION / NEXT ACTION
    ↓
DEFINE PROOF
    ↓
ACT / ACQUIRE EVIDENCE
    ↓
OBSERVE REALITY
    ↓
UPDATE
    ↓
CAPITALIZE REUSABLE CLOSURE WHEN WARRANTED
    ↓
REROUTE OR FINISH
```

## Gap router

Route by the **current blocker**, not by the wording of the user's request.

Gap labels are **diagnostic dimensions**, not mutually exclusive states.
Several may coexist. The Dominant Gap is the one whose reduction is currently
most likely to change the next useful decision, action, or proof.

- **Model Gap** — relevant reality is not understood well enough to predict, decide, act, or verify. Load `modeling`.
- **Evidence Gap** — relevant evidence is missing. If the current observation frame/channel may materially miss relevant reality, load `observability-coverage` first; otherwise load `evidence-acquisition` for retrieval, measurement, and evidence quality.
- **Decision Gap** — materially different viable actions remain. Load `decision-analysis`.
- **Capability Gap** — the required change is understood but a required capability is unavailable, undiscoverable/unlocated in the current execution context, unevaluated for the required production envelope, or has materially different sources. Load `capability-sourcing`.
- **Planning Gap** — the direction is chosen but dependent execution structure is unclear. Load `planning`.
- **Reality Gap** — the change is sufficiently understood and the required capability is available. Execute the smallest sufficient intervention.
- **Verification / Validation Gap** — something changed, but correctness or usefulness is not demonstrated. Load `validation`.

Additional task modes:

- Project structure, dependency, milestone, or work-item derivation → `project-modeling`.
- Repeated / risky / provenance-sensitive execution that needs observable gates → `workflow-hardening`. If the intervention is a new harness/workflow/Skill/validator, pair it with `capability-sourcing` before authoring the mechanism.
- Compiling work for another agent/tool → `delegation`.

For Coding Agent handoff, `delegation` should normally produce the task-specific prompt/contract.
The downstream agent should not need to interpret this whole Protocol again.
- Complex human-facing output that risks becoming a reasoning dump → `decision-surface`.

## Always-on invariants

- Need ≠ capability ≠ capability source ≠ implementation.
- Capability exists ≠ capability is discoverable / usable by the current executor. When source choice materially affects the outcome, inspect the relevant capability surface before selecting implementation.
- Do not choose an implementation merely because it matches the executor's native modality or most salient tool; judge sources against the required quality / production envelope.
- Choose models and methods for their intended use; do not force one familiar schema onto every non-trivial problem.
- A representative case is a model instantiation / test fixture, not evidence until grounded through real or test observation.
- Scope claims and prior PASS results to the population, environment, version, assumptions, and use actually supported by evidence.
- For consequential decisions or sourcing choices, cover materially different alternative/source classes rather than only familiar variants or vendors.
- Compress language, not decision-relevant distinctions; simple explanations must not erase a layer or relation that can change action, reroute, sourcing, or proof.
- When an important model is compiled into a milestone, plan, task, prompt, or implementation contract, preserve upstream semantics and separable failure modes.
- Distinguish structure coherence, implementation verification, and real-world validation when the proof type matters.
- After a decision-relevant upstream change, impact-analyze and revalidate affected downstream artifacts before relying on their prior PASS.
- Search results, platforms, samples, and telemetry streams are observations through frames, not the full relevant reality.
- When coverage can materially affect the conclusion, model the observation space before acquiring evidence.
- Do not mechanically translate a request into a task or implementation.
- Do not use more reasoning to hide an Evidence Gap.
- Do not treat generated analysis as a Source of Truth.
- Do not fabricate precision to remove an Unknown.
- Only decision-relevant Unknowns should block progress.
- Source a capability before deciding to build it when the sourcing choice materially matters.
- Build the delta, not the solved problem.
- **No meta-layer exemption:** if the proposed intervention is itself a reusable capability (harness, workflow, Skill, validator, schema, prompt system, orchestration, agent configuration), source that capability before custom-authoring it. A Protocol-generated implementation idea is not exempt.
- Before re-solving or rebuilding, check whether a prior verified closure already covers the current claim; reuse it while its scope and validity conditions still hold.
- A prior PASS closes only the claim/use envelope actually supported by its proof. Do not promote subsystem verification, one fixture, one environment, or one version into a broader closure.
- When a mature baseline materially constrains execution, keep Fixed Core / Allowed Variation / Project Delta distinct.
- When losing a consequential solved decision is likely to recur, preserve it in a discoverable and preferably enforceable project mechanism rather than relying on prompt prose or operator memory alone.
- Do not manufacture alternatives when one action is clearly implied.
- Define proof before consequential action.
- Action completion is not outcome validation.
- When evidence contradicts the model, update the model rather than defend the plan.
- Stop when the current purpose has sufficient evidence; do not perform methodology for its own sake.
- When a supported mechanical enforcement envelope exists for the artifact/result, use it as an additional gate; never promote a policy/conformance PASS into model correctness or real-world VALIDATION PASS.

## Progressive disclosure

1. Use this router first.
2. Read one primary `SKILL.md` when possible.
3. Load a second skill only when the task genuinely crosses another Gap or mode.
4. Read `PROTOCOL.md` for canonical wording, unusual edge cases, or methodology maintenance.
5. Do not load unrelated skills "just in case."

## Runtime context and visibility

When work depends on state that can become stale, ambiguous, or executor-specific, maintain compact Runtime Context:

- **Protocol** — source/version/ref when known, otherwise mark unknown.
- **Method** — relevant loaded skill(s) or selected method.
- **Source of Truth** — inspected source/current-state surface and freshness basis.
- **External Evidence** — inspected, not required, or unavailable.
- **Dominant Gap** — the gap currently governing the next useful action.

Prefer storing this in runtime/session/trace state when the host supports it. Do not mechanically re-fetch unchanged sources on every turn.

Refresh on runtime-state boundaries: a new executor without trustworthy inherited state, unknown/plausibly stale sources, changed decision-relevant upstream state, a new Source of Truth/environment/Gap, or a request for current/latest/freshly verified state.

A **Runtime Receipt** is only the operator-facing projection of this state. Surface it when requested, when a material state change affects the decision/action, when freshness/provenance/access limitations matter, or when consequential action warrants operator confirmation. Otherwise keep it in the runtime/trace and keep the answer focused.

If required access is unavailable, say so and narrow the claim. A receipt reports the basis of work; it is not evidence by itself.

## Human communication

For non-trivial work, default to a compact decision surface:

- **Bottom Line** — the most important conclusion.
- **Now** — 1–3 facts/state distinctions that materially support it.
- **Next** — one highest-leverage action or the next decision/evidence needed.
- **Proof** — the observation that will show success.

Do not force this format on trivial tasks. Keep language simple without flattening decision-relevant model distinctions. Do not expose full background, model, alternatives, or methodology unless they materially change the decision, risk requires them, or the user asks.

Runtime observability and human presentation are separate. Do not prepend runtime metadata merely to prove compliance. Before finalizing, check that the answer fits this Decision Surface; use host-supported structured-output or output-guardrail mechanisms for mechanically checkable presentation constraints when proportionate.

## Repository maintenance

- `PROTOCOL.md` is canonical.
- `enforcement/` + `conformance/` implement only the deterministic subset; keep policy semantics traceable to canonical rules and real failure fixtures.
- Runtime files are derived and must remain traceable to canonical sections.
- Before changing routing or skill boundaries, update or check [docs/runtime-map.md](docs/runtime-map.md).
- Use [examples/routing-cases.md](examples/routing-cases.md) as representative routing examples; they are not automated behavioral evals.
- Keep skill descriptions precise because agents use them for activation.
- Prefer focused skills over one giant skill.
