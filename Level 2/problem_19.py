"""
Problem 19: Check if Middle Two Digits (of a 4-digit Number) Form a Prime

Question:
Write a program to get a 4-digit number from the user and print whether the middle two digits form a prime number.

Sample Testcase(s):
Input: 6359 -> Output: Not Prime
Input: 3517 -> Output: Prime

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


number_str = input("Enter a 4-digit number: ").strip()
middle_two_digits = int(number_str[1:3])

print("Prime" if is_prime(middle_two_digits) else "Not Prime")

# Note: For input 3517, the middle two digits are "51" (3-5-1-7), and 51 = 3 x 17
# is not prime, so this program correctly prints "Not Prime" for that input.
