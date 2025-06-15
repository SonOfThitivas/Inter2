import json

class Book:
    def __init__(self, title, author, read=False):
        self.title = title
        self.author = author
        self.read = read

    def mark_as_read(self):
        self.read = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "read": self.read
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data.get("read", False))

def load_books(filename="books.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Book.from_dict(b) for b in data]
    except FileNotFoundError:
        return []

def save_books(books, filename="books.json"):
    with open(filename, "w") as f:
        json.dump([b.to_dict() for b in books], f, indent=2)

# Example usage
if __name__ == "__main__":
    books = load_books()
    b1 = Book("1984", "George Orwell")
    b2 = Book("Python Crash Course", "Eric Matthes")
    b1.mark_as_read()
    books.extend([b1, b2])
    save_books(books)
    for b in books:
        status = "Read" if b.read else "Not Read"
        print(f"{b.title} by {b.author} - {status}")