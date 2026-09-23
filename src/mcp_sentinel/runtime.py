"""Deterministic end-to-end authorization pipeline."""

from dataclasses import dataclass
from datetime import datetime, timezone

from .audit import decide
from .guard import guard
from .policy import Policy, ToolCall
from .security_contracts import ToolRequest


@dataclass(frozen=True)
class PipelineResult:
    tool: str
    allowed: bool
    reason: str
    timestamp: datetime


def authorize(policy: Policy, request: ToolRequest) -> PipelineResult:
    """Validate, guard, authorize, and return one auditable decision."""
    passed, guard_reason = guard(request)
    now = datetime.now(timezone.utc)
    if not passed:
        return PipelineResult(request.tool, False, guard_reason, now)

    decision = decide(policy, ToolCall(name=request.tool, arguments={}))
    return PipelineResult(decision.tool, decision.allowed, decision.reason, decision.timestamp)
