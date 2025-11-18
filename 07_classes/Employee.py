class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_salary(self):
        return self.base_salary    
    def info(self):
        print(f"{self.name},{self.base_salary}")    
             
class Manager(Employee):
    def __init__(self,name,base_salary,bonus):
        super().__init__(name,base_salary)
        self.bonus=bonus
    def calculate_salary(self):
        return self.base_salary+self.bonus
    def info(self):
        print(f"Name:{self.name},Salary:{self.calculate_salary()} (Manager)")

class Programmer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, base_salary=0) 
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def info(self):
        print(f"Name: {self.name}, Salary: {self.calculate_salary()} (Programmer)")        
           
