def calculate_total(amount, interest_rate, years):
    total = amount + (amount * interest_rate * years)
    return total

amount = float(input("Enter the initial amount: "))
interest_rate = float(input("Enter the annual interest rate: "))
years = int(input("Enter the number of years: "))

final_amount = calculate_total(amount, interest_rate, years)
print(f"The final amount after {years} years is: {final_amount:.2f}")
