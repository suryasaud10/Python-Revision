# Goal: Build a simple rule-based chatbot.
# Scope:
# ● Input from user like: "hello","how are you","bye".

# ● Predefined replies like: "Hi!","I'm fine, thanks!","Goodbye!"

# Key Concepts Used: if-elif, functions, loops, input/output.



def chatbot(user_input):
    user_input = user_input.strip().lower()
    
    if user_input == "hello":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    
    elif user_input == "bye":
        return "Goodbye!"
    
    else:
        return "I am sorry, I don't understand that."

def main():
    print("\nChatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You:").strip()
        response = chatbot(user_input)
        print("Chatbot: ", response)

        if user_input.strip().lower() == "bye":
            break

if __name__ == "__main__":
    main()
