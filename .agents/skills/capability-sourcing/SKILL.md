---
name: capability-sourcing
description: Decide how to obtain a required capability before committing to custom implementation. Use when execution needs a capability that is unavailable, unlocated, unevaluated, or has materially different internal/external sources. Consider reuse, standards, libraries, APIs, services, workflows, datasets, models, composition, extension, and custom build. Do not run a large landscape study for trivial commodity choices.
---

# Capability Sourcing

Use this skill for a **Capability Gap**.

Core distinctions:

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

> Build the delta, not the solved problem.

## Trigger

Use this skill when sourcing could materially change cost, schedule, risk, reliability, maintenance/ownership burden, reproducibility, interoperability, or strategic differentiation.

Use proportional rigor. Do not turn a commodity choice into a research project.

## Existing capability check

First ask whether the capability already exists in:

- the current project or adjacent modules;
- organizational systems or infrastructure;
- current workflows or automation;
- installed dependencies;
- existing APIs or data.

Prefer extending or composing an existing suitable capability over creating a duplicate.

## Existing solution landscape

When the choice matters, inspect plausible sources:

1. existing internal capability;
2. established standard / protocol;
3. mature library / framework;
4. CLI / SDK / API;
5. managed or external service;
6. existing workflow / automation;
7. existing dataset;
8. existing model;
9. composition of proven capabilities;
10. custom implementation.

Custom Build is neither automatically first nor automatically last.

## Maturity and differentiation

Estimate only as precisely as useful whether the capability is closer to:

- Genesis — novel, uncertain, rapidly changing;
- Custom — understood but context-specific;
- Product — commonly solved by established solutions;
- Commodity / Utility — standardized and routinely available.

More commoditized capability creates a stronger reason to reuse/adopt/integrate.

More novel or strategically differentiating capability creates a stronger reason to experiment/customize/build.

This is a bias, not an absolute rule.

Ask:

**Does custom ownership of this capability materially create the outcome or differentiation we care about?**

Even when the differentiating layer is custom, reuse commodity capabilities underneath it where possible.

## Fit-gap

For credible candidates classify requirements as:

- Supported
- Configurable
- Extensible
- Missing
- Incompatible

The important question is:

**How much unresolved task-specific delta remains?**

## Cheap spike

When fit is uncertain and the decision matters, run the cheapest useful representative spike before full integration or custom replacement.

Test only what can change the sourcing decision: installation, representative input, API fit, performance, output quality, observability, deployment, compatibility, or failure behavior.

## Source decision

When multiple materially different sources remain, reroute into a Decision Gap.

Use only criteria that can change the choice:

- fit for purpose;
- maturity / project or vendor health;
- time to usable capability;
- adoption and integration cost;
- custom delta;
- maintenance burden;
- total ownership cost;
- reliability;
- observability;
- reproducibility;
- interoperability;
- security / privacy;
- licensing / legal;
- switching cost / lock-in;
- failure surface;
- strategic differentiation;
- opportunity cost.

Possible outcomes:

- Reuse
- Configure
- Adopt
- Integrate
- Compose
- Extend
- Build

Prefer the source producing the best total outcome, not merely the least code.

## Custom build

Custom implementation can be correct when existing options fail essential requirements or invariants, create unacceptable security/privacy/licensing/lock-in risk, miss required performance/observability/reliability, create excessive integration complexity, cost more over the relevant lifetime, or block strategically important differentiation.

Do not force reuse merely because reuse exists.

## Stop rule

Stop sourcing research when a sufficiently suitable source is established, remaining alternatives are unlikely to change the decision, search cost exceeds expected decision value, a spike gives enough evidence, or custom implementation is demonstrably cheaper and sufficiently safe.

Capability sourcing exists to reduce work, not create analysis paralysis.
