# Real-World Retrospective Pilot v0.1

Status: **Retrospective case audit**

These cases are reconstructed from real historical user/assistant interactions. They are sanitized to preserve the failure structure without publishing unnecessary private or proprietary details.

This file tests **Protocol coverage**: if the current Protocol were applied correctly, does it contain the distinctions and routing needed to prevent the observed failure?

It does **not** prove causal model improvement. A controlled Protocol OFF vs ON eval is still required.

---

## R001 — Capability need was translated directly into a custom pipeline

**Date:** 2026-09-20

**Real task context**

A workflow needed to obtain images/content from a web source, extract structured information, and validate the result.

**Observed failure**

The assistant moved too quickly from the need to specific implementation choices such as browser automation, DOM-specific extraction, a particular OCR/document model, and a custom pipeline.

Materially different capability sources had not been compared.

**User correction**

Research mature existing options first, run a cheap spike where fit is uncertain, then choose the toolchain. Do not convert “we need this capability” directly into “build this implementation.”

**Expected Protocol behavior**

- Diagnose **Capability Gap**.
- Because multiple materially different sources remain viable, expose the resulting **Decision Gap**.
- Run capability sourcing before implementation.
- Prefer reuse/adopt/integrate and **build only the unresolved delta**.
- Define proof for the selected source before committing to a larger pipeline.

**Current v2.9 coverage:** **PASS**

The current router and capability-sourcing rules directly encode this failure mode.

---

## R002 — Plausible collected data was treated as usable evidence

**Date:** 2026-09-17

**Real task context**

An AI-assisted collection workflow was used on a small real-world POI dataset.

**Observed failure**

Some returned values were wrong or hard to verify, provenance was missing, and human verification became expensive enough that manually redoing the work could be easier.

The workflow blurred “modeling what fields should exist” with “acquiring trustworthy facts.”

**User correction**

Do not fill unknowns with plausible values. Separate schema/model design from evidence acquisition. Use source hierarchy, provenance, entity matching, explicit evidence states, and leave unresolved fields unresolved when necessary.

**Expected Protocol behavior**

- Diagnose an **Evidence Gap**, not a Modeling success.
- Prefer authoritative traces and preserve provenance.
- Distinguish Verified / Candidate / Approximate / Conflicting / Unresolved.
- Verify identity/entity matching when material.
- Narrow claims to the evidence actually obtained.
- Stop pretending that generated analysis is a Source of Truth.

**Current v2.9 coverage:** **PASS**

Evidence honesty, claim–evidence fit, Source of Truth, and evidence states directly cover the observed failure.

---

## R003 — A top-down model audit jumped ahead into lower layers

**Date:** 2026-09-20

**Real task context**

The user asked to inspect a project model from the very top and verify the logical chain layer by layer.

**Observed failure**

The assistant jumped early into Release / Capability / Architecture structure before the upstream Purpose / Outcome layers had been individually checked.

The proposed structure could be reasonable in isolation, but it violated the audit intent: lower layers were being reasoned about before upstream semantics were accepted.

**User correction**

Start at the top. Check one layer and its relationship to the next before moving downward. Do not prematurely decompose the whole project into a familiar hierarchy.

**Expected Protocol behavior**

- Treat this as a **Model Gap** with project-modeling support.
- Select the model for the intended use: this is an **audit of an existing semantic chain**, not immediate project decomposition.
- Preserve materially different layers.
- Do not compile or elaborate downstream layers before the upstream relation being audited is sufficiently trustworthy.

**Current v2.9.1 coverage:** **PASS**

This real failure exposed a missing staged-audit rule in v2.9.0. v2.9.1 now states that downstream material may be inspected to test consistency, but deeper layers must not be treated as accepted or compiled as though their upstream derivation had already passed.

---

## R004 — Implementation progress conflicted with actual runtime experience

**Date:** 2026-09-01

**Real task context**

A game prototype work item had reported implementation progress, but actual play still showed obvious problems: character scale/animation quality, environment presentation, interaction usability, and possible runtime/version mismatch.

**Observed failure**

There was a risk of treating implementation/test progress as sufficient evidence and moving on to a new work item instead of reconciling the observed runtime.

**User correction**

Stay on the current work item. First establish runtime truth, confirm that the intended build/content is actually what is being launched, then repair the observed failures. Do not declare the work complete until real play validates the intended result.

**Expected Protocol behavior**

