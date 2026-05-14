import datetime

def chatbot():
    print("🤖 ChatBot: Hello! I am your simple AI chatbot.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["exit", "quit", "bye"]:
            print("🤖 ChatBot: Goodbye! Have a great day 😊")
            break

        elif any(word in user_input for word in ["hi", "hello", "hey"]):
            print("🤖 ChatBot: Hello! How can I help you?")

        elif any(phrase in user_input for phrase in ["your name", "who are you", "name"]):
            print("🤖 ChatBot: I am a rule-based chatbot created using Python.")

        elif "ai" in user_input:
            print("🤖 ChatBot: AI stands for Artificial Intelligence.")

        elif any(word in user_input for word in ["study", "exam"]):
            print("🤖 ChatBot: Stay consistent and keep learning!")

        elif "weather" in user_input:
            print("🤖 ChatBot: I can't check live weather, but hope it's nice outside!")

        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print("🤖 ChatBot: Current time is", now)

        elif "date" in user_input:
            today = datetime.date.today()
            print("🤖 ChatBot: Today's date is", today)

        elif "help" in user_input:
            print("🤖 ChatBot: You can ask me about AI, time, date, studies, or weather.")

        elif "joke" in user_input:
            print("🤖 ChatBot: Why did the computer go to the doctor? Because it had a virus 😄")

        else:
            print("🤖 ChatBot: Sorry, I don't understand that yet.")

if __name__ == "__main__":
    chatbot()