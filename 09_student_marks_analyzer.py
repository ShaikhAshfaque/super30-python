#9.Student Marks Analyzer
# Store marks of multiple students in a list. Using loops, calculate highest marks, lowest marks, average marks, number of students who passed, and number who failed. Consider 40 as the passing mark.

# Marks of multiple students stored in a list
marks = [85, 72, 38, 91, 45, 29, 67, 55]

# Starting values
highest = marks[0]          # assume the first student's marks are the highest
lowest = marks[0]           # assume the first student's marks are the lowest
total = 0                   # sum of all marks, starts at 0
passed = 0                  # count of students who passed
failed = 0                  # count of students who failed

# Loop through each student's marks one by one
for mark in marks:

    total = total + mark            # add the marks to the total

    if mark > highest:              # bigger than the current highest?
        highest = mark              # update highest

    if mark < lowest:               # smaller than the current lowest?
        lowest = mark               # update lowest

    if mark >= 40:                  # 40 or more means pass
        passed = passed + 1
    else:                           # below 40 means fail
        failed = failed + 1

# Average = total marks / number of students
average = total / len(marks)        # len(marks) gives 8

# Print the results
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Passed:", passed)
print("Students Failed:", failed)

# Output:
# Highest Marks: 91
# Lowest Marks: 29
# Average Marks: 60.25
# Students Passed: 6
# Students Failed: 2

# Working:
# Total = 85 + 72 + 38 + 91 + 45 + 29 + 67 + 55 = 482
# Average = 482 / 8 = 60.25
# Passed (40 or more): 85, 72, 91, 45, 67, 55 = 6
# Failed (below 40): 38, 29 = 2

# Note: highest and lowest start from the first mark, not 0,
# so the answer is correct for any list of marks.