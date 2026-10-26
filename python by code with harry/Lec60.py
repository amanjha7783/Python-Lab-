# getter and setter 

class Myclass: # class definition
    def __init__(self, value): # constructor
        self._value = value # instance variable

    def show(self): # method
        print(f"value is {self._value}") # print value

    @property # getter 
    def ten_value(self): # property
        return self._value * 10 # return value
    
    @ten_value.setter # setter
    def ten_value(self, new_value): 
        self._value = new_value / 10

obj = Myclass(10) # object creation
obj.ten_value= 67 # setter
print(obj.ten_value) # getter
obj.show() # method call





























