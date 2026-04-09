---
name: xlayer-execution-proof-kit
description: Use this skill when an agent needs to turn a quote, route, transaction attempt, and result into a standardized proof object with outcome attribution.
---

# X Layer Execution Proof Kit

Use this skill to standardize execution evidence for X Layer agents.

## When to use it

- The caller wants a proof bundle after a swap attempt.
- Another agent needs a reusable evidence format.
- The caller wants to classify a failed trade as thesis, timing, or execution error.
- The caller wants a Moltbook-ready execution summary.

## Required capabilities

Use factual execution inputs only:

- quote and route data from OnchainOS or Uniswap-linked execution flow
- transaction hash or explicit failure state
- realized result or failure reason

Do not invent transaction outcomes or attribution.

## Workflow

1. Extract the swap intent.
2. Record the selected route and quote context.
3. Record the transaction result or failure.
4. Classify the outcome.
5. Return a proof object plus a public summary.

## Fixed output

Always return these sections in order:

1. `Intent`
2. `Route context`
3. `Transaction evidence`
4. `Outcome attribution`
5. `Proof bundle`
6. `Agent-ready summary`
