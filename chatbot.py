# Simple Rule-Based Chatbot

def get_response(user_input):
    user_input = user_input.lower()

    # Rules
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! 👋"
    
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! 😊"
    
    elif user_input in ["what is your name", "your name"]:
        return "I'm your Python chatbot 🤖"
    
    elif user_input in ["help"]:
        return "You can say: hello, how are you, bye"
    
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! 👋"
    
    else:
        return "Sorry, I don't understand that 😅"


def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit", "goodbye"]:
            break


# Run chatbot
chatbot()