# Telegram Bot with OpenAI Integration

This repository contains a simple Telegram bot that integrates with the OpenAI API to provide NLP-based responses. It uses the OpenAI Playground API to generate responses based on user messages. The bot also includes a command to fetch and send random quotes from an external API.

# Requirements
* Python 3.6 or higher
* `telebot` library
* `requests` library
* `openai` library
* `python-dotenv` library

# Setup
1. Clone the repository:
```bash
git clone https://github.com/manish-bhusal/telegram-bot.git
```

2. Obtain the required API keys:
* Telegram Bot Token: Create a new Telegram bot and obtain the bot token. You can follow the official Telegram Bot documentation to create your bot and obtain the token.
* OpenAI API Key: Sign up for the OpenAI Playground API and obtain your API key.

3. Create a `.env` file in the root directory of the project and add the following variables:
```makefile
BOT_TOKEN=<your-telegram-bot-token>
OPENAI_API_KEY=<your-openai-api-key>
```

4. Start the bot:
```bash
python telegram_bot.py
```

# Usage
1. Start a conversation with your Telegram bot by sending a message to the bot in the Telegram app.

2. The bot will respond with a greeting message: "Hello, how are you?"

3. You can use the following commands to interact with the bot:

* `/start`: Get a welcome message from the bot.
* `/quote`: Get a random quote fetched from an external API.

4. For all other messages, the bot will use the OpenAI API to generate an NLP-based response.

# Output
[OpenAI-Telegram-Bot](https://github.com/manish-bhusal/telegram-openai-bot/assets/84217955/eb6c6df7-7088-4cae-9bcb-bc21ada84aff)

# Credits
This project was inspired by [OpenAI Playground](https://platform.openai.com/playground) and the [Quotable API.](https://github.com/lukePeavey/quotable)

