from mcp_sentinel.policy import Policy, Rule
from mcp_sentinel.runtime import authorize
from mcp_sentinel.security_contracts import ToolRequest


def test_authorize_runs_guard_then_policy():
    result = authorize(Policy([Rule("search")]), ToolRequest("agent", "search", "read", "docs/item"))
    assert result.allowed is True
    assert result.reason == "explicit-rule"


def test_authorize_fails_closed_before_policy():
    result = authorize(Policy([Rule("search")]), ToolRequest("agent", "search", "delete", "docs/item"))
    assert result.allowed is False
    assert result.reason == "dangerous_action"


def test_authorize_denies_unknown_tool():
    result = authorize(Policy([]), ToolRequest("agent", "unknown", "read", "docs/item"))
    assert result.allowed is False
    assert result.reason == "default-deny"
