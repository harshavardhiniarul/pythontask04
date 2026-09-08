# Get a three-digit number
n = int(input())

# Remove the ten's digit
print(n - ((n // 10) % 10) * 10)