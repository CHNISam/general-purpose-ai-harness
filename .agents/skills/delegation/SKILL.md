---
name: delegation
description: Compile a sufficiently understood action into a minimal execution contract or prompt for another agent, model, tool, repository, runtime, or environment. Use only after the relevant action is sufficiently clear. Do not copy the entire world model into every prompt or turn an unverified capability assumption into an implementation mandate.
---

# Delegation and Prompt Compilation

Use when another agent or tool needs to execute a sufficiently understood action.

## Execution contract

Include only fields capable of changing execution.

Possible fields:

- Objective
- Current Problem
- Source of Truth
- Constraints
- Acceptance Criteria
- Evidence

When materially relevant:

- Required Capability
- Existing Capability / Selected Source
- Priority / Trade-off Policy
- Decision Rights
- Escalation Conditions

These are not mandatory headings.

They are an execution contract, not a universal ontology.

They do not replace Modeling, Capability Sourcing, Decision Analysis, or Planning.

For production, migration, release, destructive, expensive, irreversible, or high-risk work, make the relevant constraints, authority, capability source, and evidence explicit.

## Prompt compilation

A prompt is one deployment format for an action.

Compile the **minimum sufficient serialization of the validated model slice** relevant to the current action and executor.

Do not:

- copy the entire world model into every prompt;
- compile an unverified capability assumption into an implementation mandate;
- preserve information that cannot change judgment, choice, capability sourcing, implementation, boundary, constraints, or acceptance.

Adapt instructions to the actual agent, model, tool, repository, runtime, and environment.

If direct execution is possible and delegation adds no value, execute directly.
