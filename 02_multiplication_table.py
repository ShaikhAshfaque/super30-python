# 2.Multiplication Table Generator
# Take a number from the user and print its multiplication table from 1 × N through 10 × N using a for loop. Then modify the program so the ending range can also be supplied by the user.

number = int(input("Enter a number: "))
end = int(input("Enter a ending range: "))

for i in range(1, end+1):
    print(i, "X", number, "=", i * number)


# User se ek number input le rahe hain
# n = int(input("Enter a number: "))

# 1 se 10 tak loop chalega
# range(1, 11) mein 11 include nahi hota
# Isliye values 1, 2, 3, ..., 10 hongi
#for i in range(1, 11):

    # Current number i ko n se multiply kar rahe hain
    # Example: i = 2 aur n = 5
    # 2 * 5 = 10
#    print(i, "×", n, "=", i * n)

# Example:
# Agar user n = 5 enter karega:
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