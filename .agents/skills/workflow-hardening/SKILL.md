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

This applies recursively to harness authoring itself. Inspect the live
repository's existing instructions, tests, gates, planning/evidence surfaces and
the target agent/runtime's mature customization mechanisms before inventing a
new harness structure.

Right-size the result. Prefer extending existing repository conventions over
creating a parallel operating system. Select the delivery surface by required
scope, loading behavior, authority, determinism, context cost, and runtime
support; keep procedures out of always-on context when conditional loading is
available, and move non-negotiable checks into deterministic enforcement when
the platform can support it.

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

## Enforcement graduation

For recurring or consequential closure, separate **Epistemic Closure** from
**Operational Closure**. Ask whether violation is mechanically decidable and,
if it is, whether a violating change/state can still silently pass. Prefer the
cheapest reliable guard: type/schema, canonical boundary, diff/path guard,
dependency rule, lint, contract/fixture/runtime test, or CI/policy gate.

A guard is not proven merely because it exists. Prove a known invalid case is
rejected, a representative allowed case is accepted, and—when blocking is the
purpose—that the guard is wired into the normal execution/merge path.

Prefer enforcing invariants over freezing implementation details. Protect exact
paths only when path ownership itself is the invariant.

If the outcome is not mechanically decidable, define the Human/Product gate and
observation surface. If hardening is deferred, record enforcement debt and do
not call a documentation-only rule Operationally Closed.

A sanity check can show that something is obviously wrong. It does not prove correctness.

## Restraint

Do not build infrastructure for a cheap one-off task.

If the hardening mechanism itself becomes sufficiently complex that its behavior is unclear, treat the hardening mechanism as the new system of interest and model it.

Do not recurse further unless a real problem requires it.
