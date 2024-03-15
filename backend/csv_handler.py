import csv


def load_from_csv(csv_file_path):
    orders = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file,  delimiter=';')
        for row in csv_reader:
            orders.append(row)
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


if __name__ == "__main__":
    csv_file_path = 'backend/orders.csv'
    orders = process_orders(csv_file_path)
    print(orders[100])


