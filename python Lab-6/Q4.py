'''
4) A professor grades 80-100: A, 70-79: B, 60-69: C, 50-59: D, Below 50: F.
Write a program that takes an exam score as input and prints the corresponding grade.
Input: 73
Output: "B". - > Dictionary
'''
    
def get_grade(score):
    grades = {
        (80, 100): "A",
        (70, 79): "B",
        (60, 69): "C",
        (50, 59): "D",
        (0, 49):  "F"
    }
    
    for (low, high), grade in grades.items():
        if low <= score <= high:
            return grade
    
    return "Invalid score"

number = int(input("Enter a score: "))
print(get_grade(number))  
