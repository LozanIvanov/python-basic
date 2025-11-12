def replace_with_zero(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            numbers[i] = 0
    return numbers

arr = [2, 5, 7, 5, 9]
num = int(input("Enter a number to replace with 0: "))

result = replace_with_zero(arr, num)
print("Updated array:", result)
