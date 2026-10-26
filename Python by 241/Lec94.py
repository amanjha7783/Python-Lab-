number1 = list(range(1,11))
print(number1)
print(number1.pop())
print(number1.index(7))
number = [1,2,3,5,5,7,6,8,9,5,4,3,2,4,4]
print(number.index(4))
print(number.index(4, number.index(4)+1))
print(number.index(4, number.index(4 , number.index(4)+1)+1))