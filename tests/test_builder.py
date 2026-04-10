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


def test_labels_successful_loss_as_thesis_error():
    attempt = ExecutionAttempt(
        proof_id="proof-002",
        from_token="USD₮0",
        to_token="OKB",
        amount_in=Decimal("0.1"),
        quote=QuoteContext(dex_name="aggregator", quoted_output=Decimal("0.00119"), price_impact_percent=Decimal("0.00"), slippage_percent=Decimal("0.50")),
        tx=TxContext(tx_hash="0xf00", status="success", realized_output=Decimal("0.00118")),
        pnl_delta_percent=Decimal("-1.20"),
    )
    proof = ExecutionProofBuilder().build(attempt)
    assert proof.outcome_class == "thesis-error"
    assert "thesis" in proof.reason.lower()


def test_labels_concurrency_failure_as_execution_error():
    attempt = ExecutionAttempt(
        proof_id="proof-003",
        from_token="USD₮0",
        to_token="OKB",
        amount_in=Decimal("0.1"),
        quote=QuoteContext(dex_name="aggregator", quoted_output=Decimal("0.00119"), price_impact_percent=Decimal("0.00"), slippage_percent=Decimal("0.50")),
        tx=TxContext(tx_hash="", status="failed", failure_reason="Pay send-uop failed: another order processing"),
    )
    proof = ExecutionProofBuilder().build(attempt)
    assert proof.outcome_class == "execution-error"
    assert "wallet" in proof.reason.lower() or "order" in proof.reason.lower()
