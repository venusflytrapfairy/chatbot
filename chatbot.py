 #Create Function with Defined rules and responses
def simple_chatbot(user_input):
    rules = {
        'hello': 'Hi there! How can I help you?',
        'how are you': 'I am just a  program, but thanks for asking!',
        'bye': 'Goodbye! Have a great day!',
    }

    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if user input matches any rule
    for key, response in rules.items():
        if key in user_input:
            return response

    # If no match found, provide a default response
    return "I'm sorry, I didn't understand that."

# Simple chat interface
print("Simple Chatbot: Hello! Ask me anything or just chat with me. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print(f"Simple Chatbot: {response}")
