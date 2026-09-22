from mcp_sentinel.security_contracts import ToolRequest
from mcp_sentinel.guard import guard

def test_guard_denies_dangerous_action():
    assert guard(ToolRequest("agent","tool","delete","record"))[0] is False
