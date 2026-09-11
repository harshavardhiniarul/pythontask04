"""
Problem 1: Get a two-digit number from the user and print the digit
in the one's (units) position.

Test case:
    Input : 78
    Output: 8
"""


def ones_digit(number):
    """Return the digit in the one's position of a two-digit number."""
    return number % 10


def main():
    number = int(input("Enter a two-digit number: "))
    print("Digit in one's position:", ones_digit(number))


if __name__ == "__main__":
    main()
