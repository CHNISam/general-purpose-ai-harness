---
name: harness-engineering
description: Design observable, repeatable, and where useful blocking mechanisms for repeated, scalable, risky, failure-prone, provenance-sensitive, hard-to-reproduce, or expensive-to-verify execution. Use when manual verification or ad hoc prompting is no longer sufficient. Do not build a harness for cheap one-off low-risk work.
---

# Harness Engineering

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

Before building a new harness capability, apply **capability-sourcing**.

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

A sanity check can show that something is obviously wrong. It does not prove correctness.

## Restraint

Do not build infrastructure for a cheap one-off task.

If the harness itself becomes sufficiently complex that its behavior is unclear, treat the harness as the new system of interest and model it.

Do not recurse further unless a real problem requires it.
