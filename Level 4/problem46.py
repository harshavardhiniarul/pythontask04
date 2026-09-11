"""
Problem 46: Get a number string up to 50 digits and convert it into
an integer array.

Test case:
    Input : 12345
    Output: [1, 2, 3, 4, 5]
"""


def to_int_array(text):
    """Convert a numeric string into a list of single-digit integers."""
    return [int(digit) for digit in text]


def main():
    text = input("Enter a number (up to 50 digits): ")
    print("Integer array:", to_int_array(text))


if __name__ == "__main__":
    main()
