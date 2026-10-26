#  construcors in python

class person:

    def __init__(self,n,o):
        print("Hey, I am a person")
        self.name = n
        self.occupation = o

    def info(self): # self  ka matlab wo object jiske liye koi method call kia ja raha hai
        print(f"{self.name} is a {self.occupation}")

a = person("Aman", "Software Engineer")
b = person("Mohit", "Hr")
c = person("Arpita","doctor")

a.info()
b.info()
c.info()
