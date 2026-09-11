"""
Problem 10
Get a number from the user, find the number of digits, and print it.

Testcase:
Input: 34678       -> Output: 5
Input: 12345678    -> Output: 8
"""


def count_digits(number):
    return len(str(abs(number)))


def main():
    number = int(input("Enter a number: "))
    result = count_digits(number)
    print(result)


if __name__ == "__main__":
    main()
