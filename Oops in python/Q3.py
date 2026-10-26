class Student:
    college_name = "ABC"

    def __init__(self, name, mark): # Constructor
        self.name = name
        self.mark = mark

    def welcome(self): # instance method
        print(f"Hello, my name is {self.name} and I am a student of {self.college_name}.")

    def display_mark(self): # instance method
        print(f"My marks are {self.mark}")

s1 = Student("Aman", 97)
s1.welcome()
s1.display_mark()
