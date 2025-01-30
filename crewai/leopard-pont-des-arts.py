import requests
import json

from pydantic import Field, ConfigDict
from crewai import Agent, Task, Crew
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

###############################################################################
# 1) A Helper Class to Call Local Ollama  - No LiteLLM
###############################################################################
class DirectOllama:
    """
    Minimal class that calls http://localhost:11434/api/generate for Ollama
    and returns a plain text response. No link to LiteLLM or chain-of-thought.
    """

    def __init__(self, model: str = "qwen2.5-coder:32b", base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url

    def infer(self, prompt: str) -> str:
        """Send a prompt to local Ollama, gather the final text."""
        print("\n=== [DEBUG] Prompt to Mistral (Ollama) ===\n", prompt)

        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "options": {}
        }
        try:
            with requests.post(url, json=payload, stream=True, timeout=60) as resp:
                resp.raise_for_status()
                lines = []
                for chunk in resp.iter_lines():
                    if not chunk:
                        continue
                    data = json.loads(chunk.decode("utf-8"))
                    if "response" in data:
                        lines.append(data["response"])
                    if data.get("done"):
                        break
            return "".join(lines)

        except Exception as e:
            print(f"[DirectOllama] Error calling Ollama: {e}")
            return "Error from Ollama server."


###############################################################################
# 2) A Single Agent That Manually Calls DuckDuckGo & Local Ollama
###############################################################################
class LeopardPontDesArtsAgent(Agent):
    """
    - No "llm" field => CrewAI won't try LiteLLM.
    - Private attributes _ddg and _ollama for manual calls.
    """

    # This config allows custom (arbitrary) private attributes
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # Minimal fields so pydantic doesn't complain about "role," etc.
    role: str = Field(default="LeopardPontDesArtsAgent")
    goal: str = Field(default="Compute crossing time in seconds.")
    backstory: str = Field(default="No chain-of-thought; single pass approach.")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Private attributes (not recognized as pydantic fields):
        self._ddg = DuckDuckGoSearchAPIWrapper()
        self._ollama = DirectOllama(model="mistral")

    def execute_task(self, task, context=None, tools=None):
        question = task.description
        print(f">> [LeopardPontDesArtsAgent] Handling question: {question}")

        # Step 1: DuckDuckGo for relevant facts
        ddg_results = self._ddg.run(question)

        # Step 2: Summarize or compute with local Mistral via Ollama
        prompt = f"""
Question: {question}

DuckDuckGo Search Results:
{ddg_results}

Based on typical leopard speeds (~58 km/h) and Pont des Arts length (~155m),
estimate how many seconds a leopard would take at full speed to run across.
Provide a short numeric answer plus brief reasoning.
"""
        final_answer = self._ollama.infer(prompt)
        return final_answer


###############################################################################
# 3) Define a Single Task + Crew
###############################################################################
leopard_task = Task(
    description="How many seconds would it take for a leopard at full speed to run through Pont des Arts?",
    expected_output="Approximate time in seconds + brief reasoning",
    agent=LeopardPontDesArtsAgent()
)

crew = Crew(
    agents=[leopard_task.agent],
    tasks=[leopard_task],
    verbose=True
)

###############################################################################
# 4) Kick off the Crew
###############################################################################
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== FINAL CREW RESULT ===\n", result)