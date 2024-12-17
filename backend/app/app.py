from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask application
app = Flask(_name_)
CORS(app)  # Enable Cross-Origin Resource Sharing for communication with the frontend

# Mock data for user credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

# Mock chatbot responses
CHATBOT_RESPONSES = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand. Can you rephrase that?",
}

@app.route('/api/login', methods=['POST'])
def login():
    """
    Handles user login.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate username and password
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return jsonify({"status": "success", "message": "Login successful"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handles chatbot responses.
    """
    try:
        data = request.json
        user_message = data.get('message', '').lower()

        # Respond based on predefined chatbot responses
        response = CHATBOT_RESPONSES.get(user_message, CHATBOT_RESPONSES["default"])

        return jsonify({"status": "success", "response": response}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if _name_ == '_main_':
    app.run(debug=True, port=5000)