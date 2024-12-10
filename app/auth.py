# app/auth.py
import uuid
from flask import request
from functools import wraps

def authenticate():
    token = request.headers.get('Authorization')
    if not token:
        return False
    # Check if token is valid (You can replace this with your actual logic)
    if token == "Bearer abc123xyz":  # Example token
        return True
    return False


def generate_api_token():
    return str(uuid.uuid4())  # For token generation
