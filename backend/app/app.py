import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Function to get products from the database with optional price filter
def get_products_from_db(query, max_price=None):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()

    # If price range is specified, include it in the query
    if max_price:
        c.execute("SELECT * FROM products WHERE (name LIKE ? OR category LIKE ?) AND price <= ?", 
                  ('%' + query + '%', '%' + query + '%', max_price))
    else:
        c.execute("SELECT * FROM products WHERE name LIKE ? OR category LIKE ?", 
                  ('%' + query + '%', '%' + query + '%'))

    products = c.fetchall()
    conn.close()
    return products

# Format the response for multiple products
def format_product_response(products, query):
    if not products:
        return f"Sorry, no products found for your query: {query}."

    response_message = f"Here are some {query} that may interest you:\n"
    for product in products:
        response_message += f"- {product[1]} | Category: {product[2]} | Price: ₹{product[4]} | Stock: {product[5]}\n"
    
    return response_message

# Format the response for a single product
def format_single_product_response(product_name, product):
    response_message = f"Here is some information about {product_name}:\n"
    response_message += f"Product Name: {product[1]}\nCategory: {product[2]}\nDescription: {product[3]}\nPrice: ₹{product[4]}\nStock: {product[5]}\n"
    return response_message

# Handle login
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if username == "admin" and password == "password":
            return jsonify({"status": "success", "message": "Hello, welcome back! How can I help you today?"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Handle chat
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '').lower()

        # Handle greeting
        if "hello" in user_message or "hi" in user_message:
            return jsonify({"status": "success", "response": "Hello, welcome back! How can I help you today?"}), 200

        if "thanks" in user_message or "thankyou" in user_message:
            return jsonify({"status": "success", "response": "You are welcome!! Please feel free to ask any other queries!"}), 200

        # Handle "tell me about" queries
        if "tell me about" in user_message:
            product_name = user_message.replace("tell me about", "").strip()
            products = get_products_from_db(product_name)
            if products:
                response_message = format_single_product_response(product_name, products[0])
            else:
                response_message = f"Sorry, I couldn't find any products with the name {product_name}."
        
        # Handle price range queries (e.g., laptops under 100000)
        elif "under" in user_message:
            price_query_match = re.search(r"under (\d+)", user_message)
            if price_query_match:
                max_price = float(price_query_match.group(1))
                query = re.sub(r"under \d+", "", user_message).strip()  # Remove the price part
                products = get_products_from_db(query, max_price)
                response_message = format_product_response(products, query)
        
        # Handle product category searches (e.g., laptop, smartphone)
        else:
            categories = ["laptop", "smartphone", "mobile", "headphone", "tv", "tablet", "shirt", "pant", "gaming"]
            query_found = None
            for category in categories:
                if category in user_message:
                    query_found = category
                    break

            if query_found:
                products = get_products_from_db(query_found)
                response_message = format_product_response(products, query_found)
            else:
                # Handle direct product name search (e.g., "IQOO Neo 9 Pro")
                products = get_products_from_db(user_message)
                if products:
                    response_message = format_single_product_response(user_message, products[0])
                else:
                    response_message = "Sorry, I couldn't find any products with that name."

        return jsonify({"status": "success", "response": response_message}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

