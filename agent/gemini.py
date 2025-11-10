import os
from google.genai import Client
from google.genai.types import (
    GenerateContentConfig, 
    GenerateContentResponse, 
    ToolListUnion
)

class GeminiAgent:
    
    def __init__(self, name: str = "GeminiAgent", model:str = "gemini-2.5-flash", tools: ToolListUnion | None = None):
        self.name = name
        self.model = model
        self.tools = tools
        
        gemini_api_key = os.environ.get("GEMINI_API_KEY")
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
    
    def close(self):
        self.llm_client.close()