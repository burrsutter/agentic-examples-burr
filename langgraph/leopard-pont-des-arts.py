import os
from typing import Annotated, TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

# Environment Variables
INFERENCE_SERVER_URL = os.getenv("INFERENCE_SERVER_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Initialize LLM
llm = ChatOpenAI(
    openai_api_key=API_KEY,
    openai_api_base=f"{INFERENCE_SERVER_URL}",
    model_name=MODEL_NAME,
    top_p=0.92,
    temperature=0.01,
    max_tokens=512,
    presence_penalty=1.03,
    streaming=True
)

# Initialize Tools
tools = [DuckDuckGoSearchRun()]
llm_with_tools = llm.bind_tools(tools)

# Define State
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Build Graph
graph_builder = StateGraph(State)

def chatbot(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}  # Append response to message history

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

graph = graph_builder.compile(checkpointer=MemorySaver())
config = {"configurable": {"thread_id": "1"}}

# Agent Function
def react_agent(user_input):
    events = graph.stream({"messages": [(HumanMessage(content=user_input))]}, config, stream_mode="values")

    for event in events:
        messages = event["messages"]

        # Get only the last AI response (avoiding repeated prints)
        last_message = messages[-1]
        if isinstance(last_message, AIMessage):  # Ensure it's the LLM response
            print("\n===== \033[1mAgent Response\033[0m =====\n", last_message.content, "\n")

# Example Usage
react_agent("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")