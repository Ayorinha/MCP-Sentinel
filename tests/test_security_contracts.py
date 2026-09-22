from mcp_sentinel.security_contracts import ToolRequest,is_safe_request

def test_safe_request_requires_complete_identity():
    assert is_safe_request(ToolRequest("agent","search","read","docs"))
    assert not is_safe_request(ToolRequest("","search","read","docs"))
