# Routing Examples

These are representative examples of how the compact router is expected to behave.

They are **examples**, not measured behavioral evals or regression tests.

| Case | Expected primary route | What should usually remain unloaded |
|---|---|---|
| "Fix this obvious typo." | Direct execution | modeling, decision-analysis, capability-sourcing, planning |
| "I don't understand why this behaves differently in two cases." | Model Gap → `modeling` | capability-sourcing unless a missing capability emerges |
| "The exact official database is known; retrieve the current value." | Evidence Gap → `evidence-acquisition` | observability-coverage unless frame sufficiency is uncertain |
| "Google cannot find a local-government list; relevant publishing may happen on platform-native channels." | Evidence Gap → `observability-coverage` | decision-analysis unless materially different observation strategies remain |
| "Infer what all potential players want from 10,000 Reddit comments." | Evidence Gap → `observability-coverage` | do not treat Reddit as the target population |
| "We need actual in-game behavior, but no telemetry or equivalent trace exists." | Evidence Gap → measurement; Capability Gap if observation capability is missing | generic web retrieval |
| "Should we choose A or B? Both satisfy hard constraints." | Decision Gap → `decision-analysis` | planning until a direction is selected |
| "We need OCR. Should we build it?" | Capability Gap → `capability-sourcing` | direct custom implementation |
| "Improve this game's distant-world visual quality." | Identify required visual outcome → inspect project capability surface → `capability-sourcing` only if the source is unresolved | do not let a coding executor default to procedural code when DCC/assets/generators/specialist routes may materially change quality |
| "Implement the selected migration across five dependent stages." | Planning Gap → `planning` | decision-analysis unless a real trade-off reappears |
| "The feature is implemented; prove it works for the intended user need." | Verification / Validation Gap → `validation` | capability-sourcing unless the capability itself failed |
| "This repeated release process keeps failing and manual verification is expensive." | `workflow-hardening` task mode | project-modeling unless project structure is the blocker |
| "Derive current work from goals and dependencies." | `project-modeling` task mode | capability-sourcing unless a work item needs a missing capability |
| "Turn this validated slice into instructions for another agent." | `delegation` task mode | modeling if the slice is already sufficient |
| "Give me the conclusion without dumping the investigation." | `decision-surface` task mode | unrelated domain skills |

## Multi-gap example

A task can contain multiple simultaneous Gaps:

```text
Architecture decision
├─ Model Gap: current ownership is unclear
├─ Evidence Gap: performance data is missing
└─ Decision Gap: two viable designs exist
```

The router should not try to label the task with one permanent state.

It should choose the current **Dominant Gap**. For example:

```text
inspect current ownership
→ Model Gap reduced
→ missing performance observation becomes decisive
→ Evidence Gap becomes dominant
→ acquire evidence
→ compare the two designs
→ Decision Gap becomes dominant
```

## Over-routing failures

The Protocol is being applied poorly if the agent:
- loads all skills by default;
- treats every non-trivial request as a Model Gap;
- keeps modeling after the decisive evidence need is known;
- triggers observation-space analysis for an obvious authoritative single-source lookup;
- manufactures alternatives when one action clearly follows;
- performs a full capability landscape for a trivial commodity choice;
- plans an obvious one-step action;
- recommends workflow automation before repeated failure, risk, scale, or verification cost justifies it;
- exposes the entire methodology in the user-facing answer.

## Under-routing failures

The Protocol is also being applied poorly if the agent:
- acts while a decision-changing unknown is obvious;
- treats one observation frame as the entire target reality;
- turns a capability need directly into custom implementation;
- fails to discover a materially relevant capability that already exists in the project or workflow;
- lets the executor's native modality choose the implementation without checking production fit;
- declares success from a command or artifact without relevant proof;
- ignores evidence that contradicts the working model.

## Model-integrity regression cases

These cases are representative maintenance checks introduced in v2.8.0. They
are still examples, not automated model-behavior evals.

| Failure pattern | Expected behavior |
|---|---|
| A complex model is explained as `Need → Capability → Work Item` even though the capability-source/solution choice changes risk and proof. | Layer-Preservation Test rejects the simplification; keep `Need → Required Capability → Capability Source / Solution → Implementation / Work` at the simplest faithful level. |
| Two claims share one gameplay scenario, but failure of Claim A requires fixing motivation while failure of Claim B requires fixing consequence/agency. | Separation + Compilation Integrity require separate judgments even if one Work Item or scenario contributes evidence to both. |
| An upstream dependency changes from `BLOCKS` to `COUPLED`, but a derived execution plan still contains the old relation. | Change-Impact identifies the plan as `REVALIDATION_REQUIRED`; the stale copied fact cannot remain an active execution authority. |
| Integration tests pass for an Agent/provider path, but no target user has experienced the intended product value. | Record `VERIFICATION PASS` only; product `VALIDATION PASS` remains unsupported. |
| An abstract cross-layer model looks coherent, but no representative concrete scenario can be run end-to-end without inventing missing behavior. | Scenario / Run Test fails; do not call the model sufficiently trustworthy until the missing state, relation, precondition, or rule is modeled. |


