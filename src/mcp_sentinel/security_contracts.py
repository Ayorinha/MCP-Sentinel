"""Security contracts for tool invocation."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ToolRequest:
    principal: str
    tool: str
    action: str
    resource: str

def is_safe_request(request: ToolRequest) -> bool:
    return all(isinstance(v, str) and v.strip() for v in (request.principal, request.tool, request.action, request.resource))
