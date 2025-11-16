class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed!")
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
            return False
        self.is_borrowed = False
        return True

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if not book:
            print("Book not found!")
            return
        
        if book.borrow():
            print(f"You borrowed: '{book.title}'")

    def list_available_books(self):
        print("\nAvailable books:")
        for book in self.books:
            if not book.is_borrowed:
                print(" -", book)

    def list_all_books(self):
        print("\nAll books in library:")
        for book in self.books:
            print(" -", book)


library = Library()

library.add_book(Book("Harry Potter", "J.K. Rowling", 1997))
library.add_book(Book("The Hobbit", "J.R.R. Tolkien", 1937))
library.add_book(Book("1984", "George Orwell", 1949))

library.list_all_books()

library.borrow_book("Harry Potter")
library.borrow_book("Harry Potter")   

library.list_available_books()

library.find_book("1984").borrow()
library.list_available_books()
