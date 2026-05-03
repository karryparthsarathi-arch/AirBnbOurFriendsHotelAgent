
'''Flow of config agent cred 
.env file
   ↓
load_dotenv()
   ↓
Environment Variables
   ↓
os.getenv()
   ↓
Used in Application
'''

# Import OS module → used to access environment variables
import os  

# Import function to load variables from .env file
from dotenv import load_dotenv  

# Load variables from .env file into system environment
load_dotenv()


# Read Azure Foundry Project Endpoint from environment
FOUNDRY_PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")

# Read Agent ID from environment
FOUNDRY_AGENT_ID = os.getenv("FOUNDRY_AGENT_ID")


# Validate that required variables exist
if not FOUNDRY_PROJECT_ENDPOINT or not FOUNDRY_AGENT_ID:
    # Stop execution if missing → fail fast (best practice)
    raise ValueError("Missing environment variables. Check your .env file.")
