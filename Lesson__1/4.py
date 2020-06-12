# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
# представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_1 = ['разработка', 'администрирование', 'protocol', 'standard']
str_enc_1 = []

for elem in str_1:
	elem = str.encode(elem, encoding='utf-8')
	str_enc_1.append(elem)
print('строковое представление :')
print(type(str_enc_1), str_enc_1)


str_dec_1 = []

for elem in str_enc_1:
	elem = bytes.decode(elem, encoding='utf-8')
	str_dec_1.append(elem)

print('байтовое представление :')
print(type(str_dec_1), str_dec_1)






