import os
from contextlib import AbstractContextManager
from google.genai import Client
from google.genai.types import (
    GenerateContentConfig, 
    GenerateContentResponse, 
    ToolListUnion
)

class GeminiAgent(AbstractContextManager):
    
    def __init__(self, name: str = "GeminiAgent", model:str = "gemini-2.5-flash", tools: ToolListUnion | None = None):
        self.name = name
        self.model = model
        self.tools = tools
        
        gemini_api_key = os.environ.get("GEMINI_API_KEY")
        if gemini_api_key is None:
            raise Exception("GEMINI_API_KEY environment variable is not set.")
        
        self.llm_client = Client(api_key=gemini_api_key)
        
    async def __call__(self, prompt: str) -> GenerateContentResponse:
        return await self.llm_client.aio.models.generate_content(
                model = self.model,
                contents = prompt,
                config = GenerateContentConfig(
                    temperature = 0,
                    tools = self.tools,
                ),
            )
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.llm_client.close()