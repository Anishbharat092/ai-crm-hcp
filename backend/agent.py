from langgraph.graph import StateGraph
from tools import (
    log_interaction_tool,
    edit_interaction_tool,
    sentiment_tool,
    summary_tool,
    followup_tool
)
from groq import Groq

client = Groq(api_key="")

# ---- STEP 1: INTENT DETECTION ----
def detect_intent(state):
    prompt = f"""
    Classify user intent:
    message: {state['message']}

    Possible intents:
    - log
    - edit
    - summarize
    - sentiment
    - followup

    Return ONLY intent word.
    """

    res = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )

    state["intent"] = res.choices[0].message.content.strip().lower()
    return state


# ---- STEP 2: TOOL ROUTER ----
def route_tool(state):
    intent = state["intent"]

    if intent == "log":
        state["output"] = log_interaction_tool(state["message"])
    elif intent == "edit":
        state["output"] = edit_interaction_tool(state["message"])
    elif intent == "sentiment":
        state["output"] = sentiment_tool(state["message"])
    elif intent == "summarize":
        state["output"] = summary_tool(state["message"])
    elif intent == "followup":
        state["output"] = followup_tool(state["message"])
    else:
        state["output"] = {"error": "Unknown intent"}

    return state


# ---- GRAPH ----
def build_graph():
    graph = StateGraph(dict)

    graph.add_node("intent", detect_intent)
    graph.add_node("tool", route_tool)

    graph.set_entry_point("intent")
    graph.add_edge("intent", "tool")

    return graph.compile()


graph = build_graph()


def process_chat(message: str):
    return graph.invoke({"message": message})["output"]