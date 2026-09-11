"""
Problem 17: Prime Check and Digit Sum Check

Question:
Write a program to get a number from the user, print whether that number is prime, and check whether the sum of its digits is equal to 14.

Sample Testcase(s):
Input: 59 -> Output: Prime & Sum of Digits is 14
Input: 77 -> Output: Not Prime but sum of digits is 14
Input: 13 -> Output: Prime, but sum of Digits is not 14

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
digit_sum = sum(int(d) for d in str(number))
prime = is_prime(number)

if prime and digit_sum == 14:
    print("Prime & Sum of Digits is 14")
elif not prime and digit_sum == 14:
    print("Not Prime but sum of digits is 14")
elif prime and digit_sum != 14:
    print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime and sum of digits is not 14")
