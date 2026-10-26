number = [1,2,3,4,5]

for i in range(len(number)):
    number[i] = number[i]**2

print(number)

#  Map function 
def square(n):
    return n**2

squares = list(map(square,number))
print(squares)

list1 = ['ab','abc','abcd','acbds']

for i in range(len(list1)):
    length = len(list1[i])
    print(length)