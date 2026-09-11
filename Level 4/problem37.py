"""
Problem 37: Get an ASCII number and print its corresponding character.

Test case:
    Input : 65 -> Output: A
    Input : 97 -> Output: a
"""


def main():
    ascii_value = int(input("Enter an ASCII value: "))
    print("Character:", chr(ascii_value))


if __name__ == "__main__":
    main()
