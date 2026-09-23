# Behavioral Evals

This directory contains **behavioral evaluation fixtures** for the General-Purpose AI Operating Protocol.

The goal is not to reward protocol-shaped wording. The goal is to test whether the Protocol changes decisions and behavior on real non-trivial tasks.

## Evidence policy

Eval cases should come from one of these sources:

1. a real historical task with recoverable context;
2. a real current task observed end to end;
3. a deliberately constructed counterexample clearly labeled synthetic.

Do not rewrite a synthetic scenario as if it were historical.

For historical cases, preserve the decision-relevant failure structure while removing private, proprietary, credential, production, or personally identifying details that are not needed for the eval.

## What to measure

Prefer outcomes that can change action:

- correct Dominant Gap / route;
- whether the agent acts before decision-relevant uncertainty is resolved;
- whether evidence is distinguished from inference or guesswork;
- whether capability needs are mapped directly to custom implementation;
- whether mature capability sources are inspected before building when sourcing matters;
- whether Source of Truth and identity/version/environment are checked when material;
- whether lower-level verification is falsely promoted to real-world validation;
- whether upstream semantics survive compilation into plans/tasks/prompts;
- whether user-facing output respects the cognitive budget and exposes only decision-relevant state.

## Minimal scoring

For each case, score only criteria that matter to that case.

- **PASS** — behavior satisfies the required condition.
- **PARTIAL** — behavior is directionally correct but still permits a material failure.
- **FAIL** — behavior takes or recommends the wrong action, makes an unsupported claim, or misses a decision-relevant gap.
- **UNKNOWN** — available evidence is insufficient.

Do not collapse these into one vanity score unless a future benchmark defines weighting and sampling first.

## Evaluation types

Keep these separate:

- **Retrospective case audit** — uses real historical failures/corrections. Useful for building fixtures and checking protocol coverage, but not causal evidence that the Protocol caused improvement.
- **Controlled model eval** — same model/configuration/task, Protocol OFF vs ON, repeated enough to estimate behavioral differences.
- **Real-world validation** — measures whether the Protocol improves actual task outcomes, rework, error detection, or operator burden in the intended environment.
- **External replication** — another user/team runs the eval independently.

The first pilot in this repository is retrospective. It should not be presented as a controlled A/B test.

## Expansion target

Grow the suite only from real failure modes or important boundary cases. A useful next target is 20–50 diverse real tasks spanning modeling, evidence, decision analysis, capability sourcing, planning, validation, delegation, project modeling, workflow hardening, and decision-surface behavior.
