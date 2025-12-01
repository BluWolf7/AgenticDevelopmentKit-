import os
import sys
sys.path.append("..")
import google.cloud.logging

from google.adk.agents import Agent
from google.genai import types
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool

from dotenv import load_dotenv

load_dotenv()
cloud_logging_client= google.cloud.logging.Client()
cloud_logging_client.setup_logging()


root_agent = Agent(
    name= "crew_ai_tool_agent",
    model= os.getenv("MODEL"),
    description= "Agent to write files",
    instruction= """
    Write files as requested by the user.
    """,
    generate_content_config= types.GenerateContentConfig(
        temperature=0,
    ),
    tools= [
        CrewaiTool(
            name="check_google_cloud_release_notes",
            description= """Scrapes the latest Google Cloud changes from official Google cloud release notes webpage.
            use this tool to get latest updates about Google Cloud Products and Services""",
            tool=ScrapeWebsiteTool("https://docs.cloud.google.com/release-notes")
        )

    ]

)