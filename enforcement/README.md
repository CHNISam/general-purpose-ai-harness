# Executable Enforcement

This directory contains the **mechanically enforceable subset** of the General-Purpose AI Operating Protocol.

It does not attempt to formalize all judgment. The Protocol still owns modeling, evidence interpretation, decision-making, capability sourcing, and validation semantics that require contextual reasoning.

The executable layer is for invariants that can be checked deterministically.

## Stack

- `schemas/` — versioned machine-readable input contracts.
- `policies/` — Open Policy Agent (OPA/Rego) rules.
- `tests/` — policy regression tests.
- `../conformance/` — public fixtures and a portable runner.
- GitHub Actions — runs the same conformance checks on repository changes.
- WebAssembly — CI compiles the policy entrypoint to a portable OPA Wasm bundle.

## Current hard rules

The first policy bundle rejects, among other cases:

1. `VERIFIED` evidence without provenance.
2. generated model output promoted directly to `VERIFIED` evidence.
3. `VALIDATION_PASS` without observed validation.
4. `VALIDATION_PASS` without verified validation evidence.
5. completion while decision-relevant conflicting evidence remains unresolved.
6. reality-changing action without proof defined first.
7. required capability sourcing without a selected/justified source.
8. completion with `UNKNOWN` proof.
9. claiming a validated outcome without `VALIDATION_PASS`.
10. completion while required validation remains unobserved.

These rules are intentionally narrower than the full Protocol.

## Local use

Install the single-file OPA CLI, then run:

```bash
opa fmt --fail enforcement/policies enforcement/tests
opa check --strict --schema enforcement/schemas/decision-input.schema.json enforcement/policies
opa test enforcement/policies enforcement/tests -v
python conformance/run.py
```

To build the portable policy bundle:

```bash
mkdir -p dist
opa build -t wasm \
  -e protocol/enforcement/decision \
  enforcement/policies/protocol.rego \
  -o dist/protocol-policy.tar.gz
```

The resulting bundle contains `policy.wasm`. It can be embedded in compatible Wasm/OPA SDK hosts without requiring access to this repository or an always-on server.

## Boundary

A policy PASS means only:

> the supplied machine-readable envelope satisfies the encoded invariants.

It does **not** prove that the underlying model is correct, the evidence is true, or the real-world outcome is validated. Those remain separate proof obligations.
