# Get a four-digit number
n = int(input())

# Separate the digits
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

# Reverse the first two digits
print(b * 1000 + a * 100 + c * 10 + d)