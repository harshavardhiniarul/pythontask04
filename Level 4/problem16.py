"""
Problem 16: Write a program to print the total number of three-digit
odd numbers.

Test case:
    Output: 450
"""


def main():
    count = sum(1 for n in range(100, 1000) if n % 2 != 0)
    print("Total three-digit odd numbers:", count)


if __name__ == "__main__":
    main()
