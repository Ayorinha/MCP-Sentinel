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

GitHub Actions uses read-only repository contents permissions for CI. GitHub recommends least-privilege workflow permissions and explicit `permissions` declarations.

## Validation and release

The repository follows a five-stage engineering path:

1. Core functional
2. Tests & validation
3. Autonomous decision pipeline
4. Observability + security
5. Release / production

Stages 1–5 are implemented and the Stage 5 PR (#9) is merged to `main`. The remaining release boundary is operational: creating the first GitHub Release and, separately, configuring PyPI Trusted Publishing if package publication is desired.

See `production-readiness.md` for the current release checklist.

## Development

```bash
pip install -e . pytest ruff
pytest
ruff check src tests --select E9,F --ignore F403,F405
mcp-sentinel --principal agent --tool search --action read --resource docs/item --allow search
```

## Release

Tagged releases are built and validated by GitHub Actions. The release pipeline creates wheel and source distributions, installs the wheel, runs the CLI smoke check, validates package metadata with Twine, and uploads the distributions as workflow artifacts.

Publishing to PyPI is intentionally not automatic until a trusted-publishing relationship and protected release environment are configured.

## License

MIT — Anderson Leon Ayora.
