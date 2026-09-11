"""
Problem 31: Print the number of zeroes encountered between 0 and 1000.

Test case (added):
    Output: 193
    (This counts zeroes from 1 through 1000.)
"""


def count_zeroes(limit):
    """Count how many times the digit '0' appears in numbers 1..limit."""
    total = 0
    for n in range(1, limit + 1):
        total += str(n).count("0")
    return total


def main():
    print("Total zeroes from 1 to 1000:", count_zeroes(1000))


if __name__ == "__main__":
    main()
