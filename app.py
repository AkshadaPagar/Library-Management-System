from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from db import BOOKS_DB, MEMBERS_DB, save_data, load_data  # Import from db.py

# Initialize the Flask app and JWT manager
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'AkshadaPagar'
jwt = JWTManager(app)

# Load data at the start of the app
load_data()

# Welcome Route
@app.route('/')
def welcome():
    return jsonify({"message": "Welcome to the Library Management System!"}), 200

# Authentication Route - Login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username == 'admin' and password == 'password':  # Simple hardcoded credentials
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Book Routes
@app.route('/api/books', methods=['POST'])
@jwt_required()
def create_book():
    current_user = get_jwt_identity()
    data = request.get_json()
    book = {
        "book_id": len(BOOKS_DB) + 1,
        "title": data['title'],
        "author": data['author'],
        "genre": data['genre'],
        "published_date": data['published_date']
    }
    BOOKS_DB[book['book_id']] = book
    save_data()  # Save data after adding a new book
    return jsonify(book), 201

@app.route('/api/books', methods=['GET'])
@jwt_required()
def list_books():
    current_user = get_jwt_identity()
    title = request.args.get('title')
    author = request.args.get('author')
    books = list(BOOKS_DB.values())
    
    # Optional filtering
    if title:
        books = [book for book in books if title.lower() in book['title'].lower()]
    if author:
        books = [book for book in books if author.lower() in book['author'].lower()]

    return jsonify(books), 200

# More routes...
