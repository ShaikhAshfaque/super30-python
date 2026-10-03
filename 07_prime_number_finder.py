# 7. Prime Number Finder
# Ask the user for a starting and ending number.
# Print all prime numbers within that range using nested loops.

start = int(input("Enter starting number: "))  # Takes the starting number from the user
end = int(input("Enter ending number: "))      # Takes the ending number from the user

print("Prime number: ")  # Displays a heading before printing the prime numbers

# Go through every number from start to end
for number in range(start, end + 1):

    # Prime numbers are greater than 1
    if number > 1:

        # Assume the number is prime at first
        is_prime = True

        # Check if the number can be divided by any number
        # from 2 up to number - 1
        for i in range(2, number):

            # If the remainder is 0, the number is divisible
            # by i, so it is NOT a prime number
            if number % i == 0:
                is_prime = False

                # No need to check further
                break

        # If no divisor was found, the number is prime
        if is_prime:
            print(number)