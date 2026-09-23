# Behavioral Benchmark and External Replication Kit

This directory turns the retrospective failure set into a reproducible Protocol OFF vs ON experiment.

It is intentionally **provider-neutral**. You can use it with:

- ChatGPT web/app;
- Claude web/app;
- Gemini web/app;
- other domestic or international chat systems;
- coding-agent CLIs;
- API-based model runners;
- any system where you can capture the final output as text.

No API key is required for the **manual web replication** path.

## Evidence boundary

The 12 pilot cases are sanitized historical reconstructions.

Each case declares `source_fidelity`:

- `verbatim` — exact original task wording is preserved;
- `near-verbatim` — wording is close to recoverable historical wording;
- `reconstructed` — failure structure is historical but prompt wording is reconstructed;
- `synthetic` — deliberately constructed, not historical.

Do not silently upgrade reconstructed prompts to verbatim history.

## Fastest external replication: web/app models

Pick one model/runtime and keep it constant within each pair.

### 1. Prepare a pair

```bash
python benchmarks/prepare_pair.py --case R001 --mode repo
```

This writes:

- `OFF_PROMPT.md`
- `ON_PROMPT.md`
- `PAIR_METADATA.json`

Use `--mode portable` if the model cannot reliably read the public GitHub repository. Generate the portable runtime bundle from the same commit:

```bash
python benchmarks/export_runtime_bundle.py > protocol-runtime-bundle.md
```

### 2. Open two fresh sessions

**OFF session**

- paste only `OFF_PROMPT.md`;
- do not mention the Protocol.

**ON session**

- paste `ON_PROMPT.md`;
- in repo mode, let the model read the repository itself;
- in portable mode, attach/paste the generated runtime bundle.

Keep model, model version, effort/reasoning setting, tool access, and task context the same.

Do not put the benchmark criteria or expected answer into either session.

### 3. Capture raw outputs

Save each final output as a text file, then:

```bash
python benchmarks/capture_result.py \
  --case R001 --treatment OFF \
  --model "MODEL" --runtime "WEB" \
  --prompt-file benchmarks/work/R001/OFF_PROMPT.md \
  --output-file /path/to/off-output.txt

python benchmarks/capture_result.py \
  --case R001 --treatment ON \
  --model "MODEL" --runtime "WEB" \
  --protocol-commit "$(git rev-parse HEAD)" \
  --prompt-file benchmarks/work/R001/ON_PROMPT.md \
  --output-file /path/to/on-output.txt
```

### 4. Blind the pair

Keep the seed private from the judge until scoring is frozen.

```bash
python benchmarks/blind.py --seed "private-random-seed"
```

The judge sees **A/B**, not OFF/ON.

### 5. Create and complete score sheets

```bash
python benchmarks/create_score_sheet.py \
  --blind-case benchmarks/results/blind/R001.json \
  --judge-id judge-1
```

Replace `UNKNOWN` only after reviewing both outputs against the case-specific criteria.

Allowed states:

- `PASS`
- `PARTIAL`
- `FAIL`
- `UNKNOWN`

Do not reward Protocol vocabulary by itself. Score decisions and behavior.

### 6. Aggregate after scoring is frozen

```bash
python benchmarks/aggregate.py
```

The aggregator deliberately does **not** generate one vanity score. It reports per-treatment criterion states and paired case direction.

## What counts as a useful replication

Record at minimum:

- model/runtime;
- model version if exposed;
- reasoning/effort setting;
- tool access;
- Protocol commit;
- raw OFF and ON outputs;
- blind score sheet;
- any operator correction required;
- latency/token/cost metadata when available.

A single replication is evidence about that specific setup, not proof of universal effectiveness.

## Pilot rule

Do not modify the Protocol based on the OFF result and then count the same ON run as an unbiased controlled result.

Freeze case, Protocol commit, scoring criteria, and runtime configuration before the pair is run.

## Files

- `cases/retrospective-v1.json` — 12 frozen pilot cases and criteria.
- `schemas/` — machine-readable case/result/score contracts.
- `prepare_pair.py` — prepares OFF/ON prompts.
- `export_runtime_bundle.py` — generates a portable runtime bundle from the current checkout.
- `capture_result.py` — normalizes web/API/CLI outputs.
- `blind.py` — removes treatment labels for judging.
- `create_score_sheet.py` — creates criterion-specific blind score forms.
- `aggregate.py` — summarizes frozen judgments without collapsing them into a single score.
- `validate.py` — fixture integrity checks.
