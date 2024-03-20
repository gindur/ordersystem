import csv
import sys
import uuid



def load_from_csv(csv_file_path):
    orders = []
    company_name_to_id = {}
    customers = {}
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file,  delimiter=';')
            for row in csv_reader:
                if row['email_address'].startswith('_'):
                    row['email_address'] = row['email_address'][1:]
                row['products'] = parse_products(row['products'])
                create_customer(row, company_name_to_id, customers)
                orders.append(row)
    except OSError as e:
        print(f"Unable to open {csv_file_path}: {e}", file=sys.stderr)
        return
    return orders, customers, company_name_to_id

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

def create_customer(order_row, company_name_to_id, customers):
    company_id = None
    company_name: str = order_row['company_name']
    cn = company_name.strip().lower()
    if cn in company_name_to_id:
        company_id = company_name_to_id[cn]
    else:
        company_id = str(uuid.uuid4())
        company_name_to_id[cn] = company_id
        customers[company_id] = {
            'company_id' : company_id,
            'company_name' : company_name,
            'locations' : [],
            'contact_persons' : []
        }
    
    location_header = ['address', 'address2', 'zipcode', 'city', 'country']
    location = {label: order_row[label] for label in location_header}
    
    contact_header = ['email_address', 'firstname', 'lastname', 'phonenumber']
    contact = {label: order_row[label] for label in contact_header}
    
    if location not in customers[company_id]['locations']:
        customers[company_id]['locations'].append(location)
    if contact not in customers[company_id]['contact_persons']:
        customers[company_id]['contact_persons'].append(contact)

#creates ordertable and customers
def process_orders(csv_file_path: str):
    orders, customers, company_name_to_id = load_from_csv(csv_file_path)
    return orders, customers, company_name_to_id


