"""
Problem 13: Reverse a Number

Question:
Write a program to get a number from the user and print the reverse of that number.

Sample Testcase(s):
Input: 123456 -> Output: 654321
Input: 76895439 -> Output: 93459867
Input: 675 -> Output: 576

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


number_str = input("Enter a number: ").strip()
reversed_str = number_str[::-1]

print(reversed_str)
