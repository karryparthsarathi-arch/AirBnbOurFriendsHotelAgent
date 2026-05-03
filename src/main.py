from hotel_agent_client import AirBnbOurFriendsHotelAgent

def main():
    agent = AirBnbOurFriendsHotelAgent()

    print("\n🏨 AirBnbOurFriends Hotel AI Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Guest: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = agent.ask(user_input)
        print(f"\nAssistant: {response}\n")

if __name__ == "__main__":
    main()
