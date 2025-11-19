class Animal:
    def make_sound(self):
        print('SOME SOUND')
class Dog(Animal):
    def make_sound(self):
        print("baf")    
class Cat(Animal):
    def make_sound(self):
        print("miau") 
class Cow(Animal):
    def make_sound(self):
        print("my")                 

animals = [Dog(), Cat(), Cow()]

for i in animals:
    i.make_sound()