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
    # Agar remainder 0 hai, to number Even hai
    if i % 2 == 0:

        # Current number ko Even print kar rahe hain
        print(i, "is Even")

        # Current number i ko l_even list mein add kar rahe hain
        # append(i) ka matlab current i ko list mein add karo
        l_even.append(i)

    else:

        # Agar i % 2 == 0 False hai, to number Odd hai
        print(i, "is Odd")

        # Current number i ko l_odd list mein add kar rahe hain
        l_odd.append(i)

# len(l_even) Even list ke total numbers ki counting karega
print("Total Even Numbers:", len(l_even))

# len(l_odd) Odd list ke total numbers ki counting karega
print("Total Odd Numbers:", len(l_odd))