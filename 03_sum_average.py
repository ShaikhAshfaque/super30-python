# Numbers ki ek list bana rahe hain
numbers = [10, 20, 30, 40, 50]

# Starting mein total ko 0 rakhenge
# Abhi tak koi number add nahi hua hai
total = 0

# List ke har number par loop chalega
for i in numbers:

    # Current number ko total mein add kar rahe hain
    # Example: pehle 0 + 10 = 10
    total = total + i

# Average nikalne ke liye total ko
# list ke total numbers ki quantity se divide kar rahe hain
# len(numbers) batata hai list mein kitne numbers hain
average = total / len(numbers)

# Total print kar rahe hain
print("Total:", total)

# Average print kar rahe hain
print("Average:", average)

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
# Ab total = 150
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
# sum(numbers) use nahi karna hai
# Humne loop ke through manually total calculate kiya hai