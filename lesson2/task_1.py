"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data(), а также
сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv().
"""
import re
import csv


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for i in range(1, 4):
        with open(f'info_{i}.txt') as f:
            data = f.read()
            os_product = re.compile(r'Изготовитель системы:\s*\S*').findall(data)[0].split()[2]
            os_prod_list.append(os_product)

            os_name = re.compile(r'Название ОС:\s*\S*').findall(data)[0].split()[2]
            os_name_list.append(os_name)

            os_code = re.compile(r'Код продукта:\s*\S*').findall(data)[0].split()[2]
            os_code_list.append(os_code)

            os_type = re.compile(r'Тип системы:\s*\S*').findall(data)[0].split()[2]
            os_type_list.append(os_type)

    columns = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]

    main_data = [columns]

    for i in range(1, 3):
        row = []
        row.append(os_prod_list[i])
        row.append(os_name_list[i])
        row.append(os_code_list[i])
        row.append(os_type_list[i])

        main_data.append(row)
    return main_data


def write_to_csv():
    data = get_data()

    with open('data.csv', 'w') as f:
        f_writer = csv.writer(f)
        for i in data:
            f_writer.writerow(i)


write_to_csv()
