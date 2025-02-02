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

# OpenAI https://platform.openai.com/api-keys
# MODEL_NAME = "gpt-4o"
# INFERENCE_SERVER_URL = "https://api.openai.com/v1"
# API_KEY = os.getenv("OPENAI_API_KEY")


# MaaS https://maas.apps.prod.rhoai.rh-aiservices-bu.com/

# MODEL_NAME = "deepseek-r1-distill-qwen-14b"
# INFERENCE_SERVER_URL = os.getenv("MAAS_URL")
# API_KEY = os.getenv("MAAS_API_KEY")

MODEL_NAME = "granite-3-8b-instruct"
INFERENCE_SERVER_URL = "https://granite-3-8b-instruct-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443/v1"
API_KEY = os.getenv("MAAS_API_KEY")

# vllm on a remote server Qwen2.5-Coder-32B-Instruct
# MODEL_NAME = "/var/home/instruct/.cache/instructlab/models/Qwen/Qwen2.5-Coder-32B-Instruct"
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