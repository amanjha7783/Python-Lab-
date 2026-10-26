# find average of all numbers by tuple and use function

def average(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
    print("Average of Number is ", sum / len(number))

average(4,6,8,9)