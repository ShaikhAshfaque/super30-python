# Loop , While loop, break, continue , Nested end to end with programme

# Python Points — Must Remember
# Understand the question before writing code.
# Identify Input → Process → Output.
# Choose meaningful variable names.
# Always decide the starting value first.
# Count → count = 0
# Total → total = 0
# Attempts → attempts = 0
# Highest/Lowest → start with numbers[0]
# for loop → iterate over items/range.
# while loop → repeat while condition is true.
# if → condition checking.
# == → comparison; = → assignment. 
# % → remainder; useful for Even/Odd.
# range() → ending value is excluded.
# Every while loop needs a proper update/exit.
# while True → use break to exit.
# break → completely stops the loop.
# continue → skips current iteration.
# Maintain correct indentation.
# Remember: LOOP → CONDITION → UPDATE → OUTPUT 🔥

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# 1.Take a number N from the user. 
# Print all numbers from 1 to N, identify whether each number is even or odd, and finally display the total count of even and odd numbers.


# Taking a number N from the user
# N = [1,2,3,4,5,6,7,8,9,10]

# Creating an empty list to store even numbers
# l_even = []

# Creating an empty list to store odd numbers
# l_odd = []

# Loop will run from 1 to N
# N + 1 is used because range() does not include the last number
# for i in range(1, N + 1):

    # Checking whether the remainder is 0 when i is divided by 2
    # % means remainder
    # Remainder 0 = Even number
#    if i % 2 == 0:

        # Printing the current number as Even
#        print(i, "is Even")

        # Adding the current number i to the l_even list
        # append(i) = Add the current number to the list
#        l_even.append(i)

#    else:

        # If the number is not completely divisible by 2
        # then it is an Odd number
#        print(i, "is Odd")

        # Adding the current number i to the l_odd list
#        l_odd.append(i)

# len(l_even) counts the total number of even numbers
# print("Total Even Numbers:", len(l_even))

# len(l_odd) counts the total number of odd numbers
# print("Total Odd Numbers:", len(l_odd))

# Example:
# If N = 10:
#
# 1 is Odd
# 2 is Even
# 3 is Odd
# 4 is Even
# 5 is Odd
# 6 is Even
# 7 is Odd
# 8 is Even
# 9 is Odd
# 10 is Even
#
# Total Even Numbers: 5
# Total Odd Numbers: 5
#
# IMPORTANT:
# append(i) -> Adds the current number i to the list
#
# l_even.append(i) -> Add the current Even number to l_even
# l_odd.append(i)  -> Add the current Odd number to l_odd