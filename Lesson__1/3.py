# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

str_byte_1 = [b'attribute', b'класс', b'функция', b'type']

# выводится ошибка
#    str_byte_1 = (b'attribute', b'класс', b'функция', b'type')
#                                ^
# SyntaxError: bytes can only contain ASCII literal characters.
# преобразовываться могут только знаки входящие в кодировку ASCII.
# а это только латинский шрифт!