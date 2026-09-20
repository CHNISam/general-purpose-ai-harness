# Runtime Map

This document describes how the canonical [PROTOCOL.md](../PROTOCOL.md) is represented in the compact runtime layer.

It is a **maintenance map**, not proof of semantic completeness and not an automated verification artifact.

| Canonical concept | Primary runtime representation |
|---|---|
| Purpose / orientation | `AGENTS.md` core loop + `modeling` when unclear |
| Diagnostic dimensions | `AGENTS.md` Gap router |
| Minimum sufficient judgment | `AGENTS.md` guards + relevant skills |
| Understanding | `modeling` |
| Evidence coverage | `observability-coverage` |
| Evidence retrieval / measurement / quality | `evidence-acquisition` |
| Decision | `decision-analysis` |
| Capability sourcing | `capability-sourcing` |
| Planning | `planning` |
| Execution | direct action through the host AI/runtime |
| Proof / verification / validation | `validation` |
| Workflow hardening | `workflow-hardening` |
| Project work | `project-modeling` |
| Delegation / prompt compilation | `delegation` |
| Human-facing compression | `decision-surface` |

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

The repository itself does not claim to provide those mechanisms generically.

## Maintenance rule

When a canonical concept changes:
- update this map if its runtime representation changes;
- update only affected skills;
- remove stale names and aliases rather than preserving them indefinitely.

When a runtime refactor does not change canonical meaning:
- do not edit `PROTOCOL.md`;
- keep this map descriptive;
- avoid adding a new concept merely to explain the refactor.
