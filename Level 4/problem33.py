"""
Problem 33: Print the total number of non-decreasing numbers from 1000
to 9999. A non-decreasing number has digits that do not decrease from
left to right.

Example: 1234 is non-decreasing, whereas 2134 is not.

Test case:
    Output: 495
"""


def is_non_decreasing(number):
    """Return True if the digits of number never decrease left to right."""
    digits = str(number)
    return all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1))


def main():
    count = sum(1 for n in range(1000, 10000) if is_non_decreasing(n))
    print("Total non-decreasing numbers from 1000 to 9999:", count)


if __name__ == "__main__":
    main()
