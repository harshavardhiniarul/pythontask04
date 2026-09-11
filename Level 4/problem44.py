"""
Problem 44: Get a string of numbers up to 50 digits and remove all
leading zeroes.

Test case:
    Input : 00000012345
    Output: 12345
"""


def remove_leading_zeroes(text):
    """Strip leading zero characters from a numeric string."""
    stripped = text.lstrip("0")
    return stripped if stripped else "0"


def main():
    text = input("Enter a numeric string (up to 50 digits): ")
    print("Result:", remove_leading_zeroes(text))


if __name__ == "__main__":
    main()
