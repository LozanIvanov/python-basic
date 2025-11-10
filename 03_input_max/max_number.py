numbers = []

for i in range(5):
    num = float(input(f"Въведете число {i + 1}: "))
    numbers.append(num)

max_number = max(numbers)

print("Най-голямото число е:", max_number)
