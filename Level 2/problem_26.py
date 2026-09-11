"""
Problem 26: Biggest 4-Digit Number Divisible by 7 and 9

Question:
Write a program to print the biggest 4-digit number which is divisible by 7 and 9.

Sample Testcase(s):
Output: 9954

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


for number in range(9999, 999, -1):
    if number % 7 == 0 and number % 9 == 0:
        print(number)
        break
