# X Layer Execution Proof Kit

Reusable proof-packaging skill for X Layer agents.

`X Layer Execution Proof Kit` is built for the **OKX Build X Hackathon Skills Arena**.
It helps any agent turn a quote, route choice, transaction result, and outcome analysis into a standardized execution proof object.

## One-Line Pitch

Give any agent a trade attempt and Execution Proof Kit returns a clean proof bundle with route evidence, tx evidence, outcome attribution, and a Moltbook-ready summary.

## Why This Fits Skills Arena

This project is a reusable capability, not a full app.

Its job is narrow and valuable:

- normalize execution evidence
- explain why a trade succeeded or failed
- distinguish thesis error from execution error
- give any agent a proof object it can publish or store

## Project Intro

Most agents can say they traded. Fewer agents can prove what happened in a reusable format.

Execution Proof Kit exists to standardize:

- what was intended
- what route was selected
- what transaction was sent
- what result happened
- what kind of error or win this actually was

## Architecture Overview

There are four layers:

1. `execution_proof_kit.models`
   - typed structures for quote context, tx context, and proof output

2. `execution_proof_kit.builder.ExecutionProofBuilder`
   - turns raw execution inputs into a proof bundle
   - assigns outcome attribution labels

3. `execution_proof_kit.render`
   - renders JSON and Moltbook-ready text summaries

4. `execution_proof_kit.cli`
   - local CLI for demos and reproducible examples

## Onchain OS / Uniswap Skill Usage

The proof model is designed to sit behind:

- OnchainOS route and quote retrieval
- OnchainOS wallet and tx execution
- optional Uniswap route selection

It does not replace execution. It standardizes evidence after or around execution.

## Working Mechanics

1. An agent provides an execution attempt.
2. Execution Proof Kit records the swap intent.
3. It records the selected route and transaction evidence.
4. It records the final outcome.
5. It assigns one outcome class:
   - `success`
   - `thesis-error`
   - `timing-error`
   - `execution-error`
6. It emits a proof bundle and a public summary.

## Example Output

```json
{
  "proof_id": "proof-001",
  "outcome_class": "execution-error",
  "tx_hash": "0xabc123",
  "reason": "Quoted route was acceptable, but final execution slipped beyond the declared tolerance.",
  "moltbook_summary": "Execution failed for route-quality reasons. The thesis was acceptable; the fill path was not."
}
```

## Local Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m execution_proof_kit.cli --example failed-slip
```

## Submission Positioning

This repo belongs in the **Skills Arena**.

Why:

- it is a reusable evidence layer
- any trading or treasury agent can attach it to execution
- it improves transparency and comparability across agents

## Team

- `richard7463` - solo builder

## Status

Already done:

- standalone repo structure
- reusable skill spec
- proof-bundle builder
- CLI demo surface
- Skills Arena docs

Still required:

- live transaction examples from OnchainOS execution
- Moltbook submission post
- demo video

## Docs

- [Skill Spec](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/SKILL.md)
- [Project Positioning](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/docs/project-positioning.md)
- [Skills Arena Checklist](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/docs/skills-arena-checklist.md)
