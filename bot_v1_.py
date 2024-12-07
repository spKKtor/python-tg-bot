import telebot
from telebot import types
from urllib3 import request

from main import bot_message

token = '7864294774:AAEYz0ZHNY1WjH2Lu56ZwypjXNdWTRDuXbc'
bot = telebot.TeleBot(token)


# ---------------------------------------------------------------------

@bot.message_handler(content_types=['text'])
def bot_number(message):
    if message.text == '1':
        request = 'Один'
    elif message.text == '2':
        request = 'Два'
    elif message.text == '3':
        request = 'три'
    elif message.text == '4':
        request = 'чотири'
    elif message.text == '5':
        request = 'пять'
    else:
        request = 'Хз'


if __name__ == '__main__':
    bot.polling()
