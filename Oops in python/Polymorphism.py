class complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img

    def shown_number(self):
        print(self.real,"i +" , self.img,"j")

    def add(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal, newimg)

num1 = complex(1,3)
num1.shown_number()
num2 = complex(2,4)
num2.shown_number()

num3 = num1.add(num2)
num3.shown_number() 
