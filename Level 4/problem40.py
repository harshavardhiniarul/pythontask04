"""
Problem 40: Get an integer and print it as a string.

Test case (added):
    Input : 12345
    Output: "12345"
"""


def main():
    number = int(input("Enter an integer: "))
    text = str(number)
    print(f'"{text}"')


if __name__ == "__main__":
    main()
