x = int(input("number of passenger in bus at the time "))

# At stage A, 10 passengers got down from the bus, and 12 passengers boarded into the bus.
a = x-10+12
print("Total number of person in the bus at stage A is ", a)

#At stage B, 15 are boarded into the bus after 10 got down from it. 
b = a-10+15
print("Total number of person in the bus at stage B is ", b)

#  At stage C, 5 are boarded into the bus after 2 getting off from it.
C = b+5-2
print("Total number of person in the bus at stage c is ", C)


#  At stage D, 22 passengers got down from the bus, and 28 passengers boarded into the bus. 
D = C-22+28
print("Total number of person in the bus at stage D is ", D)

#  Finally, at stage E, 15 are boarded into the bus after 7 getting off from it
E = D+15-7
print("Total number of person in the bus at stage E is ", E)