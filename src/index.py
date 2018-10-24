import telegram
bot = telegram.Bot(token='687822837:AAEkrCh6WmnIrTA_3mZuqkbY-U8gnCYnGMc')
from telegram.ext import Updater
updater = Updater(token='687822837:AAEkrCh6WmnIrTA_3mZuqkbY-U8gnCYnGMc')
import polyglot
from polyglot.text import Text, Word

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

set_message_handler = CommandHandler('set_message', start, pass_chat_data=True)
dispatcher.add_handler(set_message_handler)

def set_message(bot, update, chat_data):
    bot.send_message(chat_id=update.message.chat_id, text='р')
def echo(bot, update, chat_data):
    print(update)
    text = Text(update.message.text)
    print("Language Detected: Code={}, Name={}\n".format(text.language.code, text.language.name))
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.all, echo, pass_chat_data=True)
dispatcher.add_handler(echo_handler)
updater.start_polling()
