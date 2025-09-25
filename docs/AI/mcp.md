# MCP
---

* It’s the **decision-making + orchestration layer** between an LLM and the outside world.
* Whether it’s a server, a local script, or a function call depends on your use case.

---
## MCP is simply a decision making AI process.
---

Conceptually, **MCP is simply a decision‑making AI process** that:

1. **Receives a request** from the user.
2. **Understands the available capabilities** (tools, APIs, data).
3. **Chooses what to do** — which tools to use, in what order, and with what parameters.
4. **Executes those tools** and feeds results back into the reasoning loop.
5. **Produces the final answer or action**.

---

You can think of it like:

* **Without MCP** → LLM just chats, no actions.
* **With MCP** → LLM chats *and* decides how to use other resources to accomplish a goal.

Whether it lives in:

* A **local script**
* A **web server**
* A **cloud service**

…doesn’t change the concept — the “MCP” part is the **orchestration brain**.

---
## Use Cases
---

* MCP is a great decision-maker when things are ambiguous or user-driven.
* But in a strict, well-bounded pipeline, procedural code will always win for speed, cost, and control.


---
## Simple How-To
---

1. Pick your LLM you want to use for MCP.
2. Define the tools you want the model to have access to (python functions).
3. Give the model access to those tools.
4. Run.

Demo....

---------------------------------------
## What kind of server is an MCP server?
---------------------------------------

An **MCP server** is not as complex as you might think. It's really just:

> A **web server** that hosts your MCP logic and exposes it over an API so other apps (or people) can use it.

---

### Why you might make MCP into a server

* You want **multiple clients** (web apps, mobile apps, scripts) to use the same tools and orchestration logic.
* You want a **centralized place** to manage:
    * API keys
    * Data sources
    * Permissions
    * Logging and monitoring of tool calls
* You want it **always running** instead of firing up the Python script each time.

---

### What it looks like

If we turned our current LangGraph example into a server:

* The LangGraph agent would still decide which tools to run.
* The tools would still be Python functions calling APIs or databases.
* But instead of calling `.invoke()` in a local script, you’d send a POST request like:

```http
POST /ask
{
  "question": "What's the population of Chicago and the weather there?"
}
```

And the server would respond with the final text answer.

---

So yes — an “MCP server” is basically:

```
Web server + MCP logic + LLM + tools
```

The “MCP” part is still the **decision-making layer**, the “server” part is just about how it’s deployed.

---

```python
"""
MCP Demo
--------

This is a demo of how to use LangChain with MCP.

To run this demo, first install the dependencies: ``uv add langchain-anthropic python-dotenv langgraph``


"""
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

load_dotenv()

# 1. Define your LLM
llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0  # tells the llm how varied responses should be. 0=always same answer (highest probability).
)

# 2. Define a tool
@tool
def get_weather(city: str) -> str:
    """Gets the weather for a given city."""
    print(f"[Tool] Getting weather for {city}")
    return f"The weather in {city} is sunny."

@tool
def get_population(city: str) -> str:
    """Gets the population of a given city."""
    return f"The population of {city} is about 3 million."


@tool
def get_latitude_and_longitude(city: str) -> str:
    """Gets the latitude and longitude of a given city."""
    return f"The population of {city} is about 3 million."



# 3. Create the agent (LangGraph style)
agent = create_react_agent(llm, [get_weather, get_population, get_latitude_and_longitude], debug=True)

# 4. Invoke it
result = agent.invoke({"messages": [{"role": "user", "content": "What is the weather like in San Francisco?."}]})

# Get the last message
last_message = result["messages"][-1]
print(last_message.content)
```