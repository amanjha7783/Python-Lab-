#  check the number in interval which is divisble by particular number

number = int(input("Enter the number : "))
starting_number = int(input("Enter the starting number : "))
ending_number = int(input("Enter the Ending number : "))
for i in range(starting_number, ending_number):
    if i % number == 0:
        print(i)