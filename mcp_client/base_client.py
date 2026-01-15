from contextlib import AbstractAsyncContextManager, AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class StdioMCPClient(AbstractAsyncContextManager):
    def __init__(self, server_params: StdioServerParameters):
        self.server_params = server_params
        self.exit_stack = AsyncExitStack()

    async def __aenter__(self) -> ClientSession:
        read, write = await self.exit_stack.enter_async_context(stdio_client(self.server_params))
        session = await self.exit_stack.enter_async_context(ClientSession(read, write))
        await session.initialize()
        return session

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.exit_stack.__aexit__(exc_type, exc_value, traceback)

