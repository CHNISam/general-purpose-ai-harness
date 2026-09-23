package protocol.enforcement_test

import rego.v1
import data.protocol.enforcement

valid_input := {
  "task_id": "T-valid",
  "action": {
    "changes_reality": true,
    "proof_defined": true,
  },
  "capability": {
    "sourcing_required": true,
    "single_obvious_source": false,
    "source_selected": "existing-library",
    "source_classes_considered": ["internal", "library"],
  },
  "evidence": [{
    "id": "EV-1",
    "state": "VERIFIED",
    "kind": "validation",
    "source_type": "observed",
    "provenance": "real-user-observation",
    "decision_relevant": true,
    "resolved": true,
  }],
  "completion": {
    "claimed": true,
    "proof_type": "VALIDATION_PASS",
    "validation_required": true,
    "validation_observed": true,
    "outcome_validated": true,
  },
}

test_valid_input_allows if {
  result := enforcement.decision with input as valid_input
  result.allow
  result.violation_count == 0
}

test_verified_without_provenance_is_blocked if {
  bad := object.union(valid_input, {
    "evidence": [{
      "id": "EV-1",
      "state": "VERIFIED",
      "kind": "validation",
      "source_type": "observed",
      "decision_relevant": true,
      "resolved": true,
    }],
  })
  result := enforcement.decision with input as bad
  not result.allow
  some violation in result.violations
  violation.code == "E001"
}

test_validation_without_observation_is_blocked if {
  bad := object.union(valid_input, {
    "completion": {
      "claimed": true,
      "proof_type": "VALIDATION_PASS",
      "validation_required": true,
      "validation_observed": false,
      "outcome_validated": true,
    },
  })
  result := enforcement.decision with input as bad
  not result.allow
  some violation in result.violations
  violation.code == "E003"
}

test_reality_change_without_defined_proof_is_blocked if {
  bad := object.union(valid_input, {
    "action": {
      "changes_reality": true,
      "proof_defined": false,
    },
  })
  result := enforcement.decision with input as bad
  not result.allow
  some violation in result.violations
  violation.code == "E006"
}

test_unsourced_capability_is_blocked if {
  bad := object.union(valid_input, {
    "capability": {
      "sourcing_required": true,
      "single_obvious_source": false,
      "source_selected": "",
      "source_classes_considered": [],
    },
  })
  result := enforcement.decision with input as bad
  not result.allow
  some violation in result.violations
  violation.code == "E007"
}

test_unresolved_conflict_blocks_completion if {
  bad := object.union(valid_input, {
    "evidence": [{
      "id": "EV-X",
      "state": "CONFLICTING",
      "kind": "validation",
      "source_type": "external",
      "provenance": "two-credible-sources-disagree",
      "decision_relevant": true,
      "resolved": false,
    }],
  })
  result := enforcement.decision with input as bad
  not result.allow
  some violation in result.violations
  violation.code == "E005"
}
