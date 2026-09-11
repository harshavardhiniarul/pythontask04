"""
Problem 17: Write a program to print the sum of all single-digit odd
numbers.

Test case:
    Output: 25
"""


def main():
    total = sum(n for n in range(0, 10) if n % 2 != 0)
    print("Sum of single-digit odd numbers:", total)


if __name__ == "__main__":
    main()
