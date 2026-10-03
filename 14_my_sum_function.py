# 14. Create Your Own sum() Function
# Write
# def my_sum(numbers)
# It should accept a list of numbers and return their sum without using Python's built-in sum().
 
# def is used to create a function.
# my_sum is the function name and (numbers) is the parameter.
# The function receives a list of numbers, like [10, 20, 30, 40, 50].
# We do not use Python's built-in sum(), we calculate the total ourselves.

def my_sum(numbers):
    total = 0                       # start the total at 0, each number is added to it

    for number in numbers:          # take each number from the list one by one
        total = total + number      # add the number to the total
        # Step by step for [10, 20, 30, 40, 50]:
        # 0 + 10 = 10
        # 10 + 20 = 30
        # 30 + 30 = 60
        # 60 + 40 = 100
        # 100 + 50 = 150

    return total                    # return sends the final answer out of the function (150 here)


numbers = [10, 20, 30, 40, 50]      # create a list of numbers

result = my_sum(numbers)            # send the list to my_sum(), result becomes 150

print("Total:", result)


# Output:
# Total: 150

# More examples:
# my_sum([1, 2, 3])       # 6
# my_sum([2.5, 1.5])      # 4.0
# my_sum([])              # 0 (empty list, the loop never runs, so total stays 0)

# Important point:
# The main goal of this assignment is to not use the built-in sum().
# Wrong:  sum(numbers)
# Right:  my_sum(numbers)
# Remember: function -> loop -> total -> return