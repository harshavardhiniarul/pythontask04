"""
Problem 41: Get an integer and print each digit as a character, one
character per line.

Test case (added):
    Input : 12345
    Output:
        1
        2
        3
        4
        5
"""


def main():
    number = input("Enter an integer: ")
    for character in number:
        print(character)


if __name__ == "__main__":
    main()
