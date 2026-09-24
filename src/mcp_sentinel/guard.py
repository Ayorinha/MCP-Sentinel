"""Defense-in-depth checks before tool authorization."""

import re

from .security_contracts import ToolRequest, is_safe_request

DENIED_ACTIONS = frozenset({"delete", "exfiltrate", "disable_security"})
_WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:/")


def guard(request: ToolRequest) -> tuple[bool, str]:
    if not is_safe_request(request):
        return False, "invalid_request"

    if request.action.casefold() in DENIED_ACTIONS:
        return False, "dangerous_action"

    normalized = request.resource.replace("\\", "/")
    if (
        normalized.startswith(("/", "~"))
        or _WINDOWS_ABSOLUTE.match(normalized)
        or "\x00" in normalized
        or any(ord(char) < 32 for char in normalized)
        or "../" in f"{normalized}/"
        or normalized == ".."
    ):
        return False, "unsafe_resource"

    return True, "guard_passed"
