# Changelog

This file records public semantic and engineering changes. Canonical methodology remains in `PROTOCOL.md`.

## v2.15.0 — 2026-09-25

### Protocol

- Added a **Problem Frame / Ownership Boundary Gate** between necessity validation and local Gap execution. A correct local Dominant Gap is now explicitly treated as frame-relative rather than automatically high leverage.
- Added the **Ownership Frontier**: project ownership is an explicit decision about which capabilities should remain project-owned versus consumed, adapted, referenced, delegated, or used as Behavioral Oracles.
- Added the **Ceiling-Baseline Counterfactual**: temporarily assume the validated parent capability already exists at production quality, subtract the work that would disappear, and use the remainder to expose candidate Project Delta before descending back to feasible sources.
- Strengthened Capability Sourcing from reuse granularity to **sourcing altitude**: inspect the highest sufficiently fitting parent-level baseline / reference / oracle first, then descend only when material constraints rule that level out.
- Added **Strategically Superseded Closure**: a local implementation may remain technically valid while a stronger parent baseline or changed ownership boundary makes continued ownership unnecessary. Closure now protects solved uncertainty and value, not incumbent implementation.
- Added a frame-escalation trigger: when repeated local closures consume meaningful work without proportional movement in the parent Outcome, revalidate the problem frame before selecting the next sibling Gap.
- Strengthened Project Modeling and Delegation so unresolved ownership / source assumptions cannot silently compile into implementation-shaped Work Items or coding prompts.

### Runtime / evidence

- Updated the compact router, modeling, capability-sourcing, project-modeling, delegation, runtime map, protocol index, method registry, README, and routing examples.
- Added R023, the real Nameless Reach failure where Why-before-How and local reuse were already present, but the current decomposition and ownership boundary still caused agents to optimize valid child work instead of challenging the frame.
- Preserved v2.14.0 under `docs/history/`.
- No new deterministic enforcement rule was added; frame validity, ownership boundaries, and strategic supersession remain contextual model / project judgments.

## v2.15.0 — 2026-09-25

### Protocol

- Added a **Problem Frame / Ownership Boundary Gate** between necessity validation and local Gap execution. A correct local Dominant Gap is now explicitly treated as frame-relative rather than automatically high leverage.
- Added the **Ownership Frontier**: project ownership is an explicit decision about which capabilities should remain project-owned versus consumed, adapted, referenced, delegated, or used as Behavioral Oracles.
- Added the **Ceiling-Baseline Counterfactual**: temporarily assume the validated parent capability already exists at production quality, subtract the work that would disappear, and use the remainder to expose candidate Project Delta before descending back to feasible sources.
- Strengthened Capability Sourcing from reuse granularity to **sourcing altitude**: inspect the highest sufficiently fitting parent-level baseline / reference / oracle first, then descend only when material constraints rule that level out.
- Added **Strategically Superseded Closure**: a local implementation may remain technically valid while a stronger parent baseline or changed ownership boundary makes continued ownership unnecessary. Closure now protects solved uncertainty and value, not incumbent implementation.
- Added a frame-escalation trigger: when repeated local closures consume meaningful work without proportional movement in the parent Outcome, revalidate the problem frame before selecting the next sibling Gap.
- Strengthened Project Modeling and Delegation so unresolved ownership / source assumptions cannot silently compile into implementation-shaped Work Items or coding prompts.

### Runtime / evidence

- Updated the compact router, modeling, capability-sourcing, project-modeling, delegation, runtime map, protocol index, README, and routing examples.
- Added R023, the real Nameless Reach failure where Why-before-How and local reuse were already present, but the current decomposition and ownership boundary still caused agents to optimize valid child work instead of challenging the frame.
- Preserved v2.14.0 under `docs/history/`.
- No new deterministic enforcement rule was added; frame validity, ownership boundaries, and strategic supersession remain contextual model / project judgments.

## v2.14.0 — 2026-09-24

### Protocol

- Promoted **Why before How / Necessity Gate** into the non-trivial runtime: a clearly stated task, requirement, component, or optimization no longer justifies itself.
- Before decomposition, sourcing, optimization, automation, or implementation, require the minimum sufficient check of the real outcome and whether the proposed work should be kept, reframed, replaced, deleted, or deferred.
- Clarified that **Five Whys** is a conditional root-cause technique for causal diagnosis, not a universal five-question ritual and not a substitute for validating whether work should exist.
- Strengthened Capability Sourcing so the current decomposition is not automatically the unit of reuse; a mature integrated parent-level baseline should be considered when it can satisfy the validated outcome with lower total delta and ownership burden.
- Clarified that Delta is baseline-relative: choosing a stronger baseline may eliminate work that looked like unavoidable project-specific Delta.

