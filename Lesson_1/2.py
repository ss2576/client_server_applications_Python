# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
# в последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

str_byte_1 = [b'class', b'function', b'method']

for elem in str_byte_1:
	print(type(elem), elem, len(elem))