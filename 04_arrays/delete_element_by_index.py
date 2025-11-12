number = int(input("Enter number of elements: "))
first=[]
for i in range(number):
    num=int(input(f"enter number {i+1}:"))
    first.append(num)

index_number= int(input("Enter index to delete (starting from 0): ")) 

if 0<=index_number<len(first):
    first.pop(index_number)

print(first)