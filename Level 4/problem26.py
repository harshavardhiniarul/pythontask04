"""
Problem 26: Print the smallest three-digit prime number.

Test case:
    Output: 101
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
    for n in range(100, 1000):
        if is_prime(n):
            print("Smallest three-digit prime number:", n)
            break


if __name__ == "__main__":
    main()
