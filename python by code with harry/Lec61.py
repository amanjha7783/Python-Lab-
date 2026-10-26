#  Inheritance in python

class Employee: # Employee class
  def __init__(self, name, id): # Constructor
    self.name = name # Employee name
    self.id = id  # Employee ID

  def showDetails(self): # Method to display employee details
    print(f"The name of Employee: {self.id} is {self.name}") # Display employee details

class Programmer(Employee): # Programmer class
  def showLanguage(self): # Method to display programming language
    print("The default langauge is Python") # Display default programming language


e1 = Employee("Rohan Das", 400) # Create an instance of Employee class
e1.showDetails() # Display employee details

e2 = Programmer("Harry", 4100) # Create an instance of Programmer class
e2.showDetails() # Display employee details
e2.showLanguage() # Display programming language


    