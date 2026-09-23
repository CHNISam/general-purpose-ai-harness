# Changelog

This file records public semantic and engineering changes. Canonical methodology remains in `PROTOCOL.md`.

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
