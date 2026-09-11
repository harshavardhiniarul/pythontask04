"""
Problem 12: Sum of All Digits

Question:
Write a program to get a number from the user and print the sum of all digits.

Sample Testcase(s):
Input: 123456 -> Output: 21
Input: 76895439 -> Output: 51
Input: 675 -> Output: 18

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


number = int(input("Enter a number: "))
total = sum(int(digit) for digit in str(abs(number)))

print(total)
