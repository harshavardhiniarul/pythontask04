"""
Problem 47: Add two integer arrays of up to 50 digits and store the
result in a 51-digit array.

Test case:
    Input : [1, 2, 3], [4, 5, 6]
    Output: [5, 7, 9]
"""


def add_digit_arrays(first, second):
    """Add two equal-length digit arrays position by position."""
    return [a + b for a, b in zip(first, second)]


def main():
    first = [1, 2, 3]
    second = [4, 5, 6]
    print("First array :", first)
    print("Second array:", second)
    print("Sum array   :", add_digit_arrays(first, second))


if __name__ == "__main__":
    main()
