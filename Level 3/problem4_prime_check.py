"""
Problem 4
Get a number from the user and check whether it is prime or not.

Testcase:
Input: 61     -> Output: Number is Prime
Input: 1200   -> Output: Number is not Prime
"""


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("Number is Prime")
    else:
        print("Number is not Prime")


if __name__ == "__main__":
    main()
