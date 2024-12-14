import telebot

token = '7864294774:AAEYz0ZHNY1WjH2Lu56ZwypjXNdWTRDuXbc'
bot = telebot.TeleBot(token)

# Функція для обробки повідомлень
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.isdigit():

        with open('2.txt', 'a') as file:
            file.write(message.text + '\n')
        bot.send_message(message.chat.id, "Число збережено ")
    else:

        with open('1.txt', 'a') as file:
            file.write(message.text + '\n')
        bot.send_message(message.chat.id, "Текст збережено")

@bot.message_handler(commands=['read'])
def bot_comands(message):
        if message.text == '/read':
            with open ('1.txt', 'r') as file:
                content = file.read()
                bot.send_content



if __name__ == '__main__':
    bot.polling()