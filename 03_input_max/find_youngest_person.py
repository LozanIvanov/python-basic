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