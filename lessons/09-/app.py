import config
import telebot
import threading
import time
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

USER_CHAT_ID = '910533962'

db = sqlite3.connect('notebook.db')
cursor = db.cursor()

cursor.execute(''' CREATE TABLE user (
    ida INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    name TEXT DEFAULT 'Unknow',
    email TEXT DEFAULT '',
    role INTEGER DEAFULT 0,
    deleted INTEGER DEAFULT 1
    )''')
db.commit()
#------------------------------------------------------------
def send_stupid_message():
    while True:
        bot.send_message(USER_CHAT_ID, 'Дурне повідослення')
        time.sleep(10)

#============================================================
@bot.message_handler(content_types=['text'])
def handler_text_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Бот працює')


if __name__=="__main__":
    thread = threading.Thread(target=send_stupid_message)
    thread.start()
    bot.infinity_polling()