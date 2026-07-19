import sys

RESPONSES = {
    "hello": "Hello there! How can I help you today?",
    "hi": "Hi! Good to see you.",
    "hey": "Hey! What's up?",
    "how are you": "I'm just a program, but I'm running smoothly. Thanks for asking!",
    "what is your name": "I'm a simple rule-based chatbot built for Project 1.",
    "who made you": "I was built as part of the DecodeLabs Industrial Training Kit.",
    "what can you do": "I can respond to greetings and a few basic questions using if-else logic.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}

EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}

FALLBACK_RESPONSE = "I do not understand. Could you rephrase that?"


def sanitize_input(raw_text: str) -> str:
    text = raw_text.strip()
    text = text.lower()
    return text


def get_response(user_input: str) -> str:
    if user_input in EXIT_COMMANDS:
        return "__EXIT__"

    if user_input == "":
        return "Please type something so I can respond."

    if user_input in RESPONSES:
        return RESPONSES[user_input]

    return FALLBACK_RESPONSE


def run_chatbot() -> None:
    print("=" * 50)
    print(" Rule-Based Chatbot (Project 1 - Logic Engine)")
    print(" Type 'hello', ask a simple question, or type")
    print(" 'exit' / 'quit' / 'bye' to end the conversation.")
    print("=" * 50)

    while True:
        raw_input_text = input("You: ")
        cleaned_input = sanitize_input(raw_input_text)
        reply = get_response(cleaned_input)

        if reply == "__EXIT__":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print(f"Bot: {reply}")


if __name__ == "__main__":
    try:
        run_chatbot()
    except KeyboardInterrupt:
        print("\nBot: Session interrupted. Goodbye!")
        sys.exit(0)