# Canonical Coverage Map

This file maps every top-level section of `HARNESS.md` v2.6 to its primary runtime representation.

Its purpose is to prevent semantic loss when the canonical single-prompt Harness is decomposed into progressive-disclosure layers.

| Canonical section | Primary runtime representation |
|---|---|
| 0. Primary Objective | `AGENTS.md` core invariants + all skills |
| 1. Runtime Kernel | `AGENTS.md` Core runtime / Always-on invariants |
| 2. Dominant Gap Routing | `AGENTS.md` Gap router + Evidence sub-routing |
| 3. Purpose | `modeling` |
| 4. Minimum Sufficient Modeling | `modeling` |
| 5. Optional Reasoning Operators | `modeling` |
| 6. Model Gates | `modeling` |
| 7. Evidence Acquisition Policy | `observability-coverage` + `evidence-acquisition` |
| 8. Capability Sourcing / Leverage Gate | `capability-sourcing` |
| 9. Decision and Action | `decision-analysis` |
| 10. Planning | `planning` |
| 11. Proof Before Action | `validation` |
| 12. Harness Engineering | `harness-engineering` |
| 13. Project Mode | `project-modeling` |
| 14. Delegation / Execution Contract | `delegation` |
| 15. Prompt Compilation | `delegation` |
| 16. Human Output Contract — Decision Surface | `decision-surface` + `AGENTS.md` Human communication |
| 17. Optional Deep-Dive Format | `decision-surface` |
| 18. Post-Action Update | `validation` |
| 19. Completion Contract | `validation` |
| 20. Silent Compliance Audit | `AGENTS.md` invariants + all relevant skills + routing evals |
| 21. Anti-Patterns | `AGENTS.md` invariants + corresponding skills |
| 22. Runtime Cheatsheet | `AGENTS.md` Gap router / Progressive disclosure |
| 23. Final Rule | `AGENTS.md` Core runtime |
| 24. Current Task | Runtime/task boundary; documented in `AGENTS.md` and README usage |

## Subsection coverage notes

### Runtime kernel

Canonical distinctions preserved in the runtime layer:

- reason internally; report decision-relevant state;
- inspect before abstracting when cheaper;
- reality-changing action boundary;
- capability is not implementation;
- evidence honesty;
- do not ask unnecessary questions.

### Model gates

The `modeling` skill preserves:

- Run Test;
- Separation Test;
- Counterfactual Test;
- Coverage Test;
- Grounding Test;
- Falsification Test;
- Generalization Test;
- Traceability Test;
- Ablation Test.

### Evidence observability and acquisition

The evidence runtime preserves:

- target reality / population;
- evidence generation;
- evidence habitats / collections;
- observation frames;
- access / retrieval channels;
- blind spots / coverage error;
- representation risk;
- complementary-frame or conclusion-scope handling;
- retrieval vs measurement routing;
- source hierarchy / authority;
- provenance;
- identity matching;
- required precision;
- conflict handling;
- acceptance state;
- stop rule.

The `observability-coverage` skill owns observation-space modeling when frame coverage can materially affect the conclusion.

The `evidence-acquisition` skill owns retrieval, measurement, and evidence quality once the frame is sufficiently understood.

### Capability sourcing

The `capability-sourcing` skill preserves:

- trigger / proportional rigor;
- existing capability check;
- external solution landscape;
- capability evolution / maturity;
- differentiation check;
- fit-gap check;
- cheap spike;
- capability source decision criteria;
- reuse/configure/adopt/integrate/compose/extend/build outcomes;
- build-the-delta principle;
- custom-build justification;
- search stop rule.

### Validation

The `validation` skill preserves the distinction between:

- verification;
- validation;
- action completion;
- capability availability;
- outcome proof;
- post-action rerouting;
- evidence-driven completion.

## Rule

If a future canonical section cannot be mapped to an always-on invariant, a focused skill, or a verification artifact, do not silently drop it.

Either:

1. add the missing runtime representation; or
2. explicitly document why the section is intentionally canonical-only.
