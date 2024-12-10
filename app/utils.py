def search_books(books, title, author):
    return [book for book in books if (title and title.lower() in book.title.lower()) or (author and author.lower() in book.author.lower())]

def paginate(books, page, limit):
    start = (page - 1) * limit
    end = start + limit
    return books[start:end]
