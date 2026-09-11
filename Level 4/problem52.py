"""
Problem 52: Get a main string and a substring. Check whether the
substring is present in the main string and print its position.

Test case:
    Input String    : hellosurabee
    Input Substring : sura
    Output           : 6
"""


def find_substring_position(main_string, substring):
    """Return the 1-indexed starting position of substring, or -1."""
    index = main_string.find(substring)
    return index + 1 if index != -1 else -1


def main():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring: ")
    position = find_substring_position(main_string, substring)
    if position != -1:
        print("Position:", position)
    else:
        print("Substring not found")


if __name__ == "__main__":
    main()
