def find_max(number):
    return max(number)
n=int(input("Enter lenght of array: "))

arr=[]

for i in range(n):
    num=float(input(f"Enter number {i+1}:"))
    arr.append(num)

max_number=find_max(arr)

print(max_number)