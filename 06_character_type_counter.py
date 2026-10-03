# 6. Vowel, Consonant, Digit and Space Counter
# Create a program that analyzes a sentence and counts vowels, consonants, digits, spaces, and special characters separately.

text = input("Enter a sentence: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0



for character in text:
    if character.lower() in "aeiou":
         vowels += 1
    elif character.isalpha():
         consonants = consonants + 1
    elif character == " ":
         spaces = spaces + 1
    else:
         special_characters = special_characters + 1


print("Vowels:", vowels)
print(consonants)
print(digits)
print(spaces)
print(special_characters)




# Taking a sentence input from the user
## text = input("Enter a sentence: ")

# Variable for counting vowels
# Starting value is set to 0 because no vowel has been counted yet
## vowels = 0

# Variable for counting consonants
## consonants = 0

# Variable for counting digits (0-9)
## digits = 0

# Variable for counting spaces
## spaces = 0

# Variable for counting special characters
## special_characters = 0

# The loop will run for each character in the sentence
# Example: In "Hello 123!", H, e, l, l, o, space, 1, 2, 3, ! will be checked one by one
## for i in text:

    # i.lower() converts the character to lowercase
    # Checking in "aeiou" whether the character is a vowel or not
    # Example: A -> a, so capital A will also be counted as a vowel
    ## if i.lower() in "aeiou":

        # If the character is a vowel, the vowel count will increase by 1
        ## vowels += 1

    # isalpha() checks whether the character is an alphabet or not
    # If it is not a vowel and is an alphabet, then it will be a consonant
    ## elif i.isalpha():

        # Increasing the consonant count by 1
        ## consonants += 1

    # isdigit() checks whether the character is a digit from 0-9
    ## elif i.isdigit():

        # If it is a digit, the digit count will increase by 1
        ## digits += 1

    # Checking whether the current character is a normal space " " or not
    ## elif i == " ":

        # If it is a space, the space count will increase by 1
        ## spaces += 1

    # If the character is not a vowel, consonant, digit, or space
    # Then it will be considered a special character
    # Example: !, @, #, $, %, & etc.
    ## else:

        # Increasing the special character count by 1
        ## special_characters += 1

# Printing the total number of vowels
## print("Vowels:", vowels)

# Printing the total number of consonants
## print("Consonants:", consonants)

# Printing the total number of digits
## print("Digits:", digits)

# Printing the total number of spaces
## print("Spaces:", spaces)

# Printing the total number of special characters
## print("Special Characters:", special_characters)