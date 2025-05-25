class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("New York Public Library")

book1 = Book("Harry Potter 1", "J.K. Rowling")
book2 = Book("Harry Potter 2", "J.K. Rowling")
book3 = Book("Harry Potter 3", "J.K. Rowling")

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

print(library.list_books())
