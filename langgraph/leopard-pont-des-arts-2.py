from typing_extensions import TypedDict
from typing import Annotated

from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    ToolMessage,
    AIMessage,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langgraph.graph import END, StateGraph, START

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools)
graph_builder.add_node("tools", tool_node)
# Any time a tool is called, we return to the chatbot to decide the next step
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")


def react_agent(user_input):
    global last_message_index
    # Start streaming the conversation
    events = graph.stream(
        {"messages": [("user", user_input)]}, config, stream_mode="values"
    )

react_agent("How many seconds would it take for a leopard at full speed to run through Pont des Arts??")