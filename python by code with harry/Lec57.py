#  Introduction to OOPS
#  class and object 

class person:
    name = "Aman"
    occupation = "HR"
    networth = 10
    def info(self): # self  ka matlab wo object jiske liye koi method call kia ja raha hai
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()
a.name = "Mohit"
a.occupation = "Software Devloper"
print(a.name)
print(a.occupation)

b.name = "Arpita"
b.occupation = "Doctor"

a.info()
b.info()
c.info()