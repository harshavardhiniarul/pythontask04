"""
Problem 48: Adjust the carry in an integer array. Convert a two-digit
number into a single digit and add the carry to the previous position.

Test case:
    Input : 6 12 3 15 7
    Output: 7 2 4 5 7
"""


def adjust_carry(digits):
    """Propagate carries leftwards so every position holds a single digit."""
    digits = digits[:]
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] >= 10:
            carry = digits[i] // 10
            digits[i] %= 10
            digits[i - 1] += carry
    return digits


def main():
    text = input("Enter numbers separated by spaces: ")
    digits = [int(value) for value in text.split()]
    print("Adjusted array:", adjust_carry(digits))


if __name__ == "__main__":
    main()
