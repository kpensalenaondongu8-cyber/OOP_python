class Vehicle:
    def __init__(self, brand, daily_rate):
        self.brand = brand
        self.daily_rate = daily_rate
        self.is_rented = False

    def calculate_cost(self, days):
        return self.daily_rate * days
    
class Car(Vehicle):
     def __init__(self, brand, daily_rate, num_doors):
         super().__init__(brand, daily_rate)    
         self.num_doors = num_doors
     def calculate_cost(self, days):
         return self.daily_rate * days + 10

class Mortocycle(Vehicle):
     def __init__(self, brand, daily_rate, has_sidecar):
         super().__init__(brand, daily_rate)
         self.has_sidecar = has_sidecar
     def calculate_cost(self, days):
         return self.daily_rate * days * 0.8

class RentalAgency:
     def __init__(self):
         self.vehicles = []

     def rent(self, vehicle):
         if not vehicle.is_rented:
             vehicle.is_rented = True 
         else:
             print("The Vehicle is Unavailable")

     def return_vehicle(self, vehicle):
         vehicle.is_rented = False
                        

car = Car("Toyota", 50, 4)
moto = Mortocycle("Harley", 50, True)
agency = RentalAgency()

agency.rent(car)
print(car.is_rented)

agency.rent(car)   

agency.return_vehicle(car)
print(car.is_rented)

vehicles = [car, moto]
for v in vehicles:
    print(v.calculate_cost(3))