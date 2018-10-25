import os
import telegram
import polyglot
from telegram.ext import Updater
from polyglot.text import Text, Word
from dotenv import load_dotenv
from polyglot.downloader import downloader
downloader.download("sentiment2.ru")

import logging
load_dotenv()
bot = telegram.Bot(token=os.getenv("BOT_TOKEN"))
updater = Updater(token=os.getenv("BOT_TOKEN"))

dispatcher = updater.dispatcher
from telegram.ext import CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

set_message_handler = CommandHandler('set_message', start, pass_chat_data=True)
dispatcher.add_handler(set_message_handler)

def set_message(bot, update, chat_data):
    bot.send_message(chat_id=update.message.chat_id, text='р')
def echo(bot, update, chat_data):
    print(update)
    text = Text(update.message.text, hint_language_code="ru")

    # print("Polarity {0}\n".format(text.polarity))
    print("{:<16}{}".format("Word", "Polarity") + "\n" + "-" * 30)
    for w in text.words:
        print("{:<16}{:>2}".format(w, w.polarity))
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.all, echo, pass_chat_data=True)
dispatcher.add_handler(echo_handler)
updater.start_polling()
