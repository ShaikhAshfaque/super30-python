# 3.Sum and Average Without sum()
# Given a list of numbers, calculate the total and average using a loop. Do not use Python's built-in sum() function.



numbers = [10, 20, 30, 40, 50]

total = 0

for i in numbers:
    total = total + i

average = total / len(numbers)


print("Total:", total)
print("Average:", average)





# Making a list of numbers
## numbers = [10, 20, 30, 40, 50]

# Setting total to 0 at the beginning
# No number has been added yet
## total = 0

# The loop will run for each number in the list
# for i in numbers:

    # Adding the current number to total
    # Example: first 0 + 10 = 10
##    total = total + i

# To calculate the average, dividing total by
# the total number of numbers in the list
# len(numbers) tells us how many numbers are in the list
## average = total / len(numbers)

# Printing the total
## print("Total:", total)

# Printing the average
## print("Average:", average)

# Step-by-step:
# Starting total = 0
#
# i = 10
# total = 0 + 10
# total = 10
#
# i = 20
# total = 10 + 20
# total = 30
#
# i = 30
# total = 30 + 30
# total = 60
#
# i = 40
# total = 60 + 40
# total = 100
#
# i = 50
# total = 100 + 50
# total = 150
#
# Now total = 150
#
# len(numbers) = 5
# Average = 150 / 5
# Average = 30.0
#
# Output:
# Total: 150
# Average: 30.0
#
# IMPORTANT:
# Do not use sum(numbers)
# We calculated the total manually using a loop