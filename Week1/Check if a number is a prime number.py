def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, num):
        if num % i == 0:
            return False  # If divisible by any number, it's not prime
    return True  # If no divisors, it's prime

# Test the function
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

