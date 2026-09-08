# Get a three-digit number
n = int(input())

# Reverse the digits
print((n % 10) * 100 + ((n // 10) % 10) * 10 + n // 100)