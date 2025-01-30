from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

from phi.model.ollama import Ollama

import os

# ollama localhost, ollama serve, ollama pull qwen2.5-coder:32b
# agent = Agent (
#     model=Ollama(id="qwen2.5-coder:32b"),
#     tools=[DuckDuckGo()],
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True,
# )

# MaaS https://maas.apps.prod.rhoai.rh-aiservices-bu.com/
# agent = Agent (
#     model=OpenAIChat(id="granite-3-8b-instruct", 
#                      base_url="https://granite-3-8b-instruct-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1",
#                      api_key=os.getenv("MAAS_API_KEY")),
#     tools=[DuckDuckGo()],
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True,
# )

# OpenAI https://platform.openai.com/api-keys
# agent = Agent (
#     model=OpenAIChat(id="gpt-4o", 
#                      base_url="https://api.openai.com/v1",
#                      api_key=os.getenv("OPENAI_API_KEY")),
#     tools=[DuckDuckGo()],
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True,
# )

# ilab serve in a remote server Qwen2.5-Coder-32B-Instruct
MODEL_NAME = "/var/home/instruct/.cache/instructlab/models/Qwen/Qwen2.5-Coder-32B-Instruct"
INFERENCE_SERVER_URL = "http://localhost:8000/v1"
API_KEY = "none"
# OR 
# ilab serve in a remote server Mistral-Small-24B-Instruct-2501
# MODEL_NAME = "openai//var/home/instruct/.cache/instructlab/models/mistralai/Mistral-Small-24B-Instruct-2501"
# INFERENCE_SERVER_URL = "http://localhost:8000/v1"
# API_KEY = "none"

agent = Agent (
    model=OpenAIChat(id=MODEL_NAME, 
                     base_url=INFERENCE_SERVER_URL,
                     api_key=API_KEY),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)



agent.print_response("How many seconds would it take for a leopard at full speed to run through Pont des Arts?", stream=False)