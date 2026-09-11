"""
Problem 7: Two-Digit Odd Numbers Whose Digit Sum is 7

Question:
Write a loop program to print the two-digit odd numbers whose sum of digits is 7.

Sample Testcase(s):
Output:
25
43
61

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


def digit_sum(n):
    return sum(int(d) for d in str(n))


for number in range(11, 100, 2):
    if digit_sum(number) == 7:
        print(number)
