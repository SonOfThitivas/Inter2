# 📚 Practice: Book Tracker (OOP + JSON)
# Concepts: Classes, Methods, JSON File I/O, CLI interaction
# Build a program to manage a small collection of books.
# Implement the missing methods yourself.

import json

class Book:
    def __init__(self, title, author, read=False):
        self.title = title
        self.author = author
        self.read = read

    def mark_as_read(self):
        # TODO: set self.read to True
        pass

    def to_dict(self):
        # TODO: return a dictionary with title, author, and read
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data.get("read", False))

def load_books(filename="books.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Book.from_dict(b) for b in data]
    except FileNotFoundError:
        print("No saved book list found. Starting fresh.")
        return []

def save_books(books, filename="books.json"):
    with open(filename, "w") as f:
        json.dump([b.to_dict() for b in books], f, indent=2)

def main():
    books = load_books()

    while True:
        print("\n1. Add book\n2. Mark as read\n3. View books\n4. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            books.append(Book(title, author))
        elif choice == "2":
            title = input("Enter book title to mark as read: ")
            for b in books:
                if b.title == title:
                    b.mark_as_read()
                    print(f"Marked '{title}' as read.")
                    break
            else:
                print("Book not found.")
        elif choice == "3":
            for b in books:
                status = "Read" if b.read else "Not Read"
                print(f"{b.title} by {b.author} - {status}")
        elif choice == "4":
            save_books(books)
            print("Books saved. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()