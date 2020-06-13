
import telebot
import random
from datetime import datetime

TOKEN = "1200317552:AAHUqxtgQGMqOFy4L7F8GzadU_9nnByPJjw"

bot = telebot.TeleBot(TOKEN)

random.seed(datetime.now())

@bot.message_handler(commands=['start', 'help'])
def initiate_convo(message):
    user_callsign = "0" + str(random.randint(1,8))
    bot.reply_to(message, "Hello! My callsign is 09.\n" + "Your callsign is " + user_callsign + ".")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, "09, roger over.")

bot.polling()