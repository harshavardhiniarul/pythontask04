"""
Problem 20: Count of Single-Digit Prime Numbers

Question:
Write a program to print the total number of single-digit prime numbers.

Sample Testcase(s):
Output: 4

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


count = sum(1 for i in range(10) if is_prime(i))
print(count)
