"""
Problem 8: Two-Digit Even Numbers Whose Digit Sum is 6

Question:
Write a loop program to print the two-digit even numbers whose sum of digits is 6.

Sample Testcase(s):
Output:
24
42
60

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


def digit_sum(n):
    return sum(int(d) for d in str(n))


for number in range(10, 100, 2):
    if digit_sum(number) == 6:
        print(number)
