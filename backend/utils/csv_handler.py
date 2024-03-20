import csv
import os
import sys
from pathlib import Path


def load_from_csv(csv_file_path):
    orders = []
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file,  delimiter=';')
            for row in csv_reader:
                if row['email_address'].startswith('_'):
                    row['email_address'] = row['email_address'][1:]
                orders.append(row)
    except OSError as e:
        print(f"Unable to open {csv_file_path}: {e}", file=sys.stderr)
        return
    return orders

def parse_products(products_str):
    products = []
    for product_str in products_str.split('%NN%'):
        attr = product_str.split('#=#')
        product = {
            'sku': attr[0],
            'price': attr[1],
            'qty': attr[2],
            'total_price': attr[3],
            'desc': attr[4]
        }
        products.append(product)
    return products


def process_orders(csv_file_path):
    orders = load_from_csv(csv_file_path)
    for order in orders:
        order['products'] = parse_products(order['products'])
    return orders

