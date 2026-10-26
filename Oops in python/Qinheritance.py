class car:
    colour = "Black "
    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("car stopped....")

class totyotacars(car):
    def __init__(self,name):
        self.name=name

car1 = totyotacars("fortuner")        
car2 = totyotacars("pirus")

# print(f"{car1.name} is {car1.start()}")
print(car1.start())
print(car1.colour)

# Multiple Inheritance
class A:
    varA = "Wlecome to the class A"
class B:
    varB = "Wlecome to the class B"
class  C(A,B):
    varC = "Wlecome to the class C"
  
C1 = C()
print(C1.varC)
print(C1.varB)
print(C1.varA)


