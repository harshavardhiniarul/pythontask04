"""
Problem 8
Get a number from the user and check whether its digits are in ascending order.

Testcase:
Input: 1234   -> Output: Yes
Input: 5687   -> Output: No
"""


def is_ascending(number):
    digits = str(number)
    return all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))


def main():
    number = int(input("Enter a number: "))
    if is_ascending(number):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
