"""
Problem 53: Get a string and count all the words in it.

Test case:
    Input : Welcome to HCL Tech
    Output: 4
"""


def count_words(text):
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def main():
    text = input("Enter a string: ")
    print("Number of words:", count_words(text))


if __name__ == "__main__":
    main()
