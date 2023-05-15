import os
import requests
import openai
import telebot
from dotenv import load_dotenv

load_dotenv()

# Load the Telegram bot token from the environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create a new Telegram bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Set up the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Handler for the '/start' command
    bot.reply_to(message, "Hello, how are you?")


@bot.message_handler(commands=['quote'])
def send_quote(message):
    # Handler for the '/quote' command
    quote = get_random_quote()
    bot.reply_to(message, quote)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # Handler for all other messages
    response = generate_response(message.text)
    bot.reply_to(message, response)


def get_random_quote():
    # Fetch a random quote from an API
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
        return f"{quote}\n- {author}"
    return "Failed to fetch a quote. Please try again later"


def generate_response(prompt):
    # Generate an NLP response using the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()


# Start the bot's infinite polling loop
bot.infinity_polling()