- Route to **Verification / Validation Gap**.
- Inspect the real Source of Truth: runtime/build/version/environment.
- Check identity/version when stale or wrong runtime is plausible.
- Distinguish implementation verification from product/visual validation.
- Reopen the Reality Gap when observed play contradicts the reported state.

**Current v2.9 coverage:** **PASS**

Validation, Source of Truth, identity/version checks, and post-action update directly cover this failure.

---

## R005 — A management UI was being invented instead of sourcing mature interaction patterns

**Date:** 2026-09-22

**Real task context**

A local product/discovery management UI needed professional navigation, tracking, hierarchy, status visibility, search, and item detail behavior.

**Observed failure**

Earlier directions risked producing a bespoke Viewer-like interface that was hard to use for real management and did not sufficiently reuse mature product/project-management interaction patterns.

**User correction**

Inspect mature products and open implementations first. Reuse the closest proven information architecture and interaction patterns from established tools where they fit; customize only where the domain semantics genuinely differ.

**Expected Protocol behavior**

- Separate the required management **capabilities** from the UI implementation.
- Source mature solution classes and patterns before inventing a new interaction model.
- Fit-gap against the local domain and Source of Truth.
- Build only the domain-specific delta.
- Validate on a real project, not a toy demo.

**Current v2.9 coverage:** **PASS**

Model selection plus method/capability sourcing and “build the delta” cover the failure.

---

## R006 — A custom harness direction omitted an obvious mature baseline

**Date:** 2026-09-10 to 2026-09-11

**Real task context**

The assistant was helping design engineering harnesses for agent-driven development and asset/workflow validation.

**Observed failure**

A proposed custom harness direction did not first inspect an obvious mature baseline and relevant industrial solutions. The result risked creating a parallel home-grown framework.

**User correction**

Research the real mature implementations first, classify what can be reused/adapted/referenced/rejected, then add only project-specific controls that remain unsolved.

**Expected Protocol behavior**

- Diagnose **Capability Gap** before design.
- Inspect internal/external mature sources.
- Cover materially different source classes, not just preferred variants.
- Use a cheap spike when fit is uncertain.
- Build only the unresolved delta.
- Do not equate “custom is possible” with “custom is justified.”

**Current v2.9 coverage:** **PASS**

This failure is explicitly represented by capability sourcing and the anti-pattern against inventing custom methods when a mature fit-for-purpose method likely exists.

---

## R007 — Progressive disclosure risked deleting accumulated semantics

**Date:** 2026-09-20

**Real task context**

The Protocol itself was being compressed into a router + skills architecture.

**Observed failure**

There was a risk that “make the runtime smaller” would become “delete or rewrite accumulated tests/checklists/methodology,” losing semantics that had been learned from earlier failures.

**User correction**

Progressive disclosure is a loading strategy, not permission to delete accumulated methodology. Preserve canonical content and intentionally retained tests; when uncertain, restore from history and apply the smallest change.

**Expected Protocol behavior**

- Compress context, not decision-relevant distinctions.
- Keep canonical vs derived authority explicit.
- Preserve semantics when compiling canonical material into runtime files.
- Treat uncertain semantic equivalence as a maintenance risk.

**Current v2.9 coverage:** **PASS**

The current repository architecture, preservation policy, compilation-integrity rules, and layer-preservation rules directly encode this lesson.

---

## R008 — A technically correct report spent attention on low-value detail

**Date:** 2026-09-23

**Real task context**

A multi-agent engineering session had accumulated substantial changes and needed a status/merge report.

**Observed failure**

The report spent too much space on diff/process detail while the operator mainly needed the current state, merge decision, and what should happen next.

**User correction**

Be much more concise. For large multi-agent changes, surface the meaningful state transition and PR/merge boundary rather than narrating every diff detail.

**Expected Protocol behavior**

- Use the **decision-surface** mode.
- Lead with Bottom Line.
- Show only 1–3 decision-relevant current facts.
- Give one primary next action and proof/exit condition.
- Do not duplicate process history or expose methodology that does not change the decision.

**Current v2.9 coverage:** **PASS**

The cognitive budget, no-duplication rule, and Bottom Line / Now / Next / Proof interface cover this failure directly.

---

## R009 — A guard was nearly bypassed before repository reality was checked

**Date:** 2026-09-21

**Real task context**

A repository guard/review capability appeared stale or missing during an engineering-governance task.

**Observed failure**

The assistant initially treated the capability as absent/stale and moved toward bypass/removal before establishing the canonical upstream state.

**User correction**

