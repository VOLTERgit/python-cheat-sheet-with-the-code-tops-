# number guessing game
import random

computer_guess = random.randint(1,100)
num = 0
status = True
while status:
    num += 1
    user_guess = int(input("Enter your guess : "))
    if user_guess > computer_guess:
        print("Hint : Guess Lower Number ")
    elif user_guess < computer_guess:
        print("Hint: Guess Upper Number ")
    else:
        if num <= 5:
            print("Right Guess !!! ")
            status = False
        else:
            print("Your are doing good but if you guess right number in just 5 tries you will win the price")
