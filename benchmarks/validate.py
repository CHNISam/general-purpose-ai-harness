#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CASES=ROOT/"benchmarks/cases/retrospective-v1.json"

def fail(msg:str)->None:
    raise SystemExit(msg)

def main()->int:
    data=json.loads(CASES.read_text(encoding="utf-8"))
    if data.get("version")!=1: fail("cases.version must be 1")
    ids=set()
    for c in data.get("cases",[]):
        required={"id","title","source_date","source_fidelity","prompt","criteria"}
        if not required <= set(c): fail(f"{c.get('id','?')}: missing fields")
        if c["id"] in ids: fail(f"duplicate case id {c['id']}")
        ids.add(c["id"])
        if c["source_fidelity"] not in {"verbatim","near-verbatim","reconstructed","synthetic"}: fail(f"{c['id']}: bad source_fidelity")
        crit_ids=[x["id"] for x in c["criteria"]]
        if len(crit_ids)!=len(set(crit_ids)): fail(f"{c['id']}: duplicate criterion")
        if not c["prompt"].strip(): fail(f"{c['id']}: empty prompt")
    if len(ids)!=12: fail(f"expected 12 pilot cases, got {len(ids)}")
    print(f"PASS: {len(ids)} benchmark cases are structurally valid.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
