"""
Problem 9: Get a two-digit number from the user and print the sum of
all digits.

Test case:
    Input : 78
    Output: 15
"""


def digit_sum(number):
    """Return the sum of the digits of a number."""
    return number % 10 + number // 10 % 10


def main():
    number = int(input("Enter a two-digit number: "))
    print("Sum of digits:", digit_sum(number))


if __name__ == "__main__":
    main()
