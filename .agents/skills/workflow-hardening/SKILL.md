---
name: workflow-hardening
description: Design observable, repeatable, and where useful blocking mechanisms for repeated, scalable, risky, failure-prone, provenance-sensitive, hard-to-reproduce, or expensive-to-verify execution. Use when manual verification or ad hoc prompting is no longer sufficient. Do not build a hardening mechanism for cheap one-off low-risk work.
---

# Workflow Hardening

Use when execution or evidence production is meaningfully:

- repeated;
- scalable;
- risky;
- failure-prone;
- provenance-sensitive;
- expensive to verify manually;
- difficult to reproduce;
- governed by important invariants;
- likely to recur.

Before building a new workflow-hardening capability, apply **capability-sourcing**.

## Objective

Convert important model claims, process states, and invariants into observable, repeatable, inspectable, and where useful blocking evidence.

Possible components:

- controlled inputs;
- fixtures / environment;
- source policy;
- runner / procedure;
- state tracking;
- guards;
- provenance;
- logging;
- sanity checks;
- validation rules;
- oracle / acceptance logic;
- retries;
- exception handling;
- human-review queues;
- evidence capture.

Prefer cheap rejection mechanisms before expensive verification.

For repeated defects or escaped regressions, ask:

> Why was this failure still representable, or why was this solved decision still open?

Escalate only as far as the evidence justifies:

1. fix the current instance;
2. detect recurrence;
3. encode the failure class as an invariant / contract;
4. remove unnecessary variation by reusing a proven baseline;
5. make the invalid state structurally impossible where practical.

When a useful closure is likely to recur, preserve its claim, scope, baseline, validity conditions, allowed variation, proof, and invalidation triggers in the lightest discoverable / enforceable mechanism that fits the risk.

A sanity check can show that something is obviously wrong. It does not prove correctness.

## Restraint

Do not build infrastructure for a cheap one-off task.

If the hardening mechanism itself becomes sufficiently complex that its behavior is unclear, treat the hardening mechanism as the new system of interest and model it.

Do not recurse further unless a real problem requires it.
