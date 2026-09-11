"""
Problem 11: Count Total Digits in a Number

Question:
Write a program to get a number from the user and print the total number of digits in that number.

Sample Testcase(s):
Input: 123456 -> Output: 6
Input: 76895439 -> Output: 8
Input: 675 -> Output: 3

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


number = int(input("Enter a number: "))
digit_count = len(str(abs(number)))

print(digit_count)
