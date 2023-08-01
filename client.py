# CLIENT

import socket

    # 1
HOST = 'localhost'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Подключено к серверу!')

while True:
    message = input('Введите сообщение: ')
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f'Сообщение от сервера: {data.decode()}')
    if not data:
        break
s.close()

    # 2, 3
def run_client():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print('Клиент запущен')
        while True:
            city = input('Введите название города (или выход для завершения): ')
            if city == 'выход':
                break
            s.sendall(city.encode())
            data = s.recv(1024)
            print(data.decode())

run_client()