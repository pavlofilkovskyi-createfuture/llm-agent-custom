import os
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google.genai import Client
from google import genai
from flask import Flask, request, jsonify

from dotenv import load_dotenv
load_dotenv()  # Load from .env file


app = Flask(__name__)

# https://github.com/modelcontextprotocol/servers/tree/main/src/git
git_server_params = StdioServerParameters(
    command = sys.executable,
    args = ["-m", "mcp_server_git"],  # MCP Server
    env = None,  # Optional environment variables
)

# https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
filesystem_server_params = StdioServerParameters(
    command = "npx",
    args = ["-y", "@modelcontextprotocol/server-filesystem", "~/Projects"],
    env = None,
)

client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

async def send_request(prompt:str):
    async with \
        stdio_client(git_server_params) as (git_read, git_write), \
        stdio_client(filesystem_server_params) as (fs_read, fs_write):
        
        async with \
            ClientSession(git_read, git_write) as git_session, \
            ClientSession(fs_read, fs_write) as fs_session:
            
            await git_session.initialize()
            await fs_session.initialize()

            response = await client.aio.models.generate_content(
                model = "gemini-2.5-flash",
                contents = prompt,
                config = genai.types.GenerateContentConfig(
                    temperature = 0,
                    tools = [git_session, fs_session],
                ),
            )
            print(response.text)
            client.close()
            return response.text

@app.route('/chat', methods=['POST'])
async def chat():
    data = request.json
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({"error": "prompt is required"}), 400
    
    response = await send_request(prompt)
    return jsonify({"response": response})

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "OK"
    })
    

if __name__ == "__main__":
    print("Starting Chat Server on http://localhost:5000")
    print("Available endpoints:")
    print("  POST /chat - Send a message")
    print("  GET /health - Check server status")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)