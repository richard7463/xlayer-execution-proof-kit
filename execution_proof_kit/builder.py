from __future__ import annotations

from decimal import Decimal

from .models import ExecutionAttempt, ExecutionProof


class ExecutionProofBuilder:
    def build(self, attempt: ExecutionAttempt) -> ExecutionProof:
        outcome_class, reason = self._classify(attempt)
        summary = self._summary(attempt, outcome_class, reason)
        return ExecutionProof(
            proof_id=attempt.proof_id,
            outcome_class=outcome_class,
            tx_hash=attempt.tx.tx_hash,
            reason=reason,
            moltbook_summary=summary,
        )

    def _classify(self, attempt: ExecutionAttempt) -> tuple[str, str]:
        if attempt.tx.status == "success":
            return "success", "Execution completed and the route delivered a settled transaction result."
        if "slippage" in attempt.tx.failure_reason.lower() or attempt.quote.price_impact_percent > attempt.quote.slippage_percent:
            return "execution-error", "Quoted route was acceptable, but execution quality failed against the declared tolerance."
        if attempt.pnl_delta_percent is not None and attempt.pnl_delta_percent < Decimal("-2.0"):
            return "thesis-error", "Execution succeeded, but the market thesis was wrong after settlement."
        if "expired" in attempt.tx.failure_reason.lower() or "stale" in attempt.tx.failure_reason.lower():
            return "timing-error", "The idea arrived too late and the transaction context degraded before execution."
        return "execution-error", "The trade failed for execution-path reasons rather than a clean thesis failure."

    @staticmethod
    def _summary(attempt: ExecutionAttempt, outcome_class: str, reason: str) -> str:
        return (
            f"Proof {attempt.proof_id}: {outcome_class}. "
            f"Route {attempt.quote.dex_name} was selected for {attempt.from_token}->{attempt.to_token}. "
            f"{reason}"
        )
