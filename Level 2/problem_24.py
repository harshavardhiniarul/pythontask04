"""
Problem 24: Count of Two-Digit Perfect Squares in a Number

Question:
Write a program to get a number from the user and print the total number of two-digit perfect square numbers in the number.

Sample Testcase(s):
Input: 163496481 -> Output: 4
Input: 364925 -> Output: 4

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


two_digit_squares = {16, 25, 36, 49, 64, 81}

number_str = input("Enter a number: ").strip()
count = 0

for i in range(len(number_str) - 1):
    pair_value = int(number_str[i:i + 2])
    if pair_value in two_digit_squares:
        count += 1

print(count)
