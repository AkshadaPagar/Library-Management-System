import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()  # Create the app using the factory function
    app.config["TESTING"] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()  # Provides a test client for making requests
