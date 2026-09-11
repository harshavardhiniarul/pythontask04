"""
Problem 7: Get a three-digit number from the user and print its reverse.

Test case:
    Input : 738
    Output: 837
"""


def reverse_three_digit(number):
    """Return the reverse of a three-digit number."""
    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10
    return ones * 100 + tens * 10 + hundreds


def main():
    number = int(input("Enter a three-digit number: "))
    print("Reversed number:", reverse_three_digit(number))


if __name__ == "__main__":
    main()
