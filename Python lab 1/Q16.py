'''
Write a program that accept three sides of triangle as input, and print whether the triangle is valid 
or not. Hint: A triangle is valid if sum of its two sides is greater than the third side. If three sides are a, 
b and c, then three conditions should be met. a + b > c a + c > b b + c > a 
'''

def traingle(a,b,c):
    if(a+b>c and b+c>a and a+c>b):
        print(f"{a}, {b} and {c} are side of valid traingle")
    else:
        print(f"{a}, {b} and {c} are not side of valid traingle")

x = int(input("ente rthe first side of traingle : "))
y = int(input("ente rthe second side of traingle : "))
z = int(input("ente rthe third side of traingle : "))
traingle(x,y,z)