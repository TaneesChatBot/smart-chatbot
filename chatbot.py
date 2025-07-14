import random

# Memory for conversation
chat_history = []

# Common Q&A database
knowledge_base = {
    "what is your name": "I'm ChatBot, your super smart chatbot!",
    "who made you": "I was created by someone who loves coding and AI who is Tanees!",
    "what is python": "Python is a programming language used for many things like websites, games, and AI.",
    "how are you": "I'm just a bunch of code, but thanks for asking!",
    "who is the president of usa": "As of 2025, the President of the USA is Joe Biden.",
    "what's the capital of france": "The capital of France is Paris.",
    "what is ai": "AI stands for Artificial Intelligence. It's how computers can learn and make decisions like humans.",
    "hi": "Hello! How can I help you today?",
    "hello": "Hey there!",
    "bye": "Goodbye! Come back soon."
}

# Random fallback replies
fallback_replies = [
    "Hmm, I'm not sure how to answer that yet.",
    "Interesting! I’ll learn more about that soon.",
    "Can you ask in a different way?",
    "Let me think... maybe try asking something else."
]

def smart_chatbot():
    print("🤖 BrainBot: Hello! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()
        chat_history.append({"user": user_input})

        if user_input == "exit":
            print("🤖 BrainBot: Bye! Talk to you later.")
            break

        # Try to answer from knowledge base
        response = knowledge_base.get(user_input, None)

        # If not found, choose a fallback
        if not response:
            response = random.choice(fallback_replies)

        print(f"🤖 BrainBot: {response}")
        chat_history.append({"bot": response})

smart_chatbot()
