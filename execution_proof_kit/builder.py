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
        failure_reason = attempt.tx.failure_reason.lower()
        if attempt.tx.status == "success":
            if attempt.pnl_delta_percent is not None and attempt.pnl_delta_percent <= Decimal("-0.50"):
                return "thesis-error", "Execution settled onchain, but the post-trade outcome invalidated the thesis."
            return "success", "Execution completed and the route delivered a settled transaction result."
        if "expired" in failure_reason or "stale" in failure_reason:
            return "timing-error", "The idea arrived too late and the transaction context degraded before execution."
        if "another order processing" in failure_reason or "send-uop" in failure_reason:
            return "execution-error", "Execution path was blocked by wallet or order concurrency before a clean fill could settle."
        if "slippage" in failure_reason or attempt.quote.price_impact_percent > attempt.quote.slippage_percent:
            return "execution-error", "Quoted route was acceptable, but execution quality failed against the declared tolerance."
        return "execution-error", "The trade failed for execution-path reasons rather than a clean thesis failure."

    @staticmethod
    def _summary(attempt: ExecutionAttempt, outcome_class: str, reason: str) -> str:
        source = f" Source: {attempt.source_project}." if attempt.source_project else ""
        return (
            f"Proof {attempt.proof_id}: {outcome_class}. "
            f"Route {attempt.quote.dex_name} was selected for {attempt.from_token}->{attempt.to_token}. "
            f"{reason}{source}"
        )
