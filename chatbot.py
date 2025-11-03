print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hey there! How can I help you?")
    elif "how are you" in user_input:
        print("Chatbot: I'm just code, but I’m doing great! What about you?")
    elif "your name" in user_input:
        print("Chatbot: I'm a simple chatbot built with if-else logic.")
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        print("Chatbot:", now.strftime("It's %H:%M right now."))
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day.")
        break
    else:
        print("Chatbot: Sorry, I don’t understand that yet.")