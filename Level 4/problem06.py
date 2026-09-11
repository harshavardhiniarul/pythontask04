"""
Problem 6: Get a two-digit number from the user and print its reverse.

Test case:
    Input : 73
    Output: 37
"""


def reverse_two_digit(number):
    """Return the reverse of a two-digit number."""
    ones = number % 10
    tens = number // 10
    return ones * 10 + tens


def main():
    number = int(input("Enter a two-digit number: "))
    print("Reversed number:", reverse_two_digit(number))


if __name__ == "__main__":
    main()
