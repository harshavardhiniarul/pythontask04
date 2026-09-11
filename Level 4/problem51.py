"""
Problem 51: Get a string and a character from the user. Find all
positions where the character is present and print them.

Test case:
    Input String   : hellohellohello
    Input Character: h
    Output          : 1, 6, 11
"""


def find_positions(text, character):
    """Return the 1-indexed positions of character within text."""
    return [index + 1 for index, char in enumerate(text) if char == character]


def main():
    text = input("Enter a string: ")
    character = input("Enter a character: ")
    positions = find_positions(text, character)
    print(", ".join(str(position) for position in positions))


if __name__ == "__main__":
    main()
