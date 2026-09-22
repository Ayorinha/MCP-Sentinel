from mcp_sentinel.core import *

def test_policy():\n g=SecurityGateway(ToolPolicy(frozenset({"read"}))); assert g.authorize("read",{}) and not g.authorize("write",{})
