from variables import ENCODING, MAX_PACKAGE_LENGTH
import json



def get_message(client):
	#Утилита приема и декодирования сообщения.
	#Принимает байты и выдает словарь, если принято что - то другое отдает ошибку значения
	encoded_response = client.recv(MAX_PACKAGE_LENGTH)
	if isinstance(encoded_response, bytes):
		json_response = encoded_response.decode(ENCODING)
		response = json.loads(json_response)
		if isinstance(response, dict):
			return response
		raise ValueError
	raise ValueError


def send_message(sock, message):
	#Утилита кодирования и отправки сообщения.
	#Принимает словарь и отправляет его.
	js_message = json.dumps(message)
	encoded_message = js_message.encode(ENCODING)
	sock.send(encoded_message)

