from pyexpat.errors import messages
from xml.dom.pulldom import default_bufsize

import telebot
from telebot import types

token = '7864294774:AAEYz0ZHNY1WjH2Lu56ZwypjXNdWTRDuXbc'
bot = telebot.TeleBot(token)

# --------------------------------------------------------------------

@bot.message_handler(commands=['Qm','9w','g5','m4', 'b'])
def bot_comands(message):
    mes = ''
    if message.text == '/Qm':
        mes = 'кратор'
    elif message.text == '/9w':
        mes = 'банан'
    if message.text == '/g5':
        mes = 'ананас'
    elif message.text == '/m4':
        mes = 'Кактус'
    elif message.text == '/b':
        bot_buttons(message)
        return True

    bot.send_message(message.chat.id, mes)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    mes = message.text + ' - Мікроволновка'
    bot.send_message(message.chat.id, mes)



def bot_buttons(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text='1')
    button_2 = types.KeyboardButton(text='2')
    button_3 = types.KeyboardButton(text='3')
    button_4 = types.KeyboardButton(text='4')

    keyboard.add(button_1, button_2, button_3, button_4)

    msg = bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    bot.register_next_step_handler(msg, button_if)


def button_if(message):
    if message.text == '1':
        bot.send_message(message.chat.id, '1. закопати путіна ')
    elif message.text == '2':
        bot.send_message(message.chat.id, '2. закопати шойгу ')
    else:
        bot.send_message(message.chat.id, '3,4. запустити русоріз ')


if __name__ == '__main__':
    bot.polling()