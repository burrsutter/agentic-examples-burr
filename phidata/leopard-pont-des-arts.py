from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

from phi.model.ollama import Ollama

import os

MODEL_NAME = os.getenv("MODEL_NAME")
INFERENCE_SERVER_URL = os.getenv("INFERENCE_SERVER_URL")
API_KEY = os.getenv("API_KEY")



# ollama 
# agent = Agent (
#     model=Ollama(id=os.getenv("MODEL_NAME")),
#     tools=[DuckDuckGo()],
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True,
# )

# openai api
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