"""
Problem 10: Get a three-digit number from the user and print the sum
of all digits.

Test case:
    Input : 738
    Output: 18
"""


def digit_sum(number):
    """Return the sum of the digits of a three-digit number."""
    total = 0
    for _ in range(3):
        total += number % 10
        number //= 10
    return total


def main():
    number = int(input("Enter a three-digit number: "))
    print("Sum of digits:", digit_sum(number))


if __name__ == "__main__":
    main()
