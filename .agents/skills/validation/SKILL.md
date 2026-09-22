---
name: validation
description: Define proof, verify implementation, validate real-world outcomes, inspect post-action evidence, and decide whether work is actually complete. Use before consequential action to define success evidence and after changes when correctness/usefulness is not yet demonstrated. Do not equate a successful command, installed library, generated artifact, or stopped agent with a validated outcome.
---

# Validation

Use for a **Verification / Validation Gap** and for proof before important action.

## Define proof before action

Ask:

- What observation would prove the Reality Gap closed?
- What would materially reduce the Evidence Gap?
- What would show an acquired capability is sufficient?
- What result would show the action failed?
- What would contradict the working model?
- Do we need Verification, Validation, or both?

### Verification

**Did we implement / integrate / configure / produce what the specified model requires?**

### Validation

**Does the resulting real system actually satisfy the intended purpose or need?**

### Proof type

Where the distinction can change interpretation or completion, label the strongest
proof actually supported:

- **STRUCTURE PASS** — the model is internally coherent for the current purpose.
- **VERIFICATION PASS** — the implementation/integration/artifact satisfies the specified model or contract.
- **VALIDATION PASS** — the resulting real system satisfies the intended purpose, need, or outcome.
- **UNKNOWN / UNTESTED** — sufficient evidence does not yet exist.

Do not promote a lower proof type into a higher one merely because the lower-level
test passed.

Prefer evidence from the real Source of Truth.

Do not confuse:

- Action completed → Outcome proven
- Library installed → Capability validated
- Tool returned success → Real state is correct

## Post-action update

Compare Intended State vs Observed State.

If a decision-relevant upstream requirement, model, source, dependency, or
assumption changed, impact-analyze which prior verification/validation results
depend on it. Mark only the affected scope as requiring revalidation; do not
silently rely on its prior PASS and do not invalidate unrelated evidence.

Compare Intended State vs Observed State.

Classify the result:

1. action succeeded and the relevant model remains supported;
2. Reality Gap remains;
3. acquired capability proved insufficient;
4. capability source decision must be revisited;
5. evidence contradicts the model;
6. new Model Gap appeared;
7. new Evidence Gap appeared;
8. action was ineffective;
9. Goal / Boundary / Assumption needs revision.

When evidence conflicts with the model, correct the model rather than defend the plan.

When an adopted capability fails, reopen the Capability Gap rather than patching indefinitely by default.

## Completion contract

Do not declare completion merely because code was written, a dependency installed, a service connected, a document produced, a command succeeded, a migration ran, an agent stopped, a plan exists, or a tool returned success.

Before completion determine:

- What changed?
- What evidence supports it?
- Is the required capability actually available?
- Was the intended result verified?
- Was the intended outcome validated where necessary?
- What materially relevant uncertainty remains?
- Did new evidence invalidate a prior assumption?

Then finish or reroute.
