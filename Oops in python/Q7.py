class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = circle(7)
print(c1.area())
print(c1.perimeter())

#  2nd way 
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
    def __str__(self): 
        return f"Circle with radius {self.radius}, area {self.area():.2f}, perimeter {self.perimeter():.2f}"

c1 = Circle(21)
print(c1)