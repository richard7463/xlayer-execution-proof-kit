from decimal import Decimal

from execution_proof_kit.builder import ExecutionProofBuilder
from execution_proof_kit.models import ExecutionAttempt, QuoteContext, TxContext


def test_labels_slippage_failure_as_execution_error():
    attempt = ExecutionAttempt(
        proof_id="proof-001",
        from_token="USDC",
        to_token="OKB",
        amount_in=Decimal("25"),
        quote=QuoteContext(dex_name="Uniswap V3", quoted_output=Decimal("104.30"), price_impact_percent=Decimal("0.90"), slippage_percent=Decimal("0.50")),
        tx=TxContext(tx_hash="0xabc123", status="failed", failure_reason="slippage exceeded"),
    )
    proof = ExecutionProofBuilder().build(attempt)
    assert proof.outcome_class == "execution-error"
    assert "execution" in proof.reason.lower()
