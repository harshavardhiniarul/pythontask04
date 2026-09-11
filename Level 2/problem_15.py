"""
Problem 15: Adjust Number Based on First Digit Parity

Question:
Write a program to get a number from the user. If the first digit is even, print the same number. If the first digit is odd, subtract 1 from the first digit and print the number.

Sample Testcase(s):
Input: 123456 -> Output: 023456
Input: 96895439 -> Output: 86895439
Input: 675 -> Output: 675
Input: 575 -> Output: 475

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


number_str = input("Enter a number: ").strip()
first_digit = int(number_str[0])

if first_digit % 2 == 0:
    result = number_str
else:
    new_first_digit = first_digit - 1
    result = str(new_first_digit) + number_str[1:]

print(result)
