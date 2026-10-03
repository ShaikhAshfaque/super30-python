# 8.Pattern Generator
# Using nested for loops, generate the following pattern for a user-supplied value of N:



# 8. Pattern Generator (Nested For Loops)

# User se N ki value li. N batata hai ki pattern mein kitni rows hongi.
n = int(input("Enter the value of N: "))    # input() text deta hai, int() use number mein badalta hai

# OUTER LOOP: ye decide karta hai ki kitni rows hongi
# range(1, n + 1) matlab 1 se n tak (n bhi shamil). N = 5 ho to i = 1, 2, 3, 4, 5
for i in range(1, n + 1):

    # INNER LOOP: ye har row ke andar numbers print karta hai
    # range(1, i + 1) matlab 1 se i tak. Matlab row number jitne hi numbers us row mein aayenge
    # i = 1 -> 1
    # i = 2 -> 1 2
    # i = 3 -> 1 2 3
    # i = 4 -> 1 2 3 4
    # i = 5 -> 1 2 3 4 5
    for j in range(1, i + 1):
        print(j, end=" ")                   # end=" " se number ke baad space aata hai, naya line nahi. Isliye numbers ek hi line mein aate hain

    print()                                 # Inner loop khatam hone par ye khaali print() agli line par le jaata hai (nayi row shuru)


# ---------- Example ----------
# Input:
# Enter the value of N: 5
#
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# ---------- Working samajhne ke liye (N = 3) ----------
# i = 1: j = 1             -> "1 "      -> print() -> nayi line
# i = 2: j = 1, 2          -> "1 2 "    -> print() -> nayi line
# i = 3: j = 1, 2, 3       -> "1 2 3 "  -> print() -> nayi line

# Yaad rakho:
# Outer loop (i) -> rows ki ginti
# Inner loop (j) -> har row ke numbers
# end=" "        -> same line mein print karne ke liye
# print()        -> next line mein jaane ke liye

# Note: N mein text (jaise "abc") daalne par int() error dega.