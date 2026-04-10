from __future__ import annotations

import argparse
import json
from decimal import Decimal
from pathlib import Path

from .builder import ExecutionProofBuilder
from .models import ExecutionAttempt, QuoteContext, TxContext
from .render import render_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="X Layer Execution Proof Kit CLI")
    parser.add_argument("--example", choices=["success", "failed-slip", "failed-stale"], default="success")
    parser.add_argument("--input-json")
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


def _decimal_or_none(value):
    if value in (None, ""):
        return None
    return Decimal(str(value))


def load_attempt(path: str) -> ExecutionAttempt:
    payload = json.loads(Path(path).read_text())
    quote = payload["quote"]
    tx = payload["tx"]
    return ExecutionAttempt(
        proof_id=payload["proof_id"],
        from_token=payload["from_token"],
        to_token=payload["to_token"],
        amount_in=Decimal(str(payload["amount_in"])),
        quote=QuoteContext(
            dex_name=quote["dex_name"],
            quoted_output=Decimal(str(quote["quoted_output"])),
            price_impact_percent=Decimal(str(quote["price_impact_percent"])),
            slippage_percent=Decimal(str(quote["slippage_percent"])),
        ),
        tx=TxContext(
            tx_hash=tx.get("tx_hash", ""),
            status=tx["status"],
            realized_output=_decimal_or_none(tx.get("realized_output")),
            failure_reason=tx.get("failure_reason", ""),
            approval_tx_hash=tx.get("approval_tx_hash", ""),
            settled_at=tx.get("settled_at", ""),
        ),
        pnl_delta_percent=_decimal_or_none(payload.get("pnl_delta_percent")),
        source_project=payload.get("source_project", ""),
        source_note=payload.get("source_note", ""),
    )


def main() -> None:
    args = parse_args()
    attempt = load_attempt(args.input_json) if args.input_json else example_attempt(args.example)
    proof = ExecutionProofBuilder().build(attempt)
    print(render_json(proof))


if __name__ == "__main__":
    main()
