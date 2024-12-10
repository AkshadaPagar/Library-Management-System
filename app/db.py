import json

# Define the books and members database dictionaries
BOOKS_DB = {}
MEMBERS_DB = {}

# Load data from JSON files
def load_data():
    global BOOKS_DB, MEMBERS_DB
    try:
        with open('books.json', 'r') as f:
            BOOKS_DB = json.load(f)
        with open('members.json', 'r') as f:
            MEMBERS_DB = json.load(f)
    except FileNotFoundError:
        BOOKS_DB = {}
        MEMBERS_DB = {}
    except json.JSONDecodeError:
        print("Error decoding JSON. Files may be corrupted.")
        BOOKS_DB = {}
        MEMBERS_DB = {}

# Save data to JSON files
def save_data():
    try:
        with open('books.json', 'w') as f:
            json.dump(BOOKS_DB, f)
        with open('members.json', 'w') as f:
            json.dump(MEMBERS_DB, f)
    except Exception as e:
        print(f"Error saving data: {e}")
