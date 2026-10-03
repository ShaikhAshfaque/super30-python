# 10.ATM Withdrawal Simulator using while
#Start with a balance of ₹10,000. Continuously show the user options to check balance, deposit money, withdraw money, or exit. 
#The program should continue until the user explicitly chooses Exit.




# 10. ATM Withdrawal Simulator using while

balance = 10000                             # Shuru mein account mein Rs.10,000 hain

while True:                                 # WHILE LOOP: infinite loop, jab tak user Exit na chune menu baar-baar aata rahega
    print("\n===== ATM MENU =====")         # Menu ki heading (\n se pehle ek khaali line aati hai)
    print("1. Check Balance")               # Option 1
    print("2. Deposit Money")               # Option 2
    print("3. Withdraw Money")              # Option 3
    print("4. Exit")                        # Option 4

    choice = input("Enter your choice: ")   # User ka choice liya

    # ---------- Option 1: Balance check ----------
    if choice == "1":                       # Agar choice 1 hai
        print("Current Balance: ₹", balance)    # Abhi ka balance print kiya

    # ---------- Option 2: Deposit ----------
    elif choice == "2":                     # Agar choice 2 hai
        amount = float(input("Enter deposit amount: ₹"))   # Kitna paisa jama karna hai, wo liya (float se decimal bhi chalega)

        if amount > 0:                      # Check kiya ki amount 0 se zyada hai (sahi amount)
            balance = balance + amount      # Amount balance mein jod diya
            print("Money deposited successfully.")     # Success message
            print("Updated Balance: ₹", balance)       # Naya balance dikhaya
        else:                               # Amount 0 ya negative hai
            print("Enter a valid amount.")  # Galat amount ka message

    # ---------- Option 3: Withdraw ----------
    elif choice == "3":                     # Agar choice 3 hai
        amount = float(input("Enter withdrawal amount: ₹"))   # Kitna paisa nikalna hai, wo liya

        if amount > 0 and amount <= balance:    # Amount sahi hai AUR balance se zyada nahi hai
            balance = balance - amount      # Balance mein se paisa ghata diya
            print("Withdrawal successful.") # Success message
            print("Remaining Balance: ₹", balance)    # Bacha hua balance dikhaya
        elif amount > balance:              # Nikalne wala amount balance se zyada hai
            print("Insufficient balance.")  # Balance kam hai, withdraw nahi hoga
        else:                               # Baaki case: amount 0 ya negative hai
            print("Enter a valid amount.")  # Galat amount ka message

    # ---------- Option 4: Exit ----------
    elif choice == "4":                     # Agar choice 4 hai
        print("Thank you for using the ATM.")   # Thank you message
        break                               # break se while loop ruk gaya, program khatam. Sirf yahi Exit ka raasta hai

    # ---------- Galat choice ----------
    else:                                   # 1 se 4 ke alawa kuch dala to
        print("Invalid choice. Please try again.")     # Galat choice ka message, loop phir se menu dikhayega


# ---------- Example output ----------
# ===== ATM MENU =====
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
#
# Enter your choice: 1
# Current Balance: ₹ 10000
#
# Enter your choice: 2
# Enter deposit amount: ₹2000
# Money deposited successfully.
# Updated Balance: ₹ 12000.0
#
# Enter your choice: 3
# Enter withdrawal amount: ₹5000
# Withdrawal successful.
# Remaining Balance: ₹ 7000.0
#
# Enter your choice: 4
# Thank you for using the ATM.

# ---------- Assignment requirements ----------
# Starting balance Rs.10,000       -> balance = 10000
# while loop                       -> while True
# Check balance / Deposit / Withdraw -> if / elif choices
# Insufficient balance check       -> elif amount > balance
# Exit option                      -> break
# Exit tak continuously run        -> while True

# Note: Deposit ya withdraw ke baad balance 12000.0 jaise decimal mein dikhta hai,
# kyunki amount float() se liya gaya hai.
# Amount mein text (jaise "abc") daalne par float() error dega.