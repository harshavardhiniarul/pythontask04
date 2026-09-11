"""
Problem 32: Print the total number of prime numbers below 1,000,000
whose sum of digits is equal to 14.

Example: 59 -> 5 + 9 = 14

Test case (added):
    Output: 1218
"""


def sieve_of_eratosthenes(limit):
    """Return a boolean list where is_prime[n] is True if n is prime."""
    is_prime = [True] * limit
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, limit, i):
                is_prime[multiple] = False
    return is_prime


def digit_sum(number):
    """Return the sum of the digits of a number."""
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def main():
    limit = 1_000_000
    is_prime = sieve_of_eratosthenes(limit)
    count = sum(
        1 for n in range(2, limit) if is_prime[n] and digit_sum(n) == 14
    )
    print("Primes below 1,000,000 with digit sum 14:", count)


if __name__ == "__main__":
    main()
