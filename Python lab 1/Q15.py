'''
 Suppose that you are playing a game with a computer. In the game, both computer and you have 
to guess a random integer between 0 and 9, including both the numbers. If you guess the same number 
as the computer, we say that you beat the computer. You will be given at most five chances to beat the 
computer. Suppose if you beat the computer in i-th chance, you get (100-20*i) points. If you could not 
beat the computer, you get 0 points. Likewise, you have to play the game for three rounds. In the end, 
if your average score is at least 50, you are the winner of the game. Otherwise, the computer is the 
winner. 
Write a python program to implement the above game. To simulate a computer guess, use the statement 
"int(random.randint(0, 9))" with "import random" at the top of the program.
'''

import random

def game():
    computer_guess = random.randint(0, 9)
    print("\nNew round started! You have 5 chances to beat the computer.")
    score = 0
    for i in range(0,5):
        user_guess = int(input("Enter your guess: "))
        if user_guess == computer_guess:
            print("You beat the computer in", i+1, "chance and you get")
            score = (100 - 20 * i)
            print("your score is", score)
            break
        else:
            print("You could not beat the computer in", i+1, "chance")
    return score

def avg_score():
    total_score = 0
    for i in range(0,3):
        total_score += game()
    avg = total_score / 3
    print(f"\nYour average score: {avg}")
    if (avg >= 50):
        print("You are the winner of the game")
    else:
        print("Computer is the winner of the game")

avg_score()