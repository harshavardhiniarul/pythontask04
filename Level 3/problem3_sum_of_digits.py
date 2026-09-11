"""
Problem 3
Get a number from the user and check whether the sum of its digits is 14.

Testcase:
Input: 59    -> Output: Sum of Digits is 14
Input: 123   -> Output: Sum of Digits is not 14
"""


def is_digit_sum_14(number):
    digit_sum = sum(int(digit) for digit in str(abs(number)))
    return digit_sum == 14


def main():
    number = int(input("Enter a number: "))
    if is_digit_sum_14(number):
        print("Sum of Digits is 14")
    else:
        print("Sum of Digits is not 14")


if __name__ == "__main__":
    main()
