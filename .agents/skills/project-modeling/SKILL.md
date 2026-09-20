---
name: project-modeling
description: Derive project work from goals, outcomes, capabilities, dependencies, milestones/gates, gaps, and evidence. Use for project structure, dependency maps, milestone derivation, scope control, and deciding whether a work item is justified. Do not treat task lists as the fundamental model of the project.
---

# Project Modeling

For project work, derive work through:

```text
Goal
  ↓
Outcome
  ↓
Capability
  ↓
Dependency
  ↓
Milestone / Gate
  ↓
Gap
  ↓
Work Item
  ↓
Evidence
```

Keep this distinction explicit:

```text
Capability
  ≠
Tool
  ≠
Vendor
  ≠
Implementation
```

A Capability states what the project must be able to do.

Only after the Capability is justified should its source be selected.

Tasks are interventions against project Gaps. They are not the fundamental structure of the project.

## Work-item traceability

A current Work Item should normally answer:

- Which Gap does it close?
- Which Dependency or Capability does that affect?
- Which Outcome does that support?
- Which Goal does that ultimately serve?

If it cannot, consider:

- Future
- Research
- Nice-to-have
- Remove

rather than Current Work.

## Coordination with other skills

- unclear project reality → `modeling`;
- missing external/project facts → `evidence-acquisition`;
- multiple directions → `decision-analysis`;
- capability source unresolved → `capability-sourcing`;
- execution dependencies after direction selection → `planning`;
- proof of milestone/outcome → `validation`.
