class Employe:
  compayName ="Apple"  # class variable 
  noofEmploye = 0

  def __init__(self, name):
    self.name = name        # instance variable 
    self.raise_amount = 0.2
    Employe.noofEmploye += 1
  

  def showDetails(self):
    print(f"The name of the Employe is {self.name} and the raise amount in {self.noofEmploye} sized {self.compayName} is {self.raise_amount}")


emp1 = Employe("Harry")
emp1.raise_amount = 0.3
emp1.compayName = "Apple India"
emp1.showDetails()

Employe.compayName = "Google"

emp2 = Employe("Rohit")
emp2.showDetails()
