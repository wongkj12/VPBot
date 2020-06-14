import random
from datetime import datetime
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import Updater 
import logging
import os
PORT = int(os.environ.get('PORT',5000))

user_callsign = "0" + str(random.randint(1,8))
#bot.reply_to(message, "Hello! My callsign is 09.\n" + "Your callsign is " + user_callsign + ".")

TOKEN = "1021846855:AAFrd221fhN-0sLJB5j_P-C4sm6wwvKmFAk"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#callback function
def start(update,context): #context refers to everything after '/' command
    user_callsign = "0" + str(random.randint(1,8))
    context.bot.send_message(chat_id=update.effective_chat.id, text=
        "Hullo! My callsign is 09.\n" + "Your callsign is " + user_callsign + ".")

def roger(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="09, roger over.")

#creating handlers

start_handler = CommandHandler('start',start) #handles /start command
roger_handler = MessageHandler(Filters.text & (~Filters.command), roger)


def main():
    updater = Updater(token = TOKEN, use_context = True) #fetches updates from Telegram
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roger_handler)

    #Starts the bot
    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=TOKEN)
    updater.bot.setWebhook('https://fast-brushlands-97835.herokuapp.com/' + TOKEN)

if __name__ == '__main__':
    main()

