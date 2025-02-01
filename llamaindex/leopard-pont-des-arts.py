import asyncio
from llama_index.llms.openai import OpenAI
from llama_index.core.workflow import Context
from llama_index.core.agent.workflow import (
    FunctionAgent,
    AgentWorkflow,
    AgentOutput,
    ToolCall,
    ToolCallResult,
)
from tavily import AsyncTavilyClient

from dotenv import load_dotenv
import os

load_dotenv()

# Initialize LLM for OpenAI's gpt-4o
llm = OpenAI(
    model="gpt-4o",
    api_key=os.getenv('API_KEY'),
)

# Helper to update context state
async def update_state(ctx: Context, updates: dict) -> None:
    state = await ctx.get("state")
    state.update(updates)
    await ctx.set("state", state)


# Tool functions
async def search_web(query: str) -> str:
    """Search the web for information on a query."""
    client = AsyncTavilyClient(api_key=os.getenv('TVLY_KEY'))
    return str(await client.search(query))


async def divide(a: float, b: float) -> float:
    # Ensure floating division is done properly
    return a / b


async def multiply(a: float, b: float) -> float:
    return a * b


async def record_notes(ctx: Context, notes: str, notes_title: str) -> str:
    state = await ctx.get("state")
    state.setdefault("research_notes", {})[notes_title] = notes
    await ctx.set("state", state)
    return "Notes recorded."


async def write_report(ctx: Context, report_content: str) -> str:
    await update_state(ctx, {"report_content": report_content})
    return "Report written."


async def review_solution(ctx: Context, review: str) -> str:
    await update_state(ctx, {"review": review})
    return "Solution reviewed."


research_agent = FunctionAgent(
    name="ResearchAgent",
    description=(
        "Useful for searching the web for required information and recording clear research notes."
    ),
    system_prompt=(
        "You are the ResearchAgent. Retrieve and record accurate data for the problem."
        "Once you have clear notes, pass control to the SolverAgent."
    ),
    llm=llm,
    tools=[search_web, record_notes],
    can_handoff_to=["SolverAgent"],
)

solver_agent = FunctionAgent(
    name="SolverAgent",
    description="Useful for thinking in mathematical calculations to provide a numerical solution.",
    system_prompt=(
        "You are the SolverAgent. Use the research notes provided to compute the correct solution. If any data is missing, request it from the ResearchAgent. Then always hand off the solution to the ReviewAgent for verification."
    ),
    llm=llm,
    tools=[divide, multiply],
    can_handoff_to=["ReviewAgent", "ResearchAgent"],
)

review_agent = FunctionAgent(
    name="ReviewAgent",
    description="Useful for verification that the solution is mathematically sound and aligns with the research notes.",
    system_prompt=(
        "You are the ReviewAgent. Critically evaluate the solution given by the SolverAgent. "
        "Check that the calculations account for the proper unit conversion and that the final "
        "result is plausible given the researched data. If the solution is incorrect, request a recalculation from "
        "the SolverAgent with specific corrections. Once verified, hand off control to the WriteAgent."
    ),
    llm=llm,
    tools=[review_solution],
    can_handoff_to=["SolverAgent", "WriteAgent"],
)

write_agent = FunctionAgent(
    name="WriteAgent",
    description="Useful for composing a final report summarizing the solution.",
    system_prompt=(
        "You are the WriteAgent. Write a report using this template:"
        "Question: [original question]\n"
        "Answer: [shortest possible answer to the original question, ideally a single number or a single word]\n"
        "Explanation: [short clear explanation of the solution given the researched inputs]"
    ),
    llm=llm,
    tools=[write_report],
    can_handoff_to=[],
)

agent_workflow = AgentWorkflow(
    agents=[research_agent, solver_agent, review_agent, write_agent],
    root_agent=research_agent.name,
    initial_state={
        "research_notes": {},
        "report_content": "Not written yet.",
        "solution": None,
        "review": None,
    },
)


async def main():
    question = "How many seconds would it take for a leopard at full speed to run through Pont des Arts?"
    # question = "How many seconds would it take for a leopard tortoise at full speed to run through Pont des Arts?"
    handler = agent_workflow.run(user_msg=(question))
    current_agent = None
    async for event in handler.stream_events():
        if (
            hasattr(event, "current_agent_name")
            and event.current_agent_name != current_agent
        ):
            current_agent = event.current_agent_name
            print(f"\n{'='*50}\nAgent: {current_agent}\n{'='*50}\n")
        if isinstance(event, AgentOutput) and event.response.content:
            print("Output:", event.response.content)
        elif isinstance(event, ToolCallResult):
            print("")
        elif isinstance(event, ToolCall):
            print(
                f"Calling Tool: {event.tool_name} with arguments: {event.tool_kwargs}"
            )

    state = await handler.ctx.get("state")
    print(f"\n{'='*50}\nFinal Report Content\n{'='*50}\n")
    print(state.get("report_content"))


if __name__ == "__main__":
    asyncio.run(main())
