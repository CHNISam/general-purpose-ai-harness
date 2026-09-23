#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    parts = [
        "# Portable Protocol Runtime Bundle",
        "",
        "Generated from the current checkout. Do not edit this generated bundle as a source of truth.",
        "",
        "## AGENTS.md",
        "",
        (ROOT / "AGENTS.md").read_text(encoding="utf-8"),
    ]
    skills = sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    for path in skills:
        parts += ["", f"## {path.relative_to(ROOT)}", "", path.read_text(encoding="utf-8")]
    print("\n".join(parts))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
