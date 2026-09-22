from mcp_sentinel.core import SecurityGateway, ToolPolicy

def test_policy_and_audit():
    g = SecurityGateway(ToolPolicy(frozenset({"read"})))
    assert g.authorize("read", {"id": 1}); assert not g.authorize("write", {})
    assert len(g.audit) == 2 and g.audit[-1]["decision"] == "deny"
