# Student ke marks se total, percentage aur grade nikalne ka function
# Ye paanch subjects ke marks (m1 se m5) leta hai
def student_grade(m1, m2, m3, m4, m5):
    marks = [m1, m2, m3, m4, m5]            # Paanchon marks ko ek list mein daal diya, taaki loop chala sakein

    for m in marks:                         # FOR LOOP: ek-ek karke har subject ke marks check karega
        if m < 0 or m > 100:                # Agar marks 0 se kam ya 100 se zyada hain, to ye galat marks hain
            return "Invalid marks! Marks 0 se 100 ke beech hone chahiye."   # Error message wapas bheja, function yahin ruk gaya

    total = sum(marks)                      # sum() list ke saare marks jod deta hai, yaani total
    percentage = total / 5                  # Total ko 5 se divide kiya (5 subjects hain), isse percentage mila

    # Grade rules: upar se neeche check hota hai, jo pehli condition sach hui wahi grade milega
    if percentage >= 90:                    # 90 ya usse zyada ho to
        grade = "A"                         # Grade A
    elif percentage >= 75:                  # Nahi to 75 ya usse zyada ho to
        grade = "B"                         # Grade B
    elif percentage >= 60:                  # Nahi to 60 ya usse zyada ho to
        grade = "C"                         # Grade C
    elif percentage >= 40:                  # Nahi to 40 ya usse zyada ho to
        grade = "D"                         # Grade D
    else:                                   # Upar ki koi condition match nahi hui, matlab 40 se kam
        grade = "Fail"                      # Grade Fail

    return total, percentage, grade         # Total, percentage aur grade teeno wapas bhej diye


# Function ko use karne ka tarika
print(student_grade(80, 70, 90, 85, 75))    # Function call kiya, output: (400, 80.0, 'B')
print(student_grade(80, 70, 190, 85, 75))   # 190 galat marks hain, output: Invalid marks! Marks 0 se 100 ke beech hone chahiye.

# ---------- Grade rules (jo maine set kiye) ----------
# Percentage      Grade
# 90 ya zyada     A
# 75 - 89         B
# 60 - 74         C
# 40 - 59         D
# 40 se kam       Fail