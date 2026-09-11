"""
Problem 14: Write a program to print the total number of single-digit
odd numbers.

Test case:
    Output: 5
"""


def main():
    count = sum(1 for n in range(0, 10) if n % 2 != 0)
    print("Total single-digit odd numbers:", count)


if __name__ == "__main__":
    main()
