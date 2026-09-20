# Routing Regression Cases

These cases are lightweight behavioral checks for `AGENTS.md` and skill activation.

They are not exhaustive correctness benchmarks. Their job is to catch obvious routing drift and over-loading.

| Case | Expected primary route | Skills that should normally stay unloaded |
|---|---|---|
| "Fix this obvious typo." | Direct execution | modeling, decision-analysis, capability-sourcing, planning |
| "I don't understand why this system behaves differently in two cases." | Model Gap | capability-sourcing unless a missing capability emerges |
| "We know the missing value; find the authoritative current number from the known official database." | Evidence Gap → evidence-acquisition | observability-coverage unless frame sufficiency is uncertain |
| "Google cannot find a local-government facility list, but the publishing ecosystem may include WeChat and platform-native sources." | Evidence Gap → observability-coverage | decision-analysis until materially different observation strategies remain |
| "Summarize what potential players want from 10,000 Reddit comments." | Evidence Gap → observability-coverage before generalizing | evidence-acquisition should not proceed as if Reddit = target population |
| "We need to know actual in-game behavior, but no telemetry or equivalent traces exist." | Evidence Gap → observability-coverage → measurement; capability-sourcing if observation capability is missing | generic retrieval-only search |
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

### Incomplete observation frame

```text
Need evidence about target reality
→ current frame may miss relevant reality
→ observability-coverage
→ map evidence generation / frames / channels
→ select one or more sufficient frames
→ evidence-acquisition
→ retrieve or measure
→ qualify evidence
→ conclusion constrained to supported scope
```

Expected behavior: do not equate one search engine, platform, sample, or telemetry stream with the whole relevant reality. Do not add more sources unless they materially improve coverage or reduce a decision-relevant blind spot.

### Known sufficient authoritative frame

```text
Need exact current value
→ known authoritative database directly covers the target entity/state
→ evidence-acquisition
→ retrieve + verify identity/version/freshness
```

Expected behavior: do not trigger a large observability study for an obvious single-source lookup.

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
- treats a search engine, platform, sample, or telemetry stream as equivalent to the full target reality;
- over-optimizes queries while the observation frame is materially incomplete;
- generalizes from an observed population to a target population without checking coverage / representation risk;
- triggers observability-coverage for obvious authoritative single-source lookups where frame sufficiency is already clear;
- treats every Reality Gap as a build request;
- runs a large solution-landscape study for trivial commodity work;
- performs formal Decision Analysis when one action is clearly implied;
- declares completion because a command/tool succeeded without outcome evidence;
- dumps the full methodology into the human-facing answer without need.
