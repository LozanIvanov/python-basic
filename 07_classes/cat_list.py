class Cat:
    def _init_(self,name,age):
        self.name=name
        self.age=age

    def _str_(self):
        return f"Cat name: {self.name}, age: {self.age}"

cats=[]
for i in range(3):
     name = input(f"Enter name for cat {i + 1}: ")
     age = int(input(f"Enter age for cat {i + 1}: ")) 

     cat=Cat(name,age)
     cats.append(cat)

print("\nAll cats:")
for cat in cats:
    print(cat)            