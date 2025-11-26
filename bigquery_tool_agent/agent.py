from google.adk.agents import Agent
import google.auth
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types

tool_config = BigQueryToolConfig(write_mode= WriteMode.BLOCKED)
application_default_credentials_tuple = google.auth.default()
credentials, project_id = application_default_credentials_tuple
credentials_config= BigQueryCredentialsConfig(
    credentials=credentials
)

bigquery_toolset = BigQueryToolset(
    credentials_config = credentials_config, bigquery_tool_config= tool_config
)

root_agent = Agent(
    name= "bigquery_tool_agent",
    model= "gemini-2.0-flash",
    description= "Agent to answer questions about BigQuery data, models and execute SQL Queries",
    instruction= """
    You are a data science agent with access to several BigQuery tools.
    Make use of those tools to answer the user's questions.
    When writing SQL queries, follow these optimization rules:
    - Always SELECT only the specific columns needed, never use SELECT *
    - Use exact matches (=) instead of wildcards (LIKE '%value%') when possible
    - Prefer WHERE clauses that filter early to reduce data scanned
    - Use LIMIT when only a subset of results is needed
    - For "top N" queries, use ORDER BY with LIMIT instead of subqueries
    - Leverage partitioned and clustered columns in WHERE clauses when available
    - Avoid unnecessary JOINs and prefer filtered subqueries
    """,
    tools=[bigquery_toolset]
)