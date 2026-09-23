#!/usr/bin/env python3
from __future__ import annotations
import argparse, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ORDER={"FAIL":0,"PARTIAL":1,"PASS":2}

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--mapping",default="benchmarks/results/blind/_PRIVATE_MAPPING.json")
    ap.add_argument("--scores",default="benchmarks/results/scores")
    ap.add_argument("--out",default="benchmarks/results/summary.json")
    args=ap.parse_args()
    mapping=json.loads((ROOT/args.mapping).read_text(encoding="utf-8"))["pairs"]
    score_dir=ROOT/args.scores
    counters={t:collections.Counter() for t in ("OFF","ON")}
    paired=collections.Counter()
    judged=0
    for path in sorted(score_dir.glob("*.json")):
        s=json.loads(path.read_text(encoding="utf-8"))
        cid=s["case_id"]
        if cid not in mapping: continue
        labels=mapping[cid]
        for label in ("A","B"):
            treatment=labels[label]
            for crit,state in s["scores"][label].items():
                counters[treatment][state]+=1
        comparable=[]
        for crit in set(s["scores"]["A"]) & set(s["scores"]["B"]):
            a=s["scores"]["A"][crit]; b=s["scores"]["B"][crit]
            if a in ORDER and b in ORDER:
                ta,tb=labels["A"],labels["B"]
                off=a if ta=="OFF" else b
                on=a if ta=="ON" else b
                comparable.append((ORDER[on],ORDER[off]))
        if comparable:
            on_sum=sum(x for x,_ in comparable); off_sum=sum(y for _,y in comparable)
            paired["ON_better" if on_sum>off_sum else "OFF_better" if off_sum>on_sum else "tie"] += 1
        judged+=1
    summary={
      "schema_version":1,
      "judged_score_files":judged,
      "criterion_state_counts":{k:dict(v) for k,v in counters.items()},
      "paired_case_direction":dict(paired),
      "warning":"No single vanity score is produced. Interpret per-criterion state counts and paired directions with model/runtime/sample-size context."
    }
    out=ROOT/args.out
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
