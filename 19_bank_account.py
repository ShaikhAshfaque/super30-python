# Bank Account Simulator

# balance holds the account money, it starts at 0.
balance = 0

# history is an empty list, all transactions are saved in it.
history = []


# Function to deposit money
def deposit(amount):
    global balance                          # global means the balance outside the function is changed
                                            # (without it, Python would create a new local variable)
    if amount <= 0:                         # amount must be above 0
        print("Amount must be greater than 0!")
        return                              # stop here, no money is added
    balance = balance + amount              # add the amount to the balance
    history.append("Deposit: " + str(amount))   # save the transaction (str() turns the number into text so it can join with "Deposit: ")
    print("Deposit successful.")


# Function to withdraw money
def withdraw(amount):
    global balance                          # we change the outside balance, so global is needed
    if amount <= 0:                         # amount must be above 0
        print("Amount must be greater than 0!")
    elif amount > balance:                  # most important check: cannot withdraw more than the balance
        print("Insufficient balance! Cannot withdraw.")
    else:                                   # amount is valid and balance is enough
        balance = balance - amount          # subtract the amount from the balance
        history.append("Withdraw: " + str(amount))  # save the transaction
        print("Withdrawal successful.")


# Function to show the current balance
def check_balance():
    print("Current Balance:", balance)


# Function to show all transactions
def transaction_history():
    if len(history) == 0:                   # history list is empty
        print("No transactions yet.")
        return
    print("--- Transaction History ---")
    for t in history:                       # each transaction comes into t one by one
        print(t)


# MAIN PROGRAM: the while loop keeps showing the menu
while True:                                 # runs until break
    print("\n1.Deposit  2.Withdraw  3.Balance  4.History  5.Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        deposit(float(input("Amount: ")))   # take the amount as a number and call deposit
    elif choice == "2":
        withdraw(float(input("Amount: ")))
    elif choice == "3":
        check_balance()
    elif choice == "4":
        transaction_history()
    elif choice == "5":
        print("Thank you!")
        break                               # stop the loop, the program ends
    else:                                   # anything other than 1 to 5
        print("Wrong choice!")


# Example output:
# Enter your choice: 1
# Amount: 5000
# Deposit successful.
#
# Enter your choice: 2
# Amount: 2000
# Withdrawal successful.
#
# Enter your choice: 2
# Amount: 9000
# Insufficient balance! Cannot withdraw.
#
# Enter your choice: 3
# Current Balance: 3000.0
#
# Enter your choice: 4
# --- Transaction History ---
# Deposit: 5000.0
# Withdraw: 2000.0

# Note: Typing text like "abc" as the amount will cause an error in float().
# It is not handled here to keep the code simple.