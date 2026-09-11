"""
Problem 22: Write a program to print the total number of three-digit
prime numbers.

Test case:
    Output: 143
"""


def is_prime(number):
    """Return True if number is prime, False otherwise."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def main():
    count = sum(1 for n in range(100, 1000) if is_prime(n))
    print("Total three-digit prime numbers:", count)


if __name__ == "__main__":
    main()
