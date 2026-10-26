#  Lambda function is use for short hand functions

def apply(fnx,value):
    return 100 + fnx(value)

double = lambda x : x*2
cube = lambda x : x**3
avg = lambda x,y,z : (x+y+z)/3

print(double(5))
print(cube(5))
print(avg(5,10,9))
print(apply(cube,5))