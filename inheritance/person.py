class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    def intro(self):
        return f"{self.name}, {self.age}, studies at {self.school}"            

all = Student("Thomas", 20, "Learn2Earn")

print(all.intro())