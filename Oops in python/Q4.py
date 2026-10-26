
class Student:
    college_name = "ABC"

    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def welcome(self):
        print(f"Hello, my name is {self.name} and I am a student of {self.college_name}.")

    def display_marks(self):
        print(f"My marks in physics: {self.mark1}")
        print(f"My marks in chemistry: {self.mark2}")
        print(f"My marks in Math: {self.mark3}")

    def avg_marks(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        print("Average of 3 subject marks is ", avg)

s1 = Student("Aman", 98, 94, 91)
s1.welcome()
s1.display_marks()
s1.avg_marks()

  