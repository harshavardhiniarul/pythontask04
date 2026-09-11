"""
Problem 5: Get a three-digit number from the user and print the digit
in the hundred's position.

Test case:
    Input : 738
    Output: 7
"""


def hundreds_digit(number):
    """Return the digit in the hundred's position of a three-digit number."""
    return number // 100


def main():
    number = int(input("Enter a three-digit number: "))
    print("Digit in hundred's position:", hundreds_digit(number))


if __name__ == "__main__":
    main()
