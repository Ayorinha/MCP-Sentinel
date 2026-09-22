from mcp_sentinel.audit import decide
from mcp_sentinel.policy import Policy, Rule, ToolCall

def test_default_deny_is_explainable():
    decision = decide(Policy([]), ToolCall("delete_email", {}))
    assert decision.allowed is False
    assert decision.reason == "default-deny"

def test_allow_rule_is_auditable():
    decision = decide(Policy([Rule("search", True)]), ToolCall("search", {}))
    assert decision.allowed is True
    assert decision.reason == "explicit-rule"
