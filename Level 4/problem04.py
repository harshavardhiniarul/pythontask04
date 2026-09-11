"""
Problem 4: Get a three-digit number from the user and print the digit
in the ten's position.

Test case:
    Input : 738
    Output: 3
"""


def tens_digit(number):
    """Return the digit in the ten's position of a three-digit number."""
    return (number // 10) % 10


def main():
    number = int(input("Enter a three-digit number: "))
    print("Digit in ten's position:", tens_digit(number))


if __name__ == "__main__":
    main()
