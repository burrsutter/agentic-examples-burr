from smolagents import CodeAgent, DuckDuckGoSearchTool
from smolagents import LiteLLMModel, HfApiModel
import os

MODEL_NAME = os.getenv("MODEL_NAME")
INFERENCE_SERVER_URL = os.getenv("INFERENCE_SERVER_URL")
API_KEY = os.getenv("API_KEY")

model = LiteLLMModel(
    model_id=MODEL_NAME,
    api_base=INFERENCE_SERVER_URL,
    api_key=API_KEY
  #  max_tokens = MAX_TOKENS
)

# OR
# HF hosted model - Qwen/Qwen2.5-Coder-32B-Instruct as of last execution
# smolagents is a Hugginface sponsored project so they have some magic for using their hosted model
# model=HfApiModel()

# Create agent
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# execute agent
agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")

