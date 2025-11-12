def print_reverse_sorted(numbers):
    numbers.sort(reverse=True)
    for num in numbers:
        print(num)

n=int(input("Enter the number of element:"))
arr=[]

for i in range(n):
    num=int(input(f"Enter number {i+1}:"))
    arr.append(num)

print("Numbers in reverse order:")  
print_reverse_sorted(arr)  