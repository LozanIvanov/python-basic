from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def make_sound(self):
        pass   #every one child have to write it it is 
    
    def info(self):
        print(f"This is a {self.__class__.__name__} named {self.name}")

class Dog(Animal):
    def make_sound(self):
        print("woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow...")

animals=[Dog("Rex"),Cat("Pussy")]

for i in animals:
    i.info()
    i.make_sound()
    