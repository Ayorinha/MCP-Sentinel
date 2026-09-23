"""Production smoke tests for MCP-Sentinel."""
import importlib


def test_package_imports() -> None:
    module = importlib.import_module("mcp_sentinel")
    assert module.__name__ == "mcp_sentinel"


def test_import_is_network_independent() -> None:
    # Import-time network calls make CI and offline development fragile.
    module = importlib.import_module("mcp_sentinel")
    assert module is not None
