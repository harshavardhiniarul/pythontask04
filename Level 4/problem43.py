"""
Problem 43: Get a string and check whether it is a valid number.

Test case:
    Input : 1234567 -> Output: Valid Number
    Input : 12abc35 -> Output: Not a Valid Number
"""


def is_valid_number(text):
    """Return True if every character in text is a digit."""
    return text.isdigit()


def main():
    text = input("Enter a string: ")
    if is_valid_number(text):
        print("Valid Number")
    else:
        print("Not a Valid Number")


if __name__ == "__main__":
    main()
