



























# 11. Password Retry System

password = "python123"                      # Pehle se tay (predefined) sahi password. User ko isi se match karna hai
attempts = 0                                # Attempts ko 0 se shuru kiya, kyunki abhi user ne koi koshish nahi ki

while attempts < 3:                         # WHILE LOOP: jab tak attempts 3 se kam hain, password poochta rahega (maximum 3 attempts)
    user_password = input("Enter password: ")   # User se password liya aur user_password mein save kiya

    if user_password == password:           # Check kiya ki user ka password sahi password ke barabar hai ya nahi
        print("Password correct. Login successful.")   # Sahi hai to login successful ka message
        break                               # break se while loop turant ruk gaya, ab aur attempts nahi poochhe jaayenge
    else:                                   # Password match nahi hua
        attempts = attempts + 1             # Attempts 1 badha diye (0 -> 1, 1 -> 2, 2 -> 3)
        print("Incorrect password.")        # Galat password ka message

if attempts == 3:                           # Loop ke baad check kiya: agar attempts 3 ho gaye, matlab teeno baar galat password dala
    print("Account Locked")                 # To account lock ho gaya


# ---------- Example: 3 baar galat password ----------
# Enter password: abc
# Incorrect password.
# Enter password: xyz
# Incorrect password.
# Enter password: 123
# Incorrect password.
# Account Locked

# ---------- Example: sahi password ----------
# Enter password: abc
# Incorrect password.
# Enter password: python123
# Password correct. Login successful.

# ---------- Yaad rakhne wali 3 important cheezein ----------
# while attempts < 3          -> maximum 3 attempts
# attempts = attempts + 1     -> galat password par attempt badhta hai
# break                       -> sahi password milte hi loop ruk jaata hai

# Note: Agar user 2nd ya 3rd attempt mein sahi password daale, to attempts 3 nahi hote,
# isliye "Account Locked" nahi dikhta. Ye sirf teeno baar galat hone par dikhta hai.