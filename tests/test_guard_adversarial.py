from mcp_sentinel.guard import guard
from mcp_sentinel.security_contracts import ToolRequest
def test_guard_fails_closed_for_invalid_identity(): assert guard(ToolRequest("", "search", "read", "docs")) == (False, "invalid_request")
def test_guard_blocks_case_insensitive_dangerous_actions(): assert guard(ToolRequest("agent", "fs", "DELETE", "docs/item"))[0] is False
def test_guard_blocks_path_traversal_and_absolute_paths():
    assert guard(ToolRequest("agent", "fs", "read", "docs/../secret"))[0] is False
    assert guard(ToolRequest("agent", "fs", "read", "\\etc\\passwd"))[0] is False
