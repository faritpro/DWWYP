import ctypes
import os
import struct
import subprocess
import webbrowser
import psutil
import pyautogui
import telebot
from telebot import types
import keyboard
import plyer



##################### Фунцци ######################

def messagee(text):
    plyer.notification.notify(message=text.split("ARG")[0],app_name='Название твоего приложения', title=text.split("ARG")[1])

# def voluem(text):
#     cur = Sound.current_volume()
#     if int(text) > 0:
#         Sound.volume_set(cur + int(text))
#     else:
#         Sound.volume_set(abs(cur - int(text)))

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

def changeBG(path):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 3)


def console(text):
    os.system(text)

def listproces(message):
    for proc in psutil.process_iter():
        bot.send_message(message.chat.id, f"{proc.name()}")

def closeprocec(text):
    for proc in psutil.process_iter():
        if proc.name() == text:
            proc.kill()
def openprocec(text):
    for rootdir, dirs, files in os.walk("D:\\"):
        for file in files:
            if file == text:
                subprocess.Popen(os.path.join(rootdir, file))
    for rootdir, dirs, files in os.walk("C:\\"):
        for file in files:
            if file == text:
                subprocess.Popen(os.path.join(rootdir, file))


def openbrow(text):
    webbrowser.open_new_tab(text)

def openask(text):
    webbrowser.open_new_tab(f'https://www.google.com/search?q={"+".join(text.split())}')

def openytube(text):
    webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={"+".join(text.split())}')

def scrinshoot():
    myScreenshot = pyautogui.screenshot()
    return myScreenshot

###################################################



try:
    with open('token.txt') as f:
        Token = f.read()
    f.close()
except FileNotFoundError:
    with open('token.txt', 'w') as y:
        Token = input(f'Введите токен от вашего теленрамм бота: ')
        y.write(Token)
    y.close()

bot = telebot.TeleBot(Token)
funct = ['📁 файл', '🖥 система', '📶 приложения', '🔎 браузер', '🎥 снимок']
lastmes = ''

@bot.message_handler(commands=['start'])
def info(message):
    bot.send_message(message.chat.id,
    f'Привет я бот для дистанционого управления твоего пк я умею:\n📁 файл, \n🖥 система, \n📶 приложения, \n🔎 браузер, \n🎥 снимок\nнажмите /on чтобы включить бота')

@bot.message_handler(commands=['on'])
def on(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in funct:
        markup.add(types.KeyboardButton(i))
    bot.send_message(message.chat.id, f'Бот включён', reply_markup=markup)


@bot.message_handler(content_types=['text', "photo"])
def file_work(message):
    global lastmes
    if message.text == "🎥 снимок":
        lastmes = "🎥 снимок"
        bot.send_photo(message.chat.id, scrinshoot())
    ####################система########################
    elif message.text == "🖥 система":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Работа с консолью"))
        markup.add(types.KeyboardButton("Измениние обоев"))
        markup.add(types.KeyboardButton("Изменение громкости"))
        markup.add(types.KeyboardButton("Высвечивание сообщения"))
        markup.add(types.KeyboardButton("Выключение пк"))
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, 'Режим Системы', reply_markup=markup)

    elif message.text == "Работа с консолью":
        bot.send_message(message.chat.id, 'Введите то что вы бы ввели в консоль:')
        lastmes = 31

    elif message.text == "Измениние обоев":
        bot.send_message(message.chat.id, 'Отправьте новые обои:')
        lastmes = 32

    elif message.text == "Изменение громкости":
        bot.send_message(message.chat.id, 'Введите на сколько хотите повысить громкость(в минус тоже можно):')
        lastmes = 33

    elif message.text == "Высвечивание сообщения":
        bot.send_message(message.chat.id, 'Введите что хотите высветить в формате(чтобудетнасианоARGзаголовок):')
        lastmes = 34

    elif message.text == "Выключение пк":
        os.system('shutdown -s -t 0')



    ####################приложение######################
    elif message.text == "📶 приложения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Список процессов"))
        markup.add(types.KeyboardButton("Завершить процесс"))
        markup.add(types.KeyboardButton("Открыть приложение"))
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, 'Режим Приложения', reply_markup=markup)

    elif message.text == "Список процессов":
        bot.send_message(message.chat.id, 'Начинается выполенение дождитесь до конца:')
        listproces(message)

    elif message.text == "Завершить процесс":
        bot.send_message(message.chat.id, 'Введите что хотите отключить формат(Навазане.exe):')
        lastmes = 21
    elif message.text == "Открыть приложение":
        bot.send_message(message.chat.id, 'Введите что хотите открыть формат(Навазане.exe):')
        lastmes = 22

    ################### Браузер ####################################
    elif message.text == '🔎 браузер':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Поиск по ссылке"))
        markup.add(types.KeyboardButton("Поиск в браузере"))
        markup.add(types.KeyboardButton("Поиск в ютубе"))
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, 'Режим Браузера', reply_markup=markup)

    elif message.text == "Поиск по ссылке":
        bot.send_message(message.chat.id, 'Введите ссылку:')
        lastmes = 11

    elif message.text == "Поиск в браузере":
        bot.send_message(message.chat.id, 'Введите что хотите найти:')
        lastmes = 12

    elif message.text == "Поиск в ютубе":
        bot.send_message(message.chat.id, 'Введите что хотите посмотреть:')
        lastmes = 13
    #############################################################
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in funct:
            markup.add(types.KeyboardButton(i))
        bot.send_message(message.chat.id, "Главное Меню", reply_markup=markup)
    else:
        if lastmes == 11:
            openbrow(message.text)
        elif lastmes == 12:
            openask(message.text)
        elif lastmes == 13:
            openytube(message.text)
        elif lastmes == 21:
            closeprocec(message.text)
        elif lastmes == 22:
            openprocec(message.text)
        elif lastmes == 31:
            console(message.text)
        elif lastmes == 32:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            download_file = bot.download_file(file_info.file_path)
            with open('1.png', 'wb') as f:
                f.write(download_file)
            changeBG("1.png")
        # elif lastmes == 33:
        #     voluem(message.text)
        elif lastmes == 34:
            messagee(message.text)


bot.polling(none_stop=True)

