import telebot
from constants import *
import hlparser

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "You can clear tickets by using /clear")


@bot.message_handler(commands=['clear'])
def clear(message):
    try:
        bot.send_message(message.chat.id, "Processing...")
        hlparser.close_tickets()
    except:
        bot.send_message(message.chat.id, "Error, something went wrong.")
        print(BaseException)
    print("Done")
    bot.send_message(message.chat.id, "Cleared!")


bot.polling()