import telebot
from constants import *
import hlparser

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "You can clear tickets by using /clear")


@bot.message_handler(commands=['clear'])
def clear(message):
    bot.send_message(message.chat.id, "Processing...")
    try:
        hlparser.close_tickets()
    except:
        print(BaseException)
    print("done")
    bot.send_message(message.chat.id, "Cleared!")


bot.polling()