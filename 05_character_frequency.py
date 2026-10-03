# 5. Character Frequency Counter
# Take a string from the user and calculate how many times each character occurs. Example: "banana" should identify the frequencies of b, a, and n.


text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] = frequency[character] + 1
    else:
       frequency[character] = 1

print("Character Frequency:")

for i in frequency:
    print(i, ":", frequency[i])







# Taking a string input from the user
## text = input("Enter a string: ")

# Creating an empty dictionary
# This dictionary will store the frequency of each character
## frequency = {}

# The loop will run for each character in the string
# Example: In "banana", b, a, n, a, n, a will be checked one by one
## for i in text:

    # Checking whether the current character
    # is already available in the dictionary
    ## if i in frequency:

        # If the character is already in the dictionary
        # then adding 1 to its existing frequency
        ## frequency[i] = frequency[i] + 1

    ## else:

        # If the character is found for the first time
        # then setting its frequency to 1
        ## frequency[i] = 1

# Printing the heading
## print("Character Frequency:")

# The loop will run for each character in the dictionary
## for i in frequency:

    # Printing the character and its frequency
    ## print(i, ":", frequency[i])

# Example:
# If the input is "banana":
#
# b is found for the first time -> b : 1
# a is found for the first time -> a : 1
# n is found for the first time -> n : 1
# a is found again               -> a : 2
# n is found again               -> n : 2
# a is found again               -> a : 3
#
# Final Output:
# Character Frequency:
# b : 1
# a : 3
# n : 2