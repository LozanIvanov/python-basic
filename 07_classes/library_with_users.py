
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

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []   

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Cannot borrow '{book.title}'. It is already borrowed.")
            return False

        book.is_borrowed = True
        self.borrowed_books.append(book)
        return True

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"{self.name} does not have '{book.title}'.")
            return False

        book.is_borrowed = False
        self.borrowed_books.remove(book)
        return True

    def list_borrowed(self):
        print(f"\nBooks borrowed by {self.name}:")
        if not self.borrowed_books:
            print("(none)")
        else:
            for b in self.borrowed_books:
                print(" -", b.title)


# -------------------------------
#        LIBRARY CLASS
# -------------------------------
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    # ---- BOOK METHODS ----
    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

    # ---- USER METHODS ----
    def add_user(self, user):
        self.users.append(user)

    def find_user(self, name):
        for u in self.users:
            if u.name.lower() == name.lower():
                return u
        return None

    # ---- ACTIONS: BORROW / RETURN ----
    def borrow_book(self, user_name, book_title):
        user = self.find_user(user_name)
        if not user:
            print("User not found!")
            return

        book = self.find_book(book_title)
        if not book:
            print("Book not found!")
            return

        if user.borrow_book(book):
            print(f"{user.name} successfully borrowed '{book.title}'.")

    def return_book(self, user_name, book_title):
        user = self.find_user(user_name)
        if not user:
            print("User not found!")
            return

        book = self.find_book(book_title)
        if not book:
            print("Book not found!")
            return

        if user.return_book(book):
            print(f"{user.name} returned '{book.title}'.")

    def list_books(self):
        print("\nAll books in library:")
        for b in self.books:
            print(" -", b)

    def list_users(self):
        print("\nRegistered users:")
        for u in self.users:
            print(" -", u.name)

if __name__ == "__main__":

    library = Library()

    library.add_book(Book("Harry Potter", "Rowling", 1997))
    library.add_book(Book("Zoro", "Oda", 2000))
    library.add_book(Book("Rome", "Mark", 1992))

    library.add_user(User("Peter"))
    library.add_user(User("Anna"))

    library.list_books()

    library.borrow_book("Peter", "Harry Potter")
    library.borrow_book("Anna", "Harry Potter")  

    peter = library.find_user("Peter")
    peter.list_borrowed()

    library.return_book("Peter", "Harry Potter")

    library.borrow_book("Anna", "Harry Potter")

    library.list_books()
