"""
Problem 45: Get a number up to 50 digits and reverse it.

Test case:
    Input : 12345678912345
    Output: 54321987654321
"""


def reverse_number_string(text):
    """Reverse a numeric string of arbitrary length."""
    return text[::-1]


def main():
    text = input("Enter a number (up to 50 digits): ")
    print("Reversed number:", reverse_number_string(text))


if __name__ == "__main__":
    main()
