import telebot

token = '8034349089:AAFeatj9ArvSBeKHX5yZVi04-9zqZsTL7qg'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def botmessage(message):
    mes = message.text + 'Мікроволновка'
    bot.send_message(message.chat.id, message.text)

bot.polling()