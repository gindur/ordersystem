CREATE TABLE customers(
    customer_id     TEXT DEFAULT lower(hex(randomblob(16)))
    company_name    TEXT,
    first_name      TEXT,
    last_name       TEXT,
    country         TEXT DEFAULT 'Sweden',
    phone_nbr       TEXT,
    email           TEXT
    PRIMARY KEY(customer_id)
)

CREATE TABLE orders(
    order_id        TEXT,
    address    TEXT,
    city    TEXT,
    zip_code    TEXT,
    payment_method      TEXT,
    customer_id     TEXT,
    date_created    DATETIME,
    date_paid       DATETIME,
    date_shipped    DATETIME,
    PRIMARY KEY(order_id),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)

CREATE TABLE products(
    sku     TEXT,
    desc     TEXT,
    price   REAL,
    size    TEXT,


)