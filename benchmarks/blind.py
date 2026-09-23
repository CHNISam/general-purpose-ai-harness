#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "benchmarks/cases/retrospective-v1.json").read_text(encoding="utf-8"))

def order(case_id: str, seed: str) -> list[str]:
    h = hashlib.sha256(f"{seed}:{case_id}".encode()).digest()[0]
    return ["OFF","ON"] if h % 2 == 0 else ["ON","OFF"]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="benchmarks/results/raw")
    ap.add_argument("--out", default="benchmarks/results/blind")
    ap.add_argument("--seed", required=True, help="Keep this value private until scoring is frozen.")
    args = ap.parse_args()

    raw = ROOT / args.raw
    out = ROOT / args.out
    out.mkdir(parents=True, exist_ok=True)
    mapping = {"schema_version":1,"pairs":{}}

    for case in CASES["cases"]:
        paths = {t: raw / f"{case['id']}-{t}.json" for t in ("OFF","ON")}
        if not all(p.exists() for p in paths.values()):
            continue
        rec = {t: json.loads(paths[t].read_text(encoding="utf-8")) for t in paths}
        if (rec["OFF"]["model"], rec["OFF"]["runtime"], rec["OFF"].get("model_version"), rec["OFF"].get("effort")) != (
            rec["ON"]["model"], rec["ON"]["runtime"], rec["ON"].get("model_version"), rec["ON"].get("effort")
        ):
            raise SystemExit(f"{case['id']}: OFF/ON model/runtime/version/effort mismatch")

        ord_ = order(case["id"], args.seed)
        labels = {"A":ord_[0],"B":ord_[1]}
        payload = {
            "schema_version":1,
            "case_id":case["id"],
            "title":case["title"],
            "criteria":case["criteria"],
            "model":rec["OFF"]["model"],
            "runtime":rec["OFF"]["runtime"],
            "model_version":rec["OFF"].get("model_version",""),
            "effort":rec["OFF"].get("effort",""),
            "A":rec[labels["A"]]["output"],
            "B":rec[labels["B"]]["output"],
        }
        (out / f"{case['id']}.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        mapping["pairs"][case["id"]] = labels

    (out / "_PRIVATE_MAPPING.json").write_text(json.dumps(mapping,indent=2)+"\n",encoding="utf-8")
    print(f"Prepared {len(mapping['pairs'])} blind pairs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
