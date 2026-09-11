"""
Problem 20: Write a program to print the total number of single-digit
prime numbers. Assume 0 and 1 are not prime.

Test case:
    Output: 4
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
    count = sum(1 for n in range(0, 10) if is_prime(n))
    print("Total single-digit prime numbers:", count)


if __name__ == "__main__":
    main()
