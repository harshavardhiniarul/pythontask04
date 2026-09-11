"""
Problem 13: Get a number from the user and print the sum of all digits.

Test case:
    Input : 123456
    Output: 21
"""


def digit_sum(number):
    """Return the sum of the digits of any non-negative integer."""
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def main():
    number = int(input("Enter a number: "))
    print("Sum of digits:", digit_sum(number))


if __name__ == "__main__":
    main()
