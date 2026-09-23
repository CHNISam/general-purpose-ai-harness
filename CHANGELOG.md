# Changelog

This file records public semantic and engineering changes. Canonical methodology remains in `PROTOCOL.md`.

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
