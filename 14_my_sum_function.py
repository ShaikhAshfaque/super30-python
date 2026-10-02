# 14. Create Your Own sum() Function

# def function banane ke liye use hota hai.
# my_sum function ka naam hai aur (numbers) ek parameter hai.
# Function ko numbers ki list milegi, jaise [10, 20, 30, 40, 50]
# Is function mein Python ka built-in sum() use nahi karna, hum khud total nikalenge.

def my_sum(numbers):
    total = 0                               # Total ko 0 se shuru kiya. Phir ek-ek number isme add hoga

    for number in numbers:                  # FOR LOOP: list ke har number ko ek-ek karke number mein leta hai
        total = total + number              # Har number ko total mein jod diya
        # Step by step (list [10, 20, 30, 40, 50] ke liye):
        # 0 + 10 = 10
        # 10 + 20 = 30
        # 30 + 30 = 60
        # 60 + 40 = 100
        # 100 + 50 = 150

    return total                            # return final answer function se bahar bhejta hai. Yahan answer 150 hai


numbers = [10, 20, 30, 40, 50]              # Numbers ki list banayi

result = my_sum(numbers)                    # List ko my_sum() function mein bheja. Function 150 return karega, to result = 150

print("Total:", result)                     # Result print kiya


# ---------- Output ----------
# Total: 150

# ---------- Aur examples ----------
# my_sum([1, 2, 3])       # 6
# my_sum([2.5, 1.5])      # 4.0
# my_sum([])              # 0 (list khaali hai, loop chalta hi nahi, isliye total 0 hi rehta hai)

# Important Point:
# Assignment ka main purpose built-in sum() use na karna hai.
# Galat:  sum(numbers)
# Sahi:   my_sum(numbers)
# Yaad rakho: function → loop → total → return, yahi is assignment ka main concept hai.