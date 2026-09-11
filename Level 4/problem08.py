"""
Problem 8: Get a four-digit number from the user and print its reverse.

Test case:
    Input : 7384
    Output: 4837
"""


def reverse_four_digit(number):
    """Return the reverse of a four-digit number."""
    reversed_number = 0
    for _ in range(4):
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return reversed_number


def main():
    number = int(input("Enter a four-digit number: "))
    print("Reversed number:", reverse_four_digit(number))


if __name__ == "__main__":
    main()
