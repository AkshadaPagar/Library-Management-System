# app/models.py
# app/models.py
class Book:
    def __init__(self, title, author, genre, published_date=None, published_year=None, book_id=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.published_date = published_date or published_year  # Use published_year if published_date is not provided


class Member:
    def __init__(self, name, email, member_id=None):
        self.member_id = member_id
        self.name = name
        self.email = email
