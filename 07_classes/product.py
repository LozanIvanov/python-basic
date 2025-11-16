class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):    
        return self.price * self.quantity
    
    def print_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total value: {self.total_value():.2f}") 


product = Product("Laptop", 999.99, 3)
product.print_info()
