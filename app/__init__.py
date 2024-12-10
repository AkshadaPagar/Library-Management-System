from flask import Flask
from flask_jwt_extended import JWTManager
from app.routes import app

# Create the Flask application instance
def create_app():
    app.config['JWT_SECRET_KEY'] = 'AkshadaPagar'  # Set your secret key for JWT
    jwt = JWTManager(app)  # Initialize the JWT manager
    return app
