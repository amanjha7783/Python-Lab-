# Public Access Specifier in Python
class Employe:
    def __init__(self):
        self.name = 'Aman'

a = Employe()
print(a.name)  

# first method to acess Private Access Modifier
class Employee:
    def __init__(self, name):
        self.__name = name  # Initialize the private attribute

# Create an instance and pass the required argument
a = Employee("Karan")

# Access the private attribute using name mangling
print(a._Employee__name)  # Output: Karan

# second method to acess Private Access Modifier
class Employee:
    def __init__(self, name):
        self.__name = "Jhon"

    def get_name(self):
        return self.__name

a = Employee("Aman")
print(a.get_name())
        