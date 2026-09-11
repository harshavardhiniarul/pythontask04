"""
Problem 28: Print the smallest four-digit prime number.

Test case:
    Output: 1009
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
    for n in range(1000, 10000):
        if is_prime(n):
            print("Smallest four-digit prime number:", n)
            break


if __name__ == "__main__":
    main()
