# 11. Password Retry System
# Store a predefined password and give the user a maximum of three attempts to enter it correctly. Use a while loop. After three incorrect attempts, display "Account Locked".

password = "python123"          # the correct password, fixed in advance
attempts = 0                    # number of wrong tries so far

while attempts < 3:             # ask for the password at most 3 times
    user_password = input("Enter password: ")   # take the password from the user

    if user_password == password:               # does it match the correct password?
        print("Password correct. Login successful.")
        break                                   # stop the loop, no more attempts needed
    else:
        attempts = attempts + 1                 # wrong password, so add 1 to attempts
        print("Incorrect password.")

if attempts == 3:               # all 3 attempts were wrong
    print("Account Locked")


# Example: 3 wrong passwords
# Enter password: abc
# Incorrect password.
# Enter password: xyz
# Incorrect password.
# Enter password: 123
# Incorrect password.
# Account Locked

# Example: correct password on the 2nd try
# Enter password: abc
# Incorrect password.
# Enter password: python123
# Password correct. Login successful.

# Key points:
# while attempts < 3        -> maximum 3 attempts
# attempts = attempts + 1   -> each wrong password increases attempts
# break                     -> a correct password stops the loop

# Note: If the correct password is entered on the 2nd or 3rd try, attempts stays below 3,
# so "Account Locked" is not shown. It appears only after 3 wrong attempts.