Inspect the real source first. The capability did exist upstream; the actual problem was local distribution drift plus an overly broad trigger. Preserve the capability and repair the routing/distribution defect instead of bypassing it.

**Expected Protocol behavior**

- Treat repository state as an **Evidence Gap** before changing governance.
- Inspect authoritative upstream/current state.
- Distinguish “capability missing” from “capability present but not distributed/routed correctly.”
- Do not weaken an invariant merely to make execution pass.
- Apply the smallest repair at the lowest incorrect layer.

**Current v2.9 coverage:** **PASS**

Source-of-Truth discipline, evidence acquisition, capability distinction, and the anti-pattern against bypassing reality through implementation all cover this failure.

---

## R010 — An execution adapter started becoming a second operating system

**Date:** 2026-09-21

**Real task context**

A concise launch kit was being refined to help a coding agent execute an already-modeled project.

**Observed failure**

The assistant proposed a growing set of session/stability/execution rules, risking duplication of the canonical Operation Protocol and the target repository's own authority.

**User correction**

Keep the launch adapter minimal. Do not create a third bootstrap or duplicate project Source of Truth. Preserve the authority boundary: outcome contract, execution adapter, and repository truth each have separate roles.

**Expected Protocol behavior**

- Use the minimum sufficient method/structure.
- Preserve authority boundaries and Source of Truth.
- Do not manufacture workflow infrastructure without a demonstrated repeated failure that requires it.
- Compile only the execution-relevant delta downstream.

**Current v2.9 coverage:** **PASS**

Minimum-sufficient-method, workflow-hardening restraint, delegation, and Source-of-Truth rules cover the failure.

---

## R011 — A task tool risked swallowing the upstream product model

**Date:** 2026-09-22

**Real task context**

A lightweight task/dependency tool had been adopted for active execution.

**Observed failure**

There was a risk of treating the task tool as the whole project-management model, even though it did not natively own Goal / Job / Opportunity / Product Hypothesis semantics.

**User correction**

Keep upstream product semantics in their existing authority. Let the task tool own execution state only. Fill capability gaps around orchestration/verification rather than replacing the entire lifecycle with a heavier platform or duplicating state.

**Expected Protocol behavior**

- Model the intended capability and authority boundary before choosing a tool.
- Run fit-gap rather than assuming a tool's schema defines the problem.
- Keep Need / Capability / Source / Implementation distinct.
- Avoid parallel Sources of Truth.
- Build/integrate only the missing delta.

**Current v2.9 coverage:** **PASS**

Model-purpose/schema-selection, capability sourcing, authority discipline, and project-modeling rules directly cover this failure.

---

## R012 — Branch cleanup risked deleting valuable unmerged work

**Date:** 2026-09-21 to 2026-09-22

**Real task context**

A repository had accumulated many short-lived branches/worktrees after multiple agent sessions.

**Observed failure**

“Clean everything up” could easily become mechanical deletion even though some branches contained valuable unique implementations or evidence that had not reached the canonical branch.

**User correction**

Re-observe each retained branch's actual state. Merge or graduate valid unique work, archive/reject obsolete work with concrete reasons, preserve blocked-but-valuable work, and only delete when canonical equivalence or obsolescence is demonstrated.

**Expected Protocol behavior**

- Inspect before acting.
- Treat uniqueness/equivalence as evidence questions.
- Define proof for safe deletion.
- Preserve decision-relevant unique code/evidence.
- Do not let cleanup convenience override Source of Truth or validation.

**Current v2.9 coverage:** **PASS**

Inspection-before-action, evidence honesty, proof-before-action, and completion/validation rules cover the failure.

---

## R013 — An available production capability was invisible to the executor

**Date:** 2026-09-23

**Real task context**

A visual-production agent in a realtime 3D project needed to improve an obviously weak distant-world silhouette. The repository already had a qualified DCC/3D asset pipeline and multiple production routes, while the coding agent also had direct procedural terrain tools.

**Observed failure**

The agent correctly diagnosed the visible gap and produced a technically sound procedural terrain solution, but it did not first surface the project's broader production capability set. The implementation route was therefore strongly shaped by the executor's native coding context and immediately visible tools.

The result was testable and useful, but the process risked a local optimum: a capability source with a higher artistic-control or production-quality ceiling could have been omitted simply because it was outside the executor's immediate modality.

**User correction**

Do not hard-code one tool as the answer. Make the project's available means discoverable, then let the agent choose among terrain authoring, DCC modeling, existing assets, generators, specialist tooling, or specialist escalation according to the actual blocker and required quality. Complex character/humanoid production should not default to a general agent hand-modeling from scratch merely because a DCC tool exists.

