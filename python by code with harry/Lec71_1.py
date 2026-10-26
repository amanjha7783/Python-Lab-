class person:

  def __init__(self, name , age):
    self.name = name
    self.age= age
    self.version = 1

p = person("Aman jha", 25)

print(p.__dict__)

print(help(person))