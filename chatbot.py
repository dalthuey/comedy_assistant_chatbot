import os
import json
from utils import OpenAIChatbot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI chatbot
chatbot = OpenAIChatbot()

# Feedback storage
feedback_log = []

# CLI Main Function
def start_cli():
    """
    Command-line interface for the Comedy Assistant Chatbot.
    """
    print("\n🎭 Welcome to the Comedy Assistant Chatbot! 🤣")
    print("Ask me to generate jokes, punchlines, or even help with joke premises!")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\n🎤 Exiting Comedy Assistant Chatbot. Keep laughing!")
            break

        # Get the bot's response
        bot_response = chatbot.get_response(user_input)
        print(f"\nBot: {bot_response}\n")

        # Ask for feedback
        feedback = input("Was this response good? (>/~/< for good/neutral/bad): ").strip()

        # Process feedback
        if feedback == ">":
            feedback_log.append({"prompt": user_input, "response": bot_response, "feedback": "👍"})
            print("Thanks for your positive feedback!\n")
        elif feedback == "~":
            feedback_log.append({"prompt": user_input, "response": bot_response, "feedback": "🤷"})
            print("Thanks for your neutral feedback!\n")
        elif feedback == "<":
            feedback_log.append({"prompt": user_input, "response": bot_response, "feedback": "👎"})
            print("Thanks for your constructive feedback!\n")
        else:
            print("Invalid input. No feedback recorded.\n")

    # Save feedback to a file at the end of the session
    save_feedback()

def save_feedback():
    """
    Saves the feedback log to a JSON file for later analysis.
    """
    if feedback_log:
        feedback_file = "feedback_log.json"
        with open(feedback_file, "w") as file:
            json.dump(feedback_log, file, indent=4)
        print(f"📁 Feedback saved to {feedback_file}")
    else:
        print("No feedback to save. Goodbye!")

# Main Function
if __name__ == "__main__":
    print("🎭 Running Comedy Assistant Chatbot in CLI mode...")
    start_cli()
