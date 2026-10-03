# 10. ATM Withdrawal Simulator using while
# Start with a balance of ₹10,000. Continuously show the user options to check balance, deposit money, withdraw money, or exit. The program should continue until the user explicitly chooses Exit.


balance = 10000                     # starting balance is Rs. 10,000

while True:                         # runs again and again until the user chooses Exit
    print("\n===== ATM MENU =====") # \n prints an empty line first
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")   # take the user's choice

    # Option 1: Check balance
    if choice == "1":
        print("Current Balance: ₹", balance)

    # Option 2: Deposit
    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))   # float allows decimals

        if amount > 0:                      # amount must be greater than 0
            balance = balance + amount      # add the amount to the balance
            print("Money deposited successfully.")
            print("Updated Balance: ₹", balance)
        else:
            print("Enter a valid amount.")

    # Option 3: Withdraw
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount > 0 and amount <= balance:    # valid amount and not more than the balance
            balance = balance - amount          # subtract the amount from the balance
            print("Withdrawal successful.")
            print("Remaining Balance: ₹", balance)
        elif amount > balance:                  # asking for more than the balance
            print("Insufficient balance.")
        else:                                   # amount is 0 or negative
            print("Enter a valid amount.")

    # Option 4: Exit
    elif choice == "4":
        print("Thank you for using the ATM.")
        break                       # break stops the while loop, so the program ends

    # Any other input
    else:
        print("Invalid choice. Please try again.")


# Example output:
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

# Assignment requirements:
# Starting balance Rs. 10,000          -> balance = 10000
# while loop                           -> while True
# Check balance / Deposit / Withdraw   -> if / elif choices
# Insufficient balance check           -> elif amount > balance
# Exit option                          -> break

# Note: The balance shows as 12000.0 after a deposit because float() is used.
# Typing text like "abc" as the amount will cause an error in float().