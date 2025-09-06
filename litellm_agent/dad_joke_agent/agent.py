from google.adk.agents import Agent
from google.adk.models import Litellm
import os
import random


model = Litellm(
    model = "openrouter/openai/gpt-4.1",
    api_key = os.getenv("OPENROUTER_API_KEY"),
    temperature = 0.7,
    max_tokens = 1000

)

def get_dad_joke() -> dict:
    """
    Get a random dad joke from a predefined list.
    """
    dad_jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call cheese that isn't yours? Nacho cheese!"
    ]
    return {"dad_joke": random.choice(dad_jokes)}

root_agent = Agent(
    name = "dad_joke_agent",
    model = "gemini-2.5-flash",
    description="Dad Joke Agent",
    instruction="""
        You are a dad joke agent. Your task is to provide a random dad joke when prompted by the user.
        """,
        tools=[get_dad_joke]

)
