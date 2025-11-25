from google.adk.agents import Agent
from google.adk.tools import google_search

def morning_greet(name: str) -> str:
    return f"Good Morning, {name}! How can i assist you today? My mood is amazing"

def evening_greet(name: str) -> str:
    return f"Good Evening, {name}! My mood is bit low How can i assist you today? "

root_agent = Agent(
    name = "my_first_agent",
    model = "gemini-2.0-flash",
    description = "An example agent that will answer user queries based on Google Search",
    instruction = """
        First ask user a name and start conversation by greeting the user based on user's greet.
        If user says Good Morning, use morning_greet tool to greet user.
        If user says Good Evening, use evening_greet tool to greet user.
        You are an AI Assistant that helps users with Google Cloud related queries based on Google Search results.
    """,
    tools = [morning_greet, evening_greet]

)

