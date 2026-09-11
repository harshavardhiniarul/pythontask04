"""
Problem 27: Count of Numbers Below 100000 With Digit Sum 14

Question:
Write a program to print the total count of numbers less than 100000 whose sum of digits is 14.

Sample Testcase(s):
Output: 4995

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


count = 0

for number in range(100000):
    digit_sum = sum(int(d) for d in str(number))
    if digit_sum == 14:
        count += 1

print(count)

# Note: The correct count of numbers from 0 to 99999 whose digits sum to 14 is 2710
# (verified both by this program and by a stars-and-bars combinatorial calculation).