**Expected Protocol behavior**

- Identify the required visual outcome before committing to an implementation form.
- Inspect the relevant **Capability Surface** when source choice can materially change quality, speed, cost, or maintainability.
- Treat a capability that exists but is not discoverable to the executor as operationally unavailable.
- Guard against executor-native modality bias.
- Compare quality / production ceiling and executor fit, not only implementation convenience and testability.
- Preserve the selected source or available-means surface when delegating the work downstream.
- For repeated multi-tool domains, expose a lightweight capability-routing entry rather than relying on operator memory.

**Current v2.10.0 coverage:** **PASS**

This case exposed a real gap in v2.9.1. Capability sourcing existed, but capability discoverability and executor-native modality bias were not explicit runtime semantics. v2.10.0 adds those semantics to the canonical runtime, capability-sourcing, and delegation layers.

---


## R014 — Protocol/current-state freshness was invisible to the operator

**Date:** 2026-09-24

**Real task context**

A general-purpose AI was repeatedly asked to work under a repository-hosted operating protocol while project state, external research, and prior conversation context were changing across sessions.

**Observed failure**

The operator often could not tell whether the agent had actually read the current Protocol, which skill/method it had loaded, whether project state had been freshly inspected, or whether external evidence had been searched.

An initial correction risked overcompensating by making a Runtime Receipt a visible banner for every complex task. That would conflate runtime observability with human-facing presentation and create unnecessary output noise.

**User correction**

Do not equate rigor with “always browse” or “always print telemetry.” Reuse context when its identity, relevance, and freshness are sufficient; refresh when runtime-state boundaries make prior context unreliable. Keep the state observable, but project it to the operator only when it affects understanding, trust, authority, debugging, or the next action.

**Expected Protocol behavior**

- Maintain decision-relevant Runtime Context when work depends on state that can become stale, ambiguous, or executor-specific.
- Prefer runtime/session/trace storage when the host supports it.
- Reuse already-inspected context when it remains sufficiently fresh for the current decision.
- Refresh on runtime-state boundaries: new/untrusted executor state, plausibly stale source, changed upstream state, new Source of Truth/environment/Gap, or current/latest verification request.
- Treat a Runtime Receipt as an operator-facing projection, not the runtime state itself.
- Surface the receipt only when requested or when freshness/provenance/access/state changes are decision-relevant.
- Keep runtime observability separate from human Output Contract conformance.
- Distinguish external evidence as inspected / not required / unavailable rather than silently implying browsing occurred.
- Treat the receipt as observability metadata, not proof that the underlying claim is correct.

**Current v2.11.1 coverage:** **PASS**

v2.11.0 introduced runtime-state freshness and observability. v2.11.1 refines that correction to match mature runtime/trace practice: record state continuously enough for execution, refresh on state boundaries, and project only the minimum operator-relevant subset. Human output conformance remains a separate Decision Surface / guardrail concern.

---

## R015 — A qualified character-rendering baseline was reused instead of reinvented

**Date:** 2026-09-22 to 2026-09-23

**Real task context**

A realtime 3D game already contained a previously qualified dynamic-toon character renderer. A later First Playable pass needed that quality in the current runtime.

**Observed pattern**

The successful route explicitly treated the prior renderer as existing production capability: it pinned the prior source revision, preserved provenance, integrated the existing renderer into the current runtime, captured matched before/after evidence, and refused to turn the task into a new character/base-renderer project.

**Why this matters**

This is the positive control for closure preservation. The expensive uncertainty around the solved rendering baseline stayed closed; work concentrated on integration and the remaining visual delta.

**Expected Protocol behavior**

- Detect the prior proven baseline before designing a new renderer.
- Treat the validated renderer as Fixed Core inside its supported envelope.
- Preserve provenance and the pinned source identity.
- Reopen only the integration assumptions actually changed by the new runtime.
- Keep Human Outcome validation separate from technical renderer verification.

**Current v2.12.0 coverage:** **PASS**

Verified Closure + Baseline Acquisition describe this successful pattern directly.

---

## R016 — Strong NPC subsystem proof did not create a player-visible “living NPC” closure

**Date:** 2026-09-24

**Real task context**

The game already had a layered NPC architecture with WorldState, needs/context, intent selection, behavior execution, reservation, atomic interaction state machines, simulation LOD, deterministic stress tests, and debug inspection. Stress evidence included tens of thousands of interaction attempts with hard invariants at zero.

