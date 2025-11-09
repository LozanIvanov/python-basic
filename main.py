"""
numbers=[1,3,2,4]
new_numbers=[]
for i in numbers:
    new_numbers.append(i*2)
print(new_numbers)
"""
"""
n=int(input("Въведете броя на хората: "))

names=[]
ages=[]

for i in range(n):
    name=input(f"Enter name {i+1}:")
    age=input(f"Enter age {i+1}:")
    names.append(name)
    ages.append(age)

min_age=min(ages)  
index=ages.index(min_age)

print(f"{names[index]} is {ages[index]} years old")
"""
"""
n=int(input("Enter number N:"))
first=[]
for i in range(n):
    num=int(input(f"Enter number {i+1}:"))
    first.append(num)

m=int(input("Enter number M:"))
second=[]
for i in range(m):
    num=int(input(f"Enter number {i+1}:"))
    second.append(num)

combined=first+second

print(first)
print(second)
print(combined)
"""
"""
numbers=[5,3,4,2,2,3,3]

search=int(input("Enter number for search:"))

count = 0

for i in numbers:
    if i == search:
       count += 1

print(count)
"""
"""
numbers = [5, -3, 7, -2, 4, -1, 6]

sum_positive=0
for i in numbers:
    if i>0:
        sum_positive+=i

print(sum_positive)
"""
numbers=[1,3,4,6,2]

is_sorted=True

for i in range(len(numbers)-1):
    if numbers[i]>numbers[i+1]:
        is_sorted=False
        break

if is_sorted:
    print("The array is sorted in ascending order")
else:  
     print("The array is NOT sorted in ascending order")  




                  
