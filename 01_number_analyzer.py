# User se ek number N input le rahe hain
N = int(input("Enter a number: "))

# Even numbers ko store karne ke liye empty list bana rahe hain
l_even = []

# Odd numbers ko store karne ke liye empty list bana rahe hain
l_odd = []

# 1 se N tak loop chalega
# N + 1 isliye likha hai kyunki range() ka last number include nahi hota
for i in range(1, N + 1):

    # Check kar rahe hain ki i ko 2 se divide karne par remainder 0 hai ya nahi
    # % ka matlab remainder hota hai
    # Remainder 0 = Even number
    if i % 2 == 0:

        # Current number ko Even print kar rahe hain
        print(i, "is Even")

        # Current number i ko l_even list mein add kar rahe hain
        # append(i) = current number ko list mein add karo
        l_even.append(i)

    else:

        # Agar number 2 se completely divide nahi hota
        # to woh Odd number hai
        print(i, "is Odd")

        # Current number i ko l_odd list mein add kar rahe hain
        l_odd.append(i)

# len(l_even) Even numbers ki total counting karega
print("Total Even Numbers:", len(l_even))

# len(l_odd) Odd numbers ki total counting karega
print("Total Odd Numbers:", len(l_odd))

# Example:
# Agar N = 10 hai:
#
# 1 is Odd
# 2 is Even
# 3 is Odd
# 4 is Even
# 5 is Odd
# 6 is Even
# 7 is Odd
# 8 is Even
# 9 is Odd
# 10 is Even
#
# Total Even Numbers: 5
# Total Odd Numbers: 5
#
# IMPORTANT:
# append(i) -> current number i ko list mein add karta hai
#
# l_even.append(i) -> current Even number ko l_even mein add karo
# l_odd.append(i)  -> current Odd number ko l_odd mein add karo