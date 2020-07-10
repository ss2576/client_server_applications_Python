import os
import subprocess

os.getcwd()
os.chdir('..')
os.chdir('client')
CLIENT = f'{os.getcwd()}\client.py'

os.getcwd()
os.chdir('..')
os.chdir('server')
SERVER = f'{os.getcwd()}\server.py'

DIR_SERVER = f'python {SERVER}'
DIR_CLIENT_SEND = f'python {CLIENT} -m send'
DIR_CLIENT_LISTEN = f'python {CLIENT} -m listen'
PROCESS =[]

while True:
	ACTION = input('Выбирете действие: q - выход,'
				   's - запустить сервер и клиенты, x - закрыть окна:')
	
	if ACTION == 'q':
		break
	elif ACTION == 's':
		PROCESS.append(subprocess.Popen(DIR_SERVER, creationflags=subprocess.CREATE_NEW_CONSOLE))
		for i in range(2):
			PROCESS.append(subprocess.Popen(DIR_CLIENT_SEND, creationflags=subprocess.CREATE_NEW_CONSOLE))
		for i in range(5):
			PROCESS.append(subprocess.Popen(DIR_CLIENT_LISTEN, creationflags=subprocess.CREATE_NEW_CONSOLE))
	elif ACTION == 'x':
		while PROCESS:
			VICTIM = PROCESS.pop()
			VICTIM.kill()
