import telebot
import sqlite3

bot = telebot.TeleBot('5501237868:AAHjB8Wdl9y1E2guviA65JhK3lZTfsCjDkE')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Название группы?')

@bot.message_handler()
def get_user_text(message):
    db = sqlite3.connect('db/database.db')
    cursor = db.cursor()
    data = cursor.execute("SELECT link FROM groups WHERE name = ?", (message.text.upper(), )).fetchone()
    if data is None:
        bot.send_message(message.chat.id, 'Такой группы не существует')
    else:
        bot.send_message(message.chat.id, 'http://nmt.edu.ru/html/' + str(*data))

bot.polling(none_stop=True)