class Shape:
    def __init__(self, name):
     self.name = name

    def area(self):    
        return 0
class Circle(Shape):
    def __init__ (self, radius):       
       
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
       
class Square(Shape):
    def area(self, side):
           return side **2
    
all_in_one = Shape("Circle")  
dog = Circle(10)
x = Square(20)
print(all_in_one.area())
print(dog.area())
print(x.area(2))  