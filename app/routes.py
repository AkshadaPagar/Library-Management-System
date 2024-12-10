from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from app.db import BOOKS_DB, MEMBERS_DB, save_data  # Assuming you have a db.py for persistent storage

# Initialize the Flask app and JWT manager
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'AkshadaPagar'
jwt = JWTManager(app)

# In-memory data (simulating a database)
BOOKS_DB = {
    1: {"title": "1984", "author": "George Orwell"},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    # Add more books here...
}

MEMBERS_DB = {
    1: {"name": "John Doe", "email": "johndoe@example.com"},
    2: {"name": "Jane Smith", "email": "janesmith@example.com"},
    # Add more members here...
}

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
    save_data()
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

@app.route('/api/books/<int:book_id>', methods=['GET'])
@jwt_required()
def get_book(book_id):
    current_user = get_jwt_identity()
    book = BOOKS_DB.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    return jsonify(book), 200

@app.route('/api/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    current_user = get_jwt_identity()
    book = BOOKS_DB.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    data = request.get_json()
    book.update(data)
    save_data()
    return jsonify(book), 200

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    current_user = get_jwt_identity()
    book = BOOKS_DB.pop(book_id, None)
    if not book:
        return jsonify({"message": "Book not found"}), 404
    save_data()
    return jsonify({"message": "Book deleted"}), 200

# Member Routes
@app.route('/api/members', methods=['POST'])
@jwt_required()
def create_member():
    current_user = get_jwt_identity()
    data = request.get_json()
    member = {
        "member_id": len(MEMBERS_DB) + 1,
        "name": data['name'],
        "email": data['email']
    }
    MEMBERS_DB[member['member_id']] = member
    save_data()
    return jsonify(member), 201

@app.route('/api/members', methods=['GET'])
@jwt_required()
def list_members():
    current_user = get_jwt_identity()
    return jsonify([member for member in MEMBERS_DB.values()]), 200

if __name__ == '__main__':
    app.run(debug=True)
