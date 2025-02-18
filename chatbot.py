import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r"how are you ?", ["I'm doing great! How about you?", "I'm fine, thanks for asking!"]),
    (r"what is your name ?", ["I'm a chatbot. You can call me ChatBot!", "I'm ChatBot!"]),
    (r"can you help me ?", ["Of course! What do you need help with?", "Sure! How can I assist you?"]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!"]),
    (r"(.*)", ["I'm not sure how to respond to that.", "Can you rephrase your question?"]),
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
def start_chat():
    print("Hello! I'm ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run chatbot
if __name__ == "__main__":
    start_chat()
