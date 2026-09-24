# Changelog

This file records public semantic and engineering changes. Canonical methodology remains in `PROTOCOL.md`.

## v2.12.0 — 2026-09-24

### Protocol

- Added **Verified Closure**: a bounded prior result may be reused without recomputation only while its claim, scope/use envelope, assumptions, dependencies, environment/version and other validity conditions still hold.
- Added explicit failure diagnoses for **False Closure**, **Lost Closure**, and **Unmaterialized Closure** without turning them into new Gap types.
- Added **managed variability**: distinguish Fixed / Proven Core, Allowed Variation, and Project Delta when a mature baseline materially constrains execution.
- Strengthened Capability Sourcing with **Baseline Acquisition / Reference Materialization** and source roles: reusable component, implementation reference, behavioral oracle, and evidence-only.
- Strengthened post-action work with proportional **closure capitalization** so recurring consequential learning becomes a discoverable / enforceable project mechanism rather than prompt prose alone.

### Runtime / evidence

- Updated the compact router plus capability-sourcing, workflow-hardening, validation, delegation, runtime map, protocol index, README, and routing examples.
- Added five sanitized real-world retrospective cases (R015–R019) covering baseline reuse, subsystem-vs-product closure, proof-scope leakage, invariant graduation, and a genuinely open product gap.
- Preserved v2.11.1 under `docs/history/`.

### Executable enforcement

- Extended the decision envelope with an optional closure block.
- Added deterministic guards for unjustified reopening of an explicitly valid in-scope closure, claiming new closure beyond declared proof scope, and completion when capitalization has explicitly been marked required but remains absent.
- Added three public conformance fixtures; the suite is now 11 cases.
- Mechanical PASS still proves only the supplied envelope satisfies encoded policy, not that the closure facts themselves are true.

## v2.11.1 — 2026-09-24

### Protocol

- Refined Runtime State Observability into **Runtime Context + operator projection**: runtime/session/trace state is distinct from what should appear in the human-facing answer.
- Replaced task-complexity-driven receipt display with **runtime-state boundary** refresh semantics: refresh when executor/source/environment/Gap/freshness changes make prior state unreliable.
- Clarified that a **Runtime Receipt** is an on-demand or decision-relevant projection, not a mandatory banner for every complex task.
- Separated runtime observability from the human **Output Contract**. Poor communication should be repaired by Decision Surface / output conformance, not by dumping more telemetry.
- Added proportional use of host-supported structured-output / output-guardrail mechanisms for mechanically checkable presentation constraints.

### Runtime / evidence

- Updated the compact router, runtime map, Protocol index, README, and R014 retrospective wording.
- Preserved v2.11.0 under `docs/history/`.
- Kept the retrospective set at fourteen cases: this patch refines the semantics learned from R014 rather than inventing a new failure class.
- No new deterministic enforcement claim is made; runtime freshness and decision relevance remain contextual judgments.

## v2.11.0 — 2026-09-24

### Protocol

- Added **Runtime State Observability and Freshness**: agents may reuse sufficiently identified, relevant, fresh context instead of mechanically re-fetching every turn.
- Added explicit refresh conditions for new/unknown/stale runtime state, changed upstream state, new Sources of Truth/environments/Gaps, and current/latest verification requests.
- Added a compact **Runtime Receipt** so Protocol source/version, selected method, Source of Truth/freshness basis, external-evidence status, and Dominant Gap can be inspected without exposing private reasoning.
- Required agents to mark unavailable retrieval channels and constrain claims rather than silently implying that a refresh occurred.

### Runtime / evidence

- Updated the compact router, runtime map, Protocol index, README, and retrospective evidence set.
- Added a fourteenth sanitized real-world retrospective case covering invisible protocol/current-state freshness and unnecessary “always browse” pressure.
- Preserved v2.10.0 under `docs/history/`.
- No deterministic enforcement claim is made for freshness judgment or Runtime Receipt truthfulness; these remain runtime/model behavior rules.

## v2.10.0 — 2026-09-23

### Protocol

- Reordered the non-trivial runtime so the Agent identifies the required change/outcome, inspects the relevant capability surface when material, then selects the capability source before choosing the intervention.
- Added **Capability Surface** semantics: a capability that exists but is not discoverable/usable by the current executor is operationally unavailable.
- Added an **executor-native modality bias guard**: do not choose code, visual authoring, spreadsheets, a familiar library, or another implementation merely because it is the executor's most salient tool.
- Added **quality / production ceiling** and **executor fit** to capability-source decisions so prototype-friendly sources are not silently treated as production-suitable.
- Strengthened delegation so a task-specific prompt preserves either the selected capability source or enough discoverable available means when source choice remains decision-relevant.

### Runtime / evidence

- Updated the compact router, capability-sourcing skill, delegation skill, runtime map, and Protocol index.
- Added a thirteenth sanitized real-world retrospective case for a capability that existed in the project but was not surfaced to the executor before implementation choice.
- Preserved v2.9.1 under `docs/history/`.
- No new deterministic enforcement claim is made for executor-bias judgment; this remains a model/runtime behavior rule rather than a mechanically proven invariant.

## v2.9.1 — 2026-09-23

### Protocol

- Added a staged-audit rule for existing layered models: downstream material may be inspected to test consistency, but deeper layers must not be treated as accepted before their upstream derivation passes.

### Evidence

- Added 12 sanitized retrospective cases reconstructed from real AI-assisted work.
- Added a controlled Protocol OFF vs ON pilot specification. The controlled pilot is designed but has **not yet been run**.

### Executable enforcement

- Added JSON Schema + OPA/Rego policy for deterministic invariants.
- Added public conformance fixtures and a portable runner.
- Added CI-built WebAssembly policy bundle.
- Added Protocol Conformance CI and OpenSSF Scorecard analysis.

### Repository governance

- Added CONTRIBUTING.md, SECURITY.md, CODEOWNERS, and Dependabot.
- Added public navigation and contribution paths for failure-driven evolution.

## v2.9.0

- Added intended-use/schema selection and model-use envelopes.
- Strengthened claim–evidence fit and representative-scenario vs evidence separation.
- Strengthened solution-space coverage and mature capability sourcing before custom methodology.
