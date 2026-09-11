"""
Problem 7
Get two numbers from the user and compare them.
If they are the same, print "Same"; otherwise print "Not Same".

Testcase:
Input: 123, 123       -> Output: Same
Input: 56789, 12345   -> Output: Not Same
"""


def compare_numbers(first, second):
    return first == second


def main():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    if compare_numbers(first, second):
        print("Same")
    else:
        print("Not Same")


if __name__ == "__main__":
    main()
