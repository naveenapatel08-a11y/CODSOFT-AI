print("===== Welcome to Simple Chatbot =====")
print("Type 'bye' to exit the chatbot")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I am doing well. How about you?")

    elif user_input == "what is your name":
        print("Bot: I am a simple rule-based chatbot.")

    elif user_input == "help":
        print("Bot: I can answer simple questions.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I did not understand that.")