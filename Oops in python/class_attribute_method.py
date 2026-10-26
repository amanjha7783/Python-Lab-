# class attribute changes on object attributes

class person:
    name = "anonymuos"

    def change_name(self,name):
        self.name = name

p1 = person()
p1.change_name("rahul kumar")
print(p1.name)
print(person.name)


print("1st way to change name of class attribute is by using class method")
class person:
    name = "anonymuos"

    def change_name(self,name):
        person.name = name

p1 = person()
p1.change_name("rahul kumar")
print(p1.name)
print(person.name)

print("2nd way to change name of class attribute is by using class method")
class person:
    name = "anonymuos"

    def change_name(self,name):
        self.__class__.name = name

p1 = person()
p1.change_name("rahul kumar")
print(p1.name)
print(person.name)

print("3rd way to change name of class attribute is by using class method")
class person:
    name = "anonymuos"

    @classmethod
    def change_name(cls,name):
        cls.name = name

p1 = person()
p1.change_name("rahul kumar")
print(p1.name)
print(person.name)