# 2. Multiplication Table Generator
# Take a number from the user and print its multiplication table from 1 × N through 10 × N using a for loop. Then modify the program so the ending range can also be supplied by the user.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(i, "×", n, "=", i * n)
    

# Taking a number input from the user
## n = int(input("Enter a number: "))

# The loop will run from 1 to 10
# range(1, 11) does not include 11
# Therefore, the values will be 1, 2, 3, ..., 10
# for i in range(1, 11):

    # Multiplying the current number i by n
    # Example: i = 2 and n = 5
    # 2 * 5 = 10
##    print(i, "×", n, "=", i * n)

# Example:
# If the user enters n = 5:
#
# 1 × 5 = 5
# 2 × 5 = 10
# 3 × 5 = 15
# 4 × 5 = 20
# 5 × 5 = 25
# 6 × 5 = 30
# 7 × 5 = 35
# 8 × 5 = 40
# 9 × 5 = 45
# 10 × 5 = 50