import os
import sys
import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google.genai import Client
from google.genai.types import GenerateContentConfig
from agent.gemini import GeminiAgent

from dotenv import load_dotenv
load_dotenv()  # Load from .env file

# https://github.com/modelcontextprotocol/servers/tree/main/src/git
# run as standalone module: python -m mcp_server_git
git_server_params = StdioServerParameters(
    command = sys.executable,
    args = ["-m", "mcp_server_git"],  # MCP Server
    env = None,  # Optional environment variables
)

# https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
filesystem_server_params = StdioServerParameters(
    command = "npx",
    args = ["-y", "@modelcontextprotocol/server-filesystem", "/Users/pfilkovskyi/Projects"],
    env = None,
)

async def main() -> None:
    
    # prompt = "Hello!"
    
    prompt = """
    You are a developer with access to MCP tools for Git and Filesystem.
    Using tools available to you perform the following task:
    1. navigate to the repository at /Users/pfilkovskyi/Projects/test-repo
    2. find existing file in it named `hello.txt` with the content 'Hello!'
    3. Modify the content of `hello.txt` to 'Hello, World!'
       if the file does not exist, create it with the content 'Hello, World!'
    4. commit changes with message 'update hello.txt'
    """
    
    async with \
        stdio_client(git_server_params) as (git_read, git_write), \
        stdio_client(filesystem_server_params) as (fs_read, fs_write):
        
        async with \
            ClientSession(git_read, git_write) as git_mcp_client, \
            ClientSession(fs_read, fs_write) as filesystem_mcp_client:
            
            await git_mcp_client.initialize()
            await filesystem_mcp_client.initialize()

            agent: GeminiAgent = GeminiAgent(tools=[git_mcp_client, filesystem_mcp_client])
            response =  await agent(prompt)
            print(response.text)
            agent.close()
    

if __name__ == "__main__":    
    asyncio.run(main())