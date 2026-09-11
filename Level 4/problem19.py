"""
Problem 19: Write a program to print the sum of all three-digit odd
numbers.

Test case:
    Output: 247500
"""


def main():
    total = sum(n for n in range(100, 1000) if n % 2 != 0)
    print("Sum of three-digit odd numbers:", total)


if __name__ == "__main__":
    main()
