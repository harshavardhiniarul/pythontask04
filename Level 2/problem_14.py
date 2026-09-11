"""
Problem 14: Interchange First and Last Digits

Question:
Write a program to get a number from the user and interchange the first and last digits, then print the result.

Sample Testcase(s):
Input: 123456 -> Output: 623451
Input: 76895439 -> Output: 96895437
Input: 675 -> Output: 576

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


number_str = input("Enter a number: ").strip()

if len(number_str) > 1:
    result = number_str[-1] + number_str[1:-1] + number_str[0]
else:
    result = number_str

print(result)