## Model-fit and credibility regression cases

These cases are representative maintenance checks for v2.9.0.

| Failure pattern | Expected behavior |
|---|---|
| The user asks whether to buy one of three subscriptions, but the agent forces the project-delivery hierarchy `Goal → Capability → Milestone → Work Item`. | Model Purpose / Schema Selection rejects the mismatch; use a decision model with Goal, criteria, alternatives, evidence, decision, and review trigger at the minimum sufficient depth. |
| A representative gameplay scenario can be narrated end-to-end, so the agent marks the product hypothesis validated without a real playtest or observation. | Scenario / Run Test allows a conceptual Scenario Pass only; the scenario design is not evidence and cannot produce a product VALIDATION PASS by itself. |
| A capability-sourcing analysis compares three LLM vendors and concludes the solution landscape was covered even though script, rule-based, hybrid, existing internal, and no-new-capability approaches could materially change the decision. | Solution-space coverage fails; inspect materially different source classes before comparing variants inside one class. |
| A model validated on one population / environment / version is reused to justify a materially different use. | Model Use Envelope + Claim–Evidence Fit require reassessing transferability and revalidation before relying on the prior PASS. |
| A clean causal chain is built from one anecdotal source and is presented as broadly verified. | Claim–Evidence Fit narrows the claim or reopens the Evidence Gap; structural coherence cannot upgrade weak or narrow evidence. |
| The agent invents a new custom requirements or architecture checklist even though a mature domain method would likely fit. | Method sourcing first inspects and tailors an established method / standard; invent only the unresolved delta. |


## Capability-surface regression cases

These cases are representative maintenance checks introduced in v2.10.0.

| Failure pattern | Expected behavior |
|---|---|
| A coding agent must improve a 3D visual result and immediately writes procedural geometry even though the project has an established DCC pipeline, qualified assets, generators, and specialist routes. | Identify the required visual outcome first, inspect the relevant Capability Surface, compare production/quality ceiling, then choose the source. The executor's native modality is not a decision criterion by itself. |
| A production capability exists in scattered documentation but the downstream executor cannot discover it from the target repository instructions or task handoff. | Treat the capability as operationally unavailable until it is made discoverable through a lightweight routing entry or preserved in the execution contract. |
| A source is fast and highly testable but cannot plausibly reach the required final fidelity. | Reject or constrain it to prototype/intermediate use; quality/production ceiling is part of fit. |
| Upstream intentionally leaves the capability source open, but prompt compression removes all available-means context. | Delegation preserves enough discoverable capability surface for the downstream executor to make the remaining choice without native-tool bias. |


## Verified-closure regression cases

These maintenance examples were added in v2.12.0.

| Failure pattern | Expected behavior |
|---|---|
| A prior renderer baseline was qualified, pinned, and still fits the same production envelope, but a new task asks the coding agent to invent a fresh renderer from a verbal style description. | Detect **Lost Closure** risk. Reuse the qualified baseline, keep it Fixed Core, and build only the integration / product-specific delta. |
| NPC reservation/HSM/LOD stress tests pass, but players still report that NPCs do not feel alive. | Preserve the subsystem VERIFICATION closure; do not rewrite it or promote it to product VALIDATION. Open the missing player-visible composition/validation gap. |
| Climb tests pass on a ridge fixture, then trees/roofs expose stuck states. | Diagnose **False Closure** if the fixture PASS was generalized beyond its proof scope. Expand/invalidate only the affected geometry envelope and preserve unrelated movement closures. |
| Vegetation repeatedly needs new local exclusions (water, road, platform, building). | Fix the escaped case, then consider closure capitalization: graduate the repeated local rule into the smallest shared spatial-placement invariant / mechanism that prevents the whole failure class. |
| Quest lifecycle/persistence/reward correctness is proven, but players cannot tell where to go. | Keep the backend closure. Guidance was never closed; classify it as an OPEN product gap rather than a regression of the quest subsystem. |


## Recursive-sourcing regression case

This maintenance example was added in v2.12.1.

| Failure pattern | Expected behavior |
|---|---|
| The project needs a stronger coding-agent harness, so the assistant writes a detailed prompt instructing another agent to invent a Closure/Reference harness from scratch. | Reclassify the proposed harness as a **meta-capability**. Inspect the existing repository harness and mature harness-authoring / agent-customization sources first; select the closest baseline and delivery surfaces, then delegate only the unresolved project-specific delta. |
