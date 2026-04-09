from __future__ import annotations

import argparse
from decimal import Decimal

from .builder import ExecutionProofBuilder
from .models import ExecutionAttempt, QuoteContext, TxContext
from .render import render_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="X Layer Execution Proof Kit CLI")
    parser.add_argument("--example", choices=["success", "failed-slip", "failed-stale"], default="success")
    return parser.parse_args()


def example_attempt(name: str) -> ExecutionAttempt:
    if name == "failed-slip":
        return ExecutionAttempt(
            proof_id="proof-001",
            from_token="USDC",
            to_token="OKB",
            amount_in=Decimal("25"),
            quote=QuoteContext(dex_name="Uniswap V3", quoted_output=Decimal("104.30"), price_impact_percent=Decimal("0.90"), slippage_percent=Decimal("0.50")),
            tx=TxContext(tx_hash="0xabc123", status="failed", failure_reason="slippage exceeded"),
        )
    if name == "failed-stale":
        return ExecutionAttempt(
            proof_id="proof-002",
            from_token="USDC",
            to_token="OKB",
            amount_in=Decimal("25"),
            quote=QuoteContext(dex_name="Oku", quoted_output=Decimal("103.80"), price_impact_percent=Decimal("0.35"), slippage_percent=Decimal("0.50")),
            tx=TxContext(tx_hash="0xdef456", status="failed", failure_reason="quote expired before submission"),
        )
    return ExecutionAttempt(
        proof_id="proof-003",
        from_token="USDC",
        to_token="OKB",
        amount_in=Decimal("25"),
        quote=QuoteContext(dex_name="Uniswap V3", quoted_output=Decimal("104.30"), price_impact_percent=Decimal("0.40"), slippage_percent=Decimal("0.50")),
        tx=TxContext(tx_hash="0xghi789", status="success", realized_output=Decimal("104.12")),
        pnl_delta_percent=Decimal("0.60"),
    )


def main() -> None:
    args = parse_args()
    proof = ExecutionProofBuilder().build(example_attempt(args.example))
    print(render_json(proof))


if __name__ == "__main__":
    main()
