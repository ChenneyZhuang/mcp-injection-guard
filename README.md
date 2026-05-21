# 🛡️ MCP Injection Guard

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/ChenneyZhuang/mcp-injection-guard/actions/workflows/ci.yml/badge.svg)](https://github.com/ChenneyZhuang/mcp-injection-guard/actions/workflows/ci.yml)

**MCP server for detecting prompt injection attacks.**  
The first free, open-source injection guard that works with any MCP-compatible AI agent.

---

## What It Does

Your AI agent calls `check_injection` before sending user input to an LLM.
The server scans for jailbreak attempts, role manipulation, system prompt overrides,
and 20+ other attack vectors — returns a risk score and details.

| Risk Level | Score | Action |
|-----------|-------|--------|
| `safe` | 0.0–0.2 | Pass through |
| `low` | 0.2–0.5 | Log and pass |
| `medium` | 0.5–0.7 | Flag for review |
| `high` | 0.7–0.9 | Block or sanitize |
| `critical` | 0.9–1.0 | Block immediately |

---

## Quick Start

### Install

```bash
pip install git+https://github.com/ChenneyZhuang/mcp-injection-guard.git
```

### Configure Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "injection-guard": {
      "command": "python3",
      "args": ["-m", "mcp_injection_guard.server"]
    }
  }
}
```

### Configure Claude Code

```bash
claude mcp add injection-guard python3 -m mcp_injection_guard.server
```

---

## Tools

### `check_injection(text: str) → dict`

Scan a single text for injection patterns.

```python
{"risk_score": 0.05, "risk_level": "safe", "safe": true, "matches": []}
```

### `batch_check(texts: list[str]) → list[dict]`

Scan multiple texts at once.

---

## How It Works

```
User Input → check_injection() → Risk Score → Your App Logic → LLM
                                        │
                                   block if critical
```

---

## Related

- [prompt-injection-guard](https://github.com/ChenneyZhuang/prompt-injection-guard) — the underlying detection engine
- [Model Context Protocol](https://modelcontextprotocol.io) — MCP specification

## License

MIT
