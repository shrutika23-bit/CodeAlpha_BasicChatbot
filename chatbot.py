def chatbot():
    print("ChatBot: Hello! Welcome to my chatbot")
    print("ChatBot: Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "hello":
            print("ChatBot: Hi!")
        elif user_input == "what is your name":
            print("ChatBot: I am a python chatBot!")
        elif user_input == "thank you":
            print("ChatBot: You're welcome!")
        elif user_input == "help":
            print("ChatBot:You can say hello,ask how I am, or type bye to exit.")
        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks!")
        elif user_input == "bye":
            print("ChatBot:Goodbye!")
            break
        else:
            print("ChatBot: Sorry,I don't understand that.")
            
chatbot()