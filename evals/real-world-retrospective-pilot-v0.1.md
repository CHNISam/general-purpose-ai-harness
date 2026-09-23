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

**Current v2.9 coverage:** **PARTIAL**

v2.9 clearly requires intended-use model selection, layer preservation, and bidirectional traceability. However, it does not yet state a strong **staged-audit rule**: when the purpose is to validate an existing top-down chain, do not reason ahead into downstream layers before the current upstream boundary is accepted.

This case is a candidate Protocol improvement, but should be tested on more than one real task before adding a new general rule.

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

# Pilot finding

This first real-world retrospective set contains twelve distinct historical failure patterns.

- Eleven are **clearly represented** in the current v2.9 rules.
- One is **partially represented**: staged top-down auditing of an existing semantic chain.

This is evidence that the current Protocol has meaningful **coverage** of failures that actually occurred in practice.

It is **not** evidence that an AI reading the Protocol will reliably behave better, nor that the Protocol caused the corrected historical behavior.

The next validation step is a controlled behavioral eval:

1. freeze a set of real sanitized prompts;
2. run the same model/configuration multiple times with Protocol OFF and ON;
3. blind-score only case-relevant criteria;
4. measure routing/action errors, unsupported completion, unnecessary custom building, evidence mistakes, and operator correction burden;
5. retain failures as regression fixtures.

Do not tune the Protocol against the test set until the baseline is recorded.
