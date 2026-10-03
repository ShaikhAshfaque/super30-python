# 15. Reusable Number Analysis Function

# def is used to create a function.
# analyze_number is the function name and (number) is the parameter.
# Each time we call the function, a number is sent into it.

def analyze_number(number):

    # Step 1: Check Positive, Negative or Zero
    if number > 0:                      # greater than 0
        number_type = "Positive"
    elif number < 0:                    # less than 0
        number_type = "Negative"
    else:                               # not positive, not negative, so it is 0
        number_type = "Zero"

    # Step 2: Check Even or Odd
    if number % 2 == 0:                 # % gives the remainder, remainder 0 after dividing by 2 means Even
        parity = "Even"
    else:
        parity = "Odd"

    # Step 3: Check Prime or Not Prime
    # A prime number is divisible only by 1 and itself (like 2, 3, 5, 7)
    if number < 2:                      # numbers below 2 (1, 0, negatives) are not prime
        prime = "Not Prime"
    else:
        is_prime = True                 # assume the number is prime

        for i in range(2, number):      # i goes from 2 to number - 1
            if number % i == 0:         # divisible by i, so it is not prime
                is_prime = False
                break                   # stop checking

        if is_prime:                    # still True after the loop
            prime = "Prime"
        else:
            prime = "Not Prime"

    # Step 4: Send all three results back together
    return {                            # return a dictionary with the results
        "type": number_type,            # Positive / Negative / Zero
        "parity": parity,               # Even / Odd
        "prime": prime                  # Prime / Not Prime
    }


result = analyze_number(7)              # call the function with 7, the returned value is saved in result

print(result)


# Output:
# {'type': 'Positive', 'parity': 'Odd', 'prime': 'Prime'}

# More examples:
# analyze_number(10)   # {'type': 'Positive', 'parity': 'Even', 'prime': 'Not Prime'}
# analyze_number(-5)   # {'type': 'Negative', 'parity': 'Odd', 'prime': 'Not Prime'}
# analyze_number(0)    # {'type': 'Zero', 'parity': 'Even', 'prime': 'Not Prime'}

# Note: The number must be a whole number (integer).
# A decimal number like 7.5 will cause an error in range().