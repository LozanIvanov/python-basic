class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def info(self):
        print(f"{self.name} - {self.price} EUR")

class Book(Product):
    def __init__(self, name, price,author):
        super().__init__(name,price)
        self.author=author
    def info(self):
        print (f"Book: {self.name} by {self.author} - {self.price} EUR")

class Laptop(Product):
    def __init__(self, name, price,cpu):
        super().__init__(name, price) 
        self.cpu=cpu
    def info(self):
        print(f"Laptop: {self.name}, CPU: {self.cpu} - {self.price} EUR")    

class Phone(Product):
    def __init__(self, name, price,brand):
        super().__init__(name, price)
        self.brand=brand
    def info(self):
        print(f"Phone: {self.name}, Brand: {self.brand} - {self.price} EUR")    

class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add(self,product) :
        self.items.append(product)  
        print(f"Added to cart: {product.name}")

    def remove(self,product_name):
        for i in self.items:
            if(i.name==product_name):
                self.items.remove(i)
                print(f"Removed from cart: {i.name}")
                return
        print("Product not found in cart.")

    def total(self):
        return sum(item.price for item in self.items)  

    def receipt(self):
        print("\n----- RECEIPT -----")  
        if not self.items:
             print("Cart is empty")
             return
        for item in self.items:
            item.info()

        print(f"TOTAL: {self.total()} EUR")   
        print("-------------------\n") 

class Store:
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        self.products.append(product)
    
    def show_products(self):
        print("\nAvailable Products:")
        for p in self.products:
            p.info()
        print()

#-------------------------------------------------------------
store = Store()
store.add_product(Book("Harry Potter", 20, "J.K. Rowling"))
store.add_product(Laptop("MacBook Air", 1200, "M1"))
store.add_product(Phone("iPhone 14", 999, "Apple"))

store.show_products()

cart = ShoppingCart()
cart.add(store.products[0])
cart.add(store.products[2])

cart.receipt()

cart.remove("Harry Potter")
cart.receipt()