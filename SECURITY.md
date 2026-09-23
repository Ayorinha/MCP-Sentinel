# Security

## Runtime controls

MCP-Sentinel follows a fail-closed security boundary:

1. Validate the incoming request.
2. Reject dangerous actions.
3. Reject unsafe resources.
4. Apply the explicit tool policy.
5. Return an auditable decision.

## Observability boundary

Authorization decisions expose the tool, decision, reason, and UTC timestamp. The core does not transmit telemetry or credentials.

## GitHub Actions

CI declares `contents: read` and does not require repository write access or secrets. This follows the principle of least privilege recommended by GitHub.

Do not add privileged workflow triggers such as `pull_request_target` unless the repository has a documented requirement and the untrusted-code boundary is preserved.

## Reporting

Do not include credentials, tokens, personal data, or production payloads in issues or pull requests. Report security-sensitive findings privately when appropriate.
