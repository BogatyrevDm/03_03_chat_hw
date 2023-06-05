"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

list_byte = ['attribute', 'класс', 'функция', 'type']
for i in list_byte:
    try:
        bytes(i, 'ascii')
    except UnicodeEncodeError:
        print(f'You can\'t encode word {i} into bytes!')
