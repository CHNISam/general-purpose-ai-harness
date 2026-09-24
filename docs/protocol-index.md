# Protocol Index

Use this file to navigate the canonical `PROTOCOL.md` without loading it wholesale.

The section numbers below are stable semantic landmarks. Search the exact heading in `PROTOCOL.md`, then read only the local section needed for the current question.

| Section | Use when |
|---|---|
| 0. PRIMARY OBJECTIVE | orienting the whole task and preventing task/feature/solution collapse |
| 1. RUNTIME KERNEL — NON-NEGOTIABLE | checking the core operating loop, Runtime Context/freshness/operator visibility, Verified Closure / managed variability, recursive sourcing / no meta-layer exemption, action boundary, capability-surface awareness, executor-bias guard, capability/implementation distinction, and evidence honesty |
| 2. DOMINANT GAP ROUTING | deciding whether the blocker is Model / Evidence / Decision / Planning / Capability / Reality / Verification-Validation |
| 3. PURPOSE | clarifying the intended real-world state and decision ownership |
| 4. MINIMUM SUFFICIENT MODELING | choosing the right model/schema for the intended use |
| 5. OPTIONAL REASONING OPERATORS | selectively using first principles, inversion, stress thinking, or another reasoning operator |
| 6. MODEL GATES | testing model quality, layer preservation, compilation integrity, proof types, and revalidation |
| 7. EVIDENCE ACQUISITION POLICY | observability, evidence states, Source of Truth, provenance, identity, coverage, and evidence quality |
| 8. CAPABILITY SOURCING / LEVERAGE GATE | inspecting available means, quality/production ceiling, and deciding whether to reuse, adopt, integrate, compose, extend, or build |
| 9. DECISION AND ACTION | comparing viable alternatives and choosing an action |
| 10. PLANNING | sequencing dependencies and coordination once the direction is known |
| 11. PROOF BEFORE ACTION | defining what evidence will show whether an action worked |
| 12. WORKFLOW HARDENING | adding repeatability, guards, automation, tests, or blocking mechanisms when justified |
| 13. PROJECT MODE | maintaining cross-layer project semantics and execution traceability |
| 14. DELEGATION / EXECUTION CONTRACT | handing work to a downstream executor without exporting the whole Protocol |
| 15. PROMPT COMPILATION | compiling upstream judgment into a task-specific prompt while preserving semantics |
| 16. HUMAN OUTPUT CONTRACT — DECISION SURFACE | minimizing operator attention, separating runtime observability from presentation, and enforcing the human-facing output contract |
| 17. OPTIONAL DEEP-DIVE FORMAT | expanding analysis only when a deeper explanation is useful |
| 18. POST-ACTION UPDATE | observing reality, updating the model, and rerouting after action |
| 19. COMPLETION CONTRACT | deciding what “done” means and avoiding false completion |
| 20. SILENT COMPLIANCE AUDIT | performing a final internal protocol audit without dumping chain-of-thought |
| 21. ANTI-PATTERNS | checking common protocol violations and failure modes |
| 22. RUNTIME CHEATSHEET | compact canonical runtime reminder |
| 23. FINAL RULE | final operating principle |
| 24. CURRENT TASK | task-local application slot in the reusable canonical prompt |

## Fast paths

### “I cannot tell whether the agent is using current Protocol/project/external state”
Read: **1.1 → 1.1.1**. Maintain Runtime Context, refresh it on state boundaries, and project a Runtime Receipt only when the operator needs that state to understand, trust, audit, or authorize the next action.

### “The answer is correct but too long or hard to scan”
Read: **16 → 20 COMMUNICATION**. Treat output conformance separately from runtime observability; compress to the Decision Surface and use a host-supported output guardrail when the presentation constraint is mechanically checkable.

### “The AI is about to build something”
Read: **1.3 → 1.4 → 8 → 11**. Confirm that capability choice was not silently determined by the executor's native tool or modality.

### “The AI keeps re-solving something the project already proved”
Read: **1.4.1 → 8.6.1 → 12 → 18 → 19**. Check whether a bounded Verified Closure already applies; preserve its Fixed Core, reopen only invalidated scope, and materialize recurring closure into a project mechanism when warranted.

### “The next step is to build a harness / Skill / validator / workflow”
Read: **1.4.2 → 8 → 12 → 14–15**. Treat the proposed mechanism as a capability in its own right: inspect the existing project/runtime harness and mature authoring sources first, select the baseline, then compile only the unresolved project delta into the downstream execution contract.

### “The data looks plausible but may be wrong”
Read: **1.5 → 7 → 6.14 → 19**.

### “Several solutions look viable”
Read: **2 Decision Gap → 8 → 9**.

### “Tests pass but I do not know whether the product actually works”
Read: **6.12 → 11 → 18 → 19**.

### “The project model is losing meaning as it becomes tasks/prompts”
Read: **6.10 → 6.11 → 6.13 → 13 → 15**.

### “The workflow keeps failing in the same way”
Read: **12**, then apply **8** before building new hardening infrastructure.

## Runtime-first rule

For ordinary tasks, do **not** start here unless the compact router or selected skill needs canonical detail.

Normal loading path remains:

```text
AGENTS.md
→ relevant .agents/skills/*/SKILL.md
→ this index when canonical navigation is needed
→ local PROTOCOL.md section only
```
