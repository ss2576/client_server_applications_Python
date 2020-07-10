import json
import socket
import datetime
import sys
from my_project.settings.decorators import log

from my_project.settings.utils import get_message, send_message
from my_project.settings.variables import (ACCOUNT_NAME, ACTION, DEFAULT_PORT, ERROR, PRESENCE, RESPONSE,
										   TIME, DEFAULT_IP_ADDRESS, USER)


@log
def create_presence(accounte_name='Guest'):
	# Функция генерирует запрос о присутсвии клиента.
	time_now = datetime.datetime.now()
	time = str(time_now.strftime("%d-%m-%Y %H:%M %S"))
	action = 'message'
	message_client = input('Введите сообщение:')
	out = {
		ACTION: action,
		TIME: time,
		USER: {
			ACCOUNT_NAME: accounte_name,
			'message_text': message_client,
		}
	}
	return out


@log
def process_ans(message):
	#  Функция разбирает ответ сервера.
	if 'message_text' in message:
		if message['message_text'] is not None:
			text = message['message_text']
			return text
		return f'400 : {message[ERROR]}'
	raise ValueError


@log
def main():
	try:
		if '-a' in sys.argv:
			server_address = sys.argv[sys.argv.index('-a') + 1]
		else:
			server_address = DEFAULT_IP_ADDRESS
	except IndexError:
		print('После параметра \'a\' - необходимо указать адрес, который будет слушать сервер.')
		sys.exit(1)
	
	# Загружаем ,на какой порт обращаться.
	try:
		if '-p' in sys.argv:
			server_port = int(sys.argv[sys.argv.index('-p') + 1])
		else:
			server_port = DEFAULT_PORT
		if server_port < 1024 or server_port > 65535:
			raise ValueError
	except IndexError:
		print('После параметра \'p\' - необходимо указать номер порта.')
		sys.exit(1)
	except ValueError:
		print('В качестве порта может указано только число в диапазоне от 1024 до 65535')
		sys.exit(1)
	
	# Инициализация сокета и обмен
	transport = socket.socket()
	transport.connect((server_address, server_port))
	message_to_server = create_presence()
	send_message(transport, message_to_server)
	try:
		answer = process_ans(get_message(transport))
		print(f'Вы посылали сообщение: {answer}')
	
	
	except (ValueError, json.JSONDecodeError):
		print('Не удалось декодировать сообщение сервера.')
	
	return server_address, server_port


if __name__ == '__main__':
	main()
