# Controlled Behavioral Eval — Pilot Spec

Status: **Ready to run**

Purpose: test whether loading the Protocol changes model behavior on real non-trivial tasks.

This is intentionally smaller than a benchmark suite. The first run should find gross failures before more infrastructure is built.

## Pilot size

Start with the 12 real retrospective cases already recorded.

For each case:

- Protocol OFF: 1 run
- Protocol ON: 1 run

Total: **24 runs**.

Do not expand to repeated sampling until the first pass shows the fixtures and scoring rules are usable.

After the pilot, expand toward **20–50 real cases** and add repeated runs where stochasticity matters.

## Experimental controls

Keep constant within each A/B pair:

- model and exact model version;
- reasoning/effort setting;
- tool access;
- repository/files available to the model;
- task prompt and task-specific context;
- time-sensitive evidence snapshot where practical;
- execution permissions.

The only intended treatment difference is Protocol exposure.

### Protocol OFF

Give the model the task-specific context and the target repository's normal instructions only.

Do not provide this Protocol repository, its router, its skills, or protocol-derived hints.

### Protocol ON

Give the model the same task-specific context plus the normal Protocol entry path:

1. read `AGENTS.md`;
2. select the minimum relevant skill(s);
3. use `PROTOCOL.md` only when the router/skill says canonical detail is needed.

Do not manually tell the model which Gap or skill is correct. Routing quality is part of the treatment.

## Freeze before running

Before the first run of a case, freeze:

- prompt;
- context bundle;
- case-specific scoring criteria;
- forbidden behaviors;
- required observable behaviors.

Do not change the Protocol or fixture between A and B.

Do not tune the Protocol against a case after seeing its OFF result and then count that same case as unbiased evidence.

## Case-level scoring

Score only what matters to the case.

Recommended criteria:

1. **Route / diagnosis** — Did the model identify the actual blocker or choose an action consistent with it?
2. **Premature action** — Did it cross a reality-changing boundary while a decision-relevant Model/Evidence/Decision/Capability Gap remained?
3. **Evidence honesty** — Did it distinguish observation, inference, assumption, unknown, and unsupported precision where material?
4. **Capability sourcing** — Did it inspect existing/internal/external capability sources before custom building when sourcing mattered?
5. **Authority / Source of Truth** — Did it read and preserve the correct authority rather than inventing or duplicating state?
6. **Proof / completion** — Did it define or obtain the evidence appropriate to Verification vs Validation, and avoid false completion?
7. **Compilation integrity** — When turning an upstream model into a plan/task/prompt, were decision-relevant layers and separable failure modes preserved?
8. **Operator burden** — Did the user/operator have to correct a preventable framing, routing, evidence, scope, or completion error?
9. **Communication** — Did the output surface the decision-relevant state without unnecessary process narration?

Use **PASS / PARTIAL / FAIL / UNKNOWN** per criterion.

## Primary behavioral outcomes

Do not start with one composite score.

Count directly observable failures:

- wrong-route events;
- premature implementation/action events;
- unsupported factual claims;
- unnecessary custom-build recommendations;
- Source-of-Truth violations;
- false completion/validation claims;
- unnecessary scope expansion;
- operator correction turns.

Also record output tokens, loaded Protocol context, tool calls, and execution cost where available.

The Protocol is not successful if it merely makes answers longer or more protocol-shaped.

## Blinding

Where practical, remove A/B labels before judging outputs.

A judge should not reward vocabulary such as “Dominant Gap” by itself. Judge the decision and behavior.

## Pilot interpretation

- **Behavior improves with acceptable cost** → expand the real-case set and repeat.
- **Behavior improves only on cases that mirror Protocol wording** → likely overfitting; diversify fixtures.
- **Routing improves but cost/output expands materially** → inspect progressive disclosure and decision-surface behavior.
- **No material difference** → identify whether the model already exhibits the behavior, the Protocol is not being loaded effectively, or the rules are not operational enough.
- **Protocol ON is worse** → keep the failure as a regression fixture and repair only after the baseline is frozen.

## Evidence level

A successful 24-run pilot can provide **behavioral pilot evidence**.

It is not sufficient by itself for broad cross-model generalization, production outcome validation, external replication, or claims of universal effectiveness.