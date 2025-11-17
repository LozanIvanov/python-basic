class Item:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"{self.title} is already borrowed!")
            return False
        self.is_borrowed = True
        return True

    def return_item(self):
        if not self.is_borrowed:
            print(f"{self.title} was not borrowed.")
            return False
        self.is_borrowed = False
        return True

    def status(self):
        return "Borrowed" if self.is_borrowed else "Available"


class Book(Item):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)   
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} ({self.year}) by {self.author} - {self.status()}"

class Magazine(Item):
    def __init__(self, title, year, issue):
        super().__init__(title, year)
        self.issue = issue

    def __str__(self):
        return f"Magazine: {self.title} Issue {self.issue} ({self.year}) - {self.status()}"

class DVD(Item):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.duration = duration  

    def __str__(self):
        return f"DVD: {self.title} ({self.year}) - {self.duration} min - {self.status()}"

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def list_items(self):
        print("\nLibrary contents:")
        for item in self.items:
            print(" -", item)

