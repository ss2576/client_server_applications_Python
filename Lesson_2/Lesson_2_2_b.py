import os
import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open(os.path.join(os.getcwd(), 'orders.json'), 'r',
              encoding='utf-8') as f_out:
        data_json = json.load(f_out)

    with open(os.path.join(os.getcwd(), 'orders.json'), 'w',
              encoding='utf-8') as f_in:
        order = {
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date,
        }

        data_json['orders'].append(order)
        json.dump(data_json, f_in, indent=4)


write_order_to_json('Jack', '6', '1333 Rub', 'book_3', '2020-07-14')
