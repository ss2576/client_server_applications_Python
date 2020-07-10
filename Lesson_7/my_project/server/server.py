import json
import socket
import sys
from select import select
import select

from my_project.settings.utils import get_message, send_message
from my_project.settings.variables import (ACCOUNT_NAME, ACTION, DEFAULT_PORT,
										   ERROR, MAX_CONNECTIONS, PRESENCE,
										   RESPONSE_DEFAULT_IP_ADDRESS, RESPONSE,
										   TIME, USER)
# from my_project.log.server_log_config import logger
from my_project.settings.decorators import log


@log
def process_client_message(message):
	if (ACTION in message and
			message[ACTION] == 'message' and
			TIME in message and
			USER in message and
			message[USER][ACCOUNT_NAME] == 'Guest'):
		text = {'message_text': message[USER]['message_text']}
		return text
	return {RESPONSE_DEFAULT_IP_ADDRESS: 400, ERROR: 'Bad Request.'}


@log
def main():
	# Загружаем какой адрес слушать.
	try:
		if '-a' in sys.argv:
			listen_address = sys.argv[sys.argv.index('-a') + 1]
		else:
			listen_address = ''
	except IndexError:
		print('После параметра \'a\' - необходимо указать адресб который будет слушать сервер.')
		sys.exit(1)
	
	# Загружаем ,на какой порт обращаться.
	try:
		if '-p' in sys.argv:
			listen_port = int(sys.argv[sys.argv.index('-p') + 1])
		else:
			listen_port = DEFAULT_PORT
		if listen_port < 1024 or listen_port > 65535:
			raise ValueError
	except IndexError:
		print('После параметра \'p\' - необходимо указать номер порта.')
		sys.exit(1)
	except ValueError:
		print('В качестве порта может указано толко число в диапазоне от 1024 до 65535')
		sys.exit(1)
	
	# Готовим сокет.
	transport = socket.socket()
	transport.bind((listen_address, listen_port))
	# список клиентов , очередь сообщений
	clients = []
	messages = []
	# Слушаем порт.
	transport.listen(MAX_CONNECTIONS)
	
	while True:
		#client, client_address = transport.accept()
		try:
			client, client_address = transport.accept()
			# message_from_client = get_message(client)
			# response = process_client_message(message_from_client)
			# send_message(client, response)
			# client.close()
		except OSError:
			pass
		else:
			clients.append(client)
		
		recv_data_lst = []
		send_data_lst = []
		err_lst = []
		# Проверяем на наличие ждущих клиентов
		try:
			if clients:
				recv_data_lst, send_data_lst, err_lst = select.select(clients, clients, [], 0)
		except OSError:
			pass
		
		# принимаем сообщения и если там есть сообщения,
		# кладём в словарь,если ошибка ,исключаем клиента.
		if recv_data_lst:
			for client_with_message in recv_data_lst:
				try:
					process_client_message(get_message(client_with_message),
										   messages, client_with_message)
				except:
					clients.remove(process_client_message)
					
		# Если есть сообщение для отправки ожидающие клиенты, отправляем им сообщение.
		message_from_client = get_message(client)
		response = process_client_message(message_from_client)
		# send_message(client, response)
		print(messages)
		print(send_data_lst)
		if messages and send_data_lst:


			del messages[0]
			for waiting_client in send_data_lst:
				try:
					send_message(waiting_client, message_from_client)
				except:
					clients.remove(waiting_client)


if __name__ == '__main__':
	main()
