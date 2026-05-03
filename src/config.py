import os
from dotenv import load_dotenv

load_dotenv()

FOUNDRY_PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
FOUNDRY_AGENT_ID = os.getenv("FOUNDRY_AGENT_ID")

if not FOUNDRY_PROJECT_ENDPOINT or not FOUNDRY_AGENT_ID:
    raise ValueError("Missing environment variables. Check your .env file.")
