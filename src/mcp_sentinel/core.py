from __future__ import annotations
from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any
@dataclass(frozen=True, slots=True)
class ToolPolicy:
    allowed_tools: frozenset[str] = frozenset(); max_arguments: int = 32
    def __post_init__(self):
        if self.max_arguments < 0: raise ValueError("max_arguments must be non-negative")
@dataclass
class SecurityGateway:
    policy: ToolPolicy; audit: list[dict[str, str]] = field(default_factory=list)
    def authorize(self, tool: str, arguments: dict[str, Any]) -> bool:
        if not tool.strip(): raise ValueError("tool must be non-empty")
        if len(arguments) > self.policy.max_arguments: decision = False
        else: decision = tool in self.policy.allowed_tools
        self.audit.append({"tool": tool, "decision": "allow" if decision else "deny", "fingerprint": self.fingerprint(tool, arguments)})
        return decision
    @staticmethod
    def fingerprint(tool: str, arguments: dict[str, Any]) -> str:
        canonical = repr(sorted((str(k), repr(v)) for k, v in arguments.items()))
        return sha256(f"{tool}|{canonical}".encode()).hexdigest()
