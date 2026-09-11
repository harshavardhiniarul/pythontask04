"""
Problem 9
Get a two-digit number from the user and swap its digits.

Testcase:
Input: 34   -> Output: 43
Input: 56   -> Output: 65
"""


def swap_digits(number):
    tens_digit = number // 10
    units_digit = number % 10
    return (units_digit * 10) + tens_digit


def main():
    number = int(input("Enter a two-digit number: "))
    result = swap_digits(number)
    print(result)


if __name__ == "__main__":
    main()
