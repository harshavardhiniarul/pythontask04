# Get a four-digit number
n = int(input())

# Separate the digits
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

# Reverse the last two digits
print(a * 1000 + b * 100 + d * 10 + c)