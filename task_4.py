"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

list_str = ["разработка", "администрирование", "protocol", "standard"]
list_uni = []
list_decode = []

for i in list_str:
    list_uni.append(i.encode('utf-8'))
print(list_uni)

for i in list_uni:
    list_decode.append(i.decode('utf-8'))

print(list_decode)
