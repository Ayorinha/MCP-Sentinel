# Architecture

## Purpose
MCP tool security and policy enforcement.

## Runtime boundary

```
Input / Adapter
     ↓
Domain Contracts
     ↓
Deterministic Core
     ↓
Validation / Safety
     ↓
Result + Observability
     ↓
External Integration (optional)
```

The domain layer must remain testable without network access, credentials or production data. External providers belong behind explicit adapters.

## Reliability principles

- Validate inputs at system boundaries.
- Keep core decisions deterministic where the domain permits it.
- Preserve provenance and auditability for consequential outputs.
- Fail explicitly rather than silently swallowing errors.
- Use synthetic/public-safe fixtures in the repository.
- Keep operational concerns separate from domain logic.

## CI contract

Every pull request runs compilation, static checks and automated tests before merge.
