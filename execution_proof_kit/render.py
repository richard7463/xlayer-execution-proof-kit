from __future__ import annotations

import json
from dataclasses import asdict

from .models import ExecutionProof


def render_json(proof: ExecutionProof) -> str:
    return json.dumps(asdict(proof), indent=2, default=str)


def render_moltbook_summary(proof: ExecutionProof) -> str:
    return proof.moltbook_summary
