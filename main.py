import socket
import telebot
import sys

bot = telebot.TeleBot(token='6135743605:AAEGkYbaBhL-oLfIut4U77ryETpetrVTgRo')
# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('127.0.0.1', 10000)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)
@bot.message_handler(commands=['start'])
def start(message):
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        # Принимаем данные порциями и ретранслируем их
        while True:
            data = connection.recv(16)
            print(f'Получено: {data.decode()}')
            if data.decode() == '123454536634':
                print('Обработка данных...')
                print('Отправка обратно клиенту{yes}')
                connection.sendall('123456'.encode())
            else:
                print('Нет данных от:', client_address)
                connection.sendall('Ошибка в доступе'.encode())
                break

    finally:
        # Очищаем соединение
        connection.close()

    bot.send_message(message.chat.id, 'popa')
bot.polling(none_stop=True)






