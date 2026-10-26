# First example of class attribute and object attribute
class student :
    college_name = "ABC" # class attribute
    name = "unknown"
    def __init__(self , fullname ,marks):
        self.name = fullname # oject attribute
        self.marks = marks
        print("adding new student name in database ")

# Note :- class attribute is shared by all objects of the class
# Note :- precedence of accessing attribute is object attribute > class attribute > instance attribute > local variable
s1 = student("karan", 95)
print(s1.name, s1.marks)
s2 = student("Arjun" , 92)
print(s2.name, s2.marks)
print(student.college_name)


#  second example of class attribute and object attribute
class cars:
    def __init__(self): # default constructor
        pass

    def __init__(self, barnd_name,model_name,colour_name): # parameterized constructor
        self.name = barnd_name
        self.model = model_name
        self.colour = colour_name
        print("cars details added to database ")


car1 = cars("BMW","X5","purpel")
print(car1.name,car1.model,car1.colour)
print(f"car_name = {car1.name} \ncar_model = {car1.model} \ncar_colour = {car1.colour}") 

 
