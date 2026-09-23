#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--blind-case", required=True)
    ap.add_argument("--judge-id", required=True)
    ap.add_argument("--out", default="benchmarks/results/scores")
    args = ap.parse_args()
    case = json.loads(Path(args.blind_case).read_text(encoding="utf-8"))
    scores = {
      "schema_version":1,
      "case_id":case["case_id"],
      "judge_id":args.judge_id,
      "scores":{
        "A":{x["id"]:"UNKNOWN" for x in case["criteria"]},
        "B":{x["id"]:"UNKNOWN" for x in case["criteria"]}
      },
      "notes":"Replace UNKNOWN with PASS/PARTIAL/FAIL only after reviewing outputs blind."
    }
    out=ROOT/args.out
    out.mkdir(parents=True,exist_ok=True)
    path=out/f"{case['case_id']}-{args.judge_id}.json"
    path.write_text(json.dumps(scores,indent=2)+"\n",encoding="utf-8")
    print(path)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
