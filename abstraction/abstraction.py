from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

class HourlyyEmployee(Employee):
    def __init__(self, name, hours_worked):
        super().__init__(name)
        self.hours_worked = hours_worked
    def calculate_pay(self):
        return self.hours_worked * 20

class SalariedEmplyee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    def calculate_pay(self):
        return self.monthly_salary
       

all_Hour = HourlyyEmployee("Thomas", 23)
all_sala = SalariedEmplyee("David",43)
all_of = [all_Hour, all_sala]

for all in all_of:
    print(all.calculate_pay())