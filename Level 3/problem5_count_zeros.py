"""
Problem 5
Get a number from the user and count the number of zeros in it.

Testcase:
Input: 100        -> Output: 2
Input: 1060030    -> Output: 4
"""


def count_zeros(number):
    return str(abs(number)).count("0")


def main():
    number = int(input("Enter a number: "))
    result = count_zeros(number)
    print(result)


if __name__ == "__main__":
    main()
