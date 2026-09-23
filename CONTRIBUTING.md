# Contributing

Contributions are welcome when they improve a real decision, action, proof, or failure mode.

## Before adding methodology

Prefer:

```text
real failure
→ diagnose
→ smallest useful correction
→ eval / conformance fixture
→ use again
```

Do not add rules, skills, abstractions, or automation solely to make the repository look more complete.

## Protocol changes

For changes to `PROTOCOL.md`:

1. state the failure, evidence, or model gap motivating the change;
2. impact-analyze affected router/skills/docs;
3. update only affected derived representations;
4. add or update a regression/eval case when practical;
5. preserve proof-type and authority distinctions.

## Executable enforcement changes

For `enforcement/` changes:

1. keep rules deterministic and machine-checkable;
2. do not encode contextual judgment merely because it can be approximated;
3. add a failing fixture before or with the fix;
4. keep policy PASS distinct from real-world validation;
5. run the conformance suite locally when possible.

## Pull requests

Keep PRs small enough that the semantic change is reviewable. Explain what changed, why it exists, and what proves it.
