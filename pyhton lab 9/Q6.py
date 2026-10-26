'''
Create a class Student with attributes name and marks. Write a method to display
them.
'''

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

s1 = student("Aman", 90)
s1.display()
s2 = student("Mohit", 85)
s2.display()



