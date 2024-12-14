from pyexpat.errors import messages
from xml.dom.pulldom import default_bufsize

import telebot
from telebot import types


token = '7864294774:AAEYz0ZHNY1WjH2Lu56ZwypjXNdWTRDuXbc'
bot = telebot.TeleBot(token)

sticker = ['CAACAgIAAxkBAAICUWdK4A2wkHJzsNi9ktRbZ7hJtUzDAALzCwAC3dgoSc4NRMNGtLEONgQ']

# --------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def comands_start(message):
     bot.send_message(message.chat.id, 'Команда СТАРТ!')

@bot.message_handler(commands=['stop'])
def comands_stop(message):
     bot.send_message(message.chat.id, 'Команда СТОП!')


@bot.message_handler(commands=['open', 'close'])
def bot_comands(message):
    mes = ''
    if message.text == '/open':
        mes = 'Закрито'
    elif message.text == '/close':
        mes = 'Відкрито'
    # elif message.text == '/b':
    #     bot_buttons(message)
    #     return True

    bot.send_message(message.chat.id, mes)


@bot.message_handler(commands=['key'])
def key_go(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton(text='Кнопка 1')
    button2 = types.KeyboardButton(text='Кнопка 2')
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, 'Клавіатура', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Кнопка 1')
def handle_button_1(message):
    bot.send_message(message.chat.id, 'Ви натиснуликнопку 1')

@bot.message_handler(content_types=['sticker'])
def handle_stickers(message):
    sticker_id = message.sticker.file_id
    emoji = message.sticker.emoji

    bot.reply_to(message, f"Ви надіслали стікер з емоджі {emoji} (ID: {sticker_id})")



@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == '1':
        bot.send_sticker(message.chat.id, sticker[0])
        return True

    mes = message.text + ' - Мікроволновка'
    bot.send_message(message.chat.id, mes)


# ------------------------------------------------------------------------

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