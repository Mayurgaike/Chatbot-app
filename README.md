E-Commerce Chatbot AI

Introduction

The E-Commerce Chatbot AI is an innovative conversational assistant developed to simplify the online shopping experience. It allows users to search for products, inquire about details such as availability and pricing, and interact in a user-friendly chat interface. Built with a Flask backend, SQLite database, and a React frontend, this chatbot ensures seamless communication between the user and the product database.

Features

Product Search: Query products by name, category, or price range.

Interactive Chat Interface: Provides an engaging and intuitive user experience.

Secure Login System: Ensures only authorized users can access the chatbot.

Efficient Backend: Handles complex queries and retrieves accurate product data.

Prerequisites

Python (>=3.6)

Node.js (>=14)

SQLite

Setup Instructions

1. Clone the Repository

`git clone <your-git-repo-url>
cd ecommerce-chatbot-ai`

2. Backend Setup

For Windows

Navigate to the backend folder:

`cd backend`

Create a virtual environment and activate it:

`python -m venv venv
venv\Scripts\activate`

Install dependencies:

`pip install flask flask-cors`

Populate the database:

`python createDatabase.py`

Start the Flask server:

`python app.py`

For Linux

Navigate to the backend folder:

`cd backend`

Create a virtual environment and activate it:

`python3 -m venv venv
source venv/bin/activate`

Install dependencies:

`pip install flask flask-cors`

Populate the database:

`python3 createDatabase.py`

Start the Flask server:

`python3 app.py`

3. Frontend Setup

For Windows and Linux

Navigate to the frontend folder:

`cd ../frontend`

Install dependencies:

`npm install`

Start the React app:

`npm start`

4. Access the Application

Open a browser and navigate to http://localhost:3000 to interact with the chatbot.

How to Use

Login:

Enter the credentials:

`Username: admin`

`Password: password`

Upon successful login, you will be redirected to the chatbot interface.

Chatbot Interaction:

Type your queries in the chat window. Examples:

`"Show me laptops."`

`"Find smartphones under 20000."`

`"Hello" or "Thank you" for general interactions.`

Project Structure

Backend: Contains Flask app and database scripts.

Frontend: Contains React components for the chat interface.

Database: Includes `products.db` and `products.json` for storing product information.

Future Enhancements

Voice Commands: Enable users to interact via voice.

Multi-language Support: Provide responses in multiple languages.

Order Placement: Allow users to place orders directly through the chatbot.

User Feedback: Integrate a feedback system for continuous improvement.

Contribution

Feel free to contribute to this project by submitting issues or pull requests in the GitHub Repository.
