# Salary calculate karne ka function
# Ye employee ka naam, basic salary, bonus % aur tax % leta hai
def calculate_salary(name, basic, bonus_percent, tax_percent):
    # Validation: data galat to nahi hai, ye check karte hain
    # basic 0 ya negative ho, bonus negative ho, ya tax 0 se kam / 100 se zyada ho to invalid hai
    if basic <= 0 or bonus_percent < 0 or tax_percent < 0 or tax_percent > 100:
        print(name, "- Invalid data!")      # Galat data par message dikhaya
        return                              # Function yahin ruk gaya, aage ka calculation nahi hoga

    bonus = basic * bonus_percent / 100     # Bonus ka amount nikala (jaise 30000 ka 10% = 3000)
    gross = basic + bonus                   # Gross salary = basic + bonus
    tax = gross * tax_percent / 100         # Tax amount nikala (tax gross salary par lagta hai)
    final = gross - tax                     # Final salary = gross mein se tax ghatao (haath mein aane wali salary)

    print("Name:", name)                    # Employee ka naam print kiya
    print("Gross Salary:", gross)           # Gross salary print ki
    print("Tax Amount:", tax)               # Tax amount print kiya
    print("Final Salary:", final)           # Final salary print ki
    print("-----")                          # Alag-alag employees ke beech line dikhane ke liye


# Paanch employees ki list banayi
# Har employee ek chhoti list hai: [naam, basic, bonus %, tax %]
employees = [
    ["Amit", 30000, 10, 5],                 # Amit: basic 30000, bonus 10%, tax 5%
    ["Neha", 45000, 15, 10],                # Neha: basic 45000, bonus 15%, tax 10%
    ["Rahul", 25000, 5, 0],                 # Rahul: basic 25000, bonus 5%, tax 0%
    ["Priya", 60000, 20, 15],               # Priya: basic 60000, bonus 20%, tax 15%
    ["Karan", 35000, 8, 8],                 # Karan: basic 35000, bonus 8%, tax 8%
]

# FOR LOOP: employees list ke har employee ko ek-ek karke emp mein lega
for emp in employees:
    # emp[0] = naam, emp[1] = basic, emp[2] = bonus %, emp[3] = tax %
    # Function ko call kiya, is tarah paanchon employees process ho jaate hain
    calculate_salary(emp[0], emp[1], emp[2], emp[3])


# ---------- Aur examples ----------
# calculate_salary("Sita", 40000, 10, 5)   # Final Salary: 41800.0
# calculate_salary("Ravi", -5000, 10, 5)   # Ravi - Invalid data!

# ---------- Example output (pehle do employees) ----------
# Name: Amit
# Gross Salary: 33000.0
# Tax Amount: 1650.0
# Final Salary: 31350.0
# -----
# Name: Neha
# Gross Salary: 51750.0
# Tax Amount: 5175.0
# Final Salary: 46575.0
# -----
# Baaki teen employees (Rahul, Priya, Karan) ka output bhi isi tarah aayega.

# Note: Yahan tax gross salary par lagaya hai (basic + bonus).
# Agar sirf basic par tax lagana ho, to tax = basic * tax_percent / 100 kar do.