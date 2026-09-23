#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--treatment", choices=["OFF","ON"], required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--runtime", required=True)
    ap.add_argument("--output-file", required=True)
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--model-version", default="")
    ap.add_argument("--effort", default="")
    ap.add_argument("--run-id", default="")
    ap.add_argument("--protocol-commit", default="")
    ap.add_argument("--notes", default="")
    ap.add_argument("--out", default="benchmarks/results/raw")
    args = ap.parse_args()

    output = Path(args.output_file).read_text(encoding="utf-8")
    prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    record = {
        "schema_version": 1,
        "case_id": args.case,
        "treatment": args.treatment,
        "model": args.model,
        "runtime": args.runtime,
        "model_version": args.model_version,
        "effort": args.effort,
        "run_id": args.run_id,
        "prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "protocol_commit": args.protocol_commit or None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "output": output,
        "notes": args.notes,
    }
    out = ROOT / args.out
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"{args.case}-{args.treatment}.json"
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
