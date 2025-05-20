from abc import ABC , abstractmethod

class Shape(ABC):           # inheriting form ABC
    @abstractmethod
    def area(self):
        pass                # because abstract method has no implimentation here

class Rectangle(Shape):
    def __init__(self ,width ,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

r= Rectangle(5,8)
print("Area of Rectangle", r.area())
s=Shape()       # it gives error