# 4.Find Maximum and Minimum Without max() / min()
# Write a program that finds the largest and smallest values in a list using loops only.


numbers = [10, 5, 25, 3, 15, 8]

largest = numbers[0]
smallest = numbers[0]


for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i
print("Largest:", largest)
print("Smallest:", smallest)








# Making a list of numbers
## numbers = [10, 5, 25, 3, 15, 8]

# Initially considering the first number in the list as the largest
# numbers[0] means the first element of the list
## largest = numbers[0]

# Initially considering the first number in the list as the smallest
## smallest = numbers[0]

# The loop will run for each number in the list
## for i in numbers:

    # Checking whether the current number is greater than the largest
    ## if i > largest:

        # If the current number is greater
        # then updating largest with the current number
        ## largest = i

    # Checking whether the current number is smaller than the smallest
    ## if i < smallest:

        # If the current number is smaller
        # then updating smallest with the current number
        ## smallest = i

# Printing the final largest value
## print("Largest:", largest)

# Printing the final smallest value
## print("Smallest:", smallest)

# Example:
# numbers = [10, 5, 25, 3, 15, 8]
#
# Starting:
# largest = 10
# smallest = 10
#
# 5 is checked:
# 5 > 10 False
# 5 < 10 True -> smallest = 5
#
# 25 is checked:
# 25 > 10 True -> largest = 25
# 25 < 5 False
#
# 3 is checked:
# 3 > 25 False
# 3 < 5 True -> smallest = 3
#
# After checking 15 and 8:
# largest = 25
# smallest = 3
#
# Output:
# Largest: 25
# Smallest: 3
#
# IMPORTANT:
# Do not use max()
# Do not use min()
# We are finding the answer using only a for loop and if conditions