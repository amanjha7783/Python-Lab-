#  How to import python functions and use it in another python file

import math
result = math.sqrt(49)
print(result)

from math import sqrt , pi # another way to import 
result = sqrt(9)*pi
print(result)

import math # importing math module
print(dir(math))

from Aman import welcome , aman  # importing function from another module(file)
welcome()
print(aman) 


