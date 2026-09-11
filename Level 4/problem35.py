"""
Problem 35: Get two numbers from the user and find their LCM.

Test case:
    Input : 20, 30
    Output: 60
"""


def gcd(a, b):
    """Return the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of a and b."""
    return a * b // gcd(a, b)


def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("LCM:", lcm(a, b))


if __name__ == "__main__":
    main()
