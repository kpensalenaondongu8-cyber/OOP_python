class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   
        self.team_size = team_size
    def info(self):
        return f"{self.name} manages a team of {self.team_size}"

team = Manager("Sarah", "$50", 5)
print(team.info())             