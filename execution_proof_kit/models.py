from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass(frozen=True)
class QuoteContext:
    dex_name: str
    quoted_output: Decimal
    price_impact_percent: Decimal
    slippage_percent: Decimal


@dataclass(frozen=True)
class TxContext:
    tx_hash: str
    status: str
    realized_output: Optional[Decimal] = None
    failure_reason: str = ""
    approval_tx_hash: str = ""
    settled_at: str = ""


@dataclass(frozen=True)
class ExecutionAttempt:
    proof_id: str
    from_token: str
    to_token: str
    amount_in: Decimal
    quote: QuoteContext
    tx: TxContext
    pnl_delta_percent: Optional[Decimal] = None
    source_project: str = ""
    source_note: str = ""


@dataclass(frozen=True)
class ExecutionProof:
    proof_id: str
    outcome_class: str
    tx_hash: str
    reason: str
    moltbook_summary: str
