# Enumerate function in python 

marks = [42,45,67,98,32,21,1,56]
# index = 0
# for marks in marks:
#     print(marks)
#     if(index == 3):
#         print("Your marks is maximum in our class ")
#     index += 1

for index, marks in enumerate(marks , start = 1):  # sath m index bhi dega
    print(marks)  # tuple milega
    if(index == 3):
        print("Your marks is maximum in our class ")