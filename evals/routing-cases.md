# Routing Regression Cases

These cases are lightweight behavioral checks for `AGENTS.md` and skill activation.

They are not exhaustive correctness benchmarks. Their job is to catch obvious routing drift and over-loading.

| Case | Expected primary route | Skills that should normally stay unloaded |
|---|---|---|
| "Fix this obvious typo." | Direct execution | modeling, decision-analysis, capability-sourcing, planning |
| "I don't understand why this system behaves differently in two cases." | Model Gap | capability-sourcing unless a missing capability emerges |
| "We know the missing value; find the authoritative current number." | Evidence Gap | modeling unless source identity is unclear |
| "Should we choose A or B? Both satisfy the hard constraints." | Decision Gap | planning until a direction is chosen |
| "We need OCR; should we build it?" | Capability Gap | planning until source is chosen |
| "Implement the already-selected migration across five dependent stages." | Planning Gap | decision-analysis unless a real trade-off reappears |
| "The feature is implemented; prove it works for the intended user need." | Verification / Validation Gap | capability-sourcing unless the capability itself failed |
| "This repeated release process keeps failing and manual verification is expensive." | Harness Engineering | project-modeling unless project structure is the blocker |
| "Derive current work from product goals and dependencies." | Project Modeling | capability-sourcing unless a work item needs a missing capability |
| "Turn this validated slice into instructions for another agent." | Delegation | modeling if the slice is already sufficient |
| "Give me the conclusion without dumping the analysis." | Decision Surface | unrelated domain skills |

## Multi-stage cases

### Unknown behavior, then known evidence need

```text
Request
→ Model Gap
→ modeling
→ exact missing observation becomes known
→ Evidence Gap
→ evidence-acquisition
```

Expected behavior: stop expanding the abstract model once the missing evidence is identified.

### Missing capability with mature alternatives

```text
Need capability
→ Capability Gap
→ capability-sourcing
→ multiple viable sources remain
→ Decision Gap
→ decision-analysis
→ source selected
→ Reality Gap
→ execute
→ validation
```

Expected behavior: do not translate "need capability" directly into custom implementation.

### Complex project request

```text
Goal unclear
→ modeling
→ project structure becomes clear
→ project-modeling
→ dependent execution selected
→ planning
→ action
→ validation
```

Expected behavior: do not load every skill at the beginning.

## Failure checks

A routing regression exists if the agent:

- loads all skills by default;
- treats every request as a Model Gap;
- keeps modeling after an exact Evidence Gap is known;
- treats every Reality Gap as a build request;
- runs a large solution-landscape study for trivial commodity work;
- performs formal Decision Analysis when one action is clearly implied;
- declares completion because a command/tool succeeded without outcome evidence;
- dumps the full methodology into the human-facing answer without need.
