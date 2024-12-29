# Comedy Assistant Chatbot

Welcome to the **Comedy Assistant Chatbot**! This project leverages OpenAI's GPT-3.5-Turbo model to create an interactive chatbot that helps you generate jokes, punchlines, and humorous premises. Whether you need a laugh or help brainstorming witty lines, this bot has you covered.

---

## Features
- **Interactive CLI Chatbot**: Engage in real-time conversations with the bot.
- **Joke and Punchline Generator**: Provide a premise or topic, and the bot generates humorous responses.
- **Feedback Loop**: Rate the bot's responses as good (`>`), neutral (`~`), or bad (`<`) to log feedback.
- **Feedback Storage**: Saves feedback to a JSON file for analysis and improvement.

---

## Requirements

### Dependencies
Ensure the following Python libraries are installed in your environment:
- `openai`
- `python-dotenv`
- `json`
- `pipenv` (for environment management)

### Python Version
This project requires Python 3.13 or higher.

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/dalthueycomedy_assistant_chatbot.git
cd comedy_assistant_chatbot
```

### Install Dependencies
1. **Install Pipenv** (if not installed):
   ```bash
   pip install pipenv
   ```
2. **Install project dependencies**:
   ```bash
   pipenv install
   ```
3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

### Add Environment Variables
Create a `.env` file in the root directory with the following content (refer to .env.example for example usage):
```plaintext
OPENAI_API_KEY=your_openai_api_key
```

---

## Running the Chatbot

### Start the CLI Chatbot
1. Ensure you are in the virtual environment:
   ```bash
   pipenv shell
   ```
2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

### Example Interaction
```plaintext
🎭 Welcome to the Comedy Assistant Chatbot! 🤣
Ask me to generate jokes, punchlines, or even help with joke premises!
Type 'exit' or 'quit' to stop.

You: Tell me a joke about cats.
Bot: Why did the cat sit on the computer? To keep an eye on the mouse!

Was this response good? (>/~/< for good/neutral/bad): >
Thanks for your positive feedback!

You: exit
📁 Feedback saved to feedback_log.json
```

---

## Feedback Logging
All feedback is stored in a `feedback_log.json` file in the following format:
```json
[
    {
        "prompt": "Tell me a joke about cats.",
        "response": "Why did the cat sit on the computer? To keep an eye on the mouse!",
        "feedback": "👍"
    }
]
```

---

## Contributing
Feel free to submit issues or pull requests to improve this project. Contributions are always welcome!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [OpenAI](https://openai.com/) for their GPT model.
- The Python community for excellent tools like `pipenv` and `python-dotenv`.
