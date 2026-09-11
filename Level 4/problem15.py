"""
Problem 15: Write a program to print the total number of two-digit
odd numbers.

Test case:
    Output: 45
"""


def main():
    count = sum(1 for n in range(10, 100) if n % 2 != 0)
    print("Total two-digit odd numbers:", count)


if __name__ == "__main__":
    main()
