"""
Problem 18: Check if Last Two Digits Form a Prime

Question:
Write a program to get a number from the user and print whether the last two digits form a prime number.

Sample Testcase(s):
Input: 359 -> Output: Prime
Input: 3577 -> Output: Not Prime

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


number_str = input("Enter a number: ").strip()
last_two_digits = int(number_str[-2:])

print("Prime" if is_prime(last_two_digits) else "Not Prime")
