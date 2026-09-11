"""
Problem 9: Sum of Two-Digit Numbers Whose Ones Digit is 5

Question:
Write a loop program to print the sum of two-digit numbers whose one's digit is 5.

Sample Testcase(s):
Output: 495

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


total = 0
for number in range(10, 100):
    if number % 10 == 5:
        total += number

print(total)
