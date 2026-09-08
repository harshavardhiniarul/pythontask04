# Get a three-digit number
n = int(input())

# Replace the one's digit with 2
print(n - n % 10 + 2)