print("Chatbot: Hi, How can I help you?")
while True:
    user = input
    if user == "hi":
        print("Chatbot: Hello, How are you?")
    elif user == "how are you":
        print("Chatbot: I'm fine. How about you?")
    elif user == "i am fine":
        print("Chatbot: Great to hear!")
    elif user == "what is your name":
        print("Chatbot: I'm a simple Python chatbot")
    elif user == "can you explain python topics in simple language":
        print("Chatbot: Do you want to start from the basics?")
    elif user == "yes":
        print("Chatbot: Okay, I will prepare simple Python topics for you.")
    elif user == "bye":
        print("Chatbot: Okay, bye. Have a nice day.")
        break
    else:
        print("Chatbot: Sorry, I don't understand that.")