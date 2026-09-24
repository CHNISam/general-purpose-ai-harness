# Runtime Map

This document describes how the canonical [PROTOCOL.md](../PROTOCOL.md) is represented in the compact runtime layer.

It is a **maintenance map**, not proof of semantic completeness and not an automated verification artifact.

| Canonical concept | Primary runtime representation |
|---|---|
| Purpose / necessity / Why-before-How | `PROTOCOL.md` 3 + 3.1 + `AGENTS.md` core loop + `modeling` |
| Runtime Context / freshness / operator projection | `PROTOCOL.md` 1.1.1 + `AGENTS.md` Runtime context and visibility |
| Diagnostic dimensions | `AGENTS.md` Gap router |
| Minimum sufficient judgment | `AGENTS.md` guards + relevant skills |
| Model Gap / minimum sufficient modeling | `modeling` |
| Model purpose / schema selection / intended-use envelope | `modeling` |
| Scenario round-trip / layer preservation / compilation integrity | `modeling` |
| Claim–evidence / model-use fit | `modeling` + `evidence-acquisition` + `validation` |
| Bidirectional project trace / capability-source layer | `project-modeling` |
| Proof-type separation / impact-based revalidation | `validation` |
| Evidence coverage | `observability-coverage` |
| Evidence retrieval / measurement / quality | `evidence-acquisition` |
| Decision / alternative-space sufficiency | `decision-analysis` |
| Capability surface awareness / discoverability / executor-bias guard | `AGENTS.md` + `capability-sourcing` + `delegation` |
| Capability sourcing / solution-space coverage / quality ceiling / sourcing granularity | `capability-sourcing` |
| Verified Closure / managed variability / baseline reuse | `PROTOCOL.md` 1.4.1 + `capability-sourcing` + `validation` |
| Recursive sourcing / no meta-layer exemption | `PROTOCOL.md` 1.4.2 + `AGENTS.md` + `capability-sourcing` + `workflow-hardening` + `delegation` |
| Closure preservation / capitalization mechanisms | `workflow-hardening` + `validation` |
| Enforcement Graduation / Operational Closure | `PROTOCOL.md` 1.4.3 + `workflow-hardening` + `validation` + executable policy where deterministically representable |
| Planning | `planning` |
| Reality Gap / execution | direct action through the host AI/runtime |
| Verification / Validation Gap + proof | `validation` |
| Workflow hardening | `workflow-hardening` |
| Project work | `project-modeling` |
| Delegation / prompt compilation | `delegation` |
| Human-facing compression | `decision-surface` |
| Output-contract conformance vs runtime observability | `PROTOCOL.md` 16 + 20 + `AGENTS.md` Human communication |
| External method / standard pointers (non-canonical) | `docs/method-registry.md` |
| Mechanically checkable Protocol invariants | `enforcement/` + `conformance/` + CI |

## Concept boundaries

### Diagnostic dimensions

The Gap router diagnoses insufficiencies. Gaps may coexist.

It does not imply a state machine.

### Methods

Skills package conditional methods or reusable task modes.

A skill existing in the repository does not make its subject a core ontology primitive.

### Guards

Always-on guards stay in `AGENTS.md` only when they are cheap, broadly applicable, and important enough to constrain many tasks.

### Mechanical enforcement

The Protocol can recommend scripts, tests, CI, linters, or other blocking mechanisms when a real workflow justifies them.

This repository now provides a **reference mechanical enforcement subset** for stable invariants that can be checked deterministically. The current policy covers evidence provenance, generated-vs-observed evidence, proof-before-action, capability-source readiness, unresolved conflicts, and proof-type/completion discipline.

The enforcement layer is intentionally not generic proof of correctness. Its PASS means only that the supplied decision envelope satisfies the encoded policy. It cannot by itself establish model correctness or real-world validation.

## Maintenance rule

When a canonical concept changes:
- impact-analyze which runtime files depend on the changed meaning;
- mark affected derived representations as requiring revalidation until synchronized;
- update this map if its runtime representation changes;
- update only affected skills;
- preserve deliberately retained semantics; retire or rename concepts only through an explicit change, with historical recovery available when useful.

A prior runtime mapping is not evidence that it remains semantically valid after an upstream canonical change.

When a runtime refactor does not change canonical meaning:
- do not edit `PROTOCOL.md`;
- keep this map descriptive;
- avoid adding a new concept merely to explain the refactor.
