# MCP Agent
This is implementation of MCP Client Server working with Gemini LLM

## Prerequisites

1. Setup virtual environment for Python \
    See instructions in [docs/venv.md](docs/venv.md)
2. Install dependecnies:
    ```bash
    uv pip install -r requirements.txt
    ```
3. Get yourself Gemini API Key from https://aistudio.google.com/api-keys
4. create `.env` file with content:
    ```
    GEMINI_API_KEY=<your Gemini api key>
    ```
5. Run prototype
    ```bash
    python main.py
    ```

6. Send prompt with POST request
    ```bash
    curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"prompt":"What is the status of my local repo here ./ ?\nuse tools provided by MCP Git server to answer the question."}'
    ```

## References
- [Google Gen AI SDK - MCP support](https://github.com/googleapis/python-genai/tree/main?tab=readme-ov-file#model-context-protocol-mcp-support-experimental)
- [MCP Specification](https://modelcontextprotocol.io/)
