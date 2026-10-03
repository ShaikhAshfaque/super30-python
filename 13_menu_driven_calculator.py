# 13. Menu-Driven Calculator
# Build a continuously running calculator using while. Provide Addition, Subtraction, Multiplication, Division, Modulus, and Exit operations. Handle division by zero properly.

# The calculator keeps running because of the while loop.
# The menu shows again and again until the user chooses Exit (6).

while True:                                 # runs until break
    print("\n===== CALCULATOR =====")       # \n prints an empty line first
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice: ")   # take the user's choice

    # Exit check
    if choice == "6":
        print("Calculator closed.")
        break                               # stop the loop, so the calculator closes

    # Take the numbers (float allows decimals like 20.5)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the chosen operation
    if choice == "1":                       # Addition
        print("Result:", num1 + num2)

    elif choice == "2":                     # Subtraction
        print("Result:", num1 - num2)

    elif choice == "3":                     # Multiplication
        print("Result:", num1 * num2)

    elif choice == "4":                     # Division
        if num2 == 0:                       # dividing by 0 causes an error, so check first
            print("Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)

    elif choice == "5":                     # Modulus (% gives the remainder, e.g. 10 % 3 = 1)
        if num2 == 0:                       # modulus by 0 is also not allowed
            print("Cannot find modulus with zero.")
        else:
            print("Result:", num1 % num2)

    else:                                   # no valid choice matched
        print("Invalid choice. Please try again.")


# Example output:
# ===== CALCULATOR =====
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulus
# 6. Exit
#
# Enter your choice: 1
# Enter first number: 20
# Enter second number: 5
# Result: 25.0
#
# Enter your choice: 4
# Enter first number: 20
# Enter second number: 0
# Cannot divide by zero.
#
# Enter your choice: 6
# Calculator closed.

# Key points:
# while True  -> keeps the calculator running
# if / elif   -> chooses the operation
# +  -  *  /  -> add, subtract, multiply, divide
# %           -> modulus (remainder)
# break       -> stops the loop
# num2 == 0   -> handles division by zero

# Note: If the choice is invalid (like 9), both numbers are still asked first,
# and then "Invalid choice" is shown. It is kept this way to stay simple.
# Typing text like "abc" as a number will cause an error in float().