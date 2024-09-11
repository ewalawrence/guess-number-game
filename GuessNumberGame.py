# Guess Number Game

import random

lowestNumber = 1
highestNumber = 100
answer = random.randint(lowestNumber, highestNumber)
guesses = 0
isGuessing = True

while isGuessing:
    guess = input(f"Enter a guess between {lowestNumber} and {highestNumber}: ")  
    if guess.isdigit():
        guess = int(guess)
        guesses += 1 

        if guess < lowestNumber or guess > highestNumber:
            print(f"Number is out of range. Enter a number between {lowestNumber} and {highestNumber}.")
        elif guess > answer:
            print("Too high! Try again!")
        elif guess < answer: 
            print("Too low! Try again!")
        else:
            print(f"CORRECT! The answer was {answer} 🙂")
            print(f"Number of guesses: {guesses}")
            isGuessing = False  
    else: 
        print(f"Invalid input. Enter a number between {lowestNumber} and {highestNumber}.")