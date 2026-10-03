# 16. Student Grade Function
# This function takes the marks of five subjects (m1 to m5)
# and returns the total, percentage and grade.

def student_grade(m1, m2, m3, m4, m5):
    marks = [m1, m2, m3, m4, m5]        # put all five marks in a list so we can use a loop

    for m in marks:                     # check each subject's marks one by one
        if m < 0 or m > 100:            # marks below 0 or above 100 are invalid
            return "Invalid marks! Marks must be between 0 and 100."   # return the error, function stops here

    total = sum(marks)                  # sum() adds all the marks in the list
    percentage = total / 5              # divide by 5 because there are 5 subjects

    # Grade rules: checked from top to bottom, the first true condition gives the grade
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:                               # below 40
        grade = "Fail"

    return total, percentage, grade     # send back total, percentage and grade together


# How to use the function
print(student_grade(80, 70, 90, 85, 75))    # Output: (400, 80.0, 'B')
print(student_grade(80, 70, 190, 85, 75))   # 190 is invalid, Output: Invalid marks! Marks must be between 0 and 100.

# Grade rules:
# Percentage      Grade
# 90 or more      A
# 75 - 89         B
# 60 - 74         C
# 40 - 59         D
# below 40        Fail