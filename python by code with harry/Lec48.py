#  local Vs Global variable

x = 10  # global variable

def my_function():
  global x
  x = 7  # this will change the value of the global variable x
  y = 5  # local variable
  print(x)
  print(y)
my_function()
print(x)  # prints 5
# print(y)
# this will cause an error 
# because y is a local variable and is not accessible outside of the function

def my_function2():
  x = 15  # this will change the value of the global variable x
  y = 35  # local variable
  print(x)
  print(y)
my_function2()