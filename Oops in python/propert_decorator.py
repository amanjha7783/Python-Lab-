# class student:
#     def __init__(self, phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.avg = str((self.phy + self.chem + self.math) / 3 ) + "%"


#     def calculateaverage(self):
#         self.avg = str((self.phy + self.chem + self.math) / 3 ) + "%"

# s1 = student(90,80,70)
# print(s1.avg)

# s1.phy = 100
# print(s1.phy)
# s1.calculateaverage()
# print(s1.avg)

class student:
    def __init__(self, phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def avg(self):
        return str((self.phy + self.chem + self.math) / 3 ) + "%"

s1 = student(90,80,70)
print(s1.avg)

s1.phy = 100
print(s1.avg)