**Observed failure**

Despite strong subsystem verification, human play still reported repetitive dialogue, weak autonomy, and NPCs that did not feel alive. The project risked treating the existence and correctness of internal NPC machinery as proof of the player-facing product Outcome.

**Expected Protocol behavior**

- Preserve the verified subsystem closures; do not rewrite reservation/HSM/LOD merely because product validation failed.
- Do not promote subsystem VERIFICATION PASS into player-visible VALIDATION PASS.
- Identify the missing composition / product-validation closure: representative residents whose schedule, context, relationships, persistence, and consequences are actually perceived in play.
- Reopen only the layer contradicted by human evidence.

**Current v2.12.0 coverage:** **PASS**

Bounded Closure and proof-type separation prevent the lower-level PASS from swallowing the higher-level open Outcome.

---

## R017 — Traversal tests passed inside their fixtures while production geometry still exposed stuck/clipping failures

**Date:** 2026-09-24

**Real task context**

The game contained substantial traversal tests and evidence for climb, glide, movement transitions, physics, and representative ridge cases. Later play still found stuck/clipping failures involving trees, roofs, water envelopes, and assembled world geometry.

**Observed failure**

A fixture-level or representative-geometry PASS could be mistaken for a universal traversal closure. Hidden production geometry and composition dependencies were outside the prior proof envelope.

**Expected Protocol behavior**

- Treat the prior traversal PASS as bounded to the tested geometry/state/environment.
- Do not discard valid movement closures unrelated to the escaped geometry.
- Expand or invalidate only the affected closure when new geometry/dependencies become material.
- Add the newly discovered dependency/fixture/invariant so the same scope mistake cannot silently recur.

**Current v2.12.0 coverage:** **PASS**

The False Closure guard and explicit closure validity conditions correctly distinguish “prior work was worthless” from “prior proof scope was narrower than production reality.”

---

## R018 — Vegetation exclusions existed as local rules but had not graduated into one spatial invariant

**Date:** 2026-09-24

**Real task context**

The world vegetation scatter already excluded roads, dirt, standing water, river corridors, platforms, slopes, and other local conditions. Human play nevertheless found grass inside buildings.

**Observed failure**

The project knew the general class of rule — decoration needs exclusion domains — but encoded it as a growing set of local conditions. Each new environment producer or forbidden region could therefore reopen the same decision and miss a case.

**Expected Protocol behavior**

- Fix the immediate escaped case if needed.
- Ask why every vegetation producer is still allowed to decide independently where decoration is legal.
- Promote recurring local exclusions into the smallest shared spatial-placement invariant / authority that fits the architecture.
- Prefer making invalid placement unrepresentable or mechanically rejected over adding another reminder in prose.

**Current v2.12.0 coverage:** **PASS**

Workflow Hardening + closure capitalization route the repeated local rule toward a class-level mechanism without requiring infrastructure for every one-off defect.

---

## R019 — Quest backend correctness was closed, but player guidance had never been closed

**Date:** 2026-09-24

**Real task context**

The game had a rigorous quest backend with lifecycle rules, prerequisites, blockers, persistence, exactly-once rewards, contention semantics, malformed fixtures, and CI checks. Human play still reported uncertainty about task start, current objective, destination, navigation, and completion feedback.

**Observed failure**

It would be incorrect to call the player-guidance problem a regression of the quest backend. The architecture itself explicitly separated quest correctness from opportunity/adoption/presentation, and the missing player-guidance semantics had never been validated as a Product Closure.

**Expected Protocol behavior**

- Preserve the verified quest-backend closure.
- Keep Quest Correctness, Player Intent, and Guidance/Presentation as separate claims.
- Classify guidance as an OPEN product gap rather than “lost closure.”
- Build and validate only the missing product-facing delta.

**Current v2.12.0 coverage:** **PASS**

The closure model does not force every defect into “reopened solved uncertainty”; it preserves genuine OPEN gaps and prevents unnecessary backend redesign.

---

## R020 — Harness authoring bypassed the same sourcing discipline it was meant to enforce

**Date:** 2026-09-24

**Real task context**

After adding Verified Closure and managed variability, the next proposed step was to
improve a game's repository harness so coding agents would preserve baselines,
constrain variation, and stop reopening solved problems.

**Observed failure**

The upstream assistant produced a long implementation prompt telling the coding
agent to design a Closure / Baseline / Reference Harness. That handoff skipped a
prior capability-sourcing step for harness authoring itself, even though mature
agent-harness patterns, Skill authoring workflows, runtime-specific instruction
surfaces, and an existing project harness were available.

