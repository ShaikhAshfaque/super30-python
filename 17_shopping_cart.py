# cart ek khaali dictionary hai. Ye hamara shopping cart hai.
# Isme item ka naam "key" hoga, aur uska price aur quantity "value".
# Example: {"pen": {"price": 10.0, "qty": 3}}
# Ise function ke bahar rakha taaki saare functions use kar sakein.
cart = {}


# Cart mein item add karne ka function
def add_item(name, price, qty):
    if price <= 0 or qty <= 0:              # Validation: price ya quantity 0 ya negative to nahi
        print("Price aur quantity 0 se zyada honi chahiye!")   # Galat value par message
        return                              # Function yahin ruk gaya, item add nahi hoga
    if name in cart:                        # Check kiya ki item pehle se cart mein hai ya nahi
        cart[name]["qty"] += qty            # Hai to sirf quantity badha di (+= matlab purani qty mein jodna)
    else:                                   # Item cart mein nahi hai
        cart[name] = {"price": price, "qty": qty}   # To naya item price aur qty ke saath bana diya
    print(name, "cart mein add ho gaya.")   # User ko confirmation message dikhaya


# Cart se item hatane ka function
def remove_item(name):
    if name in cart:                        # Check kiya ki item cart mein hai ya nahi
        del cart[name]                      # Hai to del se use cart se hata diya
        print(name, "cart se hata diya.")   # Confirmation message
    else:                                   # Item cart mein nahi hai
        print("Ye item cart mein nahi hai!")   # Error message


# Poora cart dikhane ka function
def view_cart():
    if len(cart) == 0:                      # len(cart) == 0 matlab cart khaali hai
        print("Cart khaali hai.")           # Khaali hone ka message
        return                              # Function band
    print("--- Aapka Cart ---")             # Heading print ki
    for name in cart:                       # FOR LOOP: cart ke har item ka naam ek-ek karke name mein aayega
        price = cart[name]["price"]         # Us item ka price dictionary se nikala
        qty = cart[name]["qty"]             # Us item ki quantity nikali
        print(name, "| Price:", price, "| Qty:", qty, "| Subtotal:", price * qty)
        # Upar ki line item ka naam, price, qty aur subtotal (price * qty) ek line mein print karti hai


# Cart ka total amount nikalne ka function
def calculate_total():
    total = 0                               # Total ko 0 se shuru kiya
    for name in cart:                       # FOR LOOP: har item par ek-ek karke jao
        total = total + cart[name]["price"] * cart[name]["qty"]   # Har item ka price * qty total mein jodte jao
    return total                            # Final amount wapas bhej diya


# Checkout karne ka function
def checkout():
    if len(cart) == 0:                      # Agar cart khaali hai
        print("Cart khaali hai, checkout nahi ho sakta.")   # To checkout nahi ho sakta
        return False                        # False wapas bheja, matlab checkout nahi hua
    view_cart()                             # Cart ka saara saamaan dikhaya
    print("Total Bill:", calculate_total()) # Total bill print kiya
    print("Thank you! Shopping ke liye.")   # Thank you message
    return True                             # True wapas bheja, matlab checkout ho gaya (loop ko batata hai ki rukna hai)


# MAIN PROGRAM: ye while loop menu ko baar-baar dikhata rahega
while True:                                 # WHILE LOOP: infinite loop, jab tak break na aaye chalta rahega
    print("\n1.Add  2.Remove  3.View  4.Total  5.Checkout  6.Exit")   # Menu dikhaya
    choice = input("Apna choice chuno: ")   # User ka choice string mein liya

    if choice == "1":                       # Agar choice 1 hai (Add)
        name = input("Item ka naam: ")      # Item ka naam liya
        price = float(input("Price: "))     # Price liya aur float (number) mein badla
        qty = int(input("Quantity: "))      # Quantity li aur int (poora number) mein badli
        add_item(name, price, qty)          # add_item function chalaya
    elif choice == "2":                     # Agar choice 2 hai (Remove)
        remove_item(input("Hatane wale item ka naam: "))   # Naam lekar seedha remove_item chalaya
    elif choice == "3":                     # Agar choice 3 hai (View)
        view_cart()                         # Cart dikhao
    elif choice == "4":                     # Agar choice 4 hai (Total)
        print("Total:", calculate_total())  # Total amount print karo
    elif choice == "5":                     # Agar choice 5 hai (Checkout)
        if checkout():                      # Checkout True return kare (successful ho gaya)
            break                           # To break se loop khatam, program band
                                            # (cart khaali ho to False aata hai aur loop chalta rehta hai)
    elif choice == "6":                     # Agar choice 6 hai (Exit)
        print("Bye!")                       # Bye message
        break                               # break se seedha program band
    else:                                   # 1 se 6 ke alawa kuch dala to
        print("Galat choice! 1 se 6 ke beech chuno.")   # Galat choice ka message


# ---------- Output (example run) ----------
# Apna choice chuno: 1
# Item ka naam: pen
# Price: 10
# Quantity: 3
# pen cart mein add ho gaya.
#
# Apna choice chuno: 5
# --- Aapka Cart ---
# pen | Price: 10.0 | Qty: 3 | Subtotal: 30.0
# Total Bill: 30.0
# Thank you! Shopping ke liye.

# ---------- Aur examples ----------
# add_item("book", 50, 2)    # book cart mein add ho gaya.
# add_item("book", 50, 1)    # book ki qty 3 ho jaayegi
# remove_item("laptop")      # Ye item cart mein nahi hai!

# Note: Price ya quantity mein text (jaise "abc") daalne par float() / int() error dega
# aur program crash ho jaayega. Simple rakhne ke liye ise handle nahi kiya.