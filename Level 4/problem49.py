"""
Problem 49: Write a function to convert an integer array into a
character array and print it.

Test case:
    Input : 1 4 5 8 7 6 3
    Output: 1458763
"""


def int_array_to_char_array(numbers):
    """Convert a list of single digits into a list of characters."""
    return [str(number) for number in numbers]


def main():
    text = input("Enter numbers separated by spaces: ")
    numbers = [int(value) for value in text.split()]
    characters = int_array_to_char_array(numbers)
    print("".join(characters))


if __name__ == "__main__":
    main()
