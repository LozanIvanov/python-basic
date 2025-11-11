numbers = [2, 4, 6, 8, 10]

search = int(input("Въведете число за търсене: "))

if search in numbers:
    print(f"Числото {search} съществува в масива.")
else:
    print(f"Числото {search} НЕ съществува в масива.")
