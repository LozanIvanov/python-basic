class Student:
    def _init_(self,first_name, last_name, age, average_grade):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.average_grade = average_grade

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Age: {self.age}, Grade: {self.average_grade}"
    
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i+1}:")
    first = input("First name: ")
    last = input("Last name: ")
    age = int(input("Age: "))
    grade = float(input("Average grade: "))

    students.append(Student(first, last, age, grade))

print("\nStudents older than 20 with grade > 5:")
for s in students:
    if s.age > 20 and s.average_grade > 5:
        print(s)