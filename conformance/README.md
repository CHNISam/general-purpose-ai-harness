# Protocol Conformance

This directory provides public, deterministic fixtures for the executable enforcement layer.

## Run

```bash
python conformance/run.py
```

Use `--opa /path/to/opa` when OPA is not on `PATH`.

The runner evaluates each case in `cases/manifest.json` against `enforcement/policies/protocol.rego` and fails if the allow/deny decision or required violation codes do not match.

## What this proves

A passing suite proves that the current policy implementation behaves as specified on these fixtures.

It does not prove general model quality or real-world usefulness.

Keep these proof types separate:

- policy/conformance PASS — deterministic rules behave as specified;
- behavioral eval PASS — a model behaves better under the Protocol;
- real-world VALIDATION PASS — the resulting system satisfies its intended need.

## Adding a case

1. Add a minimal JSON fixture.
2. Add it to `cases/manifest.json`.
3. State the expected allow/deny result and required violation codes.
4. Prefer a real observed failure mode when possible.
5. Keep fixtures minimal enough that a failed assertion has one obvious interpretation.
