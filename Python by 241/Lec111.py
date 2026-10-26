def func(int1, int2):
    add = int1 + int2
    multiply = int1*int2
    return add, multiply

a = 5
b  = 4
add , multiply = func(a,b)
print(func(a,b))
print(add)
print(multiply)