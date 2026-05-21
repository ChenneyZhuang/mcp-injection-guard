FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir git+https://github.com/ChenneyZhuang/mcp-injection-guard.git

ENTRYPOINT ["python3", "-m", "mcp_injection_guard.server"]
