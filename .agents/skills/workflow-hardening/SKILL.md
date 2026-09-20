---
name: workflow-hardening
description: Strengthen repeated, risky, failure-prone, provenance-sensitive, hard-to-reproduce, or expensive-to-verify workflows with reusable or mechanical controls when ad hoc execution is no longer sufficient. Use only when repeated failure, scale, risk, or verification cost justifies the added ownership burden. Do not automate cheap one-off work for completeness.
---

# Workflow Hardening

Use this task mode when repeated execution needs stronger reliability than ad hoc prompting or manual checking provides.

Typical triggers:

- the same class of failure recurs;
- execution is repeated or scaled;
- mistakes are expensive or hard to detect;
- provenance or reproducibility matters;
- important invariants must be enforced;
- manual verification has become a meaningful cost.

## First source the capability

Before building new infrastructure, inspect whether the host runtime, existing scripts, tests, CI, services, or other tools already provide the needed capability.

Use `capability-sourcing` when the sourcing choice matters.

## Choose the lightest useful mechanism

Possible mechanisms include:

- reusable procedures;
- controlled inputs or fixtures;
- scripts;
- source policies;
- state tracking;
- guards;
- logs;
- provenance capture;
- sanity checks;
- tests;
- acceptance oracles;
- retries;
- exception handling;
- human-review gates;
- CI or other mechanical enforcement.

Prefer a cheap rejection mechanism when it catches the important failure.

A sanity check can reject obvious failure; it does not prove correctness.

## Restraint

Do not build infrastructure for a cheap one-off task.

Do not add CI, validators, or automation merely to make a repository look more engineered.

If the hardening mechanism itself becomes costly or unclear, reassess whether it still reduces total burden.
