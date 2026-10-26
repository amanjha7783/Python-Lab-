import random
n = int(input("Enter the last number upto : "))
random_number = int(input("Enter the random number : "))
wining_number = random.randint(1, n)
print(f"The winning number is between 1 and {n}.")

while True:
    if(wining_number == random_number):
        print("You win")
        break
    elif(wining_number > random_number):
        print("you think the number is too low")
        print("Guess again")
    elif(wining_number < random_number):
        print("you think the number is too high")
        print("Guess again")
    random_number = int(input("Enter your next guess : "))

# import random

# def get_user_input():
#     while True:
#         try:
#             n = int(input("Enter the last number upto : "))
#             random_number = int(input("Enter your guess : "))
#             return n, random_number
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def generate_winning_number(n):
#     return random.randint(1, n)

# def game():
#     n, random_number = get_user_input()
#     winning_number = generate_winning_number(n)
#     print(f"The winning number is between 1 and {n}.")
    
#     while True:
#         if winning_number == random_number:
#             print("You win!")
#             break
#         elif winning_number > random_number:
#             print("Your guess is too low.")
#         elif winning_number < random_number:
#             print("Your guess is too high.")
#         random_number = int(input("Enter your next guess : "))

# if __name__ == "__main__":
#     game()