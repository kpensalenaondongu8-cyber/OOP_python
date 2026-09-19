class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed
    def describe(self):
        return f"{self.brand} can go {self.speed}km/h"
    
car = Car("Toyota", 180)
print(car.describe())    
