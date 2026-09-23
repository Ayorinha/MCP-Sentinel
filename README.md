# MCP-Sentinel

Security gateway for Model Context Protocol environments with deterministic tool policies, schema validation, least privilege, audit trails, and approval controls.

## Runtime flow

`ToolRequest → Guard → Policy → Audit Decision → PipelineResult`

The runtime is intentionally network-independent. Integrations belong behind explicit adapters.

## Observability

Every authorization result contains:
- tool
- allow/deny decision
- machine-readable reason
- UTC timestamp

This provides a stable audit boundary without requiring a network service or external telemetry provider.

## Security model

MCP-Sentinel validates requests before policy authorization and fails closed on unsafe requests. Resource validation rejects traversal, absolute paths, Windows drive paths, null bytes, and control characters.

GitHub Actions uses read-only repository contents permissions for CI. GitHub recommends least-privilege workflow permissions and explicit `permissions` declarations. See the repository security documentation for operational guidance.

## Development

```bash
pip install -e . pytest ruff
pytest
ruff check src tests --select E9,F --ignore F403,F405
mcp-sentinel --principal agent --tool search --action read --resource docs/item --allow search
```

## License

MIT — Anderson Leon Ayora.


## Release

Tagged releases are built and validated by GitHub Actions. The release pipeline creates wheel and source distributions, installs the wheel, runs the CLI smoke check, and validates package metadata with Twine. Publishing to PyPI is intentionally not automatic until a trusted-publishing relationship and protected release environment are configured. GitHub documents Trusted Publishing via OIDC as the recommended tokenless approach for PyPI.