'''
10) Given a trapezium (trapezoid) with bases a and b and height h,
a diagonal is drawn, dividing the trapezium into two triangles.
Write a Python program to calculate the area of one of the triangles using 
coordinate geometry or the trapezium area formula.
'''

def area_of_trapezium(a, b, h):
    return (1/2)*(a+b)*h

def area_of_triangle(a, b, h):
    return (1/2)*((a+b)/2)*h

a = float(input("Enter the length of the first base of the trapezium: "))
b = float(input("Enter the length of the second base of the trapezium: "))
h = float(input("Enter the height of the trapezium: "))

trapezium_area = area_of_trapezium(a, b, h)
triangle_area = area_of_triangle(a, b, h)

print("Area of Trapezium: ", trapezium_area)
print("Area of one of the triangles: ", triangle_area)
