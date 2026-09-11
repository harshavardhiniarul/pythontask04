"""
Problem 30: HCF of Two Numbers

Question:
Write a program to get two numbers from the user and print the HCF of those numbers.

Sample Testcase(s):
Input: 12, 18 -> Output: 6
Input: 24, 36 -> Output: 12

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


import math

a, b = map(int, input("Enter two numbers separated by space: ").split())
print(math.gcd(a, b))
