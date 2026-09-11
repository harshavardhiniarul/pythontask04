"""
Problem 34: Print the total number of palindrome numbers less than
100000.

Examples: 101, 12321, 656, 99899.

Test case (added):
    Output: 1098
"""


def is_palindrome(number):
    """Return True if number reads the same forwards and backwards."""
    text = str(number)
    return text == text[::-1]


def main():
    count = sum(1 for n in range(1, 100000) if is_palindrome(n))
    print("Total palindrome numbers less than 100000:", count)


if __name__ == "__main__":
    main()
