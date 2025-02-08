import config as c
import telebot
import threading
import time
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(c.BOT_TOKEN)

USER_CHAT_ID = '516876967'

# === SQLITE3 =================================================================
# db = sqlite3.connect(c.DB_NAME)
# cursor = db.cursor()
#
# cursor.execute('''CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     chat_id INTEGER NOT NULL UNIQUE,
#     name TEXT DEFAULT 'Невідомий',
#     deleted INTEGER DEFAULT 1
#     )''')
# db.commit()
#
# cursor.execute('''CREATE TABLE notes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     title TEXT NOT NULL,
#     content TEXT DEFAULT '',
#     notification DATETIME DEFAULT CURRENT_TIMESTAMP,
#     is_send INTEGER DEFAULT 0,
#     deleted INTEGER DEFAULT 1
#     )''')
# db.commit()


# === FUNCTIONS ===============================================================
def send_stupid_message():
    while True:

        # ....

        bot.send_message(USER_CHAT_ID, '')
        time.sleep(10)


def bot_start(message):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()

    cur.execute(f"SELECT chat_id FROM users WHERE chat_id='{message.chat.id}'")
    row = cur.fetchone()

    if not row:
        cur.execute(f"INSERT INTO users (chat_id, name) VALUES ('{message.chat.id}', '{message.from_user.username}')")
        db.commit()
        bot.send_message(message.chat.id, 'Вас додано до цього бота!')
    else:
        bot.send_message(message.chat.id, 'Ви вже підписані на цього бота.')


def add_note(message):
    bot.send_message(message.chat.id, "Введіть нотатку:")
    bot.register_next_step_handler_by_chat_id(message.chat.id, save_note)


def save_note(message):
    # 1 з можливих варіантів реалізації коду (4 з 10)
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
    row = cur.fetchone()

    if row:
        cur.execute("INSERT INTO notes (user_id, title) VALUES (?, ?)",
                    (row[0], message.text))
        db.commit()

        bot.send_message(message.chat.id, 'Нотатку збережено')

    cur.close()
    db.close()


def show_all_notes(message):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute("SELECT id FROM users WHERE chat_id='%d'" % message.chat.id)
    row = cur.fetchone()

    if row:
        cur.execute(f"SELECT id, title, notification FROM notes WHERE deleted=1 AND user_id={row[0]}")
        rows = cur.fetchall()

        notes = 'Список нотаток:\n\n'
        for r in rows:
            notes += f"/open_{r[0]}: {r[1]}. [{r[2]}]\n"

        bot.send_message(message.chat.id, notes)

    cur.close()
    db.close()

def open_note(message, note_id):
    keyboard = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('Нотатку', callback_data='/edit_' + note_id)
    b2 = InlineKeyboardButton('Час', callback_data='/time_' + note_id)
    b3 = InlineKeyboardButton('Видалити', callback_data='/delete_' + note_id)
    keyboard.add(b1, b2)
    keyboard.add(b3)

    bot.send_message(message.chat.id,f'[{note_id}] Редагувати:', reply_markup=keyboard)

def edit_note(message, note_id):
    pass

def time_note(message, note_id):
    pass

def delete_note(call, note_id):
    db = sqlite3.connect(c.DB_NAME)
    cur = db.cursor()
    cur.execute("UPDATE notes SET deleted='0' WHERE id=%d" % int( ))
    db.commit()

    if cur.rowcount > 0:
        bot.send_message(call.message.chat.id, 'Нотатка видалена!')
    else:
        bot.send_message(call.message.chat.id, ' :( ')

    cur.close()
    db.close()


# === HANDLER =================================================================

# start - підписка
# add - додати
# edit - редагувати
# delete - видалити
# all - показати всі
# day - показати за день
# end - відписатися

# Обробник команд від користувача
@bot.message_handler(commands=['start', 'add', 'all', 'day', 'end'])
def handler_commands(message):
    if '/start' == message.text:
        bot_start(message)
    elif '/add' == message.text:
        add_note(message)
    elif '/all' == message.text:
        show_all_notes(message)
    elif '/day' == message.text:
        pass
    elif '/end' == message.text:
        pass


@bot.message_handler(regexp=r"^\/open_\d+$")
def handler_open_id(message):
    values = message.text.split('_')
    open_note(message, values[1])


@bot.callback_query_handler(func=lambda call:True)
def handler_note_action(call):
    values = call.data.split('_')
    if 2 == len(values):
        if '/delete' == values[0]:
            delete_note(call, values[1])
        elif '/edit' == values[0]:
            edit_note(call, values[1])



# Обробник текстових повідомлень від користувача
@bot.message_handler(content_types=['text'])
def handler_text_message(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'БОТ Працює! )))' + str(message.chat.id))


if __name__ == "__main__":
    # thread = threading.Thread(target=send_stupid_message)
    # thread.start()
    # Запуск бота
    bot.infinity_polling()
