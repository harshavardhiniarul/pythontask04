"""
Problem 23: Count of Single-Digit Perfect Squares in a Number

Question:
Write a program to get a number from the user and print the total number of single-digit perfect square numbers in the number.

Sample Testcase(s):
Input: 123456789 -> Output: 3
Input: 987531 -> Output: 2

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


single_digit_squares = {0, 1, 4, 9}

number_str = input("Enter a number: ").strip()
count = sum(1 for digit in number_str if int(digit) in single_digit_squares)

print(count)
