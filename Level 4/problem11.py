"""
Problem 11: Get a four-digit number from the user and print the sum
of all digits.

Test case:
    Input : 7638
    Output: 24
"""


def digit_sum(number):
    """Return the sum of the digits of a four-digit number."""
    total = 0
    for _ in range(4):
        total += number % 10
        number //= 10
    return total


def main():
    number = int(input("Enter a four-digit number: "))
    print("Sum of digits:", digit_sum(number))


if __name__ == "__main__":
    main()
