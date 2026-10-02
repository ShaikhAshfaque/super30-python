# Numbers ki ek list bana rahe hain
numbers = [10, 5, 25, 3, 15, 8]

# List ke first number ko initially largest maan rahe hain
# numbers[0] ka matlab list ka first element hai
largest = numbers[0]

# List ke first number ko initially smallest maan rahe hain
smallest = numbers[0]

# List ke har number par loop chalega
for i in numbers:

    # Check kar rahe hain ki current number largest se bada hai ya nahi
    if i > largest:

        # Agar current number bada hai
        # to largest ko current number se update kar denge
        largest = i

    # Check kar rahe hain ki current number smallest se chhota hai ya nahi
    if i < smallest:

        # Agar current number chhota hai
        # to smallest ko current number se update kar denge
        smallest = i

# Final largest value print kar rahe hain
print("Largest:", largest)

# Final smallest value print kar rahe hain
print("Smallest:", smallest)

# Example:
# numbers = [10, 5, 25, 3, 15, 8]
#
# Starting:
# largest = 10
# smallest = 10
#
# 5 check hua:
# 5 > 10 False
# 5 < 10 True -> smallest = 5
#
# 25 check hua:
# 25 > 10 True -> largest = 25
# 25 < 5 False
#
# 3 check hua:
# 3 > 25 False
# 3 < 5 True -> smallest = 3
#
# 15 aur 8 check hone ke baad bhi
# largest = 25
# smallest = 3
#
# Output:
# Largest: 25
# Smallest: 3
#
# IMPORTANT:
# max() use nahi karna hai
# min() use nahi karna hai
# Hum sirf for loop aur if condition se answer find kar rahe hain