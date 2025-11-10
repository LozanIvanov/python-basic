numbers=[5,3,4,2,2,3,3]

search=int(input("Enter number for search:"))

count = 0

for i in numbers:
    if i == search:
       count += 1

print(count)