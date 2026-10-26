class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 

s1 = ("aman" , 18 , "A+")
print(s1)

del s1
print(s1) # This will raise an error because s1 has been deleted.  # Output: NameError


