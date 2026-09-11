"""
Problem 3: Get a three-digit number from the user and print the digit
in the one's position.

Test case:
    Input : 738
    Output: 8
"""


def ones_digit(number):
    """Return the digit in the one's position of a three-digit number."""
    return number % 10


def main():
    number = int(input("Enter a three-digit number: "))
    print("Digit in one's position:", ones_digit(number))


if __name__ == "__main__":
    main()
