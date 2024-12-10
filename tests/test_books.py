# tests/test_books.py

import unittest
from app import app

class LibraryApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_book(self):
        response = self.client.post('/api/books', json={
            "title": "New Book",
            "author": "John Doe",
            "genre": "Fiction",
            "published_date": "2024-01-01"
        })
        self.assertEqual(response.status_code, 201)

    def test_list_books(self):
        response = self.client.get('/api/books?page=1&limit=2')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
