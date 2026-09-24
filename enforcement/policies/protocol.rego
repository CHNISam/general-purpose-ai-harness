package protocol.enforcement

import rego.v1

default allow := false

allowed_proof_types := {
  "STRUCTURE_PASS",
  "VERIFICATION_PASS",
  "VALIDATION_PASS",
  "UNKNOWN",
}

evidence := object.get(input, "evidence", [])
action := object.get(input, "action", {})
capability := object.get(input, "capability", {})
closure := object.get(input, "closure", {})
completion := object.get(input, "completion", {})

has_verified_validation_evidence if {
  some item in evidence
  object.get(item, "state", "") == "VERIFIED"
  object.get(item, "kind", "") == "validation"
}

violations contains {
  "code": "E001",
  "message": "VERIFIED evidence must include provenance.",
} if {
  some item in evidence
  object.get(item, "state", "") == "VERIFIED"
  object.get(item, "provenance", "") == ""
}

violations contains {
  "code": "E002",
  "message": "Generated content cannot be promoted directly to VERIFIED evidence.",
} if {
  some item in evidence
  object.get(item, "state", "") == "VERIFIED"
  object.get(item, "source_type", "") == "generated"
}

violations contains {
  "code": "E003",
  "message": "VALIDATION_PASS requires an observed real-world validation result.",
} if {
  object.get(completion, "proof_type", "UNKNOWN") == "VALIDATION_PASS"
  object.get(completion, "validation_observed", false) == false
}

violations contains {
  "code": "E004",
  "message": "VALIDATION_PASS requires at least one VERIFIED validation evidence item.",
} if {
  object.get(completion, "proof_type", "UNKNOWN") == "VALIDATION_PASS"
  not has_verified_validation_evidence
}

violations contains {
  "code": "E005",
  "message": "Decision-relevant conflicting evidence must be resolved before completion.",
} if {
  object.get(completion, "claimed", false)
  some item in evidence
  object.get(item, "state", "") == "CONFLICTING"
  object.get(item, "decision_relevant", true)
  object.get(item, "resolved", false) == false
}

violations contains {
  "code": "E006",
  "message": "A reality-changing action requires proof to be defined before execution.",
} if {
  object.get(action, "changes_reality", false)
  object.get(action, "proof_defined", false) == false
}

violations contains {
  "code": "E007",
  "message": "When capability sourcing is required, a capability source must be selected or explicitly identified as a single obvious source.",
} if {
  object.get(capability, "sourcing_required", false)
  object.get(capability, "source_selected", "") == ""
  object.get(capability, "single_obvious_source", false) == false
}

violations contains {
  "code": "E008",
  "message": "Capability sourcing must cover at least one source class unless a single obvious source is explicitly justified.",
} if {
  object.get(capability, "sourcing_required", false)
  count(object.get(capability, "source_classes_considered", [])) == 0
  object.get(capability, "single_obvious_source", false) == false
}

violations contains {
  "code": "E009",
  "message": "Completion cannot be claimed with UNKNOWN proof.",
} if {
  object.get(completion, "claimed", false)
  object.get(completion, "proof_type", "UNKNOWN") == "UNKNOWN"
}

violations contains {
  "code": "E010",
  "message": "outcome_validated=true requires VALIDATION_PASS.",
} if {
  object.get(completion, "outcome_validated", false)
  object.get(completion, "proof_type", "UNKNOWN") != "VALIDATION_PASS"
}

violations contains {
  "code": "E011",
  "message": "proof_type is outside the Protocol proof vocabulary.",
} if {
  proof_type := object.get(completion, "proof_type", "UNKNOWN")
  not proof_type in allowed_proof_types
}

violations contains {
  "code": "E012",
  "message": "Completion cannot be claimed while required validation remains unobserved.",
} if {
  object.get(completion, "claimed", false)
  object.get(completion, "validation_required", false)
  object.get(completion, "validation_observed", false) == false
}

violations contains {
  "code": "E013",
  "message": "An explicitly valid in-scope closure cannot be reopened without a recorded justification.",
} if {
  object.get(closure, "existing_valid_closure", false)
  object.get(closure, "current_scope_covered", false)
  object.get(closure, "reopened", false)
  object.get(closure, "reopen_justified", false) == false
}

violations contains {
  "code": "E014",
  "message": "A new closure claim cannot exceed the declared proof scope.",
} if {
  object.get(closure, "claiming_new_closure", false)
  object.get(closure, "proof_scope_matches_claim", false) == false
}

violations contains {
  "code": "E015",
  "message": "Completion cannot be claimed when closure capitalization is explicitly required but not materialized.",
} if {
  object.get(completion, "claimed", false)
  object.get(closure, "capitalization_required", false)
  object.get(closure, "materialized", false) == false
}

allow if {
  count(violations) == 0
}

decision := {
  "allow": allow,
  "violation_count": count(violations),
  "violations": violations,
}
