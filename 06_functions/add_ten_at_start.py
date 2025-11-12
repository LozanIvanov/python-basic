def add_ten_at_start(numbers):
    numbers.insert(0,10)
    return numbers
arr=[1,2,3,4]

result=add_ten_at_start(arr)

print("Array after inserting 10 at the start:", result)