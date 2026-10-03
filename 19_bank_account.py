




















































# balance mein account ka paisa rahega, shuru mein 0 hai.
balance = 0

# history ek khaali list hai, isme saari transactions likhi jaayengi.
history = []


# Paisa jama (deposit) karne ka function
def deposit(amount):
    global balance                          # global ka matlab: function ke andar bhi bahar wala balance hi change hoga
                                            # (iske bina Python ek naya local variable bana leta)
    if amount <= 0:                         # Check kiya ki amount 0 ya negative to nahi hai
        print("Amount 0 se zyada hona chahiye!")   # Galat amount par message
        return                              # Function yahin ruk gaya, paisa add nahi hoga
    balance = balance + amount              # Amount ko balance mein jod diya
    history.append("Deposit: " + str(amount))      # Transaction list mein save ki (str() number ko text banata hai taaki "Deposit: " ke saath jud sake)
    print("Deposit ho gaya.")               # Confirmation message


# Paisa nikalne (withdraw) ka function
def withdraw(amount):
    global balance                          # Yahan bhi bahar wala balance change karna hai, isliye global
    if amount <= 0:                         # Pehle check kiya ki amount 0 ya negative to nahi
        print("Amount 0 se zyada hona chahiye!")   # Galat amount par message
    elif amount > balance:                  # Sabse zaroori check: nikalne wala paisa balance se zyada to nahi
        print("Balance kam hai! Withdraw nahi ho sakta.")   # Zyada hai to withdraw rok diya
    else:                                   # Amount sahi hai aur balance bhi kaafi hai
        balance = balance - amount          # Balance mein se paisa ghata diya
        history.append("Withdraw: " + str(amount))  # Transaction list mein save ki
        print("Withdraw ho gaya.")          # Confirmation message


# Current balance dikhane ka function
def check_balance():
    print("Current Balance:", balance)      # Sirf balance print karta hai


# Saari transactions dikhane ka function
def transaction_history():
    if len(history) == 0:                   # Agar history list khaali hai
        print("Koi transaction nahi hui.")  # To ye message dikhao
        return                              # Aur function band
    print("--- Transaction History ---")   # Heading print ki
    for t in history:                       # FOR LOOP: history ki har transaction ek-ek karke t mein aayegi
        print(t)                            # Har transaction print ki


# MAIN PROGRAM: ye while loop menu ko baar-baar dikhata rahega
while True:                                 # Infinite loop, jab tak break na aaye program chalta rahega
    print("\n1.Deposit  2.Withdraw  3.Balance  4.History  5.Exit")   # Menu dikhaya
    choice = input("Apna choice chuno: ")   # User ka choice liya

    if choice == "1":                       # Agar choice 1 hai
        deposit(float(input("Amount: ")))   # Amount lekar float (number) mein badla aur deposit chalaya
    elif choice == "2":                     # Agar choice 2 hai
        withdraw(float(input("Amount: ")))  # Amount lekar withdraw chalaya
    elif choice == "3":                     # Agar choice 3 hai
        check_balance()                     # Balance dikhao
    elif choice == "4":                     # Agar choice 4 hai
        transaction_history()               # History dikhao
    elif choice == "5":                     # Agar choice 5 hai
        print("Thank you!")                 # Bye message
        break                               # break se loop khatam, program band
    else:                                   # 1 se 5 ke alawa kuch dala to
        print("Galat choice!")              # Galat choice ka message

# ---------- Example output ----------
# Apna choice chuno: 1
# Amount: 5000
# Deposit ho gaya.
#
# Apna choice chuno: 2
# Amount: 2000
# Withdraw ho gaya.
#
# Apna choice chuno: 2
# Amount: 9000
# Balance kam hai! Withdraw nahi ho sakta.
#
# Apna choice chuno: 3
# Current Balance: 3000.0
#
# Apna choice chuno: 4
# --- Transaction History ---
# Deposit: 5000.0
# Withdraw: 2000.0
#
# Note: Amount mein text (jaise "abc") daalne par float() error dega
# aur program crash ho jaayega. Simple rakhne ke liye ise handle nahi kiya.