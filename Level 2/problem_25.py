"""
Problem 25: Count of Single-Digit Prime Numbers in a Number

Question:
Write a program to get a number from the user and print the total number of single-digit prime numbers in the number.

Sample Testcase(s):
Input: 163496481 -> Output: 1
Input: 364925 -> Output: 3

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


single_digit_primes = {2, 3, 5, 7}

number_str = input("Enter a number: ").strip()
count = sum(1 for digit in number_str if int(digit) in single_digit_primes)

print(count)
