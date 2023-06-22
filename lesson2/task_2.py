"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f:
        objs = json.load(f)
        orders = objs['orders']

    with open('orders.json', 'w', encoding='utf-8') as f:
        content_to_file = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders.append(content_to_file)
        json.dump(objs, f, indent=4, ensure_ascii=False)


write_order_to_json('Сервер', 10, 15, 'Sergeev S.', '25/11/1995')
write_order_to_json('Сервер', 100, 150, 'Ivanov', '25/11/2005')
