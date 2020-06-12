# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

# file_new = open('test_file.txt', 'w', encoding='cp1251')
file_new = open('test_file.txt', 'w', encoding='utf-8')
lst = ['сетевое  программирование', 'сокет', 'декоратор']
for elem in lst:
	file_new.write(elem + '\n')

file_new.close()
print(file_new)

# явное указание кодировки при работе с файлом
# with open('test_file.txt', encoding='cp1251') as file_new:
with open('test_file.txt', encoding='utf-8') as file_new:
	for elem in file_new:
		print(elem, end='')
