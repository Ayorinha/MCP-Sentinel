from mcp_sentinel.core import SecurityGateway, ToolPolicy

def test_policy():
    gateway = SecurityGateway(ToolPolicy(frozenset({"read"})))
    assert gateway.authorize("read", {})
    assert not gateway.authorize("write", {})
