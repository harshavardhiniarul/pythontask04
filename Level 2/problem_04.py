"""
Problem 4: Sum of 6 to 1

Question:
Write a loop program to print the sum of 6 to 1.

Sample Testcase(s):
Output: 21

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


total = 0
for number in range(6, 0, -1):
    total += number

print(total)
