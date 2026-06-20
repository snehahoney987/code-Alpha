print("Simple Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")
    elif user == "how are you":
        print("Bot: I am fine, thank you!")
    elif user == "what is your name":
        print("Bot: I am a simple chatbot.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")