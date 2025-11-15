class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive!")
            return
        if amount > self.balance:
            print("Not enough balance!")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def print_balance(self):
        print(f"{self.name}'s account balance: {self.balance}")


account = BankAccount("Ivan", 100)

account.print_balance()
account.deposit(50)
account.withdraw(30)
account.withdraw(500)
