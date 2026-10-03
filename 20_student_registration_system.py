# Student Registration System

# students is a dictionary. Each student's ID is the key,
# and the details (name, marks) are stored as a small dictionary in the value.
# Example: {"101": {"name": "Amit", "marks": 85.0}}
students = {}


# Function to add a new student
def add_student():
    sid = input("Student ID: ")             # take the student ID
    if sid in students:                     # is this ID already used?
        print("This ID already exists!")
        return                              # stop here, no student is added
    name = input("Name: ")
    marks = float(input("Marks (0-100): ")) # convert marks to a number
    if marks < 0 or marks > 100:            # validation: marks must be between 0 and 100
        print("Invalid marks!")
        return                              # stop here, no student is added
    students[sid] = {"name": name, "marks": marks}  # save name and marks under the ID
    print("Student added.")


# Function to show all students
def view_students():
    if len(students) == 0:                  # dictionary is empty
        print("No students found.")
        return
    print("--- All Students ---")
    for sid in students:                    # each student ID comes one by one
        print("ID:", sid, "| Name:", students[sid]["name"], "| Marks:", students[sid]["marks"])
        # the line above gets the name and marks of that ID and prints them


# Function to search a student by ID
def search_student():
    sid = input("Enter ID to search: ")
    if sid in students:                     # ID found in the dictionary
        print("Found! Name:", students[sid]["name"], "| Marks:", students[sid]["marks"])
    else:
        print("Student not found.")


# Function to update a student's details
def update_student():
    sid = input("Enter ID to update: ")
    if sid not in students:                 # ID does not exist
        print("Student not found.")
        return
    name = input("New name (press Enter to keep old): ")   # leave empty to keep the old name
    if name != "":                          # user typed something
        students[sid]["name"] = name        # change the name
    marks_text = input("New marks (press Enter to keep old): ")   # marks taken as text first
    if marks_text != "":                    # user typed marks
        marks = float(marks_text)           # convert text to a number
        if marks >= 0 and marks <= 100:     # marks are in the valid range
            students[sid]["marks"] = marks
        else:
            print("Invalid marks! Marks not updated.")   # old marks stay
    print("Update done.")


# Function to delete a student
def delete_student():
    sid = input("Enter ID to delete: ")
    if sid in students:                     # ID found
        del students[sid]                   # remove the student from the dictionary
        print("Student deleted.")
    else:
        print("Student not found.")


# Function to calculate the class average marks
def class_average():
    if len(students) == 0:                  # no students, so no average
        print("No students found.")
        return
    total = 0                               # start the total at 0
    for sid in students:                    # go through each student
        total = total + students[sid]["marks"]  # add each student's marks to the total
    average = total / len(students)         # divide the total by the number of students
    print("Class Average Marks:", average)


# Function to show the student with the highest marks
def top_student():
    if len(students) == 0:                  # no students
        print("No students found.")
        return
    top_id = None                           # no topper yet, so None
    top_marks = -1                          # start at -1 so the first student becomes the top
    for sid in students:                    # check each student
        if students[sid]["marks"] > top_marks:   # more than the top marks so far
            top_marks = students[sid]["marks"]   # remember the new top marks
            top_id = sid                         # remember the ID too
    print("Topper:", students[top_id]["name"], "| ID:", top_id, "| Marks:", top_marks)


# MAIN PROGRAM: the while loop keeps showing the menu
while True:                                 # runs until break
    print("\n===== Student Registration System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Average")
    print("7. Top Performer")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == "1":