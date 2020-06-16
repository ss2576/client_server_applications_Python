# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий
# выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
# формирующий новый «отчетный» файл в формате CSV. Для этого:

# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
# с данными, их открытие и считывание данных. В этой функции из считанных
# данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно
# получиться четыре списка — например, os_prod_list, os_name_list,
# os_code_list,# os_type_list. В этой же функции создать главный список для
# хранения данных# отчета — например, main_data — и поместить в него
# названия столбцов отчета# в виде списка: «Изготовитель системы»,
# «Название ОС», «Код продукта»,# «Тип системы». Значения
# для этих столбцов также оформить в виде списка и
# поместить в файл main_data (также для каждого файла);

# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import os
import csv
import re

# работаю в ОС Windowc
found_folder = 'C:/txt'
write_to_folder = 'C:/csv'
filename = 'result.csv'


def get_data():
    folder = os.scandir(found_folder)
    system_manufacturer = []
    os_name = []
    product_code = []
    type_system = []
    main_data = []

    info = {
        'Изготовитель системы': system_manufacturer,
        'Название ОС': os_name,
        'Код продукта': product_code,
        'Тип системы': type_system,
    }

    for found_file in folder:
        with open(found_file, 'r') as f_in:
            for read_string in f_in:
                match = re.search(r'([^:]*):\s*(.*)', read_string)
                if match and (match[1] in info.keys()):
                    info[match[1].strip()].append(match[2].strip())

    for elem in info.values():
        main_data.append(elem)
    main_data = [elem for elem in zip(*main_data)]
    main_data.insert(0, list(info.keys()))

    return main_data


def write_to_csv(filename):
    if not os.path.isdir(write_to_folder):
        os.makedirs(write_to_folder)

    data = get_data()
    with open(os.path.join(write_to_folder, filename),
              'w', encoding='cp1251') as f_out:
        f_n_writer = csv.writer(f_out, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(data)


write_to_csv(filename)
