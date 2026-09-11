"""
Problem 21: Count of Odd Digits in a Number

Question:
Write a program to get a number from the user and print the total number of digits that are odd.

Sample Testcase(s):
Input: 12345678 -> Output: 4
Input: 987531 -> Output: 5

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


number_str = input("Enter a number: ").strip()
count = sum(1 for digit in number_str if int(digit) % 2 != 0)

print(count)
