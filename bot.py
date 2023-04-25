import telebot

Token = '6135743605:AAEGkYbaBhL-oLfIut4U77ryETpetrVTgRo'
bot = telebot.TeleBot(Token)
funct = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
    f'Привет я бот для дистанционого управления твоего пк, для начало скачайте файл, для получение большой информации /info, инструкция по устновоке /inct')
    bot.send_document(message.chat.id, open('program.py', 'rb'))


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, f'Это телеграмм бот, созданный для дистанционным управлением твоим пк.Бот сделан учеников яндекс лицея Пермяковым Артемием. Бот умеет:')

@bot.message_handler(commands=['inct'])
def inct(message):
    bot.send_message(message.chat.id, f'1:Скачайте файл\n2:Запустите его\n3:Создайте телеграмм бота и введите токен в программу\n')

@bot.message_handler(commands=['commands'])
def com(message):
    bot.send_message(message.chat.id, f'/start, \n/info, \n/inct')

bot.polling(none_stop=True)

