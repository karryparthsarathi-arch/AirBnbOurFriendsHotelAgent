# -------------------- IMPORTS --------------------

# Used for logging application behavior (debug/info/errors)
import logging  

# Azure authentication (auto-detects credentials from CLI, VS Code, Managed Identity)
from azure.identity import DefaultAzureCredential  

# Main client to interact with Azure AI Foundry (agents, threads, runs)
from azure.ai.projects import AIProjectClient  

# Used to control ordering of messages when retrieving chat history
from azure.ai.agents.models import ListSortOrder  

# Import environment configuration (endpoint + agent ID)
from config import FOUNDRY_PROJECT_ENDPOINT, FOUNDRY_AGENT_ID  


# -------------------- LOGGING SETUP --------------------

# Configure logging level (INFO = normal execution logs)
logging.basicConfig(level=logging.INFO)

# Create a named logger for this module
logger = logging.getLogger("airbnbourfriends-hotel-agent")


# -------------------- AGENT CLASS --------------------

class AirBnbOurFriendsHotelAgent:

    def __init__(self):
        """
        Constructor: Initializes connection to Azure AI Foundry
        and loads the specific agent.
        """

        # Create client to interact with Azure AI Foundry Project
        self.project = AIProjectClient(
            credential=DefaultAzureCredential(),  # Handles authentication securely
            endpoint=FOUNDRY_PROJECT_ENDPOINT     # Project endpoint
        )

        # Fetch the specific AI agent using Agent ID
        self.agent = self.project.agents.get_agent(FOUNDRY_AGENT_ID)


    def ask(self, question: str) -> str:
        """
        Main method to send a question to the AI agent
        and retrieve a response.
        """

        # -------- Input Validation --------
        if not question.strip():
            return "Please ask a valid question."

        # -------- Step 1: Create Thread --------
        # Thread = conversation session
        thread = self.project.agents.threads.create()

        # -------- Step 2: Add User Message --------
        self.project.agents.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )

        # -------- Step 3: Execute Agent --------
        # Runs the AI agent (LLM + retrieval + prompt rules)
        run = self.project.agents.runs.create_and_process(
            thread_id=thread.id,
            agent_id=self.agent.id
        )

        # -------- Step 4: Error Handling --------
        if run.status == "failed":
            logger.error(f"Run failed: {run.last_error}")
            return "Sorry, the assistant could not process your request."

        # -------- Step 5: Retrieve Messages --------
        messages = self.project.agents.messages.list(
            thread_id=thread.id,
            order=ListSortOrder.ASCENDING
        )

        # -------- Step 6: Extract Assistant Response --------
        for msg in messages:
            if msg.role == "assistant" and msg.text_messages:
                return msg.text_messages[-1].text.value

        # -------- Step 7: Fallback --------
        return "No response found."
