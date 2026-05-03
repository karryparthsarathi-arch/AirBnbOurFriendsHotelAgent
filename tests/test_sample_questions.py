from src.hotel_agent_client import AirBnbOurFriendsHotelAgent

def test_basic_response():
    agent = AirBnbOurFriendsHotelAgent()
    resp = agent.ask("What time is check-in?")
    assert isinstance(resp, str)
