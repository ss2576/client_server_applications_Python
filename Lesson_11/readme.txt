================ Параметры запуска ================
Параметры запуска server.py:
[-p port] - порт сервера (default=7777)
[-a addr] - адрес хоста (default='')

Параметры запуска client.py:
[addr] - адрес сервера (default='localhost')
[port] - порт сервера (default=7777)

Прим.:
[] - необязательный параеметр

================== Список команд ==================
Команды на сервере:
#get_users                              - получить список активных юзеров
#add_contact <username> <contactname>   - добавить для <username> <contactname> в список контактов
#rem_contact <username> <contactname>   - удалить у <username> <contactname> из списка контактов
#get_contacts <username>                - получить список контактов для <username>

Команды на клиенте:
команды выполняемые на сервере:
#get_users                              - получить списко активных юзеров
#add_contact <username>                 - добавить <username> в список контактов
#rem_contact <username>                 - удалить <username> из списка контактов
#get_contacts                           - получить список контактов

локальные команды клиента:
!help                                   - вывод небольшой help
!set_name                               - сменить имя
!reconnect                              - переподключиться к серверу
