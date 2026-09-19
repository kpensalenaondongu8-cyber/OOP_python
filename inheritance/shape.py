class Shape:
    def __init__(self, name):
        self.name = name

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * 2

class Square(Shape):
    def __init__(self, name, paramter):
        super().__init__(name) 
        self.paramter = paramter
    def area(self):
        return self.paramter ** 2

all_in = Circle("circle", 4)
all_o = Square("square", 4)
# print(all_in.area())
# print(all_o.area())                       
shapes = [all_in, all_o]
for shape in shapes:
    print(shape.area())        