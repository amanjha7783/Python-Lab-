'''
10. Create a class Rectangle and write a method to check whether it’s a square or not.
'''

class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def check_square(self):
        if self.length == self.width:
            print("it is a square ")
        else:
            print("it is not a square ")

s1 = rectangle(8,10)
s1.check_square()
s2 = rectangle(10,10)
s2.check_square() 

 