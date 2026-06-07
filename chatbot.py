print("🤖 Welcome to DecodeLabs AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Asking bot name
    elif "your name" in user:
        print("Bot: My name is DecodeBot.")

    # Asking about AI
    elif "what is ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    # Asking about python
    elif "python" in user:
        print("Bot: Python is a popular programming language for AI.")

    # Asking how are you
    elif "how are you" in user:
        print("Bot: I am fine. Thanks for asking!")

    # Asking college
    elif "college" in user:
        print("Bot: I help students learn AI projects.")

    # Motivation
    elif "motivate me" in user:
        print("Bot: Believe in yourself. Keep learning and growing!")

    # Exit
    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")