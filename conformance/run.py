#!/usr/bin/env python3
"""Run the public Protocol conformance fixtures against OPA."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "enforcement" / "policies" / "protocol.rego"
MANIFEST = ROOT / "conformance" / "cases" / "manifest.json"


def run_case(opa: str, fixture: Path) -> dict:
    proc = subprocess.run(
        [
            opa,
            "eval",
            "--format=json",
            "--data",
            str(POLICY),
            "--input",
            str(fixture),
            "data.protocol.enforcement.decision",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"OPA failed for {fixture}:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
        )
    payload = json.loads(proc.stdout)
    try:
        return payload["result"][0]["expressions"][0]["value"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected OPA result for {fixture}: {payload}") from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--opa", default="opa", help="OPA executable path")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures: list[str] = []

    for case in manifest["cases"]:
        fixture = ROOT / case["fixture"]
        decision = run_case(args.opa, fixture)
        actual_codes = {item["code"] for item in decision.get("violations", [])}

        if decision.get("allow") is not case["expect_allow"]:
            failures.append(
                f"{case['id']}: expected allow={case['expect_allow']}, "
                f"got {decision.get('allow')}"
            )

        for code in case.get("expect_codes", []):
            if code not in actual_codes:
                failures.append(
                    f"{case['id']}: expected violation {code}, got {sorted(actual_codes)}"
                )

        forbidden = set(case.get("forbid_codes", []))
        unexpected = actual_codes & forbidden
        if unexpected:
            failures.append(
                f"{case['id']}: forbidden violations present: {sorted(unexpected)}"
            )

        status = "PASS" if not any(f.startswith(case["id"] + ":") for f in failures) else "FAIL"
        print(
            f"{status:4} {case['id']}: allow={decision.get('allow')} "
            f"violations={sorted(actual_codes)}"
        )

    if failures:
        print("\nConformance failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nAll {len(manifest['cases'])} conformance cases passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
