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


## Report a model/agent failure

Use the **Agent behavior failure** issue template when a real task exposes a behavior the current Protocol did not prevent or route correctly.

High-value reports include:

- the AI/model/runtime used;
- the smallest reproducible task context;
- the observed failure;
- why the failure mattered;
- the expected behavior;
- evidence such as output excerpts, logs, screenshots, or repository state.

Sanitize secrets and private data.

## Add a retrospective eval case

A historical case is useful when the failure and correction can be reconstructed honestly.

Do not invent a synthetic case and label it historical.

Prefer to preserve:

```text
real task
→ observed failure
→ operator correction
→ expected Protocol behavior
→ current coverage
```

## External replication

Independent replications are especially valuable.

If you run Protocol OFF vs ON or use the Protocol on a real workflow, record:

- model/runtime/version when available;
- task/context;
- treatment difference;
- scoring criteria defined before judging;
- raw outputs or sufficient evidence for review;
- costs/latency/context when available;
- failures as well as successes.

Do not convert one successful anecdote into a universal effectiveness claim.
