'''Take values of length and breadth of a quadrilateral and check if length and breadth are equal then 
call it a rhombus. Assume length of one diagonal is given as 6 cm. Now find out the length of the second 
diagonal and calculate the area of the rhombus as well.
'''

length = int(input("Enter the  value of length : "))
breadth = int(input("Enter the  value of breadth : "))
diagonal_1 = 6
if(length == breadth):
    print("It is a rohmbous ")
    diagonal_2 = 2*(length**2 - (diagonal_1/2)**2)**0.5
    print(f"second daigonal of quadiralteral is {diagonal_2} ")
    area  = 0.5*(diagonal_1*diagonal_2)
    print(f"Area of rohbous is {area}")
else:
    print("It is not a rohmbous ")
