# Salary Calculator Function
# It takes the employee name, basic salary, bonus % and tax %

def calculate_salary(name, basic, bonus_percent, tax_percent):
    # Validation: check that the data is not wrong
    # invalid if basic is 0 or negative, bonus is negative, or tax is below 0 or above 100
    if basic <= 0 or bonus_percent < 0 or tax_percent < 0 or tax_percent > 100:
        print(name, "- Invalid data!")
        return                              # stop here, no calculation is done

    bonus = basic * bonus_percent / 100     # bonus amount (e.g. 10% of 30000 = 3000)
    gross = basic + bonus                   # gross salary = basic + bonus
    tax = gross * tax_percent / 100         # tax is charged on the gross salary
    final = gross - tax                     # final salary = gross - tax (take-home salary)

    print("Name:", name)
    print("Gross Salary:", gross)
    print("Tax Amount:", tax)
    print("Final Salary:", final)
    print("-----")                          # line to separate employees


# List of five employees
# Each employee is a small list: [name, basic, bonus %, tax %]
employees = [
    ["Amit", 30000, 10, 5],                 # basic 30000, bonus 10%, tax 5%
    ["Neha", 45000, 15, 10],                # basic 45000, bonus 15%, tax 10%
    ["Rahul", 25000, 5, 0],                 # basic 25000, bonus 5%, tax 0%
    ["Priya", 60000, 20, 15],               # basic 60000, bonus 20%, tax 15%
    ["Karan", 35000, 8, 8],                 # basic 35000, bonus 8%, tax 8%
]

# Loop through each employee one by one
for emp in employees:
    # emp[0] = name, emp[1] = basic, emp[2] = bonus %, emp[3] = tax %
    # calling the function processes all five employees
    calculate_salary(emp[0], emp[1], emp[2], emp[3])


# Example output (first two employees):
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
# The other three employees (Rahul, Priya, Karan) are printed in the same way.

# More examples:
# calculate_salary("Sita", 40000, 10, 5)   # Final Salary: 41800.0
# calculate_salary("Ravi", -5000, 10, 5)   # Ravi - Invalid data!

# Note: Tax is charged on the gross salary (basic + bonus).
# To charge tax only on basic, use tax = basic * tax_percent / 100.