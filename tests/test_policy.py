from mcp_sentinel.policy import *
def test_default_deny():
 p=Policy([Rule('search')]); assert p.authorize(ToolCall('search',{})); assert not p.authorize(ToolCall('delete',{}))
