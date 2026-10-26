# Execption Handling in python 

try:
    num = int(input("Enter an integer index : "))
    a = [6,3,8,4,9] # print index number of the list
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")