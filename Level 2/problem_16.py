"""
Problem 16: Check if a Number is Prime

Question:
Write a program to get a number from the user and print whether that number is prime or not.

Sample Testcase(s):
Input: 31 -> Output: Prime
Input: 27 -> Output: Not Prime

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


number = int(input("Enter a number: "))
print("Prime" if is_prime(number) else "Not Prime")
