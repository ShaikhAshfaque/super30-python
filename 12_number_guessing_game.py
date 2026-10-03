# 12. Number Guessing Game

import random                       # random module is used to create random numbers

number = random.randint(1, 100)     # secret number between 1 and 100, hidden from the user
attempts = 0                        # number of guesses so far

while True:                         # keep asking until the guess is correct
    guess = int(input("Guess the number (1-100): "))   # int() converts the input to a number
    attempts = attempts + 1                            # count this guess

    if guess > number:              # guess is bigger than the secret number
        print("Too High")

    elif guess < number:            # guess is smaller than the secret number
        print("Too Low")

    else:                           # guess is equal to the secret number
        print("Correct!")
        print("Number of attempts:", attempts)
        break                       # stop the loop, the game is over


# Example output:
# Guess the number (1-100): 50
# Too Low
#
# Guess the number (1-100): 80
# Too High
#
# Guess the number (1-100): 65
# Too High
#
# Guess the number (1-100): 60
# Too High
#
# Guess the number (1-100): 57
# Correct!
# Number of attempts: 5

# Assignment requirements:
# Random number 1-100        -> random.randint(1, 100)
# while loop                 -> while True
# Take a guess from the user -> input()
# "Too High" / "Too Low"     -> if / elif
# Stop on correct number     -> break
# Show total attempts        -> attempts

# Note: Typing text like "abc" as a guess will cause an error in int().
# It is not handled here to keep the code simple.