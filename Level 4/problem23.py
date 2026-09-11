"""
Problem 23: Write a program to print the sum of single-digit prime
numbers.

Test case:
    Output: 18
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
    total = sum(n for n in range(0, 10) if is_prime(n))
    print("Sum of single-digit prime numbers:", total)


if __name__ == "__main__":
    main()