### Runtime / evidence

- Updated the compact router, modeling and capability-sourcing skills, runtime map, protocol index, method registry, README, and routing examples.
- Added R022, the real Nameless Reach environment-production failure where local reuse was working but the project optimized the wrong unit of work before challenging whether terrain/water/foliage/building tasks were necessary.
- Added NASA verification-vs-validation and ASQ Five Whys references to the non-canonical method registry.
- Preserved v2.13.0 under `docs/history/`.
- No new deterministic enforcement rule was added; necessity and problem-framing remain contextual model judgments.

## v2.13.0 — 2026-09-24

### Protocol

- Added **Enforcement Graduation** and the distinction between **Epistemic Closure** and **Operational Closure**.
- Added the adversarial completion question: if an executor ignores the written rule, can the invalid state still enter the system?
- For recurring/consequential mechanically decidable invariants, require the cheapest reliable enforcement when hardening is warranted, plus known-invalid rejection and representative-valid acceptance.
- For outcomes that cannot be decided mechanically, require an explicit Human/Product gate rather than fake automation.
- Prefer protecting invariants over freezing implementation details; path/diff guards are appropriate when path ownership itself is the invariant.
- Explicit enforcement debt may be accepted when proportional, but cannot be mislabeled as Operational Closure.

### Runtime / evidence

- Updated runtime skills, method registry, runtime map, protocol index, README, and routing examples.
- Added R021, the real failure where Closure routing became legible without preventing silent violation.
- External baseline: OpenAI Harness Engineering plus AWS mechanism design.
- Preserved v2.12.1 under `docs/history/`.

## v2.12.1 — 2026-09-24

### Protocol

- Added **No Meta-Layer Exemption**: reusable harnesses, Skills, validators, schemas, prompt systems, orchestration layers, and agent configurations are capabilities and must pass the same sourcing/baseline logic before custom authoring.
- Added bounded recursive routing for meta-capabilities: inspect existing project/runtime mechanisms, source mature authoring approaches, fit-gap, establish a baseline, then build only the project-specific delta.
- Strengthened Workflow Hardening so "build a harness" cannot silently skip Capability Sourcing.
- Added instruction-surface selection by scope, loading behavior, authority, determinism, context cost, and runtime support.

### Runtime / evidence

- Updated the compact router, capability-sourcing, workflow-hardening, delegation, runtime map, protocol index, method registry, README, and routing examples.
- Added R020, a real meta-regression in which an upstream prompt attempted to invent a repository harness before sourcing mature harness-authoring capability.
- Added current external method pointers for OpenAI Harness Engineering, OpenAI Cookbook harness-authoring workflow, OpenAI Skill Creator, Anthropic steering surfaces, and GitHub repository/path-scoped instructions.
- Preserved v2.12.0 under `docs/history/`.
- No new deterministic enforcement rule was added; recognizing that an intervention is itself a sourcing-relevant meta-capability remains a contextual routing judgment.

## v2.12.0 — 2026-09-24

### Protocol

- Added **Verified Closure**: a bounded prior result may be reused without recomputation only while its claim, scope/use envelope, assumptions, dependencies, environment/version and other validity conditions still hold.
- Added explicit failure diagnoses for **False Closure**, **Lost Closure**, and **Unmaterialized Closure** without turning them into new Gap types.
- Added **managed variability**: distinguish Fixed / Proven Core, Allowed Variation, and Project Delta when a mature baseline materially constrains execution.
- Strengthened Capability Sourcing with **Baseline Acquisition / Reference Materialization** and source roles: reusable component, implementation reference, behavioral oracle, and evidence-only.
- Strengthened post-action work with proportional **closure capitalization** so recurring consequential learning becomes a discoverable / enforceable project mechanism rather than prompt prose alone.

### Runtime / evidence

- Updated the compact router plus capability-sourcing, workflow-hardening, validation, delegation, runtime map, protocol index, README, and routing examples.
- Added five sanitized real-world retrospective cases (R015–R019) covering baseline reuse, subsystem-vs-product closure, proof-scope leakage, invariant graduation, and a genuinely open product gap.
- Preserved v2.11.1 under `docs/history/`.

### Executable enforcement

- Extended the decision envelope with an optional closure block.
- Added deterministic guards for unjustified reopening of an explicitly valid in-scope closure, claiming new closure beyond declared proof scope, and completion when capitalization has explicitly been marked required but remains absent.
- Added three public conformance fixtures; the suite is now 11 cases.
- Mechanical PASS still proves only the supplied envelope satisfies encoded policy, not that the closure facts themselves are true.

