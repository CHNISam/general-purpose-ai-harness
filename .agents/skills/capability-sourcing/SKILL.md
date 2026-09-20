---
name: capability-sourcing
description: Decide how to obtain a required capability before committing to custom implementation. Use when a Capability Gap matters and internal/external sourcing could materially change cost, time, reliability, ownership burden, risk, or differentiation. Do not run a broad landscape study for a trivial commodity choice.
---

# Capability Sourcing

Use this skill when a **Capability Gap** is important enough to affect the next action or decision.

Keep the distinction:

```text
Need
  ≠
Capability
  ≠
Capability Source
  ≠
Implementation
```

> Source the capability before deciding to build it.

> Build the unresolved delta, not the solved problem.

## 1. Check what already exists

First inspect relevant:

- project or organizational capabilities;
- installed dependencies and infrastructure;
- standards, protocols, libraries, APIs, services, datasets, models, or workflows.

Do not duplicate a sufficiently suitable capability merely because custom implementation is possible.

## 2. Search proportionally

Inspect alternatives only when the sourcing choice can materially affect the outcome.

The useful landscape usually includes some combination of:

- reuse / configure;
- adopt / integrate;
- compose / extend;
- custom build.

The exact categories do not matter. The unresolved task-specific delta does.

## 3. Ask a few decision questions

Compare only dimensions capable of changing the choice:

**Fit**
- Does it satisfy the important requirements and invariants?
- What task-specific delta remains?

**Adoption burden**
- How much time and integration work is required to obtain useful capability?

**Operating burden and risk**
- What maintenance, reliability, security/privacy, interoperability, failure, or lifecycle burden matters here?

**Strategic ownership**
- Does custom ownership create meaningful differentiation?
- Would reuse create material lock-in or opportunity cost?

Do not score every possible criterion.

## 4. Use a cheap spike when needed

When fit is uncertain and consequential, run the cheapest representative test that can change the sourcing decision.

Test only the uncertain property that matters: API fit, representative output quality, performance, deployment, compatibility, observability, or failure behavior.

## 5. Choose and stop

Possible outcomes include reuse, configure, adopt, integrate, compose, extend, or build.

Prefer the source that creates the best total outcome, not merely the least code.

Custom implementation is reasonable when credible existing sources fail essential requirements, create unacceptable burden or risk, or when ownership itself is strategically important.

Stop sourcing when:

- one option is sufficiently suitable;
- remaining alternatives are unlikely to change the decision;
- a cheap spike resolves the important uncertainty; or
- further search costs more than its expected decision value.

Capability sourcing exists to reduce total work and ownership burden, not create analysis paralysis.
