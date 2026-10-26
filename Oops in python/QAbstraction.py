# Abstraction
# Abstraction is a fundamental concept in object-oriented programming (OOP) 
# that allows you to hide the implementation details of an object from the outside world, 
# exposing only the necessary information to the user. This helps to reduce complexity and improve code readability.

class car:
    def __init__(self):
        self.clucth = False
        self.aclerate = False
        self.brake = False

    def start(self):
        self.clutch = True
        self.aclerate = True
        self.brake = False
        print("Car started.....")

car1 = car()
car1.start()


