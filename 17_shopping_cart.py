# 17. Shopping Cart using Functions

# cart is an empty dictionary. It is our shopping cart.
# The item name is the key, and its price and quantity are the value.
# Example: {"pen": {"price": 10.0, "qty": 3}}
# It is kept outside the functions so all functions can use it.
cart = {}


# Function to add an item to the cart
def add_item(name, price, qty):
    if price <= 0 or qty <= 0:              # validation: price and quantity must be above 0
        print("Price and quantity must be greater than 0!")
        return                              # stop here, the item is not added
    if name in cart:                        # is the item already in the cart?
        cart[name]["qty"] += qty            # yes, so only increase the quantity
    else:                                   # item is not in the cart
        cart[name] = {"price": price, "qty": qty}   # create a new item with price and qty
    print(name, "added to the cart.")


# Function to remove an item from the cart
def remove_item(name):
    if name in cart:                        # is the item in the cart?
        del cart[name]                      # del removes it from the cart
        print(name, "removed from the cart.")
    else:
        print("This item is not in the cart!")


# Function to show the whole cart
def view_cart():
    if len(cart) == 0:                      # length 0 means the cart is empty
        print("Cart is empty.")
        return
    print("--- Your Cart ---")
    for name in cart:                       # each item name comes into name one by one
        price = cart[name]["price"]         # get the item's price from the dictionary
        qty = cart[name]["qty"]             # get the item's quantity
        print(name, "| Price:", price, "| Qty:", qty, "| Subtotal:", price * qty)
        # the line above prints name, price, qty and subtotal (price * qty) in one line


# Function to calculate the total amount of the cart
def calculate_total():
    total = 0                               # start the total at 0
    for name in cart:                       # go through each item
        total = total + cart[name]["price"] * cart[name]["qty"]   # add price * qty of each item
    return total


# Function to checkout
def checkout():
    if len(cart) == 0:                      # cart is empty
        print("Cart is empty, cannot checkout.")
        return False                        # False means checkout did not happen
    view_cart()                             # show all items
    print("Total Bill:", calculate_total())
    print("Thank you for shopping!")
    return True                             # True means checkout is done (tells the loop to stop)


# MAIN PROGRAM: the while loop keeps showing the menu
while True:                                 # runs until break
    print("\n1.Add  2.Remove  3.View  4.Total  5.Checkout  6.Exit")
    choice = input("Enter your choice: ")   # take the choice as a string

    if choice == "1":                       # Add
        name = input("Item name: ")
        price = float(input("Price: "))     # float allows decimals
        qty = int(input("Quantity: "))      # int is a whole number
        add_item(name, price, qty)
    elif choice == "2":                     # Remove
        remove_item(input("Name of item to remove: "))
    elif choice == "3":                     # View
        view_cart()
    elif choice == "4":                     # Total
        print("Total:", calculate_total())
    elif choice == "5":                     # Checkout
        if checkout():                      # True means checkout was successful
            break                           # stop the loop, the program ends
                                            # (an empty cart returns False, so the loop continues)
    elif choice == "6":                     # Exit
        print("Bye!")
        break                               # stop the program
    else:                                   # anything other than 1 to 6
        print("Wrong choice! Choose between 1 and 6.")


# Output (example run):
# Enter your choice: 1
# Item name: pen
# Price: 10
# Quantity: 3
# pen added to the cart.
#
# Enter your choice: 5
# --- Your Cart ---
# pen | Price: 10.0 | Qty: 3 | Subtotal: 30.0
# Total Bill: 30.0
# Thank you for shopping!

# More examples:
# add_item("book", 50, 2)    # book added to the cart.
# add_item("book", 50, 1)    # book quantity becomes 3
# remove_item("laptop")      # This item is not in the cart!

# Note: Typing text like "abc" as price or quantity will cause an error in float() / int().
# It is not handled here to keep the code simple.