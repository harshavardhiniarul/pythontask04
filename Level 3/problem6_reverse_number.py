"""
Problem 6
Get a number from the user and reverse it.

Testcase:
Input: 123     -> Output: 321
Input: 56789   -> Output: 98765
"""


def reverse_number(number):
    return int(str(number)[::-1])


def main():
    number = int(input("Enter a number: "))
    result = reverse_number(number)
    print(result)


if __name__ == "__main__":
    main()
