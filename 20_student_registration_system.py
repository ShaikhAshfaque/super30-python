# students naam ki dictionary banayi. Isme har student ka ID "key" hoga
# aur uski details (naam, marks) ek chhoti dictionary mein "value" hongi.
# Example: {"101": {"name": "Amit", "marks": 85.0}}
students = {}


# Naya student add karne ka function
def add_student():
    sid = input("Student ID: ")             # User se student ka ID liya
    if sid in students:                     # Check kiya ki ye ID pehle se to nahi hai
        print("Ye ID pehle se hai!")        # Pehle se hai to message dikhaya
        return                              # Function yahin ruk gaya, naya student add nahi hoga
    name = input("Naam: ")                  # Student ka naam liya
    marks = float(input("Marks (0-100): ")) # Marks liye aur float (number) mein badal diye
    if marks < 0 or marks > 100:            # Validation: marks 0 se 100 ke beech hone chahiye
        print("Invalid marks!")             # Galat marks par message
        return                              # Function ruk gaya, student add nahi hoga
    students[sid] = {"name": name, "marks": marks}  # ID ke saath naam aur marks save kar diye
    print("Student add ho gaya.")           # Confirmation message


# Saare students dikhane ka function
def view_students():
    if len(students) == 0:                  # Agar dictionary khaali hai
        print("Koi student nahi hai.")      # To ye message dikhao
        return                              # Aur function band
    print("--- Saare Students ---")         # Heading print ki
    for sid in students:                    # FOR LOOP: har student ka ID ek-ek karke milega
        print("ID:", sid, "| Naam:", students[sid]["name"], "| Marks:", students[sid]["marks"])
        # Upar wali line us ID ka naam aur marks dictionary se nikal kar print karti hai


# ID se student dhundhne ka function
def search_student():
    sid = input("Search karne wala ID: ")   # User se ID liya
    if sid in students:                     # Agar ID dictionary mein mili
        print("Mil gaya! Naam:", students[sid]["name"], "| Marks:", students[sid]["marks"])
    else:                                   # Nahi mili to
        print("Student nahi mila.")         # Not found message


# Student ki details update karne ka function
def update_student():
    sid = input("Update karne wala ID: ")   # Kis student ko update karna hai, uska ID liya
    if sid not in students:                 # Agar ID hi nahi hai
        print("Student nahi mila.")         # To message dikhao
        return                              # Aur function band
    name = input("Naya naam (Enter dabao to purana rahega): ")  # Naya naam, ya khaali chhodo
    if name != "":                          # Agar user ne kuch likha hai (khaali nahi hai)
        students[sid]["name"] = name        # To naam badal do
    marks_text = input("Naye marks (Enter dabao to purane rahenge): ")  # Naye marks text mein liye
    if marks_text != "":                    # Agar user ne marks likhe hain
        marks = float(marks_text)           # Text ko number mein badla
        if marks >= 0 and marks <= 100:     # Check kiya ki marks sahi range mein hain
            students[sid]["marks"] = marks  # Sahi hain to marks badal do
        else:
            print("Invalid marks! Marks update nahi hue.")  # Galat hain to purane hi rahenge
    print("Update ho gaya.")                # Confirmation message


# Student delete karne ka function
def delete_student():
    sid = input("Delete karne wala ID: ")   # Kis student ko hatana hai, uska ID liya
    if sid in students:                     # Agar ID mili
        del students[sid]                   # To us student ko dictionary se hata diya
        print("Student delete ho gaya.")    # Confirmation message
    else:
        print("Student nahi mila.")         # ID nahi mili to message


# Class ke average marks nikalne ka function
def class_average():
    if len(students) == 0:                  # Agar koi student hi nahi hai
        print("Koi student nahi hai.")      # To average nahi nikal sakte
        return                              # Function band
    total = 0                               # Total ko 0 se shuru kiya
    for sid in students:                    # FOR LOOP: har student par ek-ek karke jao
        total = total + students[sid]["marks"]  # Har student ke marks total mein jodte jao
    average = total / len(students)         # Total ko students ki ginti se divide kiya
    print("Class Average Marks:", average)  # Average print kiya


# Sabse zyada marks wale student ko dikhane ka function
def top_student():
    if len(students) == 0:                  # Agar koi student nahi hai
        print("Koi student nahi hai.")      # To message dikhao
        return                              # Function band
    top_id = None                           # Topper ka ID abhi koi nahi, isliye None
    top_marks = -1                          # Sabse bade marks abhi -1 maane (taaki pehla student bada nikle)
    for sid in students:                    # FOR LOOP: har student ko check karo
        if students[sid]["marks"] > top_marks:   # Agar is student ke marks ab tak ke top se zyada hain
            top_marks = students[sid]["marks"]   # To naye top marks yaad kar lo
            top_id = sid                         # Aur uska ID bhi yaad kar lo
    print("Topper:", students[top_id]["name"], "| ID:", top_id, "| Marks:", top_marks)


# MAIN PROGRAM: ye while loop menu ko baar-baar dikhata rahega
while True:                                 # WHILE LOOP: jab tak break na aaye, chalta rahega
    print("\n===== Student Registration System =====")   # Menu ki heading
    print("1. Add Student")                 # Menu option 1
    print("2. View All Students")           # Menu option 2
    print("3. Search by ID")                # Menu option 3
    print("4. Update Student")              # Menu option 4
    print("5. Delete Student")              # Menu option 5
    print("6. Class Average")               # Menu option 6
    print("7. Top Performer")               # Menu option 7
    print("8. Exit")                        # Menu option 8
    choice = input("Apna choice chuno (1-8): ")   # User ka choice liya

    if choice == "1":                       # Agar choice 1 hai
        add_student()                       # To add_student function chalao
    elif choice == "2":                     # Agar choice 2 hai
        view_students()                     # To view_students function chalao
    elif choice == "3":                     # Agar choice 3 hai
        search_student()                    # To search_student function chalao
    elif choice == "4":                     # Agar choice 4 hai
        update_student()                    # To update_student function chalao
    elif choice == "5":                     # Agar choice 5 hai
        delete_student()                    # To delete_student function chalao
    elif choice == "6":                     # Agar choice 6 hai
        class_average()                     # To class_average function chalao
    elif choice == "7":                     # Agar choice 7 hai
        top_student()                       # To top_student function chalao
    elif choice == "8":                     # Agar choice 8 hai
        print("Thank you! Program band ho raha hai.")  # Bye message
        break                               # break se while loop khatam, program band
    else:                                   # Upar ke koi bhi choice nahi mile to
        print("Galat choice! 1 se 8 ke beech chuno.")  # Galat choice ka message

# ---------- Example output ----------
# Add karne ke baad View All dabane par:
# ID: 101 | Naam: Amit | Marks: 85.0
# ID: 102 | Naam: Neha | Marks: 92.0
# Class Average Marks: 88.5
# Topper: Neha | ID: 102 | Marks: 92.0
#
# Note: Marks mein text (jaise "abc") daalne par float() error dega.
# Simple rakhne ke liye ise handle nahi kiya.