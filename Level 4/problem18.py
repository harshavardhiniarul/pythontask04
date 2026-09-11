"""
Problem 18: Write a program to print the sum of all two-digit odd
numbers.

Test case:
    Output: 2475
"""


def main():
    total = sum(n for n in range(10, 100) if n % 2 != 0)
    print("Sum of two-digit odd numbers:", total)


if __name__ == "__main__":
    main()
