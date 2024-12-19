import sqlite3
import json

def create_db_from_json():
    # Load product data from the JSON file
    with open('products.json', 'r') as file:
        products = json.load(file)

    # Connect to SQLite database
    conn = sqlite3.connect('products.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        description TEXT,
        price REAL,
        stock INTEGER
    )''')

    # Insert products into the database
    for product in products:
        c.execute('''INSERT INTO products (name, category, description, price, stock)
                    VALUES (?, ?, ?, ?, ?)''',
                    (product['name'], product['category'], product['description'], product['price'], product['stock']))

    conn.commit()
    conn.close()

create_db_from_json()
