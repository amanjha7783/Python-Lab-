# 1) first question
print("first question")
numbers = [3,54,56,23,54,2]
minimum = min(numbers)
maximum = max(numbers)
print(maximum)
print(minimum)

greatest_difference = maximum - minimum
print(greatest_difference) 

# 2) second question
print("second question")
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

mixed = [2,3,4,[3,54,2],[324,564,32],32,45]
print(sublist_counter(mixed))