## v2.11.1 — 2026-09-24

### Protocol

- Refined Runtime State Observability into **Runtime Context + operator projection**: runtime/session/trace state is distinct from what should appear in the human-facing answer.
- Replaced task-complexity-driven receipt display with **runtime-state boundary** refresh semantics: refresh when executor/source/environment/Gap/freshness changes make prior state unreliable.
- Clarified that a **Runtime Receipt** is an on-demand or decision-relevant projection, not a mandatory banner for every complex task.
- Separated runtime observability from the human **Output Contract**. Poor communication should be repaired by Decision Surface / output conformance, not by dumping more telemetry.
- Added proportional use of host-supported structured-output / output-guardrail mechanisms for mechanically checkable presentation constraints.

### Runtime / evidence

- Updated the compact router, runtime map, Protocol index, README, and R014 retrospective wording.
- Preserved v2.11.0 under `docs/history/`.
- Kept the retrospective set at fourteen cases: this patch refines the semantics learned from R014 rather than inventing a new failure class.
- No new deterministic enforcement claim is made; runtime freshness and decision relevance remain contextual judgments.

## v2.11.0 — 2026-09-24

### Protocol

- Added **Runtime State Observability and Freshness**: agents may reuse sufficiently identified, relevant, fresh context instead of mechanically re-fetching every turn.
- Added explicit refresh conditions for new/unknown/stale runtime state, changed upstream state, new Sources of Truth/environments/Gaps, and current/latest verification requests.
- Added a compact **Runtime Receipt** so Protocol source/version, selected method, Source of Truth/freshness basis, external-evidence status, and Dominant Gap can be inspected without exposing private reasoning.
- Required agents to mark unavailable retrieval channels and constrain claims rather than silently implying that a refresh occurred.

### Runtime / evidence

- Updated the compact router, runtime map, Protocol index, README, and retrospective evidence set.
- Added a fourteenth sanitized real-world retrospective case covering invisible protocol/current-state freshness and unnecessary “always browse” pressure.
- Preserved v2.10.0 under `docs/history/`.
- No deterministic enforcement claim is made for freshness judgment or Runtime Receipt truthfulness; these remain runtime/model behavior rules.

## v2.10.0 — 2026-09-23

### Protocol

- Reordered the non-trivial runtime so the Agent identifies the required change/outcome, inspects the relevant capability surface when material, then selects the capability source before choosing the intervention.
- Added **Capability Surface** semantics: a capability that exists but is not discoverable/usable by the current executor is operationally unavailable.
- Added an **executor-native modality bias guard**: do not choose code, visual authoring, spreadsheets, a familiar library, or another implementation merely because it is the executor's most salient tool.
- Added **quality / production ceiling** and **executor fit** to capability-source decisions so prototype-friendly sources are not silently treated as production-suitable.
- Strengthened delegation so a task-specific prompt preserves either the selected capability source or enough discoverable available means when source choice remains decision-relevant.

### Runtime / evidence

- Updated the compact router, capability-sourcing skill, delegation skill, runtime map, and Protocol index.
- Added a thirteenth sanitized real-world retrospective case for a capability that existed in the project but was not surfaced to the executor before implementation choice.
- Preserved v2.9.1 under `docs/history/`.
- No new deterministic enforcement claim is made for executor-bias judgment; this remains a model/runtime behavior rule rather than a mechanically proven invariant.

## v2.9.1 — 2026-09-23

### Protocol

- Added a staged-audit rule for existing layered models: downstream material may be inspected to test consistency, but deeper layers must not be treated as accepted before their upstream derivation passes.

### Evidence

- Added 12 sanitized retrospective cases reconstructed from real AI-assisted work.
- Added a controlled Protocol OFF vs ON pilot specification. The controlled pilot is designed but has **not yet been run**.

### Executable enforcement

- Added JSON Schema + OPA/Rego policy for deterministic invariants.
- Added public conformance fixtures and a portable runner.
- Added CI-built WebAssembly policy bundle.
- Added Protocol Conformance CI and OpenSSF Scorecard analysis.

### Repository governance

- Added CONTRIBUTING.md, SECURITY.md, CODEOWNERS, and Dependabot.
- Added public navigation and contribution paths for failure-driven evolution.

## v2.9.0

- Added intended-use/schema selection and model-use envelopes.
- Strengthened claim–evidence fit and representative-scenario vs evidence separation.
- Strengthened solution-space coverage and mature capability sourcing before custom methodology.
