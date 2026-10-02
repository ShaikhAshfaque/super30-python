# User se ek sentence input le rahe hain
text = input("Enter a sentence: ")

# Vowels ki counting ke liye variable
# Starting value 0 rakhi hai kyunki abhi koi vowel count nahi hua
vowels = 0

# Consonants ki counting ke liye variable
consonants = 0

# Digits (0-9) ki counting ke liye variable
digits = 0

# Spaces ki counting ke liye variable
spaces = 0

# Special characters ki counting ke liye variable
special_characters = 0

# Sentence ke har ek character par loop chalega
# Example: "Hello 123!" mein H, e, l, l, o, space, 1, 2, 3, ! ek-ek karke check honge
for i in text:

    # i.lower() character ko lowercase mein convert karta hai
    # "aeiou" mein check kar rahe hain ki character vowel hai ya nahi
    # Example: A -> a, isliye capital A bhi vowel count hoga
    if i.lower() in "aeiou":

        # Agar character vowel hai to vowels ki counting 1 se increase hogi
        vowels += 1

    # isalpha() check karta hai ki character alphabet hai ya nahi
    # Agar vowel nahi tha aur alphabet hai, to woh consonant hoga
    elif i.isalpha():

        # Consonant ki counting 1 se increase kar rahe hain
        consonants += 1

    # isdigit() check karta hai ki character 0-9 mein se koi digit hai ya nahi
    elif i.isdigit():

        # Agar digit hai to digits ki counting 1 se increase hogi
        digits += 1

    # Check kar rahe hain ki current character ek normal space " " hai ya nahi
    elif i == " ":

        # Agar space hai to spaces ki counting 1 se increase hogi
        spaces += 1

    # Agar character vowel, consonant, digit ya space nahi hai
    # To woh special character maana jayega
    # Example: !, @, #, $, %, & etc.
    else:

        # Special character ki counting 1 se increase kar rahe hain
        special_characters += 1

# Total vowels print kar rahe hain
print("Vowels:", vowels)

# Total consonants print kar rahe hain
print("Consonants:", consonants)

# Total digits print kar rahe hain
print("Digits:", digits)

# Total spaces print kar rahe hain
print("Spaces:", spaces)

# Total special characters print kar rahe hain
print("Special Characters:", special_characters)