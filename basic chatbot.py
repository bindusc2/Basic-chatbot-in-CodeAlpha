print("Chatbot: Hi, How can I help you?")
while True:
    user = input("You: ").lower()
    if user == "hi":
        print("Chatbot: Hello, How are you?")
    elif user == "how are you":
        print("Chatbot: I'm fine. How about you?")
    elif user == "i am fine":
        print("Chatbot: Great to hear!")
    elif user == "what is your name":
        print("Chatbot: I'm a simple Python chatbot.")
    elif user == "can you explain python topics in simple language":
        print("Chatbot: Do you want to learn from the basics?")
    elif user == "yes":
        print("Chatbot: Okay, I will explain Python topics in simple language.")
    elif user == "thank you":
        print("Chatbot: It's my pleasure!")
    elif user == "bye":
        print("Chatbot: Bye, have a nice day!")
        break

    else:
        print("Chatbot: Invalid input.")