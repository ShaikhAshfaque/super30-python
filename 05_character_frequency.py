# 5.Character Frequency Counter
# Take a string from the user and calculate how many times each character occurs. Example: "banana" should identify the frequencies of b, a, and n.






















# User se ek string input le rahe hain
text = input("Enter a string: ")

# Empty dictionary bana rahe hain
# Is dictionary mein har character ki frequency store hogi
frequency = {}

# String ke har character par loop chalega
# Example: "banana" mein b, a, n, a, n, a ek-ek karke check honge
for i in text:

    # Check kar rahe hain ki current character
    # pehle se dictionary mein available hai ya nahi
    if i in frequency:

        # Agar character already dictionary mein hai
        # to uski existing frequency mein 1 add kar rahe hain
        frequency[i] = frequency[i] + 1

    else:

        # Agar character pehli baar mila hai
        # to uski frequency 1 set kar rahe hain
        frequency[i] = 1

# Heading print kar rahe hain
print("Character Frequency:")

# Dictionary ke har character par loop chalega
for i in frequency:

    # Character aur uski frequency print kar rahe hain
    print(i, ":", frequency[i])

# Example:
# Agar input "banana" hai:
#
# Pehli baar b mila  -> b : 1
# Pehli baar a mila  -> a : 1
# Pehli baar n mila  -> n : 1
# Dobara a mila      -> a : 2
# Dobara n mila      -> n : 2
# Dobara a mila      -> a : 3
#
# Final Output:
# Character Frequency:
# b : 1
# a : 3
# n : 2