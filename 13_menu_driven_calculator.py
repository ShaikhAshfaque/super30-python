# 13. Menu-Driven Calculator

# Ye calculator while loop ki wajah se continuously chalta rahega.
# Jab tak user Exit (6) choose nahi karta, menu baar-baar dikhega.

while True:                                 # Infinite loop, jab tak break na aaye calculator chalta rahega
    print("\n===== CALCULATOR =====")       # Heading print ki (\n se pehle ek khaali line aati hai)
    print("1. Addition")                    # Option 1
    print("2. Subtraction")                 # Option 2
    print("3. Multiplication")              # Option 3
    print("4. Division")                    # Option 4
    print("5. Modulus")                     # Option 5
    print("6. Exit")                        # Option 6

    choice = input("Enter your choice: ")   # User ka choice liya (1, 2, 3... mein se koi ek)

    # ---------- Exit check ----------
    if choice == "6":                       # Agar user ne 6 choose kiya
        print("Calculator closed.")         # Calculator band hone ka message
        break                               # break loop ko rok deta hai, isliye calculator close ho jaata hai

    # ---------- Numbers lena ----------
    num1 = float(input("Enter first number: "))    # Pehla number liya aur float mein badla (decimal numbers bhi chalenge, jaise 20.5)
    num2 = float(input("Enter second number: "))   # Doosra number liya aur float mein badla

    # ---------- Operation chunna ----------
    if choice == "1":                       # Agar choice 1 hai (Addition)
        print("Result:", num1 + num2)       # Jodke result print kiya. Jaise 20 + 5 = 25

    elif choice == "2":                     # Agar choice 2 hai (Subtraction)
        print("Result:", num1 - num2)       # Ghatake result print kiya. Jaise 20 - 5 = 15

    elif choice == "3":                     # Agar choice 3 hai (Multiplication)
        print("Result:", num1 * num2)       # Guna karke result print kiya. Jaise 20 * 5 = 100

    elif choice == "4":                     # Agar choice 4 hai (Division)
        if num2 == 0:                       # Zaroori check: doosra number 0 hai kya? (20 / 0 se Python mein error aata hai)
            print("Cannot divide by zero.") # 0 hai to error ki jagah ye message dikhaya
        else:                               # Doosra number 0 nahi hai
            print("Result:", num1 / num2)   # To division kar diya

    elif choice == "5":                     # Agar choice 5 hai (Modulus)
        # % modulus operator hai, ye division ka remainder deta hai. Jaise 10 % 3 = 1
        if num2 == 0:                       # Yahan bhi 0 check kiya, kyunki 0 se modulus bhi nahi ho sakta
            print("Cannot find modulus with zero.")   # 0 hai to message
        else:                               # 0 nahi hai
            print("Result:", num1 % num2)   # To remainder print kiya

    else:                                   # Upar ke koi bhi choice match nahi hue
        print("Invalid choice. Please try again.")    # Galat choice ka message


# ---------- Example output ----------
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

# ---------- Interview / Assignment mein yaad rakho ----------
# while True    → calculator continuously run karne ke liye
# if / elif     → operation choose karne ke liye
# +             → Addition
# -             → Subtraction
# *             → Multiplication
# /             → Division
# %             → Modulus (remainder)
# break         → loop stop karne ke liye
# num2 == 0     → division by zero handle karne ke liye

# Note: Is code mein galat choice (jaise 9) dene par bhi pehle dono numbers maange jaate hain,
# phir "Invalid choice" aata hai. Simple rakhne ke liye aise hi rakha hai.
# Numbers mein text (jaise "abc") daalne par float() error dega.