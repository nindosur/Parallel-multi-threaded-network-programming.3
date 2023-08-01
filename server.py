# SERVER
import json
import socket
import requests

    # 1
HOST = 'localhost'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('Сервер запущен, ожидает подключения....')

conn, addr = s.accept()
print(f'Собеседник {addr} подключен')

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f'Сообщение от собеседника: {data.decode()}')
    reply = input('Введите ответ сервера: ')
    conn.sendall(reply.encode())
conn.close()

    # 2, 3
weather_api = 'YOUR_API_KEY' # вставь свой api ключ

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

def run_server():
    host = 'localhost'
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f'Сервер запущен {host}:{port}.. Ожидаем подключения....')
        while True:
            try:
                conn, addr = s.accept()
                print(f'Получен запрос от {addr}')
                with conn:
                    data = conn.recv(1024)
                    if not data:
                        break
                    city = data.decode()
                    weather_data = get_weather(city)
                    if weather_data is not None:
                        message = f"Температура в городе {city}: {weather_data['main']['temp']} градусов"
                    else:
                        message = f"Не удалось получить данные для города {city}"
                    conn.sendall(message.encode())
            except:
                break

run_server()





