from smolagents import CodeAgent, DuckDuckGoSearchTool
from smolagents import LiteLLMModel, HfApiModel
import os

# Environment Variables for OpenAI
# MODEL_NAME = "gpt-4o"
# INFERENCE_SERVER_URL = "https://api.openai.com/v1"
# API_KEY = os.getenv("OPENAI_API_KEY")

# Environment Variables for MaaS https://maas.apps.prod.rhoai.rh-aiservices-bu.com/
# MODEL_NAME = "openai/granite-3-8b-instruct"
# INFERENCE_SERVER_URL = os.getenv("MAAS_URL")
# API_KEY = os.getenv("MAAS_API_KEY")
# MAX_TOKENS = 2048

# MODEL_NAME = "openai/deepseek-r1-distill-qwen-14b"
# INFERENCE_SERVER_URL = os.getenv("MAAS_URL")
# API_KEY = os.getenv("MAAS_API_KEY")
# MAX_TOKENS = 2048

# Environment Variables for Ollama
# ollama serve and ollama pull qwen2.5-coder:32b
# MODEL_NAME = "ollama/qwen2.5-coder:32b"
# API_KEY = os.getenv("ollama")
# INFERENCE_SERVER_URL = "http://localhost:11434"


# Environment Variables for ilab serve in a remote server
MODEL_NAME = "openai//var/home/instruct/.cache/instructlab/models/Qwen/Qwen2.5-Coder-32B-Instruct"
INFERENCE_SERVER_URL = "http://localhost:8000/v1"
API_KEY = "none"
# or
# MODEL_NAME = "openai//var/home/instruct/.cache/instructlab/models/mistralai/Mistral-Small-24B-Instruct-2501"
# INFERENCE_SERVER_URL = "http://localhost:8000/v1"
# API_KEY = "none"

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

