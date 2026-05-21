"""MCP server for prompt injection detection."""

from mcp.server.fastmcp import FastMCP
from guard import scan

mcp = FastMCP("Injection Guard")


@mcp.tool()
def check_injection(text: str) -> dict:
    """Scan text for prompt injection attacks.

    Returns risk score (0.0–1.0), risk level, and details.
    Use this to screen user input before passing it to an LLM.
    """
    result = scan(text)
    return {
        "risk_score": round(result.score, 4),
        "risk_level": result.risk_level.value,
        "is_injection": result.is_injection,
        "reasoning": result.reasoning,
        "patterns_matched": [
            {"name": m.name, "text": m.matched_text, "description": m.description}
            for m in result.patterns_matched
        ],
        "safe": result.risk_level.value == "safe",
    }


@mcp.tool()
def batch_check(texts: list[str]) -> list[dict]:
    """Scan multiple texts at once. Returns results for each."""
    return [check_injection(t) for t in texts]


def main():
    mcp.run()


if __name__ == "__main__":
    main()
