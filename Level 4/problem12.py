"""
Problem 12: Get a number from the user and print its reverse.

Test case:
    Input : 123456
    Output: 654321
"""


def reverse_number(number):
    """Return the reverse of any non-negative integer."""
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return reversed_number


def main():
    number = int(input("Enter a number: "))
    print("Reversed number:", reverse_number(number))


if __name__ == "__main__":
    main()
