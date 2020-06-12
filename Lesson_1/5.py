# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess
import chardet

command = input('введите команду для проверки (ping или tracert) :')
host = input('введите имя проверяемого хоста :')
args = [command, host]
PING = subprocess.Popen(args, stdout=subprocess.PIPE)

for elem in PING.stdout:
	# работаю с Windows OS
	result = chardet.detect(elem)
	data = elem.decode(result['encoding']).encode('utf-8')
	print(data.decode('utf-8'))

