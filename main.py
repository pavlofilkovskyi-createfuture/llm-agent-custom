import asyncio
from agent.gemini import GeminiAgent
from mcp_client import GitMCPClient, FilesystemMCPClient

from dotenv import load_dotenv
load_dotenv()  # Load from .env file


async def main() -> None:
    
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
        GitMCPClient() as git_mcp_client, \
        FilesystemMCPClient() as filesystem_mcp_client:

            with GeminiAgent(tools=[git_mcp_client, filesystem_mcp_client]) as agent:
                response =  await agent(prompt)
                print(response.text)
    

if __name__ == "__main__":    
    asyncio.run(main())