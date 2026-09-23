#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "benchmarks" / "cases" / "retrospective-v1.json"

def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--mode", choices=["repo","portable"], default="repo")
    ap.add_argument("--out", default="benchmarks/work")
    args = ap.parse_args()

    data = json.loads(CASES.read_text(encoding="utf-8"))
    case = next((x for x in data["cases"] if x["id"] == args.case), None)
    if not case:
        raise SystemExit(f"unknown case: {args.case}")

    out = ROOT / args.out / case["id"]
    out.mkdir(parents=True, exist_ok=True)

    task = case["prompt"].strip()
    off = f"""# Benchmark task — {case['id']} — Protocol OFF

Use only the task/context below. Do not use the General-Purpose AI Operating Protocol repository, its AGENTS.md, skills, evals, or protocol-derived hints.

## Task

{task}

Respond as you normally would for this task.
"""

    if args.mode == "repo":
        on_preamble = """Before answering, use the current public General-Purpose AI Operating Protocol repository as intended:
1. read AGENTS.md;
2. route using its own rules;
3. load only the minimum relevant skill(s);
4. do not read evals/ or benchmarks/;
5. read canonical PROTOCOL.md only if the runtime router/skill actually requires it.

Repository:
https://github.com/CHNISam/general-purpose-ai-operating-protocol
"""
    else:
        on_preamble = """Before answering, use the attached/generated Portable Protocol Runtime Bundle:
1. apply AGENTS.md;
2. route using its own rules;
3. load/apply only the minimum relevant skill(s) from the bundle;
4. do not use benchmark criteria or expected answers.

Generate the bundle from the same repository commit with:
python benchmarks/export_runtime_bundle.py > protocol-runtime-bundle.md
"""

    on = f"""# Benchmark task — {case['id']} — Protocol ON

{on_preamble}
## Task

{task}
"""

    (out / "OFF_PROMPT.md").write_text(off, encoding="utf-8")
    (out / "ON_PROMPT.md").write_text(on, encoding="utf-8")
    meta = {
        "case_id": case["id"],
        "title": case["title"],
        "source_fidelity": case["source_fidelity"],
        "off_prompt_sha256": sha(off),
        "on_prompt_sha256": sha(on),
        "protocol_commit": None,
        "mode": args.mode,
    }
    (out / "PAIR_METADATA.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
