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