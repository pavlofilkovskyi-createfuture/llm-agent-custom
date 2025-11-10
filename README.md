# MCP Agent
This is implementation of MCP Client Server working with Gemini LLM

## Prerequisites

1. Setup virtual environment for Python \
    See instructions in [docs/venv.md](docs/venv.md)
2. Install dependecnies:
    ```bash
    uv sync
    ```
3. Get yourself Gemini API Key from https://aistudio.google.com/api-keys
4. create `.env` file with content:
    ```
    GEMINI_API_KEY=<your Gemini api key>
    ```
5. Install Filesystem MCP:
    ```bash
    npm ci
    ```
6. Run prototype
    ```bash
    uv run main.py
    ```

## References
- [Google Gen AI SDK - MCP support](https://github.com/googleapis/python-genai/tree/main?tab=readme-ov-file#model-context-protocol-mcp-support-experimental)
- [MCP Specification](https://modelcontextprotocol.io/)
