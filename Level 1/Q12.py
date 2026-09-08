# Get a three-digit number
n = int(input())

# Add all three digits
print(n // 100 + (n // 10) % 10 + n % 10)