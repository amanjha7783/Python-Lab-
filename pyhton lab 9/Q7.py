'''
Create a class Circle with radius as attribute and methods to calculate area and
circumference.
'''
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.area = 3.14*radius*radius
        self.circumference = 3.14*2*radius
    def display(self):
        print(f"Area of the circle is {self.area}")
        print(f"Circumference of the circle is {self.circumference}")

c1 = Circle(7)
c1.display()
    