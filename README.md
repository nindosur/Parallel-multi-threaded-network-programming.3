### Задание 1
Реализуйте клиент — серверное приложение, позволяющее обмениваться сообщениями в формате один к 
одному. Для начала общения необходимо установить 
соединение. После соединение используется текстовый 
формат. В беседе участвуют только два человека. После 
завершения беседы сервер переходит к ожиданию нового 
участника разговора.
### Задание 2
Реализуйте погодное клиент-серверное приложение. 
Клиент обращается к серверу с указанием: страны и города. Сервер, получив запрос, возвращает погоду на неделю 
для данной местности. Используйте для реализации приложения механизмы многопоточности. Данные о погоде 
должны быть предопределенными и взяты из файла.
### Задание 3
Измените задание номер 2. Добавьте получение прогноза погоды из внешнего источника.

Дляэтоговоспользуйтесь сайтом https://openweathermap.
org. Для начала нужно зарегистрироваться на сайте по 
ссылке https://home.openweathermap.org/users/sign_up 
и получить ключ для дальнейшей работы. На странице 
https://openweathermap.org/current есть подробная документация как работать с API. Теперь после запроса от 
клиента необходимо получать данные о погоде с этого 
источника. Полученный результат возвращать клиенту.
