from mcp_sentinel.guard import guard
from mcp_sentinel.security_contracts import ToolRequest


def test_guard_fails_closed_for_invalid_identity():
    assert guard(ToolRequest("", "search", "read", "docs")) == (
        False,
        "invalid_request",
    )


def test_guard_blocks_case_insensitive_dangerous_actions():
    assert guard(ToolRequest("agent", "fs", "DELETE", "docs/item"))[0] is False


def test_guard_blocks_path_traversal_and_absolute_paths():
    assert guard(ToolRequest("agent", "fs", "read", "docs/../secret"))[0] is False
    assert guard(ToolRequest("agent", "fs", "read", "\\etc\\passwd"))[0] is False
    assert guard(ToolRequest("agent", "fs", "read", "C:\\Windows\\system32"))[0] is False


def test_guard_blocks_control_characters_and_null_bytes():
    assert guard(ToolRequest("agent", "fs", "read", "docs/secret\x00.txt"))[0] is False
    assert guard(ToolRequest("agent", "fs", "read", "docs/secret\n.txt"))[0] is False


def test_guard_allows_normal_relative_resources():
    assert guard(ToolRequest("agent", "fs", "read", "docs/item.txt")) == (
        True,
        "guard_passed",
    )
