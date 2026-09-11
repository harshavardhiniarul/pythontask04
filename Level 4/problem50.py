"""
Problem 50: Get two numbers of up to 50 digits, perform addition, and
print the result.

Test case:
    Input : 123456789123456789, 987654321987654321
    Output: 1111111111111111110
"""


def main():
    first = input("Enter the first number (up to 50 digits): ")
    second = input("Enter the second number (up to 50 digits): ")
    result = int(first) + int(second)
    print("Sum:", result)


if __name__ == "__main__":
    main()
