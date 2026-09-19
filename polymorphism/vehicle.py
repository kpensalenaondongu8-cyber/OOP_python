class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed
    def describe(self):
        return f"{self.brand} can go {self.speed}km/h"
    

class Truck(Vehicle):
    def __init__(self, brand, speed, capacity):
        super().__init__(brand) 
        self.capacity = capacity
        self.speed = speed

    def describe(self):
        return f"{self.brand} truck can go {self.speed}km/h, carries {self.capacity}kg"
    
car_all = Car("Toyota", 15)
truck_all = Truck("Tipper", 100, 25)

all_in = [car_all, truck_all]

for all in all_in:
    print(all.describe())
