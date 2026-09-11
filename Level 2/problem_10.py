"""
Problem 10: Sum of Two-Digit Odd Numbers Whose Tens Digit is 7

Question:
Write a loop program to print the sum of two-digit odd numbers whose ten's digit is 7.

Sample Testcase(s):
Output: 375

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


total = 0
for number in range(70, 80):
    if number % 2 != 0:
        total += number

print(total)
