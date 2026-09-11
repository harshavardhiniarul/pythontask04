"""
Problem 24: Write a program to print the sum of all two-digit prime
numbers.

Test case:
    Output: 1043
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
    total = sum(n for n in range(10, 100) if is_prime(n))
    print("Sum of two-digit prime numbers:", total)


if __name__ == "__main__":
    main()
