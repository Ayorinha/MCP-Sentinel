"""Defense-in-depth checks before tool authorization."""
from .security_contracts import ToolRequest

DENIED_ACTIONS = frozenset({"delete", "exfiltrate", "disable_security"})

def guard(request: ToolRequest) -> tuple[bool, str]:
    if not request.principal.strip(): return False, "missing_principal"
    if request.action.lower() in DENIED_ACTIONS: return False, "dangerous_action"
    if ".." in request.resource or request.resource.startswith("/"):
        return False, "unsafe_resource"
    return True, "guard_passed"