The failure was recursive: the proposed mechanism violated the very rule it was
supposed to enforce.

**User correction**

Apply the Protocol to its own interventions. Before asking a coding agent to build
a harness, inspect mature harness-authoring approaches and the current repository,
establish the closest baseline, then ask the coding agent to implement only the
remaining project-specific delta.

**Expected Protocol behavior**

- Recognize repository harness authoring as a **Capability Gap**, not an already
  selected custom implementation.
- Inspect the target repository's existing harness / instructions / tests / gates.
- Inspect credible mature harness-authoring and agent-customization mechanisms.
- Treat vendor file layouts as candidate baselines, not mandatory schemas.
- Select instruction / Skill / deterministic automation / isolated delegation
  surfaces according to scope, loading, authority, determinism, context cost, and
  runtime support.
- Only after the source/baseline decision, compile a short execution contract for
  the remaining project delta.
- Stop recursive sourcing once a sufficiently concrete authoring baseline is known;
  do not create infinite meta-process.

**Current v2.12.1 coverage:** **PASS**

v2.12.0 already said Workflow Hardening should apply Capability Sourcing before
building a new mechanism, but the meta-intervention boundary was not salient enough
in the runtime. v2.12.1 promotes the rule into the core runtime as **No Meta-Layer
Exemption** and mirrors it in the relevant skills and routing surfaces.

---

## R021 — Closure knowledge became legible but remained mechanically bypassable

**Date:** 2026-09-24

**Real task context**

A game repository added a concise Verified Closure routing page so future coding
agents could find proof owners, proof scope, Fixed Core, allowed variation,
remaining Delta, and invalidation triggers before implementation.

**Observed failure**

The routing improvement was useful, but it changed only Markdown surfaces. No
new diff guard, contract, lint, fixture, validator, or CI rule prevented an agent
from ignoring the written Fixed Core and submitting a violating change. The work
risked being treated as “Harness complete” because the rule was clear even though
the invalid state remained mechanically representable.

**User correction**

A recurring or consequential Closure should not stop at legibility when the
violation is objectively machine-checkable. Ask whether a violating change can
still silently pass. If yes, graduate the invariant into the cheapest reliable
mechanism and prove the mechanism rejects a bad case. Keep Human/Product judgment
for outcomes that are not mechanically decidable.

**Expected Protocol behavior**

- Distinguish **Epistemic Closure** from **Operational Closure**.
- Run Enforcement Graduation before declaring recurring/consequential closure operationally complete.
- Prefer invariant enforcement over freezing arbitrary implementation details.
- Use diff/path guards when path ownership itself is the invariant.
- Require a known-invalid negative control and representative valid control.
- Require a blocking mechanism to be wired into the normal execution/merge path.
- For non-mechanical judgments, define the Human/Product gate rather than a weak proxy.
- Permit explicit enforcement debt when proportional, but do not label it Operational Closure.

**Current v2.13.0 coverage:** **PASS**

v2.12.x made closure discoverable and sourceable but did not make the graduation
boundary explicit enough. v2.13.0 adds Enforcement Graduation to the canonical
runtime and hardening/validation paths.

---

# Pilot finding

This real-world retrospective set contains twenty-one distinct historical failure patterns.

- Fourteen were already represented through v2.11.1.
- Five cases (R015–R019) produced v2.12.0's Verified Closure, managed-variability, baseline-materialization, and closure-capitalization rules.
- R020 exposed a recursive sourcing failure at the harness-authoring layer and produced v2.12.1's No Meta-Layer Exemption rule.
- R021 exposed the difference between a legible rule and an enforceable mechanism and produced v2.13.0's Enforcement Graduation / Operational Closure rules.
- All twenty-one are now represented by current rules.

This is evidence that the Protocol is being revised against failures that actually occurred in practice, and that the current rules have meaningful **coverage** of this retrospective set.

It is **not** evidence that an AI reading the Protocol will reliably behave better, nor that the Protocol caused the corrected historical behavior.

The next validation step is a controlled behavioral eval:

1. freeze a set of real sanitized prompts;
2. run the same model/configuration multiple times with Protocol OFF and ON;
3. blind-score only case-relevant criteria;
4. measure routing/action errors, unsupported completion, unnecessary custom building, evidence mistakes, and operator correction burden;
5. retain failures as regression fixtures.

Do not tune the Protocol against the test set until the baseline is recorded.
