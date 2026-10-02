# 12. Number Guessing Game

# random Python ka module hai jo random numbers banane ke liye use hota hai.
import random

number = random.randint(1, 100)             # 1 se 100 ke beech ek random secret number banaya (jaise 57). User ko ye number nahi dikhega
attempts = 0                                # Attempts ko 0 se shuru kiya, kyunki abhi user ne koi guess nahi kiya

while True:                                 # WHILE LOOP: jab tak sahi number na mile, user se guess maangta rahega
    guess = int(input("Guess the number (1-100): "))   # User se guess liya. int() input ko number mein badalta hai
    attempts = attempts + 1                 # Har guess ke baad attempts 1 badha diya (pehli guess = 1, doosri = 2, ...)

    if guess > number:                      # Agar guess secret number se bada hai (jaise secret 57, guess 80)
        print("Too High")                   # To "Too High" dikhao

    elif guess < number:                    # Nahi to agar guess secret number se chhota hai (jaise secret 57, guess 30)
        print("Too Low")                    # To "Too Low" dikhao

    else:                                   # Na bada, na chhota, matlab guess == number, yaani sahi guess
        print("Correct!")                   # Sahi hone ka message
        print("Number of attempts:", attempts)   # Kitni koshish mein mila, wo print kiya
        break                               # break se while loop ruk gaya, game khatam


# ---------- Example output ----------
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

# ---------- Assignment requirements ----------
# Random number 1-100          -> random.randint(1, 100)
# while loop                   -> while True
# User se guess lena           -> input()
# "Too High" / "Too Low"       -> if / elif
# Correct number par stop      -> break
# Total attempts display       -> attempts

# Note: Guess mein text (jaise "abc") daalne par int() error dega.
# Simple rakhne ke liye ise handle nahi kiya.