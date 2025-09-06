from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> dict:
    """
    get the current time as a dictionary
    """
    return {
        "current_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    name = "tool_agent",
    description="Tool agent",
    model = "gemini-2.5-flash",
    instruction="""
        You are a helpful assistant that can use tools to perform tasks. Use the tools as needed to complete the user's requests.
        """,
   
    #tools = [google_search]
    #tools = [get_current_time]
)
## Add tools to the agent