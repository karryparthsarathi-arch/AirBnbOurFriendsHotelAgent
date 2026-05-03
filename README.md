# AirBnbOurFriends Hotel AI Assistant

🚀 Built using Azure AI Foundry Agents with Retrieval-Augmented Generation (RAG) and Responsible AI guardrails.

## Project Overview
AirBnbOurFriends Hotel AI Assistant answers guest queries using ONLY approved knowledge documents such as:
- Hotel Policies
- Restaurant Menus
- Spa Services
- Local Area Guide
- FAQ

It ensures accurate, source-cited, and policy-driven responses without hallucination.

## Features
- Azure AI Foundry Agent integration
- Retrieval-grounded responses (RAG)
- Mandatory source citation
- Hotel policy prioritization
- Menu-first logic for food questions
- Friendly guest responses + safe fallback

## Setup

```bash
git clone https://github.com/your-username/airbnbourfriends-hotel-ai.git
cd airbnbourfriends-hotel-ai
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
az login
```

Create `.env` from `.env.example`:
```env
FOUNDRY_PROJECT_ENDPOINT=your-endpoint
FOUNDRY_AGENT_ID=your-agent-id
```

Run:
```bash
python src/main.py
```

## Project Structure
- src/ → Python agent code
- docs/ → Architecture & prompt design
- tests/ → Test scripts

## License
Free to use for learning and portfolio.

## Contact
karryparthsarathi@gmail.com
