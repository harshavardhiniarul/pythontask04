"""
Problem 1
Get a number from the user, add 2 to it, and print the result.

Testcase:
Input: 45      -> Output: 47
Input: 56789   -> Output: 56791
"""


def add_two(number):
    return number + 2


def main():
    number = int(input("Enter a number: "))
    result = add_two(number)
    print(result)


if __name__ == "__main__":
    main()
