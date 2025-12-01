import os
import sys
sys.path.append("..")
import google.cloud.logging

from google.adk.agents import Agent
from google.adk.tools.langchain_tool import LangchainTool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from dotenv import load_dotenv

load_dotenv()
cloud_logging_client= google.cloud.logging.Client()
cloud_logging_client.setup_logging()


root_agent = Agent(
    name= "langchain_tool_agent",
    model= os.getenv("MODEL"),
    description= "Answers questions using wikipedia",
    instruction= """
    Research the topic suggested by the user, share the information you have found with the user.
    """,
    tools= [
        LangchainTool(
            tool=WikipediaQueryRun(
                api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]

)