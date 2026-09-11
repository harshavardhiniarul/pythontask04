"""
Problem 22: Count of Two-Digit Odd Numbers Within a Number

Question:
Write a program to get a number from the user and print the total number of two-digit odd numbers in the number.

Sample Testcase(s):
Input: 12345678 -> Output: 3
Input: 987531 -> Output: 4

Reference & Credit: Balajee Seshadri | Curated by Mathi Yuvarajan
"""


number_str = input("Enter a number: ").strip()
count = 0

for i in range(len(number_str) - 1):
    pair_value = int(number_str[i:i + 2])
    if pair_value % 2 != 0:
        count += 1

print(count)
