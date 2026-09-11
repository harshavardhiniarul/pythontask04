"""
Problem 30: Print the largest eight-digit prime number.

Test case:
    Output: 99999989
"""


def is_prime(number):
    """Return True if number is prime, False otherwise."""
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def main():
    for n in range(99999999, 9999999, -1):
        if is_prime(n):
            print("Largest eight-digit prime number:", n)
            break


if __name__ == "__main__":
    main()
