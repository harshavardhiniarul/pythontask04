"""
Problem 28: LCM of Two Numbers

Question:
Write a program to get two numbers from the user and print the LCM of those numbers.

Sample Testcase(s):
Input: 12, 18 -> Output: 36
Input: 15, 20 -> Output: 60

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


import math

a, b = map(int, input("Enter two numbers separated by space: ").split())
lcm = abs(a * b) // math.gcd(a, b)

print(lcm)
