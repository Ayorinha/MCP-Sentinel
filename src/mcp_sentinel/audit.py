from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Mapping

@dataclass(frozen=True)
class AuthorizationDecision:
    tool: str
    allowed: bool
    reason: str
    timestamp: datetime

def decide(policy, call) -> AuthorizationDecision:
    allowed = policy.authorize(call)
    reason = "explicit-rule" if allowed else "default-deny"
    return AuthorizationDecision(call.name, allowed, reason, datetime.now(timezone.utc))
