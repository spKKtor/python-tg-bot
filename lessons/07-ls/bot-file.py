import telebot

token = '7864294774:AAEYz0ZHNY1WjH2Lu56ZwypjXNdWTRDuXbc'
bot = telebot.TeleBot(token)

@bot.massage_handler(comands=['file'])
def read_file(message):
    try:
        with open('bot.txt') as file:
            info = file.read()
    except FileNotFoundError:
        with open('bot.txt', 'w') as file:
            file.write('')

    bot.send_message(message.chat.id, info)

@bot.message_handler(content_types=['text'])
def read_file(message):
    with open('bot.txt', 'w') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'Бот працює!')




if __name__ == '__main__':
    bot.polling()