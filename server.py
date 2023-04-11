import socket
import telebot
from telebot import types

Token = '5335248210:AAFkEFi4bVg9IOF728G6W6UoHgUynR9Hy8s'

funct = ['📁 файл', '🖥 система', '📶 приложения', '🔎 браузер', '🎥 снимок']
p = ''

bot = telebot.TeleBot(Token)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))

server.listen()


while True:
    user, data = server.accept()
    while True:
        @bot.message_handler(commands=['info'])
        def info(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("О нас"))
            bot.send_message(message.chat.id,
                             f'я уммею работать c:\n файлами,\n cистемой,\n приложениями,\n браузером,\nсфоткать ваш экран',
                             reply_markup=markup)


        @bot.message_handler(commands=['on'])
        def on(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in funct:
                markup.add(types.KeyboardButton(i))
            bot.send_message(message.chat.id, f'Бот включён', reply_markup=markup)


        @bot.message_handler(content_types=['text'])
        def file_work(message):
            if message.text == "О нас":
                bot.send_message(message.chat.id, f'я уммею работать: {p}')


        bot.polling(none_stop=True)





