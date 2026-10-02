# 15. Reusable Number Analysis Function

# def function banane ke liye use hota hai.
# analyze_number function ka naam hai aur (number) ek parameter hai.
# Jab bhi hum function ko call karenge, ek number function ke andar aayega.

# def → function banata hai
# analyze_number → function ka naam
# number → input / parameter

def analyze_number(number):

    # ---------- Step 1: Positive, Negative ya Zero check karna ----------
    if number > 0:                          # Agar number 0 se bada hai
        number_type = "Positive"            # To type Positive hai
    elif number < 0:                        # Nahi to agar number 0 se chhota hai
        number_type = "Negative"            # To type Negative hai
    else:                                   # Upar ki dono condition galat hain, matlab number 0 hai
        number_type = "Zero"                # To type Zero hai

    # ---------- Step 2: Even ya Odd check karna ----------
    if number % 2 == 0:                     # % (modulus) remainder deta hai. 2 se divide karne par remainder 0 aaye to
        parity = "Even"                     # Number Even hai
    else:                                   # Remainder 0 nahi aaya
        parity = "Odd"                      # To number Odd hai

    # ---------- Step 3: Prime ya Not Prime check karna ----------
    # Prime number wo hota hai jo sirf 1 aur khud se divide hota hai (jaise 2, 3, 5, 7)
    if number < 2:                          # 2 se chhote numbers (1, 0, negative) prime nahi hote
        prime = "Not Prime"                 # Isliye seedha Not Prime
    else:                                   # Number 2 ya usse bada hai, ab check karna padega
        is_prime = True                     # Pehle maan liya ki number prime hai (baad mein galat sabit ho sakta hai)

        for i in range(2, number):          # FOR LOOP: i ki value 2 se (number - 1) tak jaayegi
            if number % i == 0:             # Agar number kisi i se poora divide ho gaya (remainder 0)
                is_prime = False            # To number prime nahi hai
                break                       # break se loop turant ruk gaya, aage check karne ki zaroorat nahi

        if is_prime:                        # Loop ke baad agar is_prime abhi bhi True hai
            prime = "Prime"                 # To number Prime hai
        else:                               # Agar is_prime False ho gaya
            prime = "Not Prime"             # To number Not Prime hai

    # ---------- Step 4: Teeno results ek saath wapas bhejna ----------
    return {                                # return result wapas bhejta hai. Yahan dictionary bheji hai
        "type": number_type,                # "type" key mein Positive / Negative / Zero
        "parity": parity,                   # "parity" key mein Even / Odd
        "prime": prime                      # "prime" key mein Prime / Not Prime
    }


result = analyze_number(7)                  # Function ko number 7 ke saath call kiya, jo wapas aaya wo result mein save hua

print(result)                               # result ko print kiya


# ---------- Output ----------
# {'type': 'Positive', 'parity': 'Odd', 'prime': 'Prime'}

# ---------- Aur examples ----------
# analyze_number(10)   # {'type': 'Positive', 'parity': 'Even', 'prime': 'Not Prime'}
# analyze_number(-5)   # {'type': 'Negative', 'parity': 'Odd', 'prime': 'Not Prime'}
# analyze_number(0)    # {'type': 'Zero', 'parity': 'Even', 'prime': 'Not Prime'}

# Note: Is function mein number poora number (integer) hona chahiye.
# Decimal number (jaise 7.5) dene par range() error dega.