# Live Examples

`X Layer Execution Proof Kit` now includes proof bundles built from real X Layer runtime evidence on **April 10, 2026**.

## Example 1: Agent Fight Club Live Exit

- source project: `xlayer-agent-fight-club`
- transaction hash: `0xef0f5414f56b5ebc889f95102934840c22dd96da1fb0092065dd4d76e4b5a41c`
- route: aggregated Agentic Wallet execution
- outcome class: `success`
- why it matters:
  - demonstrates packaging of a successful live fighter exit
  - shows how another agent can turn runtime evidence into a reusable proof object

Files:

- [fightclub-live-exit-attempt.json](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/examples/fightclub-live-exit-attempt.json)
- [fightclub-live-exit-proof.json](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/examples/fightclub-live-exit-proof.json)

## Example 2: FlashArb Live Probe Round

- source project: `flasharb-xlayer-arbitrage-bot`
- buy tx: `0x04fde8b044b4a6e7891e1c25b653f8d6efb6da2782dd97f764281fa53999be61`
- sell tx: `0xc805abc9a0d57d203ae3effa32e2df193776277884255f54c45dcf404506fb5b`
- route: aggregated Agentic Wallet probe execution
- outcome class: `success`
- why it matters:
  - shows proof packaging for a bounded-size live route-health round
  - demonstrates that the skill can be used even when the system is prioritizing execution continuity over profit

Files:

- [flasharb-live-probe-attempt.json](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/examples/flasharb-live-probe-attempt.json)
- [flasharb-live-probe-proof.json](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/examples/flasharb-live-probe-proof.json)

## Example 3: FlashArb Live Runtime Failure

- source project: `flasharb-xlayer-arbitrage-bot`
- observed failure: `another order processing`
- outcome class: `execution-error`
- why it matters:
  - demonstrates that the skill does not only package wins
  - captures a real wallet concurrency failure from a live autonomous system

Files:

- [flasharb-order-busy-attempt.json](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/examples/flasharb-order-busy-attempt.json)
- [flasharb-order-busy-proof.json](/Users/yanqing/Documents/GitHub/miraix-interface/projects/xlayer-execution-proof-kit/examples/flasharb-order-busy-proof.json)
