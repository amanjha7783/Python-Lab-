# normal function 
def add(x,y):
  return x+y


#Static method 
class Math:
  def __init__(self, num):
    self.num = num

  def addnum(self, n):
    self.num = self.num+n

  @staticmethod # na instance and na class ko belong krte h
  def add(a,b):
    return a+b
  
a = Math(55)
print(a.num)
a.addnum(5)
print(a.num)

print(Math.add(5,6))




print(add(5,10))