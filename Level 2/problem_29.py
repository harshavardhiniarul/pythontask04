"""
Problem 29: LCM of Three Numbers

Question:
Write a program to get three numbers from the user and print the LCM of those numbers.

Sample Testcase(s):
Input: 2, 3, 4 -> Output: 12
Input: 4, 6, 8 -> Output: 24

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


import math


def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


a, b, c = map(int, input("Enter three numbers separated by space: ").split())
result = lcm(lcm(a, b), c)

print(result)
