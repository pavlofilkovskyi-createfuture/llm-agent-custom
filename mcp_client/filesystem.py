import os
from pathlib import Path
from mcp import StdioServerParameters
from .base_client import StdioMCPClient

class FilesystemMCPClient(StdioMCPClient):
    def __init__(self, root_path: str | None = None):
        if root_path is None:
            root_path = str(Path.home().expanduser().resolve())
        
        server_params = StdioServerParameters(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem", root_path],
            env=os.environ.copy()
        )
        
        super().__init__(server_params)