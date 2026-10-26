#  make flexible function by the help of * args save in tuple 

def total(a,b):
    return  a+b

def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4,5,6))

def multiply(num, *args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply(2,2,3,4))

def power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"
    
num = [1,2,3,4,5]
# print(power(1,*num))
print(power(1,2,3,4,5))



