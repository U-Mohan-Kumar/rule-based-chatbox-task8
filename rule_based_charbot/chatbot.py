"""
ChatBot: Rule-Based CLI Chatbot
Author: U. Mohan Kumar
Description: A simple chatbot using if-elif-else logic to simulate conversation.
"""

import datetime

def get_response(user_input: str) -> str:
    """
    Returns chatbot response based on user input.
    Uses keyword matching and control flow.
    """
    user_input = user_input.lower()

    if user_input == "exit":
        return "Goodbye! 👋"
    elif "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I assist you today?"
    elif "your name" in user_input:
        return "I'm ChatBot, your Python-powered assistant."
    elif "how are you" in user_input:
        return "I'm just a script, but I'm running smoothly!"
    elif "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "date" in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"
    elif "bye" in user_input:
        return "See you soon! 👋"
    else:
        return "I'm not sure how to respond to that. Try asking something else."

def main():
    """
    Main loop for chatbot interaction.
    Handles input, output, and graceful exit.
    """
    print("🤖 Hello! I'm ChatBot. Type 'exit' to end the chat.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            response = get_response(user_input)
            print(f"ChatBot: {response}")
            if user_input.lower() == "exit":
                break
        except KeyboardInterrupt:
            print("\nChatBot: Interrupted. Goodbye! 👋")
            break
        except Exception as e:
            print(f"ChatBot: Oops! An error occurred: {e}")

if __name__ == "__main__":
    main()