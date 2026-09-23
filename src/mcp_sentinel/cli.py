"""Command-line interface for deterministic authorization decisions."""

import argparse
import json

from .policy import Policy, Rule
from .runtime import authorize
from .security_contracts import ToolRequest


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate one MCP-Sentinel tool request.")
    parser.add_argument("--principal", required=True)
    parser.add_argument("--tool", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--resource", required=True)
    parser.add_argument("--allow", action="append", default=[], metavar="TOOL")
    args = parser.parse_args()

    policy = Policy([Rule(tool=name, allowed=True) for name in args.allow])
    result = authorize(
        policy,
        ToolRequest(args.principal, args.tool, args.action, args.resource),
    )
    print(json.dumps({
        "tool": result.tool,
        "allowed": result.allowed,
        "reason": result.reason,
        "timestamp": result.timestamp.isoformat(),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
