"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.
"""
list_byte = [b'class', b'function', b'method']

for i in list_byte:
    print(type(i))
    print(i)
    print(len(i))