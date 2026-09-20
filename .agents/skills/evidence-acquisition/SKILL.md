---
name: evidence-acquisition
description: Acquire and qualify real evidence when the decisive observation, fact, measurement, source, experiment, or result is known but not yet possessed. Use for research, inspection, measurement, testing, provenance checks, identity/version matching, source conflicts, or precision requirements. Do not substitute more abstract reasoning for a known Evidence Gap.
---

# Evidence Acquisition

Use this skill for an **Evidence Gap**.

## Define what evidence would resolve the gap

Before collecting broadly, identify the observation capable of changing the current decision, action, constraint, or acceptance result.

Only add evidence controls that matter:

- Source hierarchy / authority
- Provenance
- Identity matching
- Required precision
- Conflict handling
- Acceptance state
- Stop rule

## Evidence states

Where useful, classify evidence as:

- **Verified** — sufficiently supported for the current purpose.
- **Candidate** — plausible but still needs confirmation.
- **Approximate** — deliberately lower precision than Verified.
- **Conflicting** — credible evidence disagrees.
- **Unresolved** — relevant evidence remains insufficient.

Do not upgrade Candidate or Approximate evidence to Verified for convenience.

## Source of Truth

Prefer reality or an authoritative external artifact:

- actual code or runtime state;
- authoritative database;
- logs;
- measurements;
- test results;
- official documents;
- validated user behavior;
- authoritative external sources.

The agent's model, summary, interpretation, plan, generated document, or previous answer is not automatically a Source of Truth.

## Procedure

1. State the exact evidence need internally.
2. Choose the cheapest sufficiently authoritative observation/source.
3. Verify identity, version, environment, or entity matching when it can change the result.
4. Resolve or expose material source conflicts.
5. Stop when evidence is sufficient for the current purpose.

Do not research indefinitely.

## Exit

Evidence may:

- close the gap;
- contradict the working model;
- expose a new Model Gap;
- create a Decision Gap;
- show that execution can proceed.

Reroute accordingly.
