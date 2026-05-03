import logging
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.agents.models import ListSortOrder
from config import FOUNDRY_PROJECT_ENDPOINT, FOUNDRY_AGENT_ID

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("airbnbourfriends-hotel-agent")

class AirBnbOurFriendsHotelAgent:

    def __init__(self):
        self.project = AIProjectClient(
            credential=DefaultAzureCredential(),
            endpoint=FOUNDRY_PROJECT_ENDPOINT
        )
        self.agent = self.project.agents.get_agent(FOUNDRY_AGENT_ID)

    def ask(self, question: str) -> str:
        if not question.strip():
            return "Please ask a valid question."

        thread = self.project.agents.threads.create()

        self.project.agents.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )

        run = self.project.agents.runs.create_and_process(
            thread_id=thread.id,
            agent_id=self.agent.id
        )

        if run.status == "failed":
            logger.error(f"Run failed: {run.last_error}")
            return "Sorry, the assistant could not process your request."

        messages = self.project.agents.messages.list(
            thread_id=thread.id,
            order=ListSortOrder.ASCENDING
        )

        for msg in messages:
            if msg.role == "assistant" and msg.text_messages:
                return msg.text_messages[-1].text.value

        return "No response found."
