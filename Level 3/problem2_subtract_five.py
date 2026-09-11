"""
Problem 2
Get a number from the user, subtract 5 from it, and print the result.

Testcase:
Input: 45      -> Output: 40
Input: 56789   -> Output: 56784
"""


def subtract_five(number):
    return number - 5


def main():
    number = int(input("Enter a number: "))
    result = subtract_five(number)
    print(result)


if __name__ == "__main__":
    main()
