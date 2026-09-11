"""
Problem 29: Print the largest four-digit prime number.

Test case:
    Output: 9973
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
    for n in range(9999, 999, -1):
        if is_prime(n):
            print("Largest four-digit prime number:", n)
            break


if __name__ == "__main__":
    main()
