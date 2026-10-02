# 9. Student Marks Analyzer

# Kai students ke marks ek list mein store kiye
marks = [85, 72, 38, 91, 45, 29, 67, 55]

# ---------- Shuruaati values ----------
highest = marks[0]                          # Sabse bade marks: shuru mein pehle student ke marks maan liye (marks[0] = list ka pehla number)
lowest = marks[0]                           # Sabse chhote marks: shuru mein ye bhi pehle student ke marks maan liye
total = 0                                   # Total ko 0 se shuru kiya, isme sab marks jodte jaayenge
passed = 0                                  # Pass hone wale students ki ginti, abhi 0
failed = 0                                  # Fail hone wale students ki ginti, abhi 0

# FOR LOOP: list ke har student ke marks ko ek-ek karke mark mein leta hai
for mark in marks:

    total = total + mark                    # Har student ke marks total mein jod diye

    if mark > highest:                      # Agar ye marks ab tak ke highest se bade hain
        highest = mark                      # To highest ko in marks se badal do

    if mark < lowest:                       # Agar ye marks ab tak ke lowest se chhote hain
        lowest = mark                       # To lowest ko in marks se badal do

    if mark >= 40:                          # Passing mark 40 hai, isliye 40 bhi pass hoga (>= matlab bada ya barabar)
        passed = passed + 1                 # Pass count 1 badha diya
    else:                                   # 40 se kam marks
        failed = failed + 1                 # Fail count 1 badha diya

# ---------- Loop ke baad average nikalna ----------
average = total / len(marks)                # len(marks) students ki ginti deta hai (yahan 8). Total ko usse divide karke average mila

# ---------- Result print karna ----------
print("Highest Marks:", highest)            # Sabse zyada marks
print("Lowest Marks:", lowest)              # Sabse kam marks
print("Average Marks:", average)            # Average marks
print("Students Passed:", passed)           # Kitne students pass hue
print("Students Failed:", failed)           # Kitne students fail hue


# ---------- Output ----------
# Highest Marks: 91
# Lowest Marks: 29
# Average Marks: 60.25
# Students Passed: 6
# Students Failed: 2

# ---------- Working samajhne ke liye ----------
# Total: 85 + 72 + 38 + 91 + 45 + 29 + 67 + 55 = 482
# Average: 482 / 8 = 60.25
# Pass (40 ya zyada): 85, 72, 91, 45, 67, 55 = 6 students
# Fail (40 se kam): 38, 29 = 2 students

# ---------- Assignment requirements ----------
# Kai students ke marks list mein  -> marks = [...]
# Highest / Lowest marks           -> if mark > highest / if mark < lowest
# Average marks                    -> total / len(marks)
# Passed / Failed count            -> if mark >= 40 / else
# Passing mark = 40                -> mark >= 40
# Loop used                        -> for mark in marks

# Note: highest aur lowest ko 0 se shuru nahi kiya, pehle marks se shuru kiya,
# taaki list ke marks kuch bhi hon, answer sahi aaye.