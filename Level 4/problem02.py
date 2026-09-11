"""
Problem 2: Get a two-digit number from the user and print the digit
in the ten's position.

Test case:
    Input : 78
    Output: 7
"""


def tens_digit(number):
    """Return the digit in the ten's position of a two-digit number."""
    return number // 10


def main():
    number = int(input("Enter a two-digit number: "))
    print("Digit in ten's position:", tens_digit(number))


if __name__ == "__main__":
    